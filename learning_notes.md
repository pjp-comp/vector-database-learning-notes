# Vector Database — Learning Notes (Full Guide)

The complete, plain-language guide for this project. For setup, the file index,
and the future roadmap, see [README.md](README.md).

Reference: [How does a Vector Database work? (Outcome School)](https://outcomeschool.com/blog/how-does-a-vector-database-work)

---

## Phase 1 — The Core Idea (in-memory demo) ✅

### Goal of Phase 1
Understand the *concept* of a vector database using a tiny ~60-line Python demo,
with **no real database** — just Python in memory.

### The big idea
A vector database lets you search by **meaning** instead of by **exact words**.
The flow is always the same 3 steps:

1. **Text → numbers** (embeddings)
2. **Store the numbers**
3. **Compare a new query's numbers to the stored ones** to find the closest match

### Files in this phase
- [vector_db_basics.py](vector_db_basics.py) — the runnable demo

### Commands to run it
```bash
cd /Users/pragneshpatel/ai/embading
source .venv/bin/activate            # activate the virtual env
pip install -r requirements.txt      # one time
python vector_db_basics.py
```
First run is slower (downloads the ~90 MB model); after that it is cached and fast.
(Full setup details are in [README.md](README.md).)

### What the code does (step by step)
1. **Load the model** — `SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")`
   downloads a small, fast model that turns text into vectors.
   ("MiniLM" = lightweight, "L6" = 6 layers, "v2" = version 2.)
2. **The documents** — a list of 8 words we want to search over.
3. **Turn documents into vectors** — `model.encode(documents, normalize_embeddings=True)`.
   Each word becomes a list of **384 numbers**. This `vectors` variable *is* the database.
4. **Turn the query into a vector** — same process for the search word `"kitten"`.
5. **Compare and rank** — cosine similarity scores every stored word, then sorts highest-first.

### Why the model `all-MiniLM-L6-v2`?
The demo uses `sentence-transformers/all-MiniLM-L6-v2` because it's a great
beginner model for semantic search:
- Small and fast — easy to run locally.
- Produces useful embeddings out of the box (no training needed).
- Widely used in `sentence-transformers` examples.
- Outputs **384-dimensional** vectors — compact enough for simple demos.

The name decodes as: **MiniLM** = a lightweight language-model family ·
**L6** = 6 transformer layers · **v2** = a later release.

### Theory: what an "embedding" really is
An **embedding** is a list of numbers (a *vector*) that represents *meaning*.
- The model was trained on huge amounts of text, so it learned to place
  words/sentences with similar meaning **near each other** in space.
- Each number is one **dimension** — a learned "feature." You can't read them
  individually ("dimension 57 = animalness"); meaning lives in the *whole pattern*.
- Our model outputs **384 dimensions**. So every word is a point in 384-D space.
- You can't picture 384-D, but the rule from 2-D/3-D still holds:
  **close points = similar meaning**.

### Theory: the three similarity metrics
There are three common ways to measure "how close are two vectors":

| Metric | Measures | Closer means | Best for |
|---|---|---|---|
| **Cosine similarity** | the **angle** between vectors | score near **1.0** | text / semantic search |
| **Dot product** | angle **and** length combined | **higher** | normalized vectors (= cosine) |
| **Euclidean distance** | straight-line **gap** between points | **lower** (near 0) | images / spatial data |

Key fact that ties them together:
**when vectors are normalized (unit length), cosine == dot product, and they rank
results in the same order as euclidean distance.** That is exactly why the code
uses `normalize_embeddings=True` — it makes the math simple and consistent.

### The one piece of math: cosine similarity (used in this demo)
Think of each vector as an **arrow** in 384-dimensional space.
Cosine similarity measures the **angle** between two arrows:
- Same direction → score near **1.0** (very similar meaning)
- 90° apart → score near **0** (unrelated)
- Opposite → score near **-1** (opposite meaning)

It ignores *length* and only cares about *direction* — which is why it's great for
text: a long document and a short phrase about the same topic still point the same way.

Formula: `cos(a, b) = (a · b) / (|a| × |b|)`
(dot product of the two vectors, divided by their lengths).

### Real output from running it
```
Query: kitten
Nearest matches:
       cat  similarity=0.7882
     puppy  similarity=0.6146
       dog  similarity=0.5205
       car  similarity=0.4350
     apple  similarity=0.3926

Example vector shape: (384,)
```
Key insight: the word "kitten" was **never stored**, yet `cat` and `puppy` rank highest.
That is **semantic search** — matching by meaning, not spelling.

### How the demo maps to the reference article
| Article concept | What it means | In this demo? |
|---|---|---|
| **Embeddings** | Similar meaning → similar numbers | ✅ `model.encode(...)` |
| **What gets stored** (vector + original data + metadata) | Real DB stores 3 things | ⚠️ Only 2: `vectors` + `documents`. **Metadata missing** |
| **Similarity metrics** (cosine / dot / euclidean) | Ways to measure closeness | ✅ Uses **cosine** (best for text) |
| **Nearest Neighbor** | Find the closest vector | ✅ the `sorted(...)` ranking |
| **ANN / HNSW / IVF / PQ** (indexing) | Search millions *fast* | ❌ Not here — brute-force checks all 8 |

### Phase 1 takeaway
This demo is the **honest, simple version**: text → embeddings → compare all → rank.
Everything advanced in the article (HNSW, IVF, PQ indexing) only makes that same
search **faster at huge scale**. The *meaning* never changes.

---

## Phase 2 — Real Vector Databases (in progress) 🚧

### Goal of Phase 2
Move from the in-memory demo to a setup that has the three things a *real*
vector database has: **metadata**, a **real index (ANN)**, and **filtering**.

### Files in this phase
- [vector_db_phase2.py](vector_db_phase2.py) — upgraded demo using a real **FAISS** index

### Commands to run it
```bash
cd /Users/pragneshpatel/ai/embading
source .venv/bin/activate            # activate the virtual env
pip install -r requirements.txt      # one time (includes faiss-cpu)
python vector_db_phase2.py
```

### What's new vs Phase 1 (done ✅)
- [x] **Metadata** — each item is now `Item(text, category)`, not just bare text
- [x] **Real index** — uses `faiss.IndexFlatIP` instead of a hand-written Python loop
- [x] **Two metrics side by side** — cosine (via FAISS) **and** euclidean distance
- [x] **Metadata filtering** — restrict results to `category == "animal"`

### Real output from running it
```
Query: kitten

Cosine similarity (via FAISS inner-product index):
       cat  [animal ]  cosine=0.7882
     puppy  [animal ]  cosine=0.6146
       dog  [animal ]  cosine=0.5205
       ...

Euclidean distance (lower = closer):
       cat  [animal ]  distance=0.6508
     puppy  [animal ]  distance=0.8779
       dog  [animal ]  distance=0.9793
       ...

Filtered search (category == "animal" only):
       cat  cosine=0.7882
     puppy  cosine=0.6146
       dog  cosine=0.5205
```
**Key insight:** cosine and euclidean give the **same ranking** here — proof of the
theory above that *on normalized vectors the metrics agree*. The metadata filter
then cleanly drops the fruit/vehicle results.

### Theory still to learn (next ⏭️)
- [ ] **Nearest Neighbor problem** — why brute force (checking every vector) breaks at scale
- [ ] **Approximate Nearest Neighbor (ANN)** indexing — trade a tiny bit of accuracy for huge speed:
  - [ ] **HNSW** — layered graph, "big jumps" across far data, then fine-tuning
  - [ ] **IVF** — cluster vectors, search only the relevant clusters
  - [ ] **PQ (Product Quantization)** — compress vectors (e.g. 512 bytes → 8 bytes)
  - In FAISS these are just different index types (`IndexHNSWFlat`, `IndexIVFFlat`) — **same API** as the `IndexFlatIP` we already used.
- [ ] **Persistence** — save/load the index to disk (our index still vanishes on exit)
- [ ] Try a hosted/easy DB:
  - [ ] **Chroma** (local, easy, persistent — good next step)
  - [ ] **Pinecone / Weaviate / Qdrant** (hosted, production-scale)

### Phase 2 takeaway so far
The demo now looks like a real vector DB in shape: **store (vector + data + metadata)
→ index → similarity search → filter**. What's left to learn is purely about
**scale**: swapping the exact `IndexFlatIP` for an approximate index (HNSW/IVF/PQ)
and persisting it. The meaning and the workflow stay identical.
