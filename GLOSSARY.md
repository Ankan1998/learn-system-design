# 📋 System Design Glossary

A single place to look up every term used in this curriculum. Skim it now; return to it whenever a word is unfamiliar.

> Tip: Use your browser's "Find" (Ctrl/Cmd+F) to jump to a term.

---

## A

**ACID** — Atomicity, Consistency, Isolation, Durability. The guarantees a traditional (relational) database transaction provides.

**Availability** — The percentage of time a system is up and able to serve requests. Measured in "nines" (99.9% = "three nines" ≈ 8.7 hours of downtime/year).

**API (Application Programming Interface)** — A contract describing how one piece of software talks to another (e.g., a REST endpoint).

**API Gateway** — A single entry point that sits in front of many backend services, handling auth, routing, rate limiting, etc.

## B

**Backpressure** — When a downstream component is overwhelmed and signals upstream producers to slow down.

**Bloom Filter** — A space-efficient probabilistic data structure that answers "is this item *definitely not* in the set, or *possibly* in it?"

**Bottleneck** — The single component that limits the throughput of the whole system.

## C

**Cache** — A small, fast store of frequently-accessed data placed close to where it's needed to avoid slow recomputation/fetching.

**CAP Theorem** — In the presence of a network **P**artition, a distributed system must choose between **C**onsistency and **A**vailability.

**CDN (Content Delivery Network)** — A globally distributed network of servers that caches content close to users.

**Consensus** — The problem of getting multiple distributed nodes to agree on a single value (solved by Paxos, Raft).

**Consistency** — All nodes see the same data at the same time (strong), or eventually (eventual).

**Consistent Hashing** — A hashing technique that minimizes data movement when nodes are added/removed. Core to distributed caches and databases.

**CQRS** — Command Query Responsibility Segregation. Separate the write model from the read model.

## D

**DAU/MAU** — Daily/Monthly Active Users. Core inputs to capacity estimation.

**Denormalization** — Intentionally duplicating data to make reads faster (at the cost of harder writes).

**DNS (Domain Name System)** — Translates human-readable domain names (google.com) into IP addresses.

## E

**Eventual Consistency** — Given no new updates, all replicas will *eventually* converge to the same value.

**Event Sourcing** — Storing state as an immutable log of events rather than as current values.

**Exactly-Once** — A processing guarantee that each message affects the system's state once and only once (usually achieved via idempotency + dedup).

## F

**Fan-out** — Delivering one piece of data to many destinations (e.g., one tweet to all followers' timelines).

**Failover** — Automatically switching to a standby component when the primary fails.

## H

**Hash** — A function that maps data of any size to a fixed-size value. Used for lookups, sharding, and integrity.

**Heartbeat** — A periodic "I'm alive" signal used to detect node failures.

**Horizontal Scaling (Scale-out)** — Adding more machines.

**Hotspot / Hot Key** — A single key or shard receiving a disproportionate share of traffic.

## I

**Idempotency** — An operation that can be applied multiple times without changing the result beyond the first application.

**Index** — A data structure (often a B-Tree) that makes database lookups fast at the cost of extra storage and slower writes.

## L

**Latency** — Time to handle a single request (e.g., 50ms). Often discussed as percentiles: p50, p99.

**Load Balancer** — Distributes incoming requests across multiple servers.

**LSM Tree (Log-Structured Merge Tree)** — A write-optimized storage structure used by Cassandra, RocksDB, etc.

## M

**Message Queue** — A buffer that decouples producers from consumers, smoothing load and adding resilience.

**Microservices** — An architecture of small, independently deployable services.

## N

**NoSQL** — Non-relational databases (key-value, document, column-family, graph) optimized for scale and flexibility.

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

**Rate Limiting** — Capping how many requests a client may make in a time window.

**Replication** — Keeping copies of data on multiple machines for durability and read scaling.

**Reverse Proxy** — A server that forwards client requests to backend servers (e.g., Nginx).

## S

**Saga** — A sequence of local transactions with compensating actions, used for distributed transactions.

**Sharding** — See Partition.

**Sidecar** — A helper process deployed alongside a service (common in service meshes).

**SLA / SLO / SLI** — Service Level Agreement / Objective / Indicator. The promised, targeted, and measured reliability.

**Stateless** — A server that keeps no client session data between requests, making it easy to scale and replace.

## T

**Throughput** — How much work per unit time the system handles (e.g., requests/sec, MB/sec).

**Throttling** — Deliberately slowing or rejecting requests to protect a system.

**TTL (Time To Live)** — How long a cached/stored item remains valid before expiring.

## V

**Vertical Scaling (Scale-up)** — Making a single machine more powerful (more CPU/RAM).

## W

**WebSocket** — A protocol for persistent, full-duplex (two-way) communication between client and server.

**Write-Ahead Log (WAL)** — A durable append-only log written before applying changes, enabling crash recovery.

---

*Missing a term? It's defined in the topic where it first appears — check the relevant level.*
