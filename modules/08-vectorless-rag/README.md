# Phase 7 — Latest market direction: Vectorless RAG (PageIndex style)

**Big idea:** instead of turning everything into vectors and searching by
similarity, give the model the document's **structure** (its table of contents)
and let it **reason** about which section to open — like a human using a manual.

## Run
```bash
python modules/08-vectorless-rag/example.py
```
Note: this example uses **no embedding model and no vector library at all** —
retrieval is reasoning over a tree, not similarity over numbers.

## What you'll see
A question about refunds is answered by *navigating* "Billing → Refunds", not by
comparing vectors.

## About the "reasoning"
A real system uses an **LLM** to choose the right section. Here that step is faked
with simple keyword matching over section titles, so it runs with no API key. The
lesson is the *shape*: navigate structure instead of comparing vectors.

## Words to know
- **Vectorless RAG** — retrieval without embeddings or a vector database.
- **PageIndex** — a method that builds a document tree and reasons over it.
- **Reasoning-based retrieval** — "decide what's relevant" vs. "find what's similar".

→ Full explanation: [learning_notes.md](../../learning_notes.md#phase-7--latest-market-direction-vectorless-rag-with-pageindex)
