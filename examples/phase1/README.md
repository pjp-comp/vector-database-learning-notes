# Phase 1 — The core idea

**Big idea:** turn words into numbers that capture meaning, then find the nearest numbers.

This example has **no database** — just a Python list — so nothing is hidden.

## Run
```bash
# from the project root, with the venv active (see top-level README)
python examples/phase1/example.py
```

## What you'll see
"kitten" is closest to **cat** and **puppy**, and far from **train** — even though
"kitten" was never in our list. That's *semantic search*: matching by meaning.

## Words to know
- **Embedding** — the list of numbers that represents a word's meaning.
- **Vector** — another name for that list of numbers.
- **Cosine similarity** — a score (0–1) for how close two meanings are.

→ Full explanation: [learning_notes.md](../../learning_notes.md#phase-1--the-core-idea-in-memory-demo)
