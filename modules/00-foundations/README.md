# Module 00 — Foundations (mindset & setup)

> Guide module — no code to run. Read this, set up your environment, then start
> [Module 01](../01-embeddings/).

## What an AI Engineer (beginner) actually does
You build **applications on top of existing models** — you don't train models.
The job is: call LLMs well, give them the right context (RAG), wrap it in an app,
measure quality, and ship it. See [ROADMAP.md](../../ROADMAP.md) for the full
picture.

## The one mental model to carry through everything
> **Embed your data → store the vectors → embed the question → retrieve the
> nearest vectors → feed them to the LLM → measure the result.**

Modules 01–08 teach the middle (retrieval). Modules 09–12 teach the ends (the LLM
call, and turning it into a product).

## Set up your environment (do this once)
Follow [README.md → Setup](../../README.md#setup):
```bash
cd /Users/pragneshpatel/ai/embedding
source .venv/bin/activate
pip install -r requirements.txt
```

## How to actually learn here (not just run)
1. Run each module's `example.py`.
2. **Predict** what a change will do *before* you make it, then try it.
3. Read the matching section of [learning_notes.md](../../learning_notes.md).
4. Write one sentence in your own words explaining the module. If you can't, redo it.

## Prerequisites check
You need: Python basics, a terminal, and Git. If those feel shaky, spend a week
there first — everything else builds on them.

→ Next: [Module 01 — Embeddings](../01-embeddings/)
