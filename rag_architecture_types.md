# RAG Architecture Types (the big map)

The phases in [learning_notes.md](learning_notes.md) build *one* RAG loop and then
improve it. But "RAG" isn't a single design — it's a family of architectures.
This file is the map: each type, what changes, and which phase covers it.

> **One-line way to hold it all:**
> **Naive RAG** is the loop · **Advanced/Hybrid** makes each step better ·
> **Agentic** turns the loop into a decision process · **Graph** and
> **Vectorless** change *what* you retrieve over · **Multi-modal** changes the
> *type* of data · **Corrective (CRAG)** adds a safety net when retrieval is bad.

---

## 1. Naive / Standard RAG
The baseline loop: chunk docs → embed → store → at query time embed the question,
retrieve top-k nearest chunks, stuff them into the prompt, generate.
- **Here:** [Phase 4](learning_notes.md#deep-dive-phase-4--building-real-rag)
  (`modules/04-rag-basics/example_4b_rag.py`, `bonus/pdf-rag/`).
- **Good for:** getting started, FAQ bots, moderate doc sets.
- **Weak spots:** arbitrary chunking, "similarity ≠ relevance," no quality control.

## 2. Advanced / Hybrid RAG
The same loop with retrieval-quality upgrades layered around it:
- *Pre-retrieval:* query transformation (multi-query, HyDE).
- *Retrieval:* hybrid search (keyword/BM25 + vector) for exact terms **and** meaning.
- *Post-retrieval:* re-ranking with a cross-encoder; metadata filtering.
- **Here:** [Phase 5](learning_notes.md#deep-dive-phase-5--better-retrieval-quality).
- **Good for:** production systems where naive retrieval misses exact terms or ordering.

## 3. Agentic RAG
Retrieval becomes a **decision loop**: search → judge "is this enough?" → rewrite
the query / pick another source → retry → answer. Can route across multiple
indexes and tools.
- **Here:** [Phase 6](learning_notes.md#deep-dive-phase-6--advanced--agentic-retrieval).
- **Good for:** ambiguous questions, multi-step research, multiple data sources.
- **Cost:** more LLM calls, higher latency.

## 4. Corrective / Self-RAG (CRAG)
A structured cousin of agentic RAG: the model **grades** the retrieved chunks
before trusting them. If they're weak, it **falls back** (e.g. rewrite + retry, or
a different source) instead of answering from bad context.
- **Here:** [Module 07 demo](modules/07-corrective-rag/example.py).
- **Good for:** reducing hallucinations when the knowledge base has gaps.

## 5. Graph RAG
Builds a **knowledge graph** (entities + relationships) and retrieves by
traversing connections, not just vector similarity. Often combined with vectors.
- **Here:** named in [Phase 6](learning_notes.md#deep-dive-phase-6--advanced--agentic-retrieval).
- **Good for:** multi-hop questions where *relationships* carry the answer.

## 6. Vectorless / Reasoning-based RAG (PageIndex)
No embeddings, no vector DB. Build a table-of-contents tree; the LLM **reasons**
about which section to open, then reads it with context intact.
- **Here:** [Phase 7](learning_notes.md#phase-7--latest-market-direction-vectorless-rag-with-pageindex).
- **Good for:** long, well-structured docs (manuals, contracts, filings).
- **Trade-off:** weaker on huge, flat, unstructured collections.

## 7. Multi-modal RAG
The same retrieve-then-generate loop over images/audio/code, via models like CLIP
that embed several modalities into one shared space (text query → image results).
- **Here:** [image-embeddings deep dive](learning_notes.md#deep-dive-image-embeddings-searching-pictures).

## Worth knowing: long-context "RAG-less"
When the whole corpus fits, skip retrieval and paste everything into a large
context window. Simpler, but more expensive per call and weaker on large or
changing data — see the long-context note in
[Phase 6](learning_notes.md#deep-dive-phase-6--advanced--agentic-retrieval).

---

## Quick comparison

| Type | What changes | Needs vectors? | Best for |
|---|---|---|---|
| Naive | the basic loop | yes | getting started, FAQs |
| Advanced/Hybrid | better each step | yes | production retrieval quality |
| Agentic | loop → decisions | yes | ambiguous, multi-step questions |
| Corrective (CRAG) | grade + fallback | yes | knowledge bases with gaps |
| Graph | retrieve over relationships | optional | multi-hop, relational questions |
| Vectorless | reason over structure | no | long, structured documents |
| Multi-modal | non-text data | yes | image/audio/code search |
