# ✍️ Style Guide & Chapter Template

This document defines how every chapter in this curriculum is written, so the experience is consistent from Level 0 to the Bonus designs. If you contribute, follow this.

---

## Core writing principles

1. **Explain like the reader is smart but new.** No assumed jargon. The first time a term appears, define it.
2. **Analogy first, abstraction second.** Anchor every concept to something physical/everyday (a library, a restaurant, a highway, a post office) *before* the technical definition.
3. **Show, don't just tell.** Every major concept gets a diagram (Mermaid) and a concrete named example ("Netflix does X because Y").
4. **Always name the trade-off.** No technique is free. State what you give up.
5. **Numbers matter.** Use real-ish figures (latencies, QPS, storage sizes) so scale feels concrete.
6. **Short paragraphs, lots of headers, tables for comparisons.** Optimized for skimming and revision.

---

## Diagrams

- Use **Mermaid** code blocks (` ```mermaid `) — they render natively on GitHub, no image files needed.
- Prefer `flowchart`, `sequenceDiagram`, `erDiagram`, and `graph` types.
- Add `style` lines with soft fills and `color:#000` so text stays readable in both light and dark themes.
- Every diagram must have a one-line caption above or below explaining what to look at.

---

## Template A — Concept topics (Levels 0–7)

Every concept `README.md` should follow this skeleton:

```markdown
# <Topic Title>

> One-sentence definition a beginner could repeat.

**Level:** X · **Topic:** N · **Prerequisites:** [links]

---

## 🎯 The Problem (Why does this exist?)
Start with the pain. What breaks without this concept? Tell a tiny story.

## 🌍 Real-World Analogy
Anchor it to everyday life.

## 🧠 Core Idea
The actual explanation, built up step by step. Use sub-headers.

## 📊 How It Works (Diagram)
One or more Mermaid diagrams with captions.

## 🔧 Types / Variations / Strategies
Tables comparing the options.

## 🏢 Real-World Examples
Named systems: "How Netflix / Uber / Amazon / Discord uses this." At least 2–3.

## ⚖️ Trade-offs (Pros & Cons)
A table or two-column list. Always present.

## ✅ When to Use / ❌ When NOT to Use
Practical decision guidance.

## ⚠️ Common Pitfalls & Gotchas
Mistakes people actually make.

## 🎤 Interview Tips
What interviewers probe; how to talk about it; common follow-ups.

## 📝 TL;DR / Key Takeaways
3–6 bullet points for fast revision.

## 🧪 Test Yourself
3–5 questions (no answers, or collapsible answers) to self-check.

## 📚 Further Reading
Links to canonical books, papers, and engineering blogs.
```

---

## Template B — Real-world design case studies (Bonus folder)

Each design `README.md` follows the standard system-design-interview flow:

```markdown
# Design <System> (e.g., Design Uber)

> One-line description and why it's a classic problem.

**Difficulty:** ⭐–⭐⭐⭐⭐⭐ · **Builds on:** [topic links]

## 1. 🎯 Problem Statement & Scope
What are we building? What's in/out of scope?

## 2. 📋 Requirements
### Functional Requirements
### Non-Functional Requirements (scale, latency, availability, consistency)

## 3. 🧮 Capacity Estimation (Back-of-the-envelope)
DAU, QPS (read/write), storage/year, bandwidth. Show the math.

## 4. 🔌 API Design
The key endpoints / RPCs.

## 5. 🗄️ Data Model
Tables/collections, key fields, and the chosen storage type with justification.

## 6. 🏗️ High-Level Architecture
The big Mermaid diagram + a walk-through of the request flow.

## 7. 🔬 Deep Dives
The 2–4 genuinely hard parts of THIS problem, each solved in detail with diagrams.

## 8. 📈 Scaling, Bottlenecks & Failure Modes
What breaks first as you grow, and how to fix it.

## 9. ⚖️ Trade-offs & Alternatives Considered
The forks in the road and why we chose what we chose.

## 10. 🌐 How It's *Actually* Done
Notes referencing real engineering practices/blogs (Uber, Netflix, Meta, etc.).

## 11. 📝 Summary
The 30-second whiteboard recap.
```

---

## Tone

- Friendly, confident, occasionally playful. Emojis as section anchors are welcome but not on every line.
- Address the reader as "you."
- It's okay to say "this is genuinely hard" — honesty builds trust.

---

## Level README template

Each `Level-XX/README.md` contains: the level's theme, what you'll be able to do after it, the ordered topic list with one-line descriptions, prerequisites, and an estimated time.
