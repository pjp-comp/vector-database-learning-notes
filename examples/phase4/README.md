# Phase 4 — Building real RAG

**Big idea:** chop documents into chunks, retrieve the relevant ones for a
question, and feed them to an LLM so it answers from *your* data.

This phase has two sub-parts:

## 4a — Chunking
```bash
python examples/phase4/example_4a_chunking.py
```
Shows how a document is split into pieces (by paragraph, and by fixed size with
overlap). Good chunks = good retrieval.

## 4b — RAG (the full loop)
```bash
python examples/phase4/example_4b_rag.py
```
Embeds a small knowledge base, retrieves the best chunks for a question, then
builds an answer. The retrieval is real; the LLM step is a clearly-labeled
**fake** so it runs with no API key. The comment shows exactly where a real
LLM (e.g. Claude) call would go.

## Words to know
- **Chunk** — a small searchable piece of a document.
- **Overlap** — sharing text between neighbouring chunks so ideas aren't cut.
- **RAG** — Retrieval-Augmented Generation: retrieve, then let an LLM answer.
- **Context** — the retrieved chunks handed to the LLM.

→ Full explanation: [learning_notes.md](../../learning_notes.md)
