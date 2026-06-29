"""Phase 2 vector database demo — closer to a real vector DB.

This builds on Phase 1 (vector_db_basics.py) by adding the three things a
real vector database has that the tiny demo did not:

1. METADATA      -> each item stores vector + original text + metadata
2. REAL INDEX    -> uses FAISS (an ANN library) instead of a brute-force loop
3. FILTERING     -> can filter results by metadata (e.g. only category="animal")

It also shows the SAME query measured with cosine similarity AND euclidean
distance, so you can compare the two metrics side by side.

Run:
  python vector_db_phase2.py
"""

from __future__ import annotations

from dataclasses import dataclass

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass
class Item:
    """One record in our vector store: the text plus its metadata.

    A real vector DB stores exactly this shape: the original data + metadata,
    sitting next to the vector (the embedding) in the index.
    """

    text: str
    category: str


def main() -> None:
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # 1. Documents now carry METADATA (category), not just bare text.
    items = [
        Item("cat", "animal"),
        Item("dog", "animal"),
        Item("puppy", "animal"),
        Item("apple", "fruit"),
        Item("orange", "fruit"),
        Item("car", "vehicle"),
        Item("bus", "vehicle"),
        Item("train", "vehicle"),
    ]

    texts = [item.text for item in items]

    # Normalized embeddings: with unit-length vectors, an INNER-PRODUCT search
    # is identical to COSINE similarity. This is how real DBs do "cosine".
    vectors = model.encode(texts, normalize_embeddings=True).astype("float32")
    dim = vectors.shape[1]  # 384 for all-MiniLM-L6-v2

    # 2. Build a REAL FAISS index.
    #    IndexFlatIP = inner product. On normalized vectors == cosine similarity.
    #    (FAISS also offers IndexHNSWFlat / IndexIVFFlat for huge-scale ANN —
    #     same API, just approximate + much faster on millions of vectors.)
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)

    query = "kitten"
    query_vector = model.encode([query], normalize_embeddings=True).astype("float32")

    # 3a. Search with the FAISS index (cosine via inner product).
    k = len(items)  # ask for all, so we can also show filtering
    scores, ids = index.search(query_vector, k)

    print(f"Query: {query}\n")

    print("Cosine similarity (via FAISS inner-product index):")
    for score, idx in zip(scores[0], ids[0]):
        item = items[idx]
        print(f"  {item.text:>8}  [{item.category:<7}]  cosine={score:.4f}")

    # 3b. Same query, EUCLIDEAN distance, computed directly so you can compare.
    #     Lower distance = more similar (opposite direction from cosine).
    euclid = np.linalg.norm(vectors - query_vector, axis=1)
    euclid_ranked = sorted(zip(items, euclid), key=lambda pair: pair[1])
    print("\nEuclidean distance (lower = closer):")
    for item, dist in euclid_ranked:
        print(f"  {item.text:>8}  [{item.category:<7}]  distance={dist:.4f}")

    # 4. METADATA FILTERING: only keep "animal" results, then rank by cosine.
    print('\nFiltered search (category == "animal" only):')
    for score, idx in zip(scores[0], ids[0]):
        item = items[idx]
        if item.category == "animal":
            print(f"  {item.text:>8}  cosine={score:.4f}")

    print("\nWhat changed vs Phase 1:")
    print("- Each item now stores metadata (category), not just text.")
    print("- A real FAISS index does the search instead of a Python loop.")
    print("- We compared cosine vs euclidean on the same query.")
    print("- We filtered results by metadata after the similarity search.")


if __name__ == "__main__":
    main()
