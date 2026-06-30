"""
PHASE 3 — Scaling the index (ANN: Approximate Nearest Neighbour).

The problem:
    With a few items, checking every vector one-by-one ("brute force") is fine.
    With millions, that becomes too slow. ANN indexes find the nearest vectors
    *approximately* but MUCH faster.

This example:
    1. Makes 50,000 fake vectors (random numbers; no model needed here).
    2. Searches them with a brute-force index (exact, slower).
    3. Searches them with an HNSW index (approximate, faster).
    4. Shows the two usually agree on the top result.
    5. Saves the index to disk and loads it back (persistence).

We use random vectors so it runs fast and needs no model download.

Run (from the project root, with the venv active):
    python modules/03-scaling-ann/example.py
"""

import os
import time

import faiss
import numpy as np

N = 50_000   # number of vectors
DIM = 128    # numbers per vector

print(f"Creating {N:,} random vectors of length {DIM}...")
rng = np.random.default_rng(42)
data = rng.random((N, DIM), dtype="float32")
query = rng.random((1, DIM), dtype="float32")


def time_search(index, label):
    start = time.perf_counter()
    distances, ids = index.search(query, 5)  # top 5 nearest
    elapsed_ms = (time.perf_counter() - start) * 1000
    print(f"  {label:<22} top result = id {ids[0][0]:<6}  ({elapsed_ms:.2f} ms)")
    return ids[0][0]


# 1. Brute force: IndexFlatL2 checks every vector. Exact, but slower at scale.
flat = faiss.IndexFlatL2(DIM)
flat.add(data)

# 2. HNSW: a graph index. Approximate, but scales to millions quickly.
hnsw = faiss.IndexHNSWFlat(DIM, 32)  # 32 = graph connections per node
hnsw.add(data)

print("\nSearching the same query two ways:")
exact_top = time_search(flat, "Brute force (exact)")
approx_top = time_search(hnsw, "HNSW (approximate)")

if exact_top == approx_top:
    print("\nBoth agree on the nearest vector — approximate ~= exact, but faster.")
else:
    print("\nThey differ slightly: that's the 'approximate' trade-off for speed.")

# 3. Persistence: save the index to disk, then load it back.
path = os.path.join(os.path.dirname(__file__), "hnsw.index")
faiss.write_index(hnsw, path)
reloaded = faiss.read_index(path)
print(f"\nSaved the index to disk and reloaded it ({reloaded.ntotal:,} vectors).")
os.remove(path)  # clean up the demo file

print(
    "\nTakeaway: same idea as Phase 2 (find nearest), but an ANN index makes it"
    "\nfast at huge scale, and the index can be saved so it survives restarts."
)
