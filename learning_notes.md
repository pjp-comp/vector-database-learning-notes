# Vector Database — Learning Notes (Full Guide)

The complete, plain-language guide for this project. For setup, the file index,
and the future roadmap, see [README.md](README.md).

Reference: [How does a Vector Database work? (Outcome School)](https://outcomeschool.com/blog/how-does-a-vector-database-work)

---

## Start here (read this first if you're brand new)

No code, no math yet — just the idea, with everyday pictures.

### 1. Computers don't understand words, they understand numbers
When you read "cat" and "kitten" you instantly feel they're related. A computer
sees two different strings of letters with nothing in common. To make a computer
*feel* that they're related, we first turn each word into **numbers**.

### 2. An "embedding" is just a list of numbers that captures meaning
Imagine giving every word a set of scores, like a personality profile:

| word | "animal-ness" | "small-ness" | "vehicle-ness" |
|---|---|---|---|
| cat | 0.9 | 0.6 | 0.0 |
| kitten | 0.9 | 0.9 | 0.0 |
| bus | 0.0 | 0.1 | 0.9 |

Notice **cat** and **kitten** got similar scores, and **bus** is way off.
That list of scores is an **embedding**. Real embeddings aren't hand-made and
aren't 3 numbers — an AI model produces them automatically, and ours has **384**
numbers per word. But the idea is exactly this: *similar meaning → similar numbers.*

### 3. Picture the numbers as points on a map
If each word is a list of numbers, you can imagine plotting it as a **point**.
Words with similar meaning land **near each other**:

```
        cat  kitten
         •    •
           dog •

   apple •   • orange

                       car • bus
```

"Finding similar meaning" becomes "**find the nearest points**." That's the whole
trick behind semantic search.

### 4. A vector database stores these points and finds the nearest ones — fast
- **Vector** = the list of numbers (the point).
- **Vector database** = a store built to hold millions of these points and answer
  "*which points are nearest to this one?*" very quickly.

### 5. Why anyone cares (the payoff)
This lets software search by **meaning**, not exact words. Type "young cat" and it
finds a doc that says "kitten." This is the engine behind AI search, chatbots that
answer from *your* documents, recommendations, and more.

> **One sentence to remember:** turn things into numbers that capture meaning,
> store the numbers, then answer questions by finding the closest numbers.

Everything below builds this up step by step, with a runnable example for each phase
(see the [examples/](examples/) folder).

---

## Why vector databases matter in AI engineering

### The problem they solve
Normal (SQL/keyword) databases match **exact text**. If you search "kitten" they
won't find a document that says "young cat" — different words, same meaning.
AI applications need to search by **meaning**, not spelling. Vector databases
make that possible: they store the *meaning* of data as numbers (embeddings) and
find the closest meanings fast.

### Why this is important now
Large Language Models (LLMs) are powerful but have two big limits:
- They only know what they were **trained on** (a fixed cutoff date).
- They can **make things up** (hallucinate) when they don't know.

A vector database fixes both. You store *your own* data (docs, tickets, PDFs) as
vectors, and at question time you **retrieve the most relevant pieces** and hand
them to the LLM as context. This pattern is called **RAG** (Retrieval-Augmented
Generation) and it's the backbone of most real AI products today.

### Where you'll use one (real examples)
- **RAG / chatbots over your docs** — answer questions using your own content.
- **Semantic search** — "find me notes *about* X" instead of exact keyword match.
- **Recommendations** — "items similar to this one" (similar vectors).
- **Deduplication / clustering** — group near-identical content.
- **Image / audio search** — same idea, just embeddings of images or sound.
- **Long-term memory for agents** — store past interactions, recall relevant ones.

### Where you *don't* need one
- Exact lookups (by ID, email, exact name) — a normal database is better.
- Small, fixed lists you can scan in a loop (like this learning demo!).
- Structured filtering with no notion of "similar meaning."

### The mental model for an AI engineer
> **Embed your data → store the vectors → at query time, embed the question,
> retrieve the nearest vectors, and feed them to the LLM.**

Everything in this project is teaching the middle part — *store and retrieve by
meaning* — which is the piece that makes modern AI apps actually useful on
**your** data.

---

## Phase 1 — The Core Idea (in-memory demo)

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
- [examples/phase1/example.py](examples/phase1/example.py) — the runnable demo

### Commands to run it
```bash
cd /Users/pragneshpatel/ai/embading
source .venv/bin/activate            # activate the virtual env
pip install -r requirements.txt      # one time
python examples/phase1/example.py
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

## Phase 2 — Real Vector Databases

### Goal of Phase 2
Move from the in-memory demo to a setup that has the three things a *real*
vector database has: **metadata**, a **real index (ANN)**, and **filtering**.

### Files in this phase
- [examples/phase2/example.py](examples/phase2/example.py) — upgraded demo using a real **FAISS** index

### Commands to run it
```bash
cd /Users/pragneshpatel/ai/embading
source .venv/bin/activate            # activate the virtual env
pip install -r requirements.txt      # one time (includes faiss-cpu)
python examples/phase2/example.py
```

### What's new vs Phase 1
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

### Related theory (scaling the index)
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

### Phase 2 takeaway
The demo now looks like a real vector DB in shape: **store (vector + data + metadata)
→ index → similarity search → filter**. What's left to learn is purely about
**scale**: swapping the exact `IndexFlatIP` for an approximate index (HNSW/IVF/PQ)
and persisting it. The meaning and the workflow stay identical.

→ Example: [examples/phase2/example.py](examples/phase2/example.py)

---

## Deep dive: Phase 3 — Scaling the index (ANN)

> Example: [examples/phase3/example.py](examples/phase3/example.py)

### The problem, with a real-life picture
In Phase 2 we compared the query against **every** stored vector. With 8 items
that's instant. But imagine a library with **10 million books** and you check
every single one to find the closest match — that's far too slow.

This is the **nearest-neighbour problem**: finding the closest point is easy when
there are few points and painfully slow when there are millions.

### The fix: "approximate" instead of "perfect"
Here's the key insight that powers real vector databases:

> You almost never need the *mathematically perfect* closest match. The
> *99%-as-good* match found **100× faster** is what you actually want.

That trade — give up a tiny bit of accuracy for a huge speed gain — is called
**Approximate Nearest Neighbour (ANN)**. Our [phase3 example](examples/phase3/example.py)
shows it: on 50,000 vectors the approximate search is far faster and lands on
essentially the same answer.

### The three popular ANN tricks (in plain words)
- **HNSW** — *"build a road network."* Imagine highways connecting far-apart
  cities and small streets within a city. To find a nearby point you take
  highways to get close fast, then local streets to fine-tune. (It's a layered
  graph: big jumps first, small steps last.)
- **IVF** — *"sort into buckets first."* Group similar vectors into clusters
  (like shelves in a library). When a query comes in, figure out which shelf it
  belongs to and only search that shelf, ignoring the rest.
- **PQ (Product Quantization)** — *"compress to save space."* Replace each long
  vector with a short code (e.g. shrink 512 bytes to 8). Millions of vectors then
  fit in memory and comparisons get cheaper, at a small accuracy cost.

In FAISS these are just different index types (`IndexHNSWFlat`, `IndexIVFFlat`),
with the **same `.add()` / `.search()` API** as the simple index from Phase 2.

### Persistence
Our earlier indexes lived in memory and vanished when the program ended. Real
systems **save the index to disk** and load it on startup so you don't re-embed
everything each time. The phase3 example does a save-and-reload to show this.

### Phase 3 takeaway
Same goal as before — *find the nearest vectors* — but ANN makes it fast at huge
scale, and persistence makes it durable. Nothing about *meaning* changes.

---

## Deep dive: Phase 4 — Building real RAG

> Examples: [chunking](examples/phase4/example_4a_chunking.py) ·
> [RAG loop](examples/phase4/example_4b_rag.py) · [over a PDF](examples/pdf-rag/example.py)

### What RAG is, in one breath
**RAG = Retrieval-Augmented Generation.** You *retrieve* the relevant pieces of
your own data, then let an LLM *generate* an answer using them. It's how you make
a chatbot that answers from **your** documents instead of guessing.

### Why we need "chunking" first
You can't usefully embed a whole 50-page PDF as one vector — it would blur every
topic into one average and lose detail. So you **chunk**: split the document into
small pieces and embed each piece separately.

Think of chunks as **index cards**. Each card holds one small, focused idea, so
when you search you get back exactly the right card — not the whole book.

**Chunking choices matter:**
- *Too big* → each chunk covers many topics; retrieval gets fuzzy.
- *Too small* → ideas get cut in half and lose context.
- *Overlap* → let neighbouring chunks share a little text, so a sentence split
  across a boundary still appears whole in at least one chunk.
- *Smarter splits* → break on paragraphs, sentences, or meaning ("semantic
  chunking") instead of blindly every N characters.

### The full RAG loop (the pattern behind most AI apps)
1. **Load** your documents (PDF, web pages, tickets…).
2. **Chunk** them into pieces.
3. **Embed** each chunk and **store** the vectors (Phases 1–3).
4. **Retrieve**: embed the user's question, find the nearest chunks.
5. **Generate**: hand those chunks to an LLM as context; it answers using them.

Our [PDF RAG example](examples/pdf-rag/example.py) does steps 1–4 for real on an
actual PDF and fakes step 5 (so it runs with no API key). Swap the fake for a real
LLM call and you have a working RAG app.

### Where the vectors live in production
For real apps you don't keep vectors in a Python list — you use a vector DB:
- **Chroma** — easy, local, persistent; a great first real DB.
- **pgvector** — add vector search to a Postgres database you already run.
- **Pinecone / Weaviate / Qdrant** — hosted, built for large scale.

### Phase 4 takeaway
RAG is the payoff of everything before it: embeddings + storage + retrieval, wired
to an LLM so it answers from your data. Chunking quality quietly decides how good
the whole thing feels.

---

## Deep dive: Phase 5 — Better retrieval quality

> Example: [examples/phase5/example.py](examples/phase5/example.py)

Plain vector search is good, but two upgrades fix most of its weak spots.

### 1. Hybrid search — meaning *and* exact words
Vector search is great at *meaning* but can fumble **exact terms** — product
codes, error numbers, names (e.g. `E-404`). Old-fashioned **keyword search** is
the opposite: perfect on exact terms, blind to meaning.

**Hybrid search runs both and blends the scores**, so you catch *"young cat" ≈
"kitten"* (meaning) **and** an exact `E-404` (keyword). The classic keyword
algorithm is **BM25**; our example uses a simpler word-overlap to show the idea.
The [phase5 example](examples/phase5/example.py) shows a query where vector-only
search struggles but hybrid puts the right doc on top.

### 2. Re-ranking — a careful second look
Fast search over millions of items has to cut corners, so its top-10 isn't always
in the *perfect* order. **Re-ranking** takes that shortlist and re-scores it with a
slower, smarter model so the truly-best result rises to #1.

The smarter model is usually a **cross-encoder**: instead of embedding the query
and document separately, it reads them **together** and judges relevance directly.
More accurate, too slow to run on everything — perfect for re-ordering a shortlist.

### 3. Query transformation — fix the question before searching
Sometimes the user's wording is the problem. Tricks:
- **Multi-query** — generate a few rephrasings and search them all.
- **HyDE** — ask an LLM to *draft a hypothetical answer*, then search with that
  (a full answer often matches the right documents better than a short question).

### 4. Evaluation — measure, don't guess
"Did that change help?" is unanswerable by vibes. Tools like **RAGAS** score
retrieval and answer quality (is the answer grounded in the retrieved text? is the
right context being retrieved?) so you can improve on numbers, not hunches.

### Phase 5 takeaway
Retrieval quality is tunable: combine keyword + vector (hybrid), re-order with a
cross-encoder (re-rank), improve the question (transform), and track it all
(evaluate).

---

## Deep dive: Phase 6 — Advanced & agentic retrieval

> Example: [examples/phase6/example.py](examples/phase6/example.py)

Everything so far retrieves **once**. The frontier is making retrieval **smarter
and more interactive**.

### Agentic RAG — retrieve in a loop
A plain RAG app does one search and lives with the result. An **agent** behaves
like a researcher:
1. Search.
2. Look at what came back and ask *"is this good enough to answer?"*
3. If not, **rewrite the query** (or pick a different source) and search again.
4. Repeat until satisfied, then answer.

Our [phase6 example](examples/phase6/example.py) shows a vague question getting a
weak first result; the agent notices the low score, rewrites the query, and the
second search succeeds. Real agents use an **LLM** to do the judging and rewriting.

### Other advanced directions (worth knowing the names)
- **Multi-modal embeddings** — the same idea for **images, audio, code**, not just
  text. (See the image-embeddings deep dive below.)
- **Knowledge graphs / GraphRAG** — instead of only "what's similar," follow
  **relationships** between facts ("who reports to whom," "which part fits which
  model"). Great when connections matter, not just resemblance.
- **Long-context vs. retrieval** — modern LLMs can read huge amounts at once.
  Sometimes you can just *paste everything* and skip retrieval; but retrieval is
  still cheaper, faster, and more precise for large or changing data. Knowing
  *when* to retrieve vs. *when* to rely on a big context window is a real skill.

### Phase 6 takeaway
Retrieval grows from a one-shot lookup into a **decision process**: an agent that
chooses what to fetch, checks it, and tries again — often across multiple data
types and sources.

---

## Deep dive: Image embeddings (searching pictures)

> Example: [examples/image-embeddings/example.py](examples/image-embeddings/example.py) ·
> Reference: [How do image embeddings work? (Outcome School)](https://outcomeschool.com/blog/how-do-image-embeddings-work)

### The same idea, now for pictures
Everything so far turned **text** into meaning-numbers. The exact same trick works
on **images**: a model reads a picture and outputs an embedding — a list of numbers
that captures *what the image means*. Two similar pictures get similar numbers; a
cat photo and a car photo get very different ones.

### Pixels vs. meaning
A raw image is just a giant grid of color values — it tells you how the image
*looks*, pixel by pixel. An embedding tells you what the image *means*. A neural
network learns this in stages:
- **early layers** spot edges and corners,
- **middle layers** find parts (an eye, a wheel),
- **deep layers** recognize whole objects,
- the **final layer** outputs the embedding.

(These networks are **CNNs** or **Vision Transformers** — you don't need the
internals, just the idea: picture in, meaning-numbers out.)

### CLIP: the trick that lets text search images
The star model is **CLIP**. Its superpower: it embeds **images and text into the
same number-space**. So a photo of a red circle and the words *"a red circle"* land
near each other. That unlocks **cross-modal search** — type words, get matching
pictures (and vice versa). Our [image example](examples/image-embeddings/example.py)
shows both image-to-image similarity and text-to-image search.

### Why it matters
Same workflow as text — embed, store, search by similarity — but now over images.
It powers reverse image search, duplicate/near-duplicate detection, product
matching, face grouping, and recommendations.

### Takeaway
Embeddings aren't a text-only idea. *Any* data a model can "understand" — text,
images, audio, code — can become a vector, and then everything you learned about
storing and searching vectors applies unchanged.

---

## Phase 7 — Latest market direction (Vectorless RAG with PageIndex)

> A different *philosophy* of retrieval, not just a bigger index.
> Examples: [tiny demo](examples/phase7/example.py) ·
> [over a PDF](examples/pdf-vectorless/example.py)

Reference: *What Is PageIndex? How to Build a Vectorless RAG System
(No Embeddings, No Vector DB).*

### First, the one-line summary
Everything in Phases 1–6 finds information by **"what looks similar"** (vector
math). The newest direction flips that to **"what is actually relevant"** by
letting the LLM *think* about where the answer lives — the same way a person uses
a book's table of contents instead of scanning every page.

### The problem it tackles
Classic embedding RAG (Phases 1–4) has known weak spots:
- **Chunking is arbitrary.** To embed a document you must chop it into pieces. A
  fixed cut can split one idea across two chunks, so neither chunk fully makes
  sense on its own.
- **Similarity ≠ relevance.** The vector that is *closest* in number-space is not
  always the passage that *answers* the question. Two sentences can look similar
  yet one is the real answer and the other is a distraction.
- **Lost context.** A chunk is retrieved alone, stripped of the section it came
  from, so the model loses the "where am I in the document" signal.
- **Tuning + infrastructure overhead.** Chunk size, overlap, top-k, which
  embedding model, which index — all need tuning. Plus you must host and maintain
  a vector database.

### What PageIndex does differently (in plain words)
Think of how *you* find an answer in a thick manual:
1. You open the **table of contents**.
2. You reason: "this question is about billing → Chapter 4 → 'Refunds' section."
3. You jump straight there and read.

PageIndex makes the LLM do exactly that:
1. It builds a **tree / table-of-contents view** of the document (sections →
   subsections), instead of a pile of vectors.
2. At question time the **LLM reasons** over that tree to decide *which node* to
   open — no distance math involved.
3. It reads that section (with its surrounding context intact) and answers.

So:
- **No embeddings and no vector database** — retrieval is *reasoning over
  structure*, not *similarity over numbers*.
- **Context stays whole** — you keep the section → subsection hierarchy.
- **Decisions are explainable** — the model can say *why* it opened a section,
  which is hard to get from "these vectors were 0.83 similar."

### A concrete mini-example
Question: *"What is the refund window for annual plans?"*
- **Embedding RAG:** embeds the question, pulls the top-k chunks whose vectors are
  nearest. It might grab a chunk that mentions "annual plans" but is about
  *upgrades*, because the words look similar.
- **PageIndex:** the LLM reads the table of contents, reasons "Billing → Refunds →
  Annual", opens that exact section, and reads the real policy.

### How it compares to what we built
| | Phases 1–4 (embedding RAG) | PageIndex (vectorless) |
|---|---|---|
| How it finds info | nearest vector by similarity | LLM reasons over doc structure |
| Needs embeddings? | yes | no |
| Needs a vector DB? | yes | no |
| Chunking required? | yes | mostly no (uses the document's own structure) |
| Explainable choice? | hard | yes (the reasoning is visible) |
| Best at | huge, flat, unstructured collections | long, well-structured documents |

### When to use which (the honest take)
- **Vectorless / PageIndex shines** on long, *structured* documents — manuals,
  contracts, financial filings, textbooks — where structure carries meaning and
  accuracy matters more than raw speed.
- **Classic embedding RAG still wins** when you have a *huge, flat* pile of
  loosely-structured text (millions of short snippets, chat logs, product
  reviews) where there's no clean hierarchy to reason over and speed matters.
- They're **not enemies** — real systems increasingly *combine* them: reason to
  the right document/section, then optionally use vectors inside it.

### Why this is "the latest direction"
It rides the trend of LLMs getting **much better at reasoning** and handling
**longer context**. As models can read and think over more text reliably, the
job of retrieval shifts from "compress everything into vectors and hope similarity
finds it" toward "let a smart model decide what to read." That's the broader
theme: **reasoning-based retrieval** replacing pure **similarity-based retrieval**.

### Phase 7 goals
- [ ] Read the PageIndex article end to end
- [ ] Be able to explain **reasoning-based** vs. **similarity-based** retrieval in one sentence each
- [ ] Know **when** vectorless wins vs. when classic embedding RAG is still better
- [ ] Optionally build a tiny PageIndex-style demo and compare its answers to our Phase 2 setup
