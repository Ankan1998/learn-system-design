# 📋 System Design Glossary

A single place to look up every term used in this curriculum. Skim it now; return to it whenever a word is unfamiliar.

> Tip: Use your browser's "Find" (Ctrl/Cmd+F) to jump to a term.

---

## A

**ACID** — Atomicity, Consistency, Isolation, Durability. The guarantees a traditional (relational) database transaction provides.

**Availability** — The percentage of time a system is up and able to serve requests. Measured in "nines" (99.9% = "three nines" ≈ 8.7 hours of downtime/year).

**API (Application Programming Interface)** — A contract describing how one piece of software talks to another (e.g., a REST endpoint).

**API Gateway** — A single entry point that sits in front of many backend services, handling auth, routing, rate limiting, etc.

**Authentication (AuthN) / Authorization (AuthZ)** — AuthN verifies *who you are* (login, tokens); AuthZ verifies *what you're allowed to do* (roles, permissions).

## B

**Backpressure** — When a downstream component is overwhelmed and signals upstream producers to slow down.

**Bloom Filter** — A space-efficient probabilistic data structure that answers "is this item *definitely not* in the set, or *possibly* in it?"

**Bottleneck** — The single component that limits the throughput of the whole system.

## C

**Cache** — A small, fast store of frequently-accessed data placed close to where it's needed to avoid slow recomputation/fetching.

**CAP Theorem** — In the presence of a network **P**artition, a distributed system must choose between **C**onsistency and **A**vailability.

**CDC (Change Data Capture)** — Streaming a database's change log (WAL/binlog) to downstream systems — caches, search indexes, warehouses — so they stay in sync without dual writes.

**CDN (Content Delivery Network)** — A globally distributed network of servers that caches content close to users.

**Cold Start** — The extra latency when a serverless function (or new server/connection) must be initialized from scratch before serving its first request.

**Consensus** — The problem of getting multiple distributed nodes to agree on a single value (solved by Paxos, Raft).

**Consistency** — All nodes see the same data at the same time (strong), or eventually (eventual).

**Consistent Hashing** — A hashing technique that minimizes data movement when nodes are added/removed. Core to distributed caches and databases.

**CQRS** — Command Query Responsibility Segregation. Separate the write model from the read model.

## D

**DAU/MAU** — Daily/Monthly Active Users. Core inputs to capacity estimation.

**Denormalization** — Intentionally duplicating data to make reads faster (at the cost of harder writes).

**DNS (Domain Name System)** — Translates human-readable domain names (google.com) into IP addresses.

## E

**Embedding** — A dense numeric vector representing the *meaning* of text/images, enabling semantic (similarity) search instead of exact keyword match.

**Eventual Consistency** — Given no new updates, all replicas will *eventually* converge to the same value.

**Event Sourcing** — Storing state as an immutable log of events rather than as current values.

**Exactly-Once** — A processing guarantee that each message affects the system's state once and only once (usually achieved via idempotency + dedup).

## F

**FaaS (Function as a Service)** — Serverless compute where you deploy single functions triggered by events; the platform handles servers and scaling (AWS Lambda, Cloud Functions).

**Fan-out** — Delivering one piece of data to many destinations (e.g., one tweet to all followers' timelines).

**Failover** — Automatically switching to a standby component when the primary fails.

## H

**Hash** — A function that maps data of any size to a fixed-size value. Used for lookups, sharding, and integrity.

**Heartbeat** — A periodic "I'm alive" signal used to detect node failures.

**HNSW (Hierarchical Navigable Small World)** — The layered-graph index most vector databases use for fast approximate nearest-neighbor search.

**Horizontal Scaling (Scale-out)** — Adding more machines.

**Hotspot / Hot Key** — A single key or shard receiving a disproportionate share of traffic.

## I

**Idempotency** — An operation that can be applied multiple times without changing the result beyond the first application.

**Index** — A data structure (often a B-Tree) that makes database lookups fast at the cost of extra storage and slower writes.

## J

**JWT (JSON Web Token)** — A signed, self-contained token (`header.payload.signature`) that lets servers verify identity without a session store. Revocation is its weak spot.

## L

**Latency** — Time to handle a single request (e.g., 50ms). Often discussed as percentiles: p50, p99.

**Load Balancer** — Distributes incoming requests across multiple servers.

**LSM Tree (Log-Structured Merge Tree)** — A write-optimized storage structure used by Cassandra, RocksDB, etc.

## M

**Message Queue** — A buffer that decouples producers from consumers, smoothing load and adding resilience.

**Microservices** — An architecture of small, independently deployable services.

**mTLS (Mutual TLS)** — TLS where *both* client and server present certificates; the standard for service-to-service authentication in zero-trust networks and service meshes.

## N

**NewSQL / Distributed SQL** — Databases offering SQL + ACID transactions with horizontal scale (Google Spanner, CockroachDB, TiDB).

**NoSQL** — Non-relational databases (key-value, document, column-family, graph) optimized for scale and flexibility.

## O

**OAuth 2.0** — The standard protocol for *delegated authorization* — letting an app act on your behalf without seeing your password. **OIDC** adds an identity (login) layer on top of it.

**Outbox Pattern** — Writing an event to an "outbox" table in the *same transaction* as the business change, then relaying it to a queue — the standard fix for the dual-write problem.

## P

**Partition (Sharding)** — Splitting one dataset across multiple machines.

**Partition Tolerance** — The system keeps working despite network failures between nodes.

**Percentile (p50, p95, p99)** — p99 latency = the value below which 99% of requests fall. Tail latency matters at scale.

**Proxy** — An intermediary. A *forward* proxy represents clients; a *reverse* proxy represents servers.

**Pub/Sub** — Publish-Subscribe. Publishers send messages to topics; subscribers receive them without knowing each other.

## Q

**QPS / RPS** — Queries/Requests Per Second. The fundamental throughput unit.

**Quorum** — The minimum number of nodes that must agree for an operation to succeed (e.g., majority).

## R

**RAG (Retrieval-Augmented Generation)** — Retrieving relevant documents (usually via vector search) and inserting them into an LLM's prompt so answers are grounded in your data.

**Rate Limiting** — Capping how many requests a client may make in a time window.

**RBAC / ABAC** — Role-Based vs Attribute-Based Access Control: authorization by assigned roles vs by evaluating attributes of the user, resource, and context.

**Replication** — Keeping copies of data on multiple machines for durability and read scaling.

**Reverse Proxy** — A server that forwards client requests to backend servers (e.g., Nginx).

## S

**Saga** — A sequence of local transactions with compensating actions, used for distributed transactions.

**Serverless** — Running code without managing servers; you pay per use and the platform scales (even to zero). See FaaS.

**Service Mesh** — An infrastructure layer of sidecar proxies plus a control plane that handles mTLS, retries, routing, and telemetry between microservices (Istio, Linkerd).

**Sharding** — See Partition.

**Sidecar** — A helper process deployed alongside a service (common in service meshes).

**SLA / SLO / SLI** — Service Level Agreement / Objective / Indicator. The promised, targeted, and measured reliability.

**Stateless** — A server that keeps no client session data between requests, making it easy to scale and replace.

## T

**Throughput** — How much work per unit time the system handles (e.g., requests/sec, MB/sec).

**Throttling** — Deliberately slowing or rejecting requests to protect a system.

**Time-Series Database (TSDB)** — A database optimized for timestamped, append-only data (metrics, IoT) with heavy compression and time-window queries (InfluxDB, Prometheus).

**TTL (Time To Live)** — How long a cached/stored item remains valid before expiring.

## V

**Vector Database** — A database that indexes embeddings for fast approximate nearest-neighbor (semantic) search (pgvector, Pinecone, Milvus, Qdrant).

**Vertical Scaling (Scale-up)** — Making a single machine more powerful (more CPU/RAM).

## W

**Webhook** — An HTTP callback your platform sends to a customer's URL when an event happens — "we call you" instead of you polling us.

**WebSocket** — A protocol for persistent, full-duplex (two-way) communication between client and server.

**Write-Ahead Log (WAL)** — A durable append-only log written before applying changes, enabling crash recovery.

---

*Missing a term? It's defined in the topic where it first appears — check the relevant level.*
