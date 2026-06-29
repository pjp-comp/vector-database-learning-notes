# Phase 3 — Scaling the index (ANN)

**Big idea:** checking every vector is fine for a few items but too slow for
millions. **Approximate Nearest Neighbour (ANN)** indexes find the nearest
vectors *almost* perfectly, but much faster.

## Run
```bash
python examples/phase3/example.py
```
(Uses random vectors, so no model download — runs in seconds.)

## What you'll see
- A **brute-force** search (exact) vs an **HNSW** search (approximate) on 50,000 vectors.
- They usually agree on the top result — that's the deal: tiny accuracy cost, big speed win.
- The index is **saved to disk and reloaded** (persistence).

## Words to know
- **Brute force** — compare against every vector. Exact, slow at scale.
- **ANN** — approximate nearest neighbour; trades a little accuracy for big speed.
- **HNSW / IVF / PQ** — popular ANN index types (graph / clustering / compression).
- **Persistence** — saving the index so it survives a restart.

→ Full explanation: [learning_notes.md](../../learning_notes.md#related-theory-scaling-the-index)
