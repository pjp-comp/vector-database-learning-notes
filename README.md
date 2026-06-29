# Vector Database — Learning Project

A hands-on project for learning how vector databases work, built up in phases
from a tiny in-memory demo to a real indexed search with FAISS.

Reference reading: [How does a Vector Database work? (Outcome School)](https://outcomeschool.com/blog/how-does-a-vector-database-work)

---

## Setup

This project uses a virtual environment (`.venv`) and `requirements.txt`.

```bash
# 1. Go into the project folder
cd /Users/pragneshpatel/ai/embading

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Install dependencies (one time)
pip install -r requirements.txt
```

When the env is active your prompt shows `(.venv)`. To leave it later: `deactivate`.

> First run downloads the embedding model (~90 MB); after that it is cached and fast.

---

## Run the demos

With the env activated (see above):

```bash
# Phase 1 — the core idea, in memory
python vector_db_basics.py

# Phase 2 — real FAISS index, metadata, filtering
python vector_db_phase2.py
```

---

## File index

| File | What it is |
|---|---|
| [README.md](README.md) | This index — setup, file map, and the learning roadmap |
| [learning_notes.md](learning_notes.md) | **The full guide** — theory + walkthrough for both phases |
| [vector_db_basics.py](vector_db_basics.py) | Phase 1 demo — text → embeddings → cosine search (in memory) |
| [vector_db_phase2.py](vector_db_phase2.py) | Phase 2 demo — FAISS index + metadata + filtering |
| [requirements.txt](requirements.txt) | Python dependencies |

Start with **[learning_notes.md](learning_notes.md)** — it explains everything in plain language.

---

## Learning roadmap

### ✅ Phase 1 — The core idea (done)
- What an embedding is (text → a list of numbers / a vector)
- Cosine similarity and the other metrics (dot product, euclidean)
- Semantic search by meaning, not exact words — all in memory
- → details in [learning_notes.md](learning_notes.md#phase-1--the-core-idea-in-memory-demo-)

### 🚧 Phase 2 — Real vector databases (in progress)
- Storing **metadata** alongside vectors
- Using a real **FAISS** index instead of a brute-force loop
- Comparing **cosine vs. euclidean** on the same query
- **Filtering** results by metadata
- → details in [learning_notes.md](learning_notes.md#phase-2--real-vector-databases-in-progress-)

### ⏭️ Future things to learn (next)
- [ ] **Nearest Neighbor problem** — why brute force breaks at scale
- [ ] **Approximate Nearest Neighbor (ANN)** indexing — speed vs. accuracy trade-off
  - [ ] **HNSW** — layered graph, big jumps then fine-tuning
  - [ ] **IVF** — cluster vectors, search only relevant clusters
  - [ ] **PQ (Product Quantization)** — compress vectors (e.g. 512 → 8 bytes)
- [ ] **Persistence** — save/load the index to disk
- [ ] **Chunking & real documents** — embed paragraphs, not just single words
- [ ] **Chroma** — an easy local, persistent vector DB (good next step)
- [ ] **Hosted DBs** — Pinecone / Weaviate / Qdrant (production scale)
- [ ] **RAG** — use retrieved vectors to feed an LLM (retrieval-augmented generation)
