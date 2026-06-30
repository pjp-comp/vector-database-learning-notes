# Module 10 — Building apps around your pipeline

> Guide module. Turns "a script that retrieves and answers" into "an app other
> people can use."

A RAG script is not a product. This module is the wrapping: an interface, config,
and secrets handled properly.

## What to learn
1. **An API layer (FastAPI)** — expose your pipeline as an HTTP endpoint:
   `POST /ask {"question": "..."}` → `{"answer": "...", "sources": [...]}`.
   This is how other software (or a frontend) talks to your RAG.
2. **A quick UI (Streamlit)** — a chat box + answer + the retrieved sources, in
   ~30 lines. Great for demos and your capstone.
3. **Secrets & config** — **never** hardcode API keys. Use environment variables
   (`ANTHROPIC_API_KEY`) and a `.env` file that is **git-ignored**. Make model
   name, top-k, and chunk size config values, not magic numbers.
4. **Returning sources** — always send back *which chunks* the answer came from.
   It builds trust and makes debugging possible.
5. **Errors & limits** — handle the LLM being slow, rate-limited, or down; show a
   sensible message instead of crashing.

## Shape to aim for
```
your-app/
  retrieval.py     # embed + search (modules 01-05 logic)
  llm.py           # the real Claude call (module 09)
  app.py           # FastAPI or Streamlit entry point
  .env             # ANTHROPIC_API_KEY=...   (git-ignored!)
  requirements.txt
```

## Why this matters for a job
"I built a RAG script" is common. "I deployed a small RAG app with a UI that cites
its sources" is a portfolio piece. This module is that difference.

→ Next: [Module 11 — Evaluation](../11-evaluation/)
