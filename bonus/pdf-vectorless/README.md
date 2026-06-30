# PDF Vectorless RAG — PageIndex style over a real PDF

**Big idea:** answer questions about a PDF **without embeddings or a vector DB**.
Build a tree of the PDF's headings (its table of contents) and *reason* about which
section to open — the way you'd flip to the right chapter of a manual. This is
Phase 7 applied to a real file.

## Run
```bash
python bonus/pdf-vectorless/example.py
```
Uses the same `bonus/handbook.pdf` as the PDF RAG demo (auto-created if missing).
Notice this script imports **no embedding model and no vector library**.

## What you'll see
The PDF's headings are listed, the script reasons that "1.1 Refunds" matches the
question, opens it, and answers — all by navigating structure, not comparing vectors.
(The reasoning step is a labeled fake; a real system uses an LLM here.)

## Compare
Run [bonus/pdf-rag/example.py](../pdf-rag/) to answer the **same PDF and
question with embeddings** instead, and see the difference in approach.

## Words to know
- **Vectorless RAG** — retrieval with no embeddings/vector DB.
- **Document tree** — the PDF's heading hierarchy used as a map.
- **Reasoning-based retrieval** — "decide what's relevant" vs. "find what's similar".

→ Full explanation: [learning_notes.md](../../learning_notes.md#phase-7--latest-market-direction-vectorless-rag-with-pageindex)
