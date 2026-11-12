# 🏗️ The Complete System Design Curriculum

> From "What is a server?" to "Design a global, multi-region, exactly-once payment system."
> A free, structured, beginner-to-ultra-advanced path to mastering system design — with diagrams, real-world examples, and analogies you'll actually remember.

[![Levels](https://img.shields.io/badge/Levels-8-blue)]()
[![Topics](https://img.shields.io/badge/Topics-73-green)]()
[![Case Studies](https://img.shields.io/badge/Real--World%20Designs-46-orange)]()
[![Made for](https://img.shields.io/badge/Made%20for-Beginners%20%E2%86%92%20Pros-purple)]()

---

## 🎯 What is this?

This repository is a **one-stop, self-paced course** to learn system design from the absolute basics to a professional, interview-ready, and real-world-ready level.

It is built like a video game: you start at **Level 0** and unlock the next level only after the previous one makes sense. Each level builds directly on the one before it. By the end, you'll be able to read a sentence like *"design a service that ingests 5 million events per second with sub-100ms p99 latency and no data loss"* and know exactly where to start.

Every single topic includes:

- 📖 **A detailed README** — explains the *what*, the *why*, and the *how*, in plain English.
- 📊 **Diagrams** — visual mental models (rendered automatically on GitHub via Mermaid).
- 🌍 **Real-world examples** — how Netflix, Uber, Amazon, WhatsApp, Google, and others actually do it.
- 🧠 **Analogies** — every abstract idea is anchored to something from everyday life.
- ⚖️ **Trade-offs** — there are no "best" solutions in system design, only trade-offs. We make them explicit.
- 🎤 **Interview tips** — what interviewers actually probe for.
- 📝 **TL;DR + key takeaways** — for fast revision before an interview.

---

## 👤 Who is this for?

| You are… | This repo gives you… |
|---|---|
| A **student / beginner** who has never built a backend | A gentle, jargon-free on-ramp starting from "what is a client and a server" |
| A **developer** who can build apps but freezes in design interviews | A structured vocabulary and a repeatable framework |
| A **senior engineer** prepping for L5/L6/staff interviews | Deep dives on consensus, CQRS, multi-region, and 46 full case studies |
| A **curious mind** who wants to know how Uber/WhatsApp actually work | The Bonus folder — real architectures, demystified |

**Prerequisites:** Basic programming knowledge (you've written a function and called an API). That's it. We explain everything else.

---

## 🗺️ The Learning Roadmap

```mermaid
flowchart TD
    L0["<b>Level 0 — Foundations</b><br/>How the internet, servers,<br/>and networks actually work"]
    L1["<b>Level 1 — Building Blocks</b><br/>Scaling, load balancers,<br/>caching, databases, CDNs"]
    L2["<b>Level 2 — The Data Layer</b><br/>Replication, sharding,<br/>indexing, transactions"]
    L3["<b>Level 3 — Communication</b><br/>REST, gRPC, queues,<br/>pub/sub, websockets"]
    L4["<b>Level 4 — Distributed Systems</b><br/>CAP, consensus, consistency,<br/>clocks, idempotency"]
    L5["<b>Level 5 — Architecture Patterns</b><br/>Microservices, event-driven,<br/>CQRS, resilience"]
    L6["<b>Level 6 — Scale & Reliability</b><br/>Observability, HA/DR,<br/>multi-region, security"]
    L7["<b>Level 7 — Big Data & Specialized</b><br/>Stream/batch processing,<br/>search, ML & AI systems"]
    BONUS["<b>🏆 Bonus — 46 Real-World Designs</b><br/>URL shortener → Uber →<br/>Stock exchange → ChatGPT"]

    L0 --> L1 --> L2 --> L3 --> L4 --> L5 --> L6 --> L7 --> BONUS

    style L0 fill:#e3f2fd,stroke:#1976d2,color:#000
    style L1 fill:#e8f5e9,stroke:#388e3c,color:#000
    style L2 fill:#e8f5e9,stroke:#388e3c,color:#000
    style L3 fill:#fff3e0,stroke:#f57c00,color:#000
    style L4 fill:#fff3e0,stroke:#f57c00,color:#000
    style L5 fill:#fce4ec,stroke:#c2185b,color:#000
    style L6 fill:#fce4ec,stroke:#c2185b,color:#000
    style L7 fill:#f3e5f5,stroke:#7b1fa2,color:#000
    style BONUS fill:#fffde7,stroke:#fbc02d,color:#000
```

---

## 📚 Full Curriculum

### 🟦 [Level 0 — Foundations](./Level-00-Foundations/README.md)
*The "how does any of this work" level. Don't skip it.*
1. [What is System Design?](./Level-00-Foundations/01-What-is-System-Design/README.md)
2. [The Client-Server Model](./Level-00-Foundations/02-Client-Server-Model/README.md)
3. [How the Internet Works](./Level-00-Foundations/03-How-the-Internet-Works/README.md)
4. [Network Protocols — IP, TCP, UDP](./Level-00-Foundations/04-Network-Protocols/README.md)
5. [DNS — The Internet's Phonebook](./Level-00-Foundations/05-DNS/README.md)
6. [HTTP & HTTPS](./Level-00-Foundations/06-HTTP-and-HTTPS/README.md)
7. [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

### 🟩 [Level 1 — Building Blocks](./Level-01-Building-Blocks/README.md)
*The core LEGO bricks of every system.*
1. [Scalability — Vertical vs Horizontal](./Level-01-Building-Blocks/01-Scalability/README.md)
2. [Load Balancing](./Level-01-Building-Blocks/02-Load-Balancing/README.md)
3. [Caching](./Level-01-Building-Blocks/03-Caching/README.md)
4. [Databases — SQL vs NoSQL](./Level-01-Building-Blocks/04-Databases-SQL-vs-NoSQL/README.md)
5. [Proxies — Forward & Reverse](./Level-01-Building-Blocks/05-Proxies/README.md)
6. [Content Delivery Networks (CDN)](./Level-01-Building-Blocks/06-CDN/README.md)
7. [Stateless vs Stateful Systems](./Level-01-Building-Blocks/07-Stateless-vs-Stateful/README.md)
8. [Concurrency Models & Async I/O](./Level-01-Building-Blocks/08-Concurrency-and-Async-IO/README.md)

### 🟩 [Level 2 — The Data Layer](./Level-02-Data-Layer/README.md)
*Where your data lives, and how to keep it fast and safe.*
1. [Database Replication](./Level-02-Data-Layer/01-Database-Replication/README.md)
2. [Sharding & Partitioning](./Level-02-Data-Layer/02-Sharding-and-Partitioning/README.md)
3. [Indexing](./Level-02-Data-Layer/03-Indexing/README.md)
4. [Database Internals — B-Trees & LSM Trees](./Level-02-Data-Layer/04-Database-Internals/README.md)
5. [ACID & Transactions](./Level-02-Data-Layer/05-ACID-and-Transactions/README.md)
6. [Connection Pooling](./Level-02-Data-Layer/06-Connection-Pooling/README.md)
7. [Data Modeling](./Level-02-Data-Layer/07-Data-Modeling/README.md)
8. [Consistent Hashing](./Level-02-Data-Layer/08-Consistent-Hashing/README.md)
9. [Object & Blob Storage (S3)](./Level-02-Data-Layer/09-Object-Storage/README.md)
10. [Change Data Capture (CDC)](./Level-02-Data-Layer/10-Change-Data-Capture/README.md)
11. [Schema Migrations & Zero-Downtime Changes](./Level-02-Data-Layer/11-Schema-Migrations/README.md)

### 🟧 [Level 3 — Communication](./Level-03-Communication/README.md)
*How services talk to each other and to clients.*
1. [API Design & REST](./Level-03-Communication/01-API-Design-REST/README.md)
2. [GraphQL](./Level-03-Communication/02-GraphQL/README.md)
3. [gRPC & RPC](./Level-03-Communication/03-gRPC-and-RPC/README.md)
4. [Message Queues](./Level-03-Communication/04-Message-Queues/README.md)
5. [Publish-Subscribe (Pub/Sub)](./Level-03-Communication/05-Pub-Sub/README.md)
6. [WebSockets & Real-Time Communication](./Level-03-Communication/06-WebSockets-and-Realtime/README.md)
7. [Rate Limiting](./Level-03-Communication/07-Rate-Limiting/README.md)
8. [Authentication & Authorization](./Level-03-Communication/08-Authentication-and-Authorization/README.md)
9. [Data Serialization & Schema Evolution](./Level-03-Communication/09-Data-Serialization-and-Schema-Evolution/README.md)

### 🟧 [Level 4 — Distributed Systems](./Level-04-Distributed-Systems/README.md)
*The hard, beautiful core. Where most senior interviews live.*
1. [The CAP Theorem](./Level-04-Distributed-Systems/01-CAP-Theorem/README.md)
2. [Consistency Models](./Level-04-Distributed-Systems/02-Consistency-Models/README.md)
3. [Consensus — Paxos & Raft](./Level-04-Distributed-Systems/03-Consensus-Paxos-Raft/README.md)
4. [Distributed Transactions — 2PC & Saga](./Level-04-Distributed-Systems/04-Distributed-Transactions/README.md)
5. [Leader Election](./Level-04-Distributed-Systems/05-Leader-Election/README.md)
6. [Clocks & Event Ordering](./Level-04-Distributed-Systems/06-Clocks-and-Ordering/README.md)
7. [Idempotency & Exactly-Once](./Level-04-Distributed-Systems/07-Idempotency-and-Exactly-Once/README.md)
8. [Distributed Locking](./Level-04-Distributed-Systems/08-Distributed-Locking/README.md)
9. [CRDTs & Conflict Resolution](./Level-04-Distributed-Systems/09-CRDTs-and-Conflict-Resolution/README.md)
10. [Gossip Protocols, Membership & Failure Detection](./Level-04-Distributed-Systems/10-Gossip-and-Failure-Detection/README.md)

### 🟥 [Level 5 — Architecture Patterns](./Level-05-Architecture-Patterns/README.md)
*Proven blueprints for organizing large systems.*
1. [Monolith vs Microservices](./Level-05-Architecture-Patterns/01-Monolith-vs-Microservices/README.md)
2. [Event-Driven Architecture](./Level-05-Architecture-Patterns/02-Event-Driven-Architecture/README.md)
3. [CQRS & Event Sourcing](./Level-05-Architecture-Patterns/03-CQRS-and-Event-Sourcing/README.md)
4. [Service Discovery](./Level-05-Architecture-Patterns/04-Service-Discovery/README.md)
5. [API Gateway](./Level-05-Architecture-Patterns/05-API-Gateway/README.md)
6. [Resilience Patterns — Circuit Breakers, Bulkheads, Retries](./Level-05-Architecture-Patterns/06-Resilience-Patterns/README.md)
7. [Saga & Workflow Orchestration](./Level-05-Architecture-Patterns/07-Saga-and-Orchestration/README.md)
8. [Serverless Architecture — FaaS & Beyond](./Level-05-Architecture-Patterns/08-Serverless-Architecture/README.md)
9. [Service Mesh](./Level-05-Architecture-Patterns/09-Service-Mesh/README.md)
10. [Multi-Tenancy & SaaS Architecture](./Level-05-Architecture-Patterns/10-Multi-Tenancy/README.md)

### 🟥 [Level 6 — Scale & Reliability](./Level-06-Scale-and-Reliability/README.md)
*Making it observable, available, and safe at planet scale.*
1. [Observability — Logs, Metrics, Traces](./Level-06-Scale-and-Reliability/01-Observability/README.md)
2. [Capacity Planning & Back-of-the-Envelope Estimation](./Level-06-Scale-and-Reliability/02-Capacity-Planning-and-Estimation/README.md)
3. [High Availability & Disaster Recovery](./Level-06-Scale-and-Reliability/03-High-Availability-and-DR/README.md)
4. [Deployment Strategies — Blue/Green, Canary](./Level-06-Scale-and-Reliability/04-Deployment-Strategies/README.md)
5. [Security at Scale](./Level-06-Scale-and-Reliability/05-Security-at-Scale/README.md)
6. [Multi-Region & Geo-Distribution](./Level-06-Scale-and-Reliability/06-Multi-Region-and-Geo-Distribution/README.md)
7. [Containers & Orchestration — Docker & Kubernetes](./Level-06-Scale-and-Reliability/07-Containers-and-Orchestration/README.md)
8. [Testing Distributed Systems — Load, Chaos & Canary](./Level-06-Scale-and-Reliability/08-Testing-Distributed-Systems/README.md)
9. [Data Privacy, Encryption & Compliance](./Level-06-Scale-and-Reliability/09-Data-Privacy-and-Encryption/README.md)

### 🟪 [Level 7 — Big Data & Specialized Systems](./Level-07-Big-Data-and-Specialized/README.md)
*The pro tier: data-intensive and specialized architectures.*
1. [Batch Processing — MapReduce & Spark](./Level-07-Big-Data-and-Specialized/01-Batch-Processing/README.md)
2. [Stream Processing — Kafka & Flink](./Level-07-Big-Data-and-Specialized/02-Stream-Processing/README.md)
3. [Data Warehouses & Data Lakes](./Level-07-Big-Data-and-Specialized/03-Data-Warehouses-and-Lakes/README.md)
4. [Search Systems — Inverted Indexes & Elasticsearch](./Level-07-Big-Data-and-Specialized/04-Search-Systems/README.md)
5. [Recommendation & ML Systems](./Level-07-Big-Data-and-Specialized/05-Recommendation-and-ML-Systems/README.md)
6. [Probabilistic Data Structures — Bloom Filters, HyperLogLog](./Level-07-Big-Data-and-Specialized/06-Probabilistic-Data-Structures/README.md)
7. [Geospatial Indexing — Geohash, S2, H3](./Level-07-Big-Data-and-Specialized/07-Geospatial-Indexing/README.md)
8. [Specialized Databases — Time-Series, Graph & NewSQL](./Level-07-Big-Data-and-Specialized/08-Specialized-Databases/README.md)
9. [AI & LLM Infrastructure — Vector Search, RAG & Inference](./Level-07-Big-Data-and-Specialized/09-AI-and-LLM-Infrastructure/README.md)

### 🏆 [Bonus — 46 Real-World System Designs](./Bonus-Real-World-Architectures/README.md)
*Apply everything. Ordered from easiest to hardest.*

| # | Design | Difficulty | Key concepts |
|---|--------|-----------|--------------|
| 1 | [URL Shortener (TinyURL/Bitly)](./Bonus-Real-World-Architectures/01-URL-Shortener/README.md) | ⭐ | Hashing, base62, read-heavy caching |
| 2 | [Pastebin](./Bonus-Real-World-Architectures/02-Pastebin/README.md) | ⭐ | Blob storage, TTL, key generation |
| 3 | [Distributed Rate Limiter](./Bonus-Real-World-Architectures/03-Rate-Limiter/README.md) | ⭐⭐ | Token bucket, Redis, sliding window |
| 4 | [Notification Service](./Bonus-Real-World-Architectures/04-Notification-Service/README.md) | ⭐⭐ | Fan-out, queues, retries, fault isolation |
| 5 | [Web Crawler](./Bonus-Real-World-Architectures/05-Web-Crawler/README.md) | ⭐⭐ | BFS, politeness, dedup, frontier |
| 6 | [News Feed (Twitter/X)](./Bonus-Real-World-Architectures/06-News-Feed-Twitter/README.md) | ⭐⭐⭐ | Fan-out on write vs read, timelines |
| 7 | [Instagram](./Bonus-Real-World-Architectures/07-Instagram/README.md) | ⭐⭐⭐ | Media storage, feed, followers graph |
| 8 | [WhatsApp / Chat](./Bonus-Real-World-Architectures/08-WhatsApp-Chat/README.md) | ⭐⭐⭐ | WebSockets, presence, delivery receipts |
| 9 | [YouTube / Netflix Streaming](./Bonus-Real-World-Architectures/09-YouTube-Netflix-Streaming/README.md) | ⭐⭐⭐ | Transcoding, CDN, adaptive bitrate |
| 10 | [Typeahead / Autocomplete](./Bonus-Real-World-Architectures/10-Typeahead-Autocomplete/README.md) | ⭐⭐⭐ | Tries, ranking, prefix sharding |
| 11 | [Uber / Lyft](./Bonus-Real-World-Architectures/11-Uber-Ride-Sharing/README.md) | ⭐⭐⭐⭐ | Geospatial, matching, real-time tracking |
| 12 | [Zomato / Swiggy / DoorDash](./Bonus-Real-World-Architectures/12-Food-Delivery/README.md) | ⭐⭐⭐⭐ | Three-sided marketplace, ETA, logistics |
| 13 | [Airbnb / Booking](./Bonus-Real-World-Architectures/13-Airbnb-Booking/README.md) | ⭐⭐⭐⭐ | Availability, search, double-booking |
| 14 | [Google Drive / Dropbox](./Bonus-Real-World-Architectures/14-Google-Drive-Dropbox/README.md) | ⭐⭐⭐⭐ | File sync, chunking, conflict resolution |
| 15 | [Google Maps](./Bonus-Real-World-Architectures/15-Google-Maps/README.md) | ⭐⭐⭐⭐ | Graphs, routing, geospatial indexing |
| 16 | [Ticketmaster](./Bonus-Real-World-Architectures/16-Ticketmaster/README.md) | ⭐⭐⭐⭐ | Concurrency, locking, fairness, spikes |
| 17 | [Payment System (Stripe)](./Bonus-Real-World-Architectures/17-Payment-System/README.md) | ⭐⭐⭐⭐⭐ | Idempotency, ledgers, exactly-once |
| 18 | [Distributed Cache (Redis)](./Bonus-Real-World-Architectures/18-Distributed-Cache/README.md) | ⭐⭐⭐⭐⭐ | Consistent hashing, eviction, replication |
| 19 | [Distributed Message Queue (Kafka)](./Bonus-Real-World-Architectures/19-Distributed-Message-Queue/README.md) | ⭐⭐⭐⭐⭐ | Logs, partitions, consumer groups |
| 20 | [Ad Click Aggregator](./Bonus-Real-World-Architectures/20-Ad-Click-Aggregator/README.md) | ⭐⭐⭐⭐⭐ | Stream processing, idempotency, accuracy |
| 21 | [Distributed Job Scheduler](./Bonus-Real-World-Architectures/21-Distributed-Job-Scheduler/README.md) | ⭐⭐⭐⭐⭐ | Cron at scale, leader election, at-least-once |
| 22 | [Google Search](./Bonus-Real-World-Architectures/22-Google-Search/README.md) | ⭐⭐⭐⭐⭐ | Crawling, indexing, ranking |
| 23 | [Distributed Counter / Analytics](./Bonus-Real-World-Architectures/23-Distributed-Counter-Analytics/README.md) | ⭐⭐⭐⭐⭐ | CRDTs, approximation, hot keys |
| 24 | [Stock Exchange](./Bonus-Real-World-Architectures/24-Stock-Exchange/README.md) | ⭐⭐⭐⭐⭐ | Matching engine, low latency, ordering |
| 25 | [Live Streaming (Twitch)](./Bonus-Real-World-Architectures/25-Live-Streaming/README.md) | ⭐⭐⭐⭐⭐ | Low-latency video, chat scale, ingest |
| 26 | [Unique ID Generator (Snowflake)](./Bonus-Real-World-Architectures/26-Unique-ID-Generator/README.md) | ⭐⭐ | Snowflake IDs, time-sortable, clock skew |
| 27 | [Distributed Key-Value Store (Dynamo)](./Bonus-Real-World-Architectures/27-Key-Value-Store/README.md) | ⭐⭐⭐⭐⭐ | Consistent hashing, quorums, vector clocks |
| 28 | [Google Docs (Collaborative Editing)](./Bonus-Real-World-Architectures/28-Google-Docs-Collaborative-Editing/README.md) | ⭐⭐⭐⭐⭐ | OT vs CRDTs, real-time sync |
| 29 | [Nearby Friends / Yelp (Proximity)](./Bonus-Real-World-Architectures/29-Nearby-Friends-Proximity/README.md) | ⭐⭐⭐⭐ | Geospatial index, dynamic location fan-out |
| 30 | [Video Conferencing (Zoom)](./Bonus-Real-World-Architectures/30-Video-Conferencing/README.md) | ⭐⭐⭐⭐⭐ | WebRTC, SFU vs MCU, NAT traversal |
| 31 | [E-Commerce Platform (Amazon)](./Bonus-Real-World-Architectures/31-E-Commerce-Platform/README.md) | ⭐⭐⭐⭐ | Catalog, cart, inventory, checkout saga |
| 32 | [Email Service (Gmail)](./Bonus-Real-World-Architectures/32-Email-Service/README.md) | ⭐⭐⭐⭐ | SMTP, object storage, per-user search, spam |
| 33 | [Content Delivery Network (CDN)](./Bonus-Real-World-Architectures/33-Content-Delivery-Network/README.md) | ⭐⭐⭐⭐ | Edge routing, cache hierarchy, purge |
| 34 | [Distributed Logging & Monitoring (Datadog)](./Bonus-Real-World-Architectures/34-Distributed-Logging-Monitoring/README.md) | ⭐⭐⭐⭐ | Ingestion, time-series, alerting, cardinality |
| 35 | [Gaming Leaderboard](./Bonus-Real-World-Architectures/35-Gaming-Leaderboard/README.md) | ⭐⭐ | Redis sorted sets, rank queries, sharded ranking |
| 36 | [Webhook Delivery Service](./Bonus-Real-World-Architectures/36-Webhook-Delivery-Service/README.md) | ⭐⭐⭐ | At-least-once delivery, retries, HMAC signatures |
| 37 | [Distributed File System (GFS/HDFS)](./Bonus-Real-World-Architectures/37-Distributed-File-System/README.md) | ⭐⭐⭐⭐⭐ | Chunk servers, master metadata, replication pipeline |
| 38 | [LLM Chat Service (ChatGPT)](./Bonus-Real-World-Architectures/38-LLM-Chat-Service/README.md) | ⭐⭐⭐⭐⭐ | GPU inference, token streaming, semantic caching |
| 39 | [Distributed Coordination Service (ZooKeeper/etcd)](./Bonus-Real-World-Architectures/39-Distributed-Coordination-Service/README.md) | ⭐⭐⭐⭐⭐ | Consensus, sessions, watches, locks & leader election |
| 40 | [A/B Testing Platform](./Bonus-Real-World-Architectures/40-Experimentation-Platform/README.md) | ⭐⭐⭐⭐ | Hash bucketing, layers, exposure logging, stats engine |
| 41 | [Online Code Judge (LeetCode)](./Bonus-Real-World-Architectures/41-Online-Code-Judge/README.md) | ⭐⭐⭐ | Sandboxing, cgroups/seccomp, priority queues, fair limits |
| 42 | [Social Graph Store (Facebook TAO)](./Bonus-Real-World-Architectures/42-Social-Graph-Store/README.md) | ⭐⭐⭐⭐⭐ | Objects & associations, leader/follower cache, read-after-write |
| 43 | [Calendar & Scheduling (Google Calendar)](./Bonus-Real-World-Architectures/43-Calendar-and-Scheduling/README.md) | ⭐⭐⭐ | Recurrence rules, time zones/DST, free/busy, reminders at scale |
| 44 | [Identity & Access Service (Auth0/Okta)](./Bonus-Real-World-Architectures/44-Identity-and-Access-Service/README.md) | ⭐⭐⭐⭐ | OIDC/PKCE, JWKS rotation, refresh-token families, revocation, passkeys |
| 45 | [Fraud Detection System (Stripe Radar)](./Bonus-Real-World-Architectures/45-Fraud-Detection-System/README.md) | ⭐⭐⭐⭐ | 100 ms scoring, feature store, velocity counters, graph features, delayed labels |
| 46 | [Distributed SQL Database (Spanner/CockroachDB)](./Bonus-Real-World-Architectures/46-Distributed-SQL-Database/README.md) | ⭐⭐⭐⭐⭐ | Ranges, Raft per range, write intents, parallel commits, TrueTime vs HLC |

---

## 🧭 How to use this repository

1. **Start at Level 0.** Even if you think you know it, skim it — the vocabulary is used everywhere later.
2. **Read one topic per sitting.** Each README is designed to be a complete lesson of roughly 30–50 minutes.
3. **Look at the diagrams first, then read.** The visual gives you a hook to hang the details on.
4. **Do the "Test Yourself" questions** at the end of each topic before moving on.
5. **After Level 4, start the Bonus designs in parallel.** Theory + practice reinforce each other.
6. **Before an interview,** re-read just the `TL;DR` and `Interview Tips` sections of each topic.

### Suggested pace

| Goal | Pace | Time to finish |
|---|---|---|
| Interview in 2–3 weeks | The [Interview Playbook](./INTERVIEW_PLAYBOOK.md) first, then 4–5 topics/day (Levels 0–5 in full, the rest via their TL;DR) plus one core design a day | ~3 weeks |
| Solid, lasting understanding | 1 topic or design per day | ~4 months |
| Casual learning | 2–3 topics/week | ~10–12 months |

---

## 🧱 How each topic folder is organized

```
Level-XX-Name/
└── NN-Topic-Name/
    └── README.md   ← everything: explanation, diagrams, examples, trade-offs, interview tips
```

Every topic README follows the same structure so you always know where to find things. A shared [GLOSSARY.md](./GLOSSARY.md) defines every term in one place.

---

## ⭐ The Golden Rules of System Design

Keep these in mind through every topic:

1. **There is no "best," only trade-offs.** Every choice costs you something. Name the cost.
2. **Scale changes everything.** A design for 100 users is wrong for 100 million, and vice-versa.
3. **The bottleneck is usually the database.** Most scaling work is about reads, writes, and data.
4. **Everything fails, all the time.** Design for failure as the normal case, not the exception.
5. **Estimate before you architect.** Numbers (QPS, storage, bandwidth) drive the design.
6. **Keep it simple.** The best design is the simplest one that meets the requirements. Don't add Kafka because it sounds cool.

---

## 📖 Quick links

- 🎤 [Interview playbook](./INTERVIEW_PLAYBOOK.md) — the 45-minute framework, phrase bank & cheat-sheet numbers
- 📋 [Glossary of terms](./GLOSSARY.md)

---

## 🌐 Read it as a website

The whole curriculum is also published as a searchable site with rendered diagrams,
a sidebar, and light/dark mode: **<https://ankan1998.github.io/learn-system-design/>**

Run it locally with Docker:

```bash
docker compose up site
```

Then open <http://localhost:8080>. For live-reloading while writing:

```bash
docker compose --profile dev up dev
```

<details>
<summary>How the site is built (no Docker required)</summary>

```bash
pip install -r requirements-docs.txt
python scripts/build_docs.py   # stages markdown into docs/, rewriting links
mkdocs serve                   # http://127.0.0.1:8000
```

`scripts/build_docs.py` flattens each `Level-XX/NN-Topic/README.md` into
`docs/Level-XX/NN-Topic.md` so the sidebar lists topics directly, and rewrites
every internal link to match. `docs/` and `site/` are generated — the markdown
in the level folders stays the single source of truth. Pushing to `master`
publishes automatically via GitHub Actions.

</details>

<details>
<summary>Checks to run after editing content</summary>

```bash
python scripts/update_nav.py   # regenerates the Previous / Next / "See it applied in" footer on every page
python scripts/verify.py       # internal links, Mermaid syntax, page template, counts
```

Both also run in CI, so a stale footer or a broken link fails the build before anything is published.

</details>

---

*Happy learning. By the end of this, "design Twitter" won't scare you — it'll excite you.* 🚀
