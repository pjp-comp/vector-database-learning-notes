# Phase 2 — A real vector database (FAISS)

**Big idea:** store the meaning *and* tags for each item in a real search index,
then search and filter.

## Run
```bash
python modules/02-vector-databases/example.py
```

## What's new vs Phase 1
- **Metadata** — each item has a `category` tag, not just text.
- **Real index** — uses **FAISS** instead of a hand-written loop.
- **Filtering** — show only results where `category == "animal"`.

## Words to know
- **Metadata** — extra tags stored with each item (category, date, author...).
- **Index** — a data structure built for fast "find the nearest" queries.
- **FAISS** — a popular library for vector search.

→ Full explanation: [learning_notes.md](../../learning_notes.md#phase-2--real-vector-databases)
