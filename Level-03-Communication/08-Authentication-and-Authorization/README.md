# Authentication & Authorization

> **Authentication (AuthN)** proves *who you are*; **Authorization (AuthZ)** decides *what you're allowed to do* — every secure system needs both, and confusing them is the root of countless breaches.

**Level:** 3 · **Topic:** 8 · **Prerequisites:** [HTTP & HTTPS](../../Level-00-Foundations/06-HTTP-and-HTTPS/README.md) · [API Design (REST)](../01-API-Design-REST/README.md) · [Stateless vs Stateful](../../Level-01-Building-Blocks/07-Stateless-vs-Stateful/README.md)

---

## 🎯 The Problem (Why does this exist?)

HTTP is stateless and anonymous. When a request arrives saying `GET /account/balance`, the server has no idea who sent it. Worse, anyone can *claim* to be anyone — a request is just bytes on a wire.

So every real system must answer two separate questions on every single request:

1. **Who is this?** (Authentication) — Is this really `alice@example.com`, or an attacker replaying stolen bytes?
2. **Can they do this?** (Authorization) — Alice is real, but is she allowed to read *Bob's* balance? Delete the production database? Refund a payment?

Get question 1 wrong and attackers impersonate users. Get question 2 wrong and legitimate users access things they shouldn't — this is **Broken Access Control**, the #1 category in the [OWASP Top 10](https://owasp.org/Top10/). Both failures make headlines; only the mechanisms differ.

---

## 🌍 Real-World Analogy

Think of a music festival:

- **The bouncer at the gate checks your ID** — that's **authentication**. They verify you are who your ticket says you are. Fake ID? You don't get in.
- **The wristband you're given grants access** — that's **authorization**. A green wristband gets you into the general area; a gold one adds backstage; a red "crew" band opens the sound booth. The bartender never re-checks your ID — they just look at the wristband.

Notice the design: identity is verified **once** (expensive, careful), then a cheap-to-check credential (the wristband) is issued and checked **everywhere else**. Sessions, JWTs, and access tokens are all just different kinds of wristbands — with different answers to "what if someone steals it?" and "how do we take it back?"

---

## 🧠 Core Idea

### AuthN vs AuthZ — keep them separate

```mermaid
flowchart LR
    R["Incoming request"] --> AN{"AuthN:<br/>Who are you?"}
    AN -- "Invalid credentials" --> E401["401 Unauthorized<br/>(really means: unauthenticated)"]
    AN -- "Identity verified" --> AZ{"AuthZ:<br/>May you do this?"}
    AZ -- "No permission" --> E403["403 Forbidden"]
    AZ -- "Allowed" --> OK["200 OK — do the work"]

    classDef green fill:#dcfce7,stroke:#86efac,color:#000
    classDef blue fill:#dbeafe,stroke:#93c5fd,color:#000
    classDef yellow fill:#fef9c3,stroke:#fde047,color:#000
    classDef purple fill:#f3e8ff,stroke:#c084fc,color:#000
    class R purple
    class AN blue
    class AZ yellow
    class E401,E403 purple
    class OK green
```

*Caption: two independent gates. Fun HTTP trivia: `401 Unauthorized` actually means "unauthenticated"; `403 Forbidden` is the true authorization failure.*

### Passwords done right (briefly)

Passwords are the oldest AuthN factor. The rules are short and non-negotiable:

- **Never store plaintext or fast hashes** (MD5, SHA-256 alone). Attackers with a leaked DB can brute-force billions of SHA-256 guesses per second on a GPU.
- **Use a slow, salted, memory-hard hash:** **bcrypt** (battle-tested) or **argon2id** (modern winner of the Password Hashing Competition). Both bake in a random **salt** per password, so two users with `hunter2` get different hashes and precomputed rainbow tables are useless.
- Tune the cost factor so one hash takes ~100–500 ms — trivial for a login, ruinous for a brute-forcer. Pair with [rate limiting](../07-Rate-Limiting/README.md) on the login endpoint.
- Add **MFA** (TOTP codes, passkeys/WebAuthn) — a stolen password alone shouldn't be enough.

### Session-based auth — the server remembers you

The classic model: after login, the server creates a **session record** and hands the browser an opaque random ID in a cookie.

```mermaid
sequenceDiagram
    autonumber
    participant B as Browser
    participant S as Server
    participant DB as Session Store<br/>(Redis / DB)

    B->>S: POST /login (email + password)
    S->>S: Verify with bcrypt/argon2
    S->>DB: Create session sid=x7f3... → user 42, expiry
    S-->>B: Set-Cookie: sid=x7f3...;<br/>HttpOnly; Secure; SameSite=Lax
    B->>S: GET /account (cookie sent automatically)
    S->>DB: Look up sid=x7f3...
    DB-->>S: user 42, still valid
    S-->>B: 200 OK — Alice's account page
```

*Caption: the session ID is meaningless by itself — all the state lives server-side, which is exactly why revocation is trivial (delete the row).*

Key properties:

- **Instant revocation:** logout / "log out all devices" / ban = delete the session record. Done.
- **Server-side state:** every app server must reach the session store — this is the [stateful trade-off](../../Level-01-Building-Blocks/07-Stateless-vs-Stateful/README.md). At scale you use a shared Redis, adding one fast lookup (~1 ms) per request.
- **CSRF danger:** because browsers attach cookies *automatically*, a malicious site can trigger requests to your site with the victim's cookie riding along (Cross-Site Request Forgery). Defend with `SameSite=Lax/Strict` cookies plus **anti-CSRF tokens** for state-changing requests.
- Cookie flags matter: `HttpOnly` (JavaScript can't read it — blunts XSS token theft), `Secure` (HTTPS only).

### Token-based auth — JWT, the self-contained wristband

A **JSON Web Token (JWT)** flips the model: instead of an opaque ID pointing to server state, the token *carries* the state, cryptographically signed.

```mermaid
flowchart TB
    T["JWT = header.payload.signature<br/>eyJhbGciOi...<br/>.eyJzdWIiOi...<br/>.SflKxwRJSM..."]
    T --> H["HEADER (base64url JSON)<br/>alg: RS256, typ: JWT"]
    T --> P["PAYLOAD — claims (base64url JSON)<br/>sub: user_42<br/>exp: 1751500800<br/>iss: auth.example.com<br/>scope: read:orders"]
    T --> S["SIGNATURE<br/>sign(header + '.' + payload, key)<br/>tamper-proof, NOT encrypted"]

    classDef green fill:#dcfce7,stroke:#86efac,color:#000
    classDef blue fill:#dbeafe,stroke:#93c5fd,color:#000
    classDef yellow fill:#fef9c3,stroke:#fde047,color:#000
    classDef purple fill:#f3e8ff,stroke:#c084fc,color:#000
    class T purple
    class H blue
    class P yellow
    class S green
```

*Caption: three base64url parts joined by dots. Anyone can DECODE the payload (it's not encrypted!) — the signature only proves it wasn't tampered with.*

Any server holding the verification key can validate a JWT **without a database call** — stateless verification. That's the superpower and the curse:

- **The revocation problem.** A signed JWT is valid until `exp`, period. Ban a user, and their token still works for up to its lifetime. Mitigations: short lifetimes (5–15 min) + refresh tokens, or a server-side denylist of revoked token IDs (`jti`) — which quietly reintroduces the state you were avoiding.
- **`alg: none` attack.** Early JWT libraries honored a header saying "algorithm: none — no signature needed," letting attackers forge admin tokens. Modern libraries reject it, but the lesson stands: **the server must pin its accepted algorithms**, never trust the token's header. See [RFC 8725 (JWT Best Current Practices)](https://datatracker.ietf.org/doc/html/rfc8725).
- **Where to store it in a browser?** `localStorage` is readable by any JavaScript — one XSS bug and tokens are exfiltrated. An **`HttpOnly` cookie** is invisible to JS (but then CSRF defenses apply again). Rule of thumb: `HttpOnly; Secure; SameSite` cookie beats localStorage for browser apps.
- **Refresh tokens & rotation.** Pair a short-lived access token with a long-lived **refresh token** stored securely. When the access token expires, the client exchanges the refresh token for a fresh pair. With **rotation**, every use issues a *new* refresh token and invalidates the old one — if a stolen refresh token is ever reused, the server detects the collision and kills the whole token family.

### Sessions vs JWT

| Dimension | Server-side sessions | JWT (stateless tokens) |
|---|---|---|
| **Revocation** | ✅ Instant — delete the record | ❌ Hard — valid until `exp` (needs denylist or short TTL) |
| **Per-request cost** | Session-store lookup (~1 ms Redis) | Signature check only — no I/O |
| **Horizontal scaling** | Needs shared session store | Any node with the public key can verify |
| **Cross-service / cross-domain** | Awkward (cookie + shared store) | ✅ Natural fit for APIs & microservices |
| **Size on the wire** | ~32-byte opaque ID | 300 B–1 KB+, sent on *every* request |
| **Data freshness** | Always current (read from store) | Stale until token expiry (role changes lag) |
| **Best for** | Classic web apps, admin panels | Service-to-service, mobile/SPA APIs, federation |

> Honest take: for a single web app, boring server-side sessions are usually the right answer. JWTs shine when tokens must cross service or organization boundaries.

### OAuth 2.0 — delegated authorization

OAuth 2.0 ([RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)) answers a different question: *"How does app A access your data in app B without ever learning your app-B password?"* Think "let this photo printer read my Google Photos."

Four roles:

| Role | Who | Festival analogy |
|---|---|---|
| **Resource Owner** | The user (owns the data) | You |
| **Client** | The app wanting access | Your friend picking up your ticket |
| **Authorization Server** | Issues tokens after consent (e.g., `accounts.google.com`) | Box office verifying + issuing wristbands |
| **Resource Server** | The API holding the data | Gate staff checking wristbands |

The gold-standard flow is **Authorization Code with PKCE** ([RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)):

```mermaid
sequenceDiagram
    autonumber
    participant U as User<br/>(Resource Owner)
    participant C as Client App<br/>(SPA / mobile)
    participant AS as Authorization Server
    participant RS as Resource Server (API)

    C->>C: Generate random code_verifier<br/>code_challenge = SHA256(verifier)
    C->>AS: Redirect to /authorize<br/>(client_id, scope, redirect_uri, code_challenge)
    AS->>U: Login + consent screen<br/>("App X wants to read your photos")
    U->>AS: Authenticates, clicks Allow
    AS-->>C: Redirect back with one-time authorization code
    C->>AS: POST /token (code + code_verifier)
    AS->>AS: SHA256(verifier) == challenge?<br/>Proves same app that started the flow
    AS-->>C: access_token (+ refresh_token)
    C->>RS: GET /photos<br/>Authorization: Bearer access_token
    RS-->>C: 200 OK — photos
```

*Caption: PKCE ("pixy") binds the token exchange to whoever started the flow — an attacker who intercepts the redirect code can't redeem it without the secret `code_verifier`.*

Other flows worth knowing:

- **Client Credentials flow** — no user at all; a backend service authenticates *as itself* (client ID + secret) to call another service. The standard machine-to-machine flow.
- **Implicit flow is dead.** It returned tokens directly in the URL fragment — leaking them into browser history, logs, and referrer headers, with no client verification. PKCE made it obsolete; [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) formally deprecates it.

### OIDC — the identity layer on top

OAuth is pure *authorization* — an access token says "may access photos," not "this is Alice." **OpenID Connect (OIDC)** adds a thin identity layer: the same code flow also returns an **ID token** (a JWT with `sub`, `email`, `name` claims) so the client learns *who logged in*.

| | **ID token** | **Access token** |
|---|---|---|
| Audience | The client app | The resource server (API) |
| Purpose | "This is Alice" (AuthN) | "Bearer may read photos" (AuthZ) |
| Send to APIs? | ❌ Never | ✅ Yes, as `Authorization: Bearer` |

Every "Sign in with Google/Apple/GitHub" button is OIDC: your app redirects to Google, Google authenticates the user, and hands back an ID token your app verifies with Google's published public keys. You never see (or store!) the user's Google password.

### SSO & SAML — the enterprise flavor

**Single Sign-On (SSO):** authenticate once with a central Identity Provider (IdP), then access many apps without re-logging in. **SAML 2.0** is the pre-OAuth enterprise standard — XML assertions instead of JWTs, browser-redirect based, still everywhere in corporate software ("Login with Okta" for Salesforce/Workday/Jira). New systems typically choose OIDC; supporting SAML is the toll you pay to sell to enterprises.

### API keys — the simplest wristband

A long random secret identifying a *program*, not a person: `sk_live_4eC39HqLyjWDarjtT1zdp7dc` (Stripe-style). Best practices baked into that format: a **prefix** (`sk_live_` vs `pk_test_`) so leaked keys are identifiable and scanners like GitHub secret scanning can spot them, **scoping** (restricted keys that can only, say, read charges), and **rotation** (issue new, run both briefly, revoke old). Keys are checked server-side (store only a hash), and every key check should be paired with [rate limits](../07-Rate-Limiting/README.md) per key.

### mTLS — service-to-service auth

In **mutual TLS**, *both* sides present certificates during the handshake — the client proves its identity cryptographically before a single byte of application data flows. This is the backbone of zero-trust service meshes (Istio/Linkerd issue and rotate short-lived certs per workload automatically, following the [SPIFFE](https://spiffe.io/) identity model). No passwords, no tokens to leak in logs — but real operational cost in certificate issuance, rotation, and debugging.

### Authorization models — RBAC, ABAC, ReBAC

```mermaid
flowchart TB
    subgraph RBAC["RBAC — role-based"]
        U1["User: alice"] --> RO["Role: editor"]
        RO --> P1["Permissions:<br/>create_post, edit_post"]
    end
    subgraph ABAC["ABAC — attribute-based"]
        RULE["Policy rule:<br/>allow if user.dept == doc.dept<br/>AND time is 9am–5pm<br/>AND device is managed"]
    end
    subgraph ReBAC["ReBAC — relationship-based"]
        D["doc:budget-2026"] -- "owner" --> U2["bob"]
        F["folder:finance"] -- "viewer" --> G["group:accounting"]
        D -- "parent" --> F
    end

    classDef green fill:#dcfce7,stroke:#86efac,color:#000
    classDef blue fill:#dbeafe,stroke:#93c5fd,color:#000
    classDef yellow fill:#fef9c3,stroke:#fde047,color:#000
    classDef purple fill:#f3e8ff,stroke:#c084fc,color:#000
    class U1,RO,P1 blue
    class RULE yellow
    class D,F,U2,G green
    class RBAC,ABAC,ReBAC purple
```

*Caption: three ways to answer "may Alice edit this document?" — by her role, by evaluating attributes against policy, or by walking a relationship graph.*

| Model | Grants access by | Great for | Weakness |
|---|---|---|---|
| **RBAC** | Roles → permission bundles | Org hierarchies, admin panels, 90% of apps | Role explosion ("editor-but-only-EU-weekdays") |
| **ABAC** | Policy over attributes (user, resource, context) | Compliance-heavy, contextual rules (AWS IAM policies) | Policies get hard to reason about and audit |
| **ReBAC** | Relationships in a graph ("owner of", "member of team that…") | Per-object sharing à la Google Docs | Needs a dedicated system to answer checks fast |

**Google Zanzibar** is the famous ReBAC system — a single global service answering ~10 million "can X do Y to Z?" checks/second for Docs, Drive, and YouTube ([Zanzibar paper, 2019](https://research.google/pubs/pub48190/)). Open-source descendants: SpiceDB, OpenFGA, Ory Keto.

---

## 🏢 Real-World Examples

- **Auth0 / Okta** — identity-as-a-service: hosted login pages, OIDC/SAML federation, MFA, token issuance. Startups outsource the entire AuthN problem for the same reason they don't build their own payment rails.
- **Google Sign-In** — textbook OIDC: your app receives an ID token signed by Google, verifies it against Google's public JWKS keys, and trusts the `sub`/`email` claims. Billions of logins with zero password handling by third-party apps.
- **Stripe API keys** — the reference design for API keys: prefixed (`sk_live_`, `sk_test_`), scopable restricted keys, one-click rotation, and automatic revocation when GitHub secret scanning finds one in a public repo ([Stripe docs](https://docs.stripe.com/keys)).
- **GitHub personal access tokens** — fine-grained PATs scope down to specific repos and permissions with mandatory expiry, replacing the old god-mode classic tokens.
- **AWS IAM** — ABAC at planetary scale: JSON policies evaluate principal, action, resource, and condition attributes on every API call; explicit `Deny` always beats `Allow`. Famously powerful, famously easy to misconfigure — which is why "public S3 bucket" is its own genre of breach.

---

## ⚖️ Trade-offs

| Mechanism | ✅ Strength | ❌ Cost |
|---|---|---|
| Sessions | Instant revocation, small cookie, simple mental model | Shared state; CSRF surface |
| JWT | Stateless verify, crosses service boundaries | Revocation is hard; bigger requests; footguns (alg, storage) |
| OAuth 2.0 + PKCE | Delegation without password sharing; standard | Redirect complexity; many flows to get wrong |
| SAML | Enterprise ubiquity | XML complexity; painful debugging |
| API keys | Dead simple for M2M | Long-lived secrets leak; no user context |
| mTLS | Strongest service identity, nothing to steal from logs | Cert lifecycle operations |
| RBAC → ABAC → ReBAC | Increasing expressiveness | Increasing complexity and infrastructure |

---

## ✅ When to Use / ❌ When NOT to Use

- **Classic server-rendered web app?** ✅ Sessions in `HttpOnly` cookies + CSRF tokens. ❌ Don't reach for JWTs "because modern."
- **Public API / mobile backend / microservices?** ✅ Short-lived JWT access tokens + rotating refresh tokens, issued via OAuth/OIDC.
- **Third-party developers calling your API?** ✅ Scoped, prefixed API keys (or OAuth client credentials for bigger partners).
- **Service-to-service inside your infra?** ✅ mTLS via a service mesh, or client-credentials tokens.
- **"Sign in with X"?** ✅ OIDC Authorization Code + PKCE. ❌ Never the implicit flow; never roll your own federation.
- **Building auth from scratch when Auth0/Okta/Cognito/Keycloak exists?** ❌ Only with a dedicated security team and a strong reason.

---

## ⚠️ Common Pitfalls & Gotchas

1. **Confusing 401 and 403** — and worse, confusing the *checks*: authenticating the user but forgetting to verify they own resource `/orders/12345` (an IDOR — insecure direct object reference).
2. **JWTs in localStorage.** One XSS vulnerability = mass token theft. Prefer `HttpOnly` cookies and accept the CSRF work.
3. **Trusting the JWT header's `alg`.** Pin allowed algorithms server-side; reject `none`; don't let an RS256 public key be reused as an HS256 secret (a real historical exploit).
4. **Long-lived access tokens with no revocation story.** A 30-day JWT means a 30-day window for every stolen token. Keep access tokens at minutes, not days.
5. **No refresh-token rotation.** Without rotation + reuse detection, one stolen refresh token = silent permanent access.
6. **Storing API keys or password hashes wrong** — plaintext keys in the DB, fast unsalted hashes, secrets in git. Hash keys like passwords; scan repos; rotate on any doubt.
7. **Authorization checks only in the UI.** Hiding the Delete button is not AuthZ. Every check must be enforced server-side, ideally at a chokepoint like the [API Gateway](../../Level-05-Architecture-Patterns/05-API-Gateway/README.md) *and* in the service.
8. **Rolling your own crypto or auth protocol.** The standards (OAuth, OIDC, WebAuthn) encode decades of exploited mistakes. Deviating from them means rediscovering those exploits in production. More at [Security at Scale](../../Level-06-Scale-and-Reliability/05-Security-at-Scale/README.md).

---

## 🎤 Interview Tips

- **Lead with the distinction:** "First, AuthN vs AuthZ — verifying identity vs granting permission. They're separate gates and separate failure modes (401 vs 403)."
- **Sessions vs JWT is the classic probe.** Give the honest answer: sessions for a single web app (instant revocation), JWTs when tokens cross service boundaries — and name the revocation problem *before* they ask.
- **Expect "how do you revoke a JWT?"** — short TTL + refresh rotation, or a `jti` denylist, and note that the denylist reintroduces state.
- **Draw the OAuth PKCE sequence** for any "Sign in with Google" or third-party-API question; naming the four roles (resource owner, client, auth server, resource server) signals real understanding.
- **Know why implicit flow died** (tokens in URL fragments) — it's a favorite senior-level follow-up.
- **For AuthZ design questions** (e.g., "design Google Docs sharing"), reach for ReBAC and name-drop Zanzibar; for org-level admin, RBAC; for AWS-style policy conditions, ABAC.
- Mention defense in depth: gateway does coarse token validation, services re-check fine-grained permissions.

---

## 📝 TL;DR

| Concept | One-liner |
|---|---|
| AuthN vs AuthZ | Bouncer checks ID (who) vs wristband grants access (what) |
| Passwords | bcrypt/argon2id + salt + MFA; never fast hashes |
| Sessions | Opaque cookie → server-side store; easy revoke; CSRF care |
| JWT | Signed self-contained claims; stateless verify; hard revoke; short TTL + refresh rotation |
| OAuth 2.0 | Delegated authorization; Auth Code + PKCE; implicit flow is dead |
| OIDC | OAuth + ID token = "Sign in with Google" |
| API keys / mTLS | Machine identities: scoped prefixed keys; certs for service mesh |
| RBAC / ABAC / ReBAC | Roles → attributes → relationship graphs (Zanzibar) |

---

## 🧪 Test Yourself

1. **A user is banned mid-session. With server-side sessions this takes effect immediately, but with JWTs it may not. Why, and what are two mitigations?**

<details><summary>Show answer</summary>

A JWT is verified purely by its signature and `exp` claim — no server lookup — so a signed token stays valid until it expires even if the user is banned. Mitigations: (1) short access-token lifetimes (5–15 min) paired with refresh tokens, so bans take effect at the next refresh, and (2) a server-side denylist of revoked token IDs (`jti`) checked on each request — which trades away some of the statelessness that motivated JWTs in the first place.

</details>

2. **Your SPA stores its JWT in localStorage "so it survives page reloads." What's the risk, what's the alternative, and what new problem does the alternative introduce?**

<details><summary>Show answer</summary>

localStorage is readable by any JavaScript on the page, so a single XSS vulnerability lets an attacker exfiltrate every user's token. The alternative is an `HttpOnly; Secure; SameSite` cookie, which JavaScript cannot read. The new problem: cookies are attached automatically by the browser, reopening CSRF — so you must add `SameSite` restrictions and anti-CSRF tokens for state-changing requests.

</details>

3. **In the OAuth Authorization Code flow, what specific attack does PKCE prevent, and how does the `code_verifier`/`code_challenge` pair achieve it?**

<details><summary>Show answer</summary>

Authorization code interception: the code returns via a browser/app redirect, which a malicious app or network observer might capture and try to exchange for tokens. With PKCE, the client sends `code_challenge = SHA256(code_verifier)` when starting the flow, and must present the original random `code_verifier` when redeeming the code. The auth server recomputes the hash and rejects any mismatch — an attacker holding only the intercepted code (and the public challenge) cannot produce the verifier.

</details>

4. **You're designing Google-Docs-style sharing: users share individual documents with people, groups, and via folder inheritance. Why does RBAC fit poorly, and what model fits?**

<details><summary>Show answer</summary>

RBAC assigns permissions via a small set of global roles, but here access is per-object and per-relationship ("Bob is *owner of this doc*", "the accounting *group* can view this *folder*, and the doc *inherits* from it") — modeling that as roles causes role explosion. This is ReBAC: store relationships as a graph and answer "can X do Y on Z?" by traversing it. Google built Zanzibar for exactly this; SpiceDB and OpenFGA are open-source implementations.

</details>

5. **An ID token and an access token both come back from an OIDC login. Your teammate sends the ID token to your API as the Bearer credential "since it's also a JWT." What's wrong?**

<details><summary>Show answer</summary>

They have different audiences and purposes. The ID token is addressed to the *client app* (`aud` = client ID) and only asserts identity — "Alice logged in." The access token is addressed to the *resource server* and carries the authorization (scopes) to call it. An API accepting ID tokens breaks audience validation: any app Alice ever logged into could replay her ID token against your API. APIs must accept only access tokens and validate `aud`/`scope`.

</details>

---

## 📚 Further Reading

- [RFC 6749 — The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749) · [RFC 7636 — PKCE](https://datatracker.ietf.org/doc/html/rfc7636) · [RFC 8725 — JWT Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) — Authentication, Session Management, and Password Storage cheat sheets are gold.
- [Zanzibar: Google's Consistent, Global Authorization System (2019)](https://research.google/pubs/pub48190/) — the ReBAC paper.
- [Auth0 — Which OAuth 2.0 Flow Should I Use?](https://auth0.com/docs/get-started/authentication-and-authorization-flow/which-oauth-2-0-flow-should-i-use)
- [Stripe — API Keys documentation](https://docs.stripe.com/keys) — study the key design, it's the industry reference.
- [Critical vulnerabilities in JSON Web Token libraries (Auth0, 2015)](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/) — the `alg: none` story firsthand.

---

⬅️ Previous: [Rate Limiting](../07-Rate-Limiting/README.md) · ➡️ Next: [Level 4 — Distributed Systems](../../Level-04-Distributed-Systems/README.md) · 🏠 [Level 3 Index](../README.md)
