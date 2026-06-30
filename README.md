# Vector Database — Learning Project

A hands-on project for learning how vector databases work, built up in phases
from a tiny in-memory demo to a real indexed search with FAISS.


## Why this matters in AI engineering

Normal databases match **exact words**; AI apps need to search by **meaning**.
A vector database stores the *meaning* of data as numbers (embeddings) and finds
the closest matches fast. This is what lets you build **RAG** (Retrieval-Augmented
Generation) — giving an LLM your own up-to-date data so it answers from facts
instead of hallucinating. It powers semantic search, recommendations, dedup, image
search, and agent memory.

> Mental model: **embed your data → store vectors → embed the question →
> retrieve nearest vectors → feed them to the LLM.**

Full breakdown of *why, where, and when* in [learning_notes.md](learning_notes.md#why-vector-databases-matter-in-ai-engineering).

---

## Setup

This project uses a virtual environment (`.venv`) and `requirements.txt`.

```bash
# 1. Go into the project folder
cd /Users/pragneshpatel/ai/embedding

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Install dependencies (one time)
pip install -r requirements.txt
```

When the env is active your prompt shows `(.venv)`. To leave it later: `deactivate`.

> First run downloads the embedding model (~90 MB); after that it is cached and fast.

---

## Run the examples

Runnable, beginner-commented examples live in [modules/](modules/) (the core
curriculum) and [bonus/](bonus/) (images + real PDFs). Each prints what it's
doing. With the env activated:

**Core path (one module at a time):**
```bash
python modules/01-embeddings/example.py               # the core idea, in memory
python modules/02-vector-databases/example.py         # real FAISS index + metadata + filtering
python modules/03-scaling-ann/example.py              # ANN at scale (brute force vs HNSW)
python modules/04-rag-basics/example_4a_chunking.py   # splitting documents into chunks
python modules/04-rag-basics/example_4b_rag.py        # the full RAG loop
python modules/05-retrieval-quality/example.py        # hybrid search + re-ranking
python modules/06-agentic-rag/example.py              # agentic (search, judge, retry)
python modules/07-corrective-rag/example.py           # corrective RAG (grade, correct, refuse)
python modules/08-vectorless-rag/example.py           # vectorless RAG (PageIndex style)
```

**Bonus demos (apply the ideas to images and real PDFs):**
```bash
python bonus/image-embeddings/example.py    # pictures as vectors + text-to-image (CLIP)
python bonus/pdf-rag/example.py             # classic RAG over a real PDF
python bonus/pdf-vectorless/example.py      # SAME PDF answered with NO embeddings
```

> Modules that would normally call an LLM (04b, 06, 07, both PDF demos) use a
> small, clearly-labeled **fake LLM** so everything runs with no API key. The
> retrieval parts are real. Each folder also has its own short `README.md`.
> Tip: run the two PDF demos back-to-back to compare embedding RAG vs. vectorless.

> **Following the roadmap?** [ROADMAP.md](ROADMAP.md) is the beginner
> AI-Engineer learning path and tells you which module to do when (and what to
> learn beyond this repo).

---

## File index

| Path | What it is |
|---|---|
| [ROADMAP.md](ROADMAP.md) | **The beginner AI Engineer roadmap** — the learning path; start here |
| [README.md](README.md) | This index — setup, file map, and run commands |
| [learning_notes.md](learning_notes.md) | **The full theory guide** — plain-language explanation for every module |
| [rag_architecture_types.md](rag_architecture_types.md) | One-page map of the RAG architecture types (naive, hybrid, agentic, CRAG, graph, vectorless, multi-modal) |
| [modules/](modules/) | The core curriculum: `01-embeddings` … `08-vectorless-rag`, plus roadmap-only modules `09`–`12` and `capstone` |
| [bonus/](bonus/) | Applied demos: `image-embeddings`, `pdf-rag`, `pdf-vectorless` |
| [requirements.txt](requirements.txt) | Python dependencies |

**New to this?** Read [ROADMAP.md](ROADMAP.md), then the "Start here" section of
**[learning_notes.md](learning_notes.md#start-here-read-this-first-if-youre-brand-new)**,
then run `modules/01-embeddings/example.py`.

---

## Learning roadmap

The full beginner **AI Engineer** learning path now lives in its own file:
**[ROADMAP.md](ROADMAP.md)** — it sequences the modules below and adds the parts a
real job expects (LLM APIs, app-building, evaluation, deployment, a capstone).

The deep theory for the retrieval/RAG modules (01–08) is in
[learning_notes.md](learning_notes.md), which is organized by "phase." This table
maps those phases to the module folders:

| learning_notes "phase" | Module folder |
|---|---|
| Phase 1 — the core idea | [modules/01-embeddings](modules/01-embeddings/) |
| Phase 2 — real vector databases | [modules/02-vector-databases](modules/02-vector-databases/) |
| Phase 3 — scaling the index (ANN) | [modules/03-scaling-ann](modules/03-scaling-ann/) |
| Phase 4 — building real RAG | [modules/04-rag-basics](modules/04-rag-basics/) |
| Phase 5 — better retrieval quality | [modules/05-retrieval-quality](modules/05-retrieval-quality/) |
| Phase 6 — agentic retrieval | [modules/06-agentic-rag](modules/06-agentic-rag/) |
| Phase 6b — corrective RAG (CRAG) | [modules/07-corrective-rag](modules/07-corrective-rag/) |
| Phase 7 — vectorless RAG | [modules/08-vectorless-rag](modules/08-vectorless-rag/) |
| (image embeddings deep dive) | [bonus/image-embeddings](bonus/image-embeddings/) |

Modules **09–12** and the **capstone** are roadmap-stage guides (LLM APIs, apps,
evaluation, deployment) — see [ROADMAP.md](ROADMAP.md).
