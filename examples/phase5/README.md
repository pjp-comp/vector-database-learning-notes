# Phase 5 — Better retrieval quality

**Big idea:** plain vector search isn't always enough. Two upgrades fix most
quality problems: **hybrid search** and **re-ranking**.

## Run
```bash
python examples/phase5/example.py
```

## What you'll see
A query with an exact term (`E-404`) where vector-only search struggles, but
**hybrid search** (vector + keyword) puts the right document on top.

## Words to know
- **Hybrid search** — combine vector (meaning) + keyword (exact terms).
- **BM25** — the classic keyword-ranking algorithm (we use a simpler overlap here).
- **Re-ranking** — re-score a shortlist more carefully so the best result rises.
- **Cross-encoder** — a model used as a high-quality re-ranker in real apps.
- **Query transformation** — rewriting/expanding the question before searching (e.g. HyDE).

→ Full explanation: [learning_notes.md](../../learning_notes.md)
