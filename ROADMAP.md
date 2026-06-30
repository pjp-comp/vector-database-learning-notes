# Beginner AI Engineer — Roadmap

A practical, honest path from "I understand embeddings" to "I can build and ship a
small AI product." It's built around **this repo** (which already covers embeddings,
vector search, and RAG very well) and fills in the parts a real beginner
AI-Engineer role expects: **LLM APIs, app-building, evaluation, and deployment.**

> **The honest framing:** This repo's modules 01–08 are a *deep* dive into one
> slice of AI engineering — retrieval and RAG. That slice is valuable and
> in-demand, but it isn't the whole job. Modules 09–12 + the capstone are the rest
> of the map. Some of those are taught here as guides (not runnable demos yet),
> because they need an API key and external services — that's called out clearly.

---

## How to use this roadmap

1. Set up the environment once — see [README.md](README.md#setup).
2. Work the modules **in order**. Each has a runnable `example.py` (or a guide).
3. For the theory behind any module, read the matching section in
   [learning_notes.md](learning_notes.md).
4. Don't just run the examples — **change them** and predict what happens first.
   That's where the learning is.
5. Finish with the [capstone](modules/capstone/) — building one end-to-end thing
   is worth more than any number of tutorials.

**Suggested pace:** ~1 module per few evenings. The whole path is realistically
**6–10 weeks** part-time. It is not a race.

---

## What an "AI Engineer (beginner)" actually does

Not an ML researcher (they train models). An AI *engineer* **builds applications
on top of existing models**. Day to day that means:

- Calling LLM APIs well (prompting, tool use, structured output).
- Giving models the right context (RAG / retrieval) — **most of this repo**.
- Wrapping it in an app or API others can use.
- Measuring quality so changes are improvements, not vibes.
- Shipping it and keeping it running (cost, latency, errors).

You do **not** need deep math or to train models from scratch to start.

---

## Prerequisites (be honest with yourself)

- **Python basics** — functions, lists/dicts, imports, running a script, pip/venv.
- **A terminal** — `cd`, run a command, activate a virtualenv.
- **Git basics** — clone, commit, push (you're already doing this).
- *Nice to have, not required:* what an API is, basic JSON.

If Python feels shaky, spend a week on it first — everything else builds on it.

---

## The path at a glance

| # | Module | What you learn | Runnable here? |
|---|---|---|---|
| 00 | [foundations](modules/00-foundations/) | mindset, mental models, setup | guide |
| 01 | [embeddings](modules/01-embeddings/) | text → vectors, semantic search | ✅ |
| 02 | [vector-databases](modules/02-vector-databases/) | real index (FAISS), metadata, filtering | ✅ |
| 03 | [scaling-ann](modules/03-scaling-ann/) | ANN (HNSW/IVF/PQ), persistence | ✅ |
| 04 | [rag-basics](modules/04-rag-basics/) | chunking + the full RAG loop | ✅ |
| 05 | [retrieval-quality](modules/05-retrieval-quality/) | hybrid search, re-ranking, query transforms | ✅ |
| 06 | [agentic-rag](modules/06-agentic-rag/) | retrieve → judge → retry | ✅ |
| 07 | [corrective-rag](modules/07-corrective-rag/) | grade retrieval, fall back, refuse | ✅ |
| 08 | [vectorless-rag](modules/08-vectorless-rag/) | reasoning over structure (PageIndex) | ✅ |
| 09 | [llm-apis](modules/09-llm-apis/) | calling Claude: prompting, tool use, structured output | guide |
| 10 | [building-apps](modules/10-building-apps/) | wrap RAG in an API/UI, secrets, config | guide |
| 11 | [evaluation](modules/11-evaluation/) | measuring retrieval + answer quality | guide |
| 12 | [deployment](modules/12-deployment/) | ship it, basic ops, cost & latency | guide |
| — | [capstone](modules/capstone/) | build one real end-to-end AI app | project |
| ⊕ | [bonus/](bonus/) | images (CLIP), real PDFs | ✅ |

---

## The stages

### Stage 1 — Foundations & the core idea (modules 00–03)
**Goal:** understand how meaning becomes numbers, and how to store/search those
numbers fast.

- Embeddings, similarity (cosine/dot/euclidean), semantic search.
- A real vector index (FAISS), metadata, filtering.
- Scaling: ANN (HNSW, IVF, PQ) and persistence.

You finish this stage able to explain *"search by meaning, not exact words"* and
back it with running code. This is the bedrock of RAG.

### Stage 2 — RAG, the workhorse pattern (modules 04–08)
**Goal:** turn retrieval into answers, then make retrieval *good*.

- The RAG loop: load → chunk → embed → retrieve → generate.
- Quality upgrades: hybrid search, re-ranking, query transformation.
- Smarter retrieval: agentic loops, corrective/CRAG fallbacks.
- An alternative philosophy: vectorless / reasoning-based retrieval.

This is the heart of most beginner AI-Engineer work and the deepest part of this
repo. See [rag_architecture_types.md](rag_architecture_types.md) for the full map
of RAG designs.

### Stage 3 — From notebook to product (modules 09–12)
**Goal:** the skills that turn "a script that retrieves" into "an app people use."

- **LLM APIs (09):** prompting, system prompts, tool use, structured (JSON) output,
  streaming, token/cost basics — using **Claude** (the latest models:
  Opus 4.8 / Sonnet 4.6 / Haiku 4.5). See the [Claude API reference](modules/09-llm-apis/).
- **Building apps (10):** wrap your RAG pipeline behind a small API (FastAPI) or a
  simple UI (Streamlit); handle API keys/secrets and config properly.
- **Evaluation (11):** stop guessing — measure retrieval quality and answer
  faithfulness (RAGAS-style) so each change is a real improvement.
- **Deployment (12):** put it somewhere others can reach; watch cost, latency, and
  errors; the basics of keeping it alive.

> Modules 09–12 are **guides** here, not no-API-key demos: they need a real LLM
> key and external services, so this repo explains *what to do and why*, then
> points you at the real tools. Wire a real Claude call into module 04b's fake LLM
> as your first concrete step.

### Stage 4 — Capstone (build one real thing)
**Goal:** prove it to yourself. Pick one and ship it end-to-end.

See [modules/capstone/](modules/capstone/) for full briefs. Examples:
- **"Chat with your docs"** — RAG over your own PDFs/notes, real Claude answers,
  a Streamlit UI, basic eval, deployed.
- **A support-FAQ bot** — hybrid search + re-ranking + CRAG refusal when unsure.

One finished, deployed capstone beats ten half-tutorials on a résumé.

---

## What's intentionally NOT here (and where to go next)

This roadmap gets you to *beginner job-ready*. Deliberately out of scope for now:

- **Fine-tuning / training models** — you rarely need it early; prompting + RAG
  goes very far. Learn it once you hit a real wall.
- **Deep ML math** — useful later, not a blocker to start.
- **Multi-agent orchestration frameworks, GraphRAG at scale, MLOps** — these are
  "intermediate+." You'll meet them naturally after the capstone.

---

## A note on staying current

AI moves fast. Two durable habits:
1. **Default to the latest, most capable models** (right now: the Claude 4.x
   family). Don't hardcode old model names into your mental defaults.
2. **Learn the patterns, not the libraries.** Frameworks churn; the ideas in this
   repo (embed → retrieve → ground → generate → evaluate) are stable.

Now: open [modules/00-foundations/](modules/00-foundations/) and start.
