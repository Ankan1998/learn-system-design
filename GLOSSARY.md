# 📋 System Design Glossary

A single place to look up every term used in this curriculum. Skim it now; return to it whenever a word is unfamiliar. Each entry ends with a link to the topic that explains it properly.

> Tip: Use your browser's "Find" (Ctrl/Cmd+F) to jump to a term.

**Jump to:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [V](#v) · [W](#w) · [Z](#z)

---

## A

**ACID** — Atomicity, Consistency, Isolation, Durability. The guarantees a traditional (relational) database transaction provides. → [ACID and Transactions](./Level-02-Data-Layer/05-ACID-and-Transactions/README.md)

**Active-Active / Active-Passive** — Two ways to run redundant sites. Active-active: every site serves traffic at once. Active-passive: one serves while the other waits on standby, ready to take over. → [High Availability and DR](./Level-06-Scale-and-Reliability/03-High-Availability-and-DR/README.md)

**Anycast** — Announcing the same IP address from many locations so the network routes each user to the nearest one. Used by DNS providers and CDNs. → [CDN](./Level-01-Building-Blocks/06-CDN/README.md)

**API (Application Programming Interface)** — A contract describing how one piece of software talks to another (e.g., a REST endpoint). → [API Design & REST](./Level-03-Communication/01-API-Design-REST/README.md)

**API Gateway** — A single entry point that sits in front of many backend services, handling auth, routing, rate limiting, etc. → [API Gateway](./Level-05-Architecture-Patterns/05-API-Gateway/README.md)

**At-Least-Once / At-Most-Once Delivery** — Delivery guarantees for messages. At-least-once never loses a message but may deliver it twice; at-most-once never duplicates but may lose one. → [Message Queues](./Level-03-Communication/04-Message-Queues/README.md)

**Authentication (AuthN) / Authorization (AuthZ)** — AuthN verifies *who you are* (login, tokens); AuthZ verifies *what you're allowed to do* (roles, permissions). → [Authentication and Authorization](./Level-03-Communication/08-Authentication-and-Authorization/README.md)

**Availability** — The percentage of time a system is up and able to serve requests. Measured in "nines" (99.9% = "three nines" ≈ 8.7 hours of downtime/year). → [High Availability and DR](./Level-06-Scale-and-Reliability/03-High-Availability-and-DR/README.md)

## B

**Back-of-the-Envelope Estimation** — Quick arithmetic on users, QPS, storage, and bandwidth, done before designing, to size the system. → [Capacity Planning and Estimation](./Level-06-Scale-and-Reliability/02-Capacity-Planning-and-Estimation/README.md)

**Backpressure** — When a downstream component is overwhelmed and signals upstream producers to slow down. → [Message Queues](./Level-03-Communication/04-Message-Queues/README.md)

**Bloom Filter** — A space-efficient probabilistic data structure that answers "is this item *definitely not* in the set, or *possibly* in it?" → [Probabilistic Data Structures](./Level-07-Big-Data-and-Specialized/06-Probabilistic-Data-Structures/README.md)

**Blue-Green Deployment** — Running two identical environments and switching all traffic from the old one (blue) to the new one (green) at once, with instant rollback. → [Deployment Strategies](./Level-06-Scale-and-Reliability/04-Deployment-Strategies/README.md)

**Bottleneck** — The single component that limits the throughput of the whole system. → [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

**B-Tree** — The balanced, sorted tree behind most relational indexes. It finds any key in a handful of page reads. → [Indexing](./Level-02-Data-Layer/03-Indexing/README.md)

**Bulkhead** — Isolating resources (thread pools, connections) per dependency so one slow dependency cannot sink everything else. → [Resilience Patterns](./Level-05-Architecture-Patterns/06-Resilience-Patterns/README.md)

## C

**Cache** — A small, fast store of frequently-accessed data placed close to where it's needed to avoid slow recomputation/fetching. → [Caching](./Level-01-Building-Blocks/03-Caching/README.md)

**Cache-Aside (Lazy Loading)** — The application checks the cache first and, on a miss, reads the database and fills the cache itself. → [Caching](./Level-01-Building-Blocks/03-Caching/README.md)

**Cache Stampede (Thundering Herd)** — Many requests miss the same expired cache key at once and all hit the database together. → [Caching](./Level-01-Building-Blocks/03-Caching/README.md)

**Canary Release** — Shipping a new version to a small slice of traffic first and widening only if its metrics stay healthy. → [Deployment Strategies](./Level-06-Scale-and-Reliability/04-Deployment-Strategies/README.md)

**CAP Theorem** — In the presence of a network **P**artition, a distributed system must choose between **C**onsistency and **A**vailability. → [CAP Theorem](./Level-04-Distributed-Systems/01-CAP-Theorem/README.md)

**CDC (Change Data Capture)** — Streaming a database's change log (WAL/binlog) to downstream systems — caches, search indexes, warehouses — so they stay in sync without dual writes. → [Change Data Capture](./Level-02-Data-Layer/10-Change-Data-Capture/README.md)

**CDN (Content Delivery Network)** — A globally distributed network of servers that caches content close to users. → [CDN](./Level-01-Building-Blocks/06-CDN/README.md)

**Chaos Engineering** — Deliberately injecting failures (killed instances, added latency, network partitions) under a stated hypothesis and a bounded blast radius, to prove a system degrades gracefully before real failures test it. → [Testing Distributed Systems](./Level-06-Scale-and-Reliability/08-Testing-Distributed-Systems/README.md)

**Circuit Breaker** — A wrapper that stops calling a failing dependency for a while, failing fast instead of piling up timeouts. → [Resilience Patterns](./Level-05-Architecture-Patterns/06-Resilience-Patterns/README.md)

**Cold Start** — The extra latency when a serverless function (or new server/connection) must be initialized from scratch before serving its first request. → [Serverless Architecture](./Level-05-Architecture-Patterns/08-Serverless-Architecture/README.md)

**Compaction** — The background merging of an LSM tree's files, which discards overwritten and deleted data. → [Database Internals](./Level-02-Data-Layer/04-Database-Internals/README.md)

**Connection Pool** — A reusable set of open database connections shared by requests, avoiding the cost of opening one per request. → [Connection Pooling](./Level-02-Data-Layer/06-Connection-Pooling/README.md)

**Consensus** — The problem of getting multiple distributed nodes to agree on a single value (solved by Paxos, Raft). → [Consensus: Paxos & Raft](./Level-04-Distributed-Systems/03-Consensus-Paxos-Raft/README.md)

**Consistency** — All nodes see the same data at the same time (strong), or eventually (eventual). → [Consistency Models](./Level-04-Distributed-Systems/02-Consistency-Models/README.md)

**Consistent Hashing** — A hashing technique that minimizes data movement when nodes are added/removed. Core to distributed caches and databases. → [Consistent Hashing](./Level-02-Data-Layer/08-Consistent-Hashing/README.md)

**Consumer Group** — A set of consumers that split a topic's partitions among themselves so each message is handled by exactly one of them. → [Pub/Sub](./Level-03-Communication/05-Pub-Sub/README.md)

**CQRS** — Command Query Responsibility Segregation. Separate the write model from the read model. → [CQRS & Event Sourcing](./Level-05-Architecture-Patterns/03-CQRS-and-Event-Sourcing/README.md)

**CRDT (Conflict-free Replicated Data Type)** — A data structure (counter, set, register, sequence) whose replicas can be updated concurrently without coordination and are guaranteed to converge when merged, because the merge is commutative, associative, and idempotent. Gives *strong eventual consistency*; cannot enforce cross-object invariants. → [CRDTs and Conflict Resolution](./Level-04-Distributed-Systems/09-CRDTs-and-Conflict-Resolution/README.md)

**Crypto-shredding** — Deleting data everywhere at once by destroying the per-user or per-tenant encryption key that protects it; the standard way to honor erasure requests in immutable logs and backups. → [Data Privacy, Encryption & Compliance](./Level-06-Scale-and-Reliability/09-Data-Privacy-and-Encryption/README.md)

## D

**Data Lake / Lakehouse** — A data lake stores raw files cheaply in object storage. A lakehouse adds table formats (Iceberg, Delta) so those files can be queried like a warehouse. → [Data Warehouses & Lakes](./Level-07-Big-Data-and-Specialized/03-Data-Warehouses-and-Lakes/README.md)

**Data Warehouse** — A database built for analytics: columnar storage, huge scans, few writes. → [Data Warehouses & Lakes](./Level-07-Big-Data-and-Specialized/03-Data-Warehouses-and-Lakes/README.md)

**DAU/MAU** — Daily/Monthly Active Users. Core inputs to capacity estimation. → [Capacity Planning and Estimation](./Level-06-Scale-and-Reliability/02-Capacity-Planning-and-Estimation/README.md)

**Dead-Letter Queue (DLQ)** — Where messages go after repeatedly failing processing, so they stop blocking the queue and can be inspected. → [Message Queues](./Level-03-Communication/04-Message-Queues/README.md)

**Denormalization** — Intentionally duplicating data to make reads faster (at the cost of harder writes). → [Data Modeling](./Level-02-Data-Layer/07-Data-Modeling/README.md)

**Distributed Lock** — A lock that gives one process at a time exclusive access to a resource across machines. → [Distributed Locking](./Level-04-Distributed-Systems/08-Distributed-Locking/README.md)

**DNS (Domain Name System)** — Translates human-readable domain names (google.com) into IP addresses. → [DNS](./Level-00-Foundations/05-DNS/README.md)

## E

**Embedding** — A dense numeric vector representing the *meaning* of text/images, enabling semantic (similarity) search instead of exact keyword match. → [AI & LLM Infrastructure](./Level-07-Big-Data-and-Specialized/09-AI-and-LLM-Infrastructure/README.md)

**Envelope Encryption** — Encrypting data with a local data key (DEK), then encrypting that key with a master key (KEK) that never leaves the KMS; rotation and deletion become cheap key operations instead of data rewrites. → [Data Privacy, Encryption & Compliance](./Level-06-Scale-and-Reliability/09-Data-Privacy-and-Encryption/README.md)

**Erasure Coding** — Storing data as k data pieces plus m parity pieces so that any k of them can rebuild it. Far cheaper than keeping three full copies. → [Design: Distributed File System](./Bonus-Real-World-Architectures/37-Distributed-File-System/README.md)

**Error Budget** — The amount of unreliability an SLO allows (99.9% leaves 0.1%). Spend it on releases; stop when it is gone. → [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

**ETL / ELT** — Extract-Transform-Load reshapes data before loading it into a warehouse. ELT loads it first and transforms inside the warehouse. → [Batch Processing](./Level-07-Big-Data-and-Specialized/01-Batch-Processing/README.md)

**Event Loop** — A single thread that waits on thousands of sockets at once (epoll/kqueue) and runs a small handler only when one is ready; the concurrency model behind Nginx, Node.js, and Redis. Rule: never block it. → [Concurrency Models & Async I/O](./Level-01-Building-Blocks/08-Concurrency-and-Async-IO/README.md)

**Event Sourcing** — Storing state as an immutable log of events rather than as current values. → [CQRS & Event Sourcing](./Level-05-Architecture-Patterns/03-CQRS-and-Event-Sourcing/README.md)

**Eventual Consistency** — Given no new updates, all replicas will *eventually* converge to the same value. → [Consistency Models](./Level-04-Distributed-Systems/02-Consistency-Models/README.md)

**Exactly-Once** — A processing guarantee that each message affects the system's state once and only once (usually achieved via idempotency + dedup). → [Idempotency and Exactly-Once](./Level-04-Distributed-Systems/07-Idempotency-and-Exactly-Once/README.md)

**Expand / Contract** — The zero-downtime schema-change pattern: add the new shape alongside the old, dual-write and backfill, switch reads, then remove the old shape in a later release — so old and new code always coexist safely. → [Schema Migrations](./Level-02-Data-Layer/11-Schema-Migrations/README.md)

## F

**FaaS (Function as a Service)** — Serverless compute where you deploy single functions triggered by events; the platform handles servers and scaling (AWS Lambda, Cloud Functions). → [Serverless Architecture](./Level-05-Architecture-Patterns/08-Serverless-Architecture/README.md)

**Failover** — Automatically switching to a standby component when the primary fails. → [High Availability and DR](./Level-06-Scale-and-Reliability/03-High-Availability-and-DR/README.md)

**Fan-out** — Delivering one piece of data to many destinations (e.g., one tweet to all followers' timelines). → [Design: News Feed](./Bonus-Real-World-Architectures/06-News-Feed-Twitter/README.md)

**Feature Flag** — A runtime switch that turns a code path on or off without a deploy. → [Deployment Strategies](./Level-06-Scale-and-Reliability/04-Deployment-Strategies/README.md)

**Feature Store** — A system that keeps ML features in two synchronized forms: an *online* low-latency store for serving and an *offline* historical store for training, with point-in-time correctness so models never train on data from the future. → [Recommendation & ML Systems](./Level-07-Big-Data-and-Specialized/05-Recommendation-and-ML-Systems/README.md)

**Fencing Token** — A monotonically increasing number issued with a lock or lease; the protected resource rejects any request carrying an older token, so a client that lost its lock without noticing cannot corrupt data. → [Distributed Locking](./Level-04-Distributed-Systems/08-Distributed-Locking/README.md)

## G

**Geohash** — An encoding that turns a latitude/longitude into a short string, where a shared prefix means nearby. → [Geospatial Indexing](./Level-07-Big-Data-and-Specialized/07-Geospatial-Indexing/README.md)

**Gossip Protocol** — An epidemic-style protocol where each node periodically shares what it knows with a few random peers, so cluster-wide state (membership, liveness, metadata) converges in O(log N) rounds with no coordinator (Cassandra, Consul, Redis Cluster). → [Gossip and Failure Detection](./Level-04-Distributed-Systems/10-Gossip-and-Failure-Detection/README.md)

**GraphQL** — A query language for APIs in which the client asks for exactly the fields it needs from a single endpoint. → [GraphQL](./Level-03-Communication/02-GraphQL/README.md)

**Green Threads (Goroutines, Virtual Threads)** — Lightweight threads scheduled by the language runtime rather than the OS, costing a few KB each, so millions can exist; they park cheaply on I/O while a handful of OS threads do the actual work. → [Concurrency Models & Async I/O](./Level-01-Building-Blocks/08-Concurrency-and-Async-IO/README.md)

**gRPC** — A high-performance RPC framework that uses Protocol Buffers over HTTP/2. → [gRPC and RPC](./Level-03-Communication/03-gRPC-and-RPC/README.md)

## H

**Hash** — A function that maps data of any size to a fixed-size value. Used for lookups, sharding, and integrity.

**Head-of-Line Blocking** — One slow item at the front of a queue or connection holding up everything behind it. → [HTTP and HTTPS](./Level-00-Foundations/06-HTTP-and-HTTPS/README.md)

**Heartbeat** — A periodic "I'm alive" signal used to detect node failures. → [Gossip and Failure Detection](./Level-04-Distributed-Systems/10-Gossip-and-Failure-Detection/README.md)

**Hinted Handoff** — When a replica is down, another node keeps its writes as "hints" and replays them when it returns. → [Design: Key-Value Store](./Bonus-Real-World-Architectures/27-Key-Value-Store/README.md)

**HNSW (Hierarchical Navigable Small World)** — The layered-graph index most vector databases use for fast approximate nearest-neighbor search. → [AI & LLM Infrastructure](./Level-07-Big-Data-and-Specialized/09-AI-and-LLM-Infrastructure/README.md)

**Horizontal Scaling (Scale-out)** — Adding more machines. → [Scalability](./Level-01-Building-Blocks/01-Scalability/README.md)

**Hotspot / Hot Key** — A single key or shard receiving a disproportionate share of traffic. → [Sharding and Partitioning](./Level-02-Data-Layer/02-Sharding-and-Partitioning/README.md)

**Hybrid Logical Clock (HLC)** — A timestamp that combines wall-clock time with a logical counter, giving causally consistent ordering that stays close to real time. → [Clocks and Ordering](./Level-04-Distributed-Systems/06-Clocks-and-Ordering/README.md)

**HyperLogLog** — A probabilistic structure that estimates the number of distinct items using a few kilobytes of memory. → [Probabilistic Data Structures](./Level-07-Big-Data-and-Specialized/06-Probabilistic-Data-Structures/README.md)

## I

**Idempotency** — An operation that can be applied multiple times without changing the result beyond the first application. → [Idempotency and Exactly-Once](./Level-04-Distributed-Systems/07-Idempotency-and-Exactly-Once/README.md)

**Index** — A data structure (often a B-Tree) that makes database lookups fast at the cost of extra storage and slower writes. → [Indexing](./Level-02-Data-Layer/03-Indexing/README.md)

**Inverted Index** — A map from each word to the documents that contain it. The core of full-text search. → [Search Systems](./Level-07-Big-Data-and-Specialized/04-Search-Systems/README.md)

**Isolation Level** — How much concurrent transactions can see of each other (read committed, repeatable read, serializable). → [ACID and Transactions](./Level-02-Data-Layer/05-ACID-and-Transactions/README.md)

## J

**JWT (JSON Web Token)** — A signed, self-contained token (`header.payload.signature`) that lets servers verify identity without a session store. Revocation is its weak spot. → [Authentication and Authorization](./Level-03-Communication/08-Authentication-and-Authorization/README.md)

## K

**Key-Value Store** — A database with just get and put by key: simple, fast, and easy to partition. → [Design: Key-Value Store](./Bonus-Real-World-Architectures/27-Key-Value-Store/README.md)

**KMS (Key Management Service)** — A managed service that holds master encryption keys and wraps or unwraps data keys without ever exporting the master key. → [Data Privacy, Encryption & Compliance](./Level-06-Scale-and-Reliability/09-Data-Privacy-and-Encryption/README.md)

## L

**Lamport Clock** — A logical counter that orders events without relying on wall-clock time. → [Clocks and Ordering](./Level-04-Distributed-Systems/06-Clocks-and-Ordering/README.md)

**Latency** — Time to handle a single request (e.g., 50ms). Often discussed as percentiles: p50, p99. → [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

**Leader Election** — Choosing one node to coordinate, and choosing a new one safely when it fails. → [Leader Election](./Level-04-Distributed-Systems/05-Leader-Election/README.md)

**Lease** — A lock or leadership claim that expires on its own unless it is renewed. → [Distributed Locking](./Level-04-Distributed-Systems/08-Distributed-Locking/README.md)

**Linearizability** — The strongest single-object consistency: every operation appears to take effect instantly, in real-time order. → [Consistency Models](./Level-04-Distributed-Systems/02-Consistency-Models/README.md)

**Little's Law** — Work in flight = throughput × latency. The one formula for sizing thread pools, connection pools, and queue depth: 10K requests/s at 200 ms means 2,000 requests in progress at all times. → [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

**Load Balancer** — Distributes incoming requests across multiple servers. → [Load Balancing](./Level-01-Building-Blocks/02-Load-Balancing/README.md)

**Long Polling** — The client sends a request that the server holds open until it has news; then the client immediately asks again. → [WebSockets and Real-Time](./Level-03-Communication/06-WebSockets-and-Realtime/README.md)

**LSM Tree (Log-Structured Merge Tree)** — A write-optimized storage structure used by Cassandra, RocksDB, etc. → [Database Internals](./Level-02-Data-Layer/04-Database-Internals/README.md)

## M

**MapReduce** — A batch model that processes huge datasets with a parallel map step followed by a grouped reduce step. → [Batch Processing](./Level-07-Big-Data-and-Specialized/01-Batch-Processing/README.md)

**Materialized View** — A precomputed query result stored like a table and refreshed as the source data changes. → [CQRS & Event Sourcing](./Level-05-Architecture-Patterns/03-CQRS-and-Event-Sourcing/README.md)

**Merkle Tree** — A tree of hashes that lets two replicas find the differences between their data by comparing only a few hashes. → [Design: Key-Value Store](./Bonus-Real-World-Architectures/27-Key-Value-Store/README.md)

**Message Queue** — A buffer that decouples producers from consumers, smoothing load and adding resilience. → [Message Queues](./Level-03-Communication/04-Message-Queues/README.md)

**Microservices** — An architecture of small, independently deployable services. → [Monolith vs Microservices](./Level-05-Architecture-Patterns/01-Monolith-vs-Microservices/README.md)

**mTLS (Mutual TLS)** — TLS where *both* client and server present certificates; the standard for service-to-service authentication in zero-trust networks and service meshes. → [Service Mesh](./Level-05-Architecture-Patterns/09-Service-Mesh/README.md)

**Multi-Tenancy** — One deployment serving many customers (tenants) whose data and traffic must stay isolated. Models range from *pool* (shared rows tagged by tenant) to *bridge* (a database per tenant) to *silo* (a full stack per tenant). → [Multi-Tenancy](./Level-05-Architecture-Patterns/10-Multi-Tenancy/README.md)

**MVCC (Multi-Version Concurrency Control)** — Keeping several versions of a row so that readers see a consistent snapshot without blocking writers. → [ACID and Transactions](./Level-02-Data-Layer/05-ACID-and-Transactions/README.md)

## N

**N+1 Query Problem** — Fetching a list with one query and then running one more query for every item in it. → [GraphQL](./Level-03-Communication/02-GraphQL/README.md)

**NewSQL / Distributed SQL** — Databases offering SQL + ACID transactions with horizontal scale (Google Spanner, CockroachDB, TiDB). → [Specialized Databases](./Level-07-Big-Data-and-Specialized/08-Specialized-Databases/README.md)

**Noisy Neighbor** — One tenant's heavy workload degrading everyone else on shared infrastructure; contained with per-tenant limits, fair queuing, bulkheads, and shuffle sharding. → [Multi-Tenancy](./Level-05-Architecture-Patterns/10-Multi-Tenancy/README.md)

**Normalization** — Organizing tables so that each fact is stored once, at the cost of joins when reading. → [Data Modeling](./Level-02-Data-Layer/07-Data-Modeling/README.md)

**NoSQL** — Non-relational databases (key-value, document, column-family, graph) optimized for scale and flexibility. → [Databases: SQL vs NoSQL](./Level-01-Building-Blocks/04-Databases-SQL-vs-NoSQL/README.md)

## O

**OAuth 2.0** — The standard protocol for *delegated authorization* — letting an app act on your behalf without seeing your password. **OIDC** adds an identity (login) layer on top of it. → [Authentication and Authorization](./Level-03-Communication/08-Authentication-and-Authorization/README.md)

**Object Storage** — Storage for large blobs addressed by key over HTTP (S3, GCS, Azure Blob). → [Object Storage](./Level-02-Data-Layer/09-Object-Storage/README.md)

**Observability** — Being able to understand what a system is doing from its metrics, logs, and traces. → [Observability](./Level-06-Scale-and-Reliability/01-Observability/README.md)

**OIDC (OpenID Connect)** — An identity layer on top of OAuth 2.0 that tells an app who the user is through a signed ID token. → [Authentication and Authorization](./Level-03-Communication/08-Authentication-and-Authorization/README.md)

**OLTP / OLAP** — OLTP systems handle many small transactions (orders, payments). OLAP systems run large analytical queries over history. → [Data Warehouses & Lakes](./Level-07-Big-Data-and-Specialized/03-Data-Warehouses-and-Lakes/README.md)

**Optimistic / Pessimistic Locking** — Pessimistic locking blocks others before changing data. Optimistic locking lets everyone proceed and rejects a write if the row changed underneath it. → [ACID and Transactions](./Level-02-Data-Layer/05-ACID-and-Transactions/README.md)

**Outbox Pattern** — Writing an event to an "outbox" table in the *same transaction* as the business change, then relaying it to a queue — the standard fix for the dual-write problem. → [Change Data Capture](./Level-02-Data-Layer/10-Change-Data-Capture/README.md)

## P

**PACELC** — An extension of CAP: during a Partition choose Availability or Consistency; Else choose Latency or Consistency. → [CAP Theorem](./Level-04-Distributed-Systems/01-CAP-Theorem/README.md)

**Partition (Sharding)** — Splitting one dataset across multiple machines. → [Sharding and Partitioning](./Level-02-Data-Layer/02-Sharding-and-Partitioning/README.md)

**Partition Tolerance** — The system keeps working despite network failures between nodes. → [CAP Theorem](./Level-04-Distributed-Systems/01-CAP-Theorem/README.md)

**Passkey (WebAuthn)** — A phishing-resistant login credential: the server stores only a public key and the device signs a per-login challenge, so there is no shared secret to steal or stuff. → [Authentication and Authorization](./Level-03-Communication/08-Authentication-and-Authorization/README.md)

**Paxos / Raft** — The two best-known consensus algorithms. Raft was designed to be the understandable one. → [Consensus: Paxos & Raft](./Level-04-Distributed-Systems/03-Consensus-Paxos-Raft/README.md)

**Percentile (p50, p95, p99)** — p99 latency = the value below which 99% of requests fall. Tail latency matters at scale. → [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

**Phi-Accrual Failure Detector** — A failure detector that outputs a continuous suspicion level (φ) calibrated to a peer's observed heartbeat history instead of a fixed timeout; used by Cassandra and Akka. → [Gossip and Failure Detection](./Level-04-Distributed-Systems/10-Gossip-and-Failure-Detection/README.md)

**Presigned URL** — A time-limited signed link that lets a client upload to or download from object storage directly. → [Object Storage](./Level-02-Data-Layer/09-Object-Storage/README.md)

**Protocol Buffers (Protobuf)** — A compact binary serialization format with a schema and numbered fields. → [Data Serialization and Schema Evolution](./Level-03-Communication/09-Data-Serialization-and-Schema-Evolution/README.md)

**Proxy** — An intermediary. A *forward* proxy represents clients; a *reverse* proxy represents servers. → [Proxies](./Level-01-Building-Blocks/05-Proxies/README.md)

**Pub/Sub** — Publish-Subscribe. Publishers send messages to topics; subscribers receive them without knowing each other. → [Pub/Sub](./Level-03-Communication/05-Pub-Sub/README.md)

## Q

**QPS / RPS** — Queries/Requests Per Second. The fundamental throughput unit. → [Capacity Planning and Estimation](./Level-06-Scale-and-Reliability/02-Capacity-Planning-and-Estimation/README.md)

**Quorum** — The minimum number of nodes that must agree for an operation to succeed (e.g., majority). → [Database Replication](./Level-02-Data-Layer/01-Database-Replication/README.md)

## R

**RAG (Retrieval-Augmented Generation)** — Retrieving relevant documents (usually via vector search) and inserting them into an LLM's prompt so answers are grounded in your data. → [AI & LLM Infrastructure](./Level-07-Big-Data-and-Specialized/09-AI-and-LLM-Infrastructure/README.md)

**Rate Limiting** — Capping how many requests a client may make in a time window. → [Rate Limiting](./Level-03-Communication/07-Rate-Limiting/README.md)

**RBAC / ABAC** — Role-Based vs Attribute-Based Access Control: authorization by assigned roles vs by evaluating attributes of the user, resource, and context. → [Authentication and Authorization](./Level-03-Communication/08-Authentication-and-Authorization/README.md)

**Read Replica** — A copy of the database that serves reads to take load off the primary. → [Database Replication](./Level-02-Data-Layer/01-Database-Replication/README.md)

**Read-Your-Writes** — A guarantee that after you write something, your own later reads will see it. → [Consistency Models](./Level-04-Distributed-Systems/02-Consistency-Models/README.md)

**Replication** — Keeping copies of data on multiple machines for durability and read scaling. → [Database Replication](./Level-02-Data-Layer/01-Database-Replication/README.md)

**Replication Lag** — How far a replica is behind its primary. → [Database Replication](./Level-02-Data-Layer/01-Database-Replication/README.md)

**Retry with Backoff and Jitter** — Waiting longer after each failed attempt, with some randomness added so that clients do not all retry at the same moment. → [Resilience Patterns](./Level-05-Architecture-Patterns/06-Resilience-Patterns/README.md)

**Reverse Proxy** — A server that forwards client requests to backend servers (e.g., Nginx). → [Proxies](./Level-01-Building-Blocks/05-Proxies/README.md)

**RPO / RTO** — Recovery Point Objective is how much data you can afford to lose. Recovery Time Objective is how long you can afford to be down. → [High Availability and DR](./Level-06-Scale-and-Reliability/03-High-Availability-and-DR/README.md)

## S

**Saga** — A sequence of local transactions with compensating actions, used for distributed transactions. → [Saga & Orchestration](./Level-05-Architecture-Patterns/07-Saga-and-Orchestration/README.md)

**Scatter-Gather** — Sending a query to every shard in parallel and merging the answers. → [Sharding and Partitioning](./Level-02-Data-Layer/02-Sharding-and-Partitioning/README.md)

**Schema Registry** — A service that stores versioned schemas for event streams, hands producers a compact schema ID to embed in each message, and rejects incompatible schema changes at registration time. → [Data Serialization and Schema Evolution](./Level-03-Communication/09-Data-Serialization-and-Schema-Evolution/README.md)

**Serializability** — The strongest transaction isolation: the outcome is the same as running the transactions one at a time. → [Consistency Models](./Level-04-Distributed-Systems/02-Consistency-Models/README.md)

**Serverless** — Running code without managing servers; you pay per use and the platform scales (even to zero). See FaaS. → [Serverless Architecture](./Level-05-Architecture-Patterns/08-Serverless-Architecture/README.md)

**Server-Sent Events (SSE)** — A one-way stream of events from server to browser over an ordinary HTTP response. → [WebSockets and Real-Time](./Level-03-Communication/06-WebSockets-and-Realtime/README.md)

**Service Mesh** — An infrastructure layer of sidecar proxies plus a control plane that handles mTLS, retries, routing, and telemetry between microservices (Istio, Linkerd). → [Service Mesh](./Level-05-Architecture-Patterns/09-Service-Mesh/README.md)

**Sharding** — See Partition. → [Sharding and Partitioning](./Level-02-Data-Layer/02-Sharding-and-Partitioning/README.md)

**Shuffle Sharding** — Assigning each tenant to a small random subset of nodes so that a misbehaving tenant overloads only its own subset — and shares that exact subset with almost no one else. → [Multi-Tenancy](./Level-05-Architecture-Patterns/10-Multi-Tenancy/README.md)

**Sidecar** — A helper process deployed alongside a service (common in service meshes). → [Service Mesh](./Level-05-Architecture-Patterns/09-Service-Mesh/README.md)

**SLA / SLO / SLI** — Service Level Agreement / Objective / Indicator. The promised, targeted, and measured reliability. → [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

**Snowflake ID** — A 64-bit, roughly time-sortable unique ID made of a timestamp, a machine ID, and a sequence number. → [Design: Unique ID Generator](./Bonus-Real-World-Architectures/26-Unique-ID-Generator/README.md)

**Split-Brain** — Two nodes both believing they are the leader, usually after a network partition. → [Leader Election](./Level-04-Distributed-Systems/05-Leader-Election/README.md)

**SSTable (Sorted String Table)** — An immutable, sorted file of key-value pairs: the on-disk unit of an LSM tree. → [Database Internals](./Level-02-Data-Layer/04-Database-Internals/README.md)

**Stateless** — A server that keeps no client session data between requests, making it easy to scale and replace. → [Stateless vs Stateful](./Level-01-Building-Blocks/07-Stateless-vs-Stateful/README.md)

**Sticky Session** — Routing a user's requests to the same server every time because their session lives there. → [Stateless vs Stateful](./Level-01-Building-Blocks/07-Stateless-vs-Stateful/README.md)

**Strangler Fig** — Migrating off a legacy system by routing one feature at a time to its replacement until nothing is left. → [Monolith vs Microservices](./Level-05-Architecture-Patterns/01-Monolith-vs-Microservices/README.md)

**SWIM** — Scalable Weakly-consistent Infection-style Membership: a gossip-based protocol that detects failures with random direct pings, indirect pings through other members, and a suspicion period the accused node can refute (Consul/Serf, Ringpop). → [Gossip and Failure Detection](./Level-04-Distributed-Systems/10-Gossip-and-Failure-Detection/README.md)

## T

**Throttling** — Deliberately slowing or rejecting requests to protect a system. → [Rate Limiting](./Level-03-Communication/07-Rate-Limiting/README.md)

**Throughput** — How much work per unit time the system handles (e.g., requests/sec, MB/sec). → [Latency, Throughput & Performance](./Level-00-Foundations/07-Latency-Throughput-Performance/README.md)

**Time-Series Database (TSDB)** — A database optimized for timestamped, append-only data (metrics, IoT) with heavy compression and time-window queries (InfluxDB, Prometheus). → [Specialized Databases](./Level-07-Big-Data-and-Specialized/08-Specialized-Databases/README.md)

**Token Bucket** — A rate-limiting algorithm: tokens refill at a steady rate, each request spends one, and bursts are allowed up to the bucket size. → [Rate Limiting](./Level-03-Communication/07-Rate-Limiting/README.md)

**Tokenization** — Replacing a sensitive value (such as a card number) with a random token and keeping the real value only in a tightly controlled vault; the main tool for shrinking compliance scope. → [Data Privacy, Encryption & Compliance](./Level-06-Scale-and-Reliability/09-Data-Privacy-and-Encryption/README.md)

**Tombstone** — A marker recording that something was deleted, kept so that replicas and late-arriving updates learn about the deletion instead of resurrecting the data; used in LSM trees, Kafka compaction, CRDTs, and gossip membership. → [Database Internals](./Level-02-Data-Layer/04-Database-Internals/README.md)

**Trie** — A prefix tree in which each path from the root spells a string. The basis of autocomplete. → [Design: Typeahead](./Bonus-Real-World-Architectures/10-Typeahead-Autocomplete/README.md)

**TTL (Time To Live)** — How long a cached/stored item remains valid before expiring. → [Caching](./Level-01-Building-Blocks/03-Caching/README.md)

**Two-Phase Commit (2PC)** — A protocol in which a coordinator asks every participant to prepare, then tells them all to commit or all to abort. → [Distributed Transactions](./Level-04-Distributed-Systems/04-Distributed-Transactions/README.md)

## V

**Vector Clock** — One counter per node, carried with the data, that lets replicas tell whether two versions are ordered or concurrent. → [Clocks and Ordering](./Level-04-Distributed-Systems/06-Clocks-and-Ordering/README.md)

**Vector Database** — A database that indexes embeddings for fast approximate nearest-neighbor (semantic) search (pgvector, Pinecone, Milvus, Qdrant). → [AI & LLM Infrastructure](./Level-07-Big-Data-and-Specialized/09-AI-and-LLM-Infrastructure/README.md)

**Vertical Scaling (Scale-up)** — Making a single machine more powerful (more CPU/RAM). → [Scalability](./Level-01-Building-Blocks/01-Scalability/README.md)

**Virtual Node (vnode)** — Giving each physical server many positions on a consistent-hash ring so that load spreads evenly. → [Consistent Hashing](./Level-02-Data-Layer/08-Consistent-Hashing/README.md)

## W

**Watermark** — A stream processor's estimate that no events older than a given time are still on their way, which lets it close a window. → [Stream Processing](./Level-07-Big-Data-and-Specialized/02-Stream-Processing/README.md)

**Webhook** — An HTTP callback your platform sends to a customer's URL when an event happens — "we call you" instead of you polling us. → [Design: Webhook Delivery](./Bonus-Real-World-Architectures/36-Webhook-Delivery-Service/README.md)

**WebSocket** — A protocol for persistent, full-duplex (two-way) communication between client and server. → [WebSockets and Real-Time](./Level-03-Communication/06-WebSockets-and-Realtime/README.md)

**Write-Ahead Log (WAL)** — A durable append-only log written before applying changes, enabling crash recovery. → [Database Internals](./Level-02-Data-Layer/04-Database-Internals/README.md)

**Write-Through / Write-Behind** — Cache write policies. Write-through updates the cache and the database together. Write-behind updates the cache now and the database later. → [Caching](./Level-01-Building-Blocks/03-Caching/README.md)

## Z

**Zero Trust** — A security model in which no request is trusted because of where it comes from; each one is authenticated and authorized. → [Security at Scale](./Level-06-Scale-and-Reliability/05-Security-at-Scale/README.md)

**ZooKeeper / etcd** — Small, strongly consistent stores that other systems use for configuration, leader election, and locks. → [Design: Coordination Service](./Bonus-Real-World-Architectures/39-Distributed-Coordination-Service/README.md)

---

*Missing a term? It's defined in the topic where it first appears — check the relevant level.*
