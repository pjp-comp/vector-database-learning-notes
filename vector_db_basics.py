"""Tiny vector database demo.

This shows two ideas:
1. How text becomes vectors using a Hugging Face embedding model.
2. How a vector database finds the nearest item with cosine similarity.

Run:
  python vector_db_basics.py
"""

from __future__ import annotations

import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denom = float(np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0.0:
        return 0.0
    return float(np.dot(a, b) / denom)


def main() -> None:
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    documents = [
        "cat",
        "dog",
        "puppy",
        "apple",
        "orange",
        "car",
        "bus",
        "train",
    ]

    vectors = model.encode(documents, normalize_embeddings=True)

    query = "kitten"
    query_vector = model.encode([query], normalize_embeddings=True)[0]

    scores = [cosine_similarity(query_vector, vector) for vector in vectors]
    ranked = sorted(zip(documents, scores), key=lambda item: item[1], reverse=True)

    print("Query:", query)
    print("Nearest matches:")
    for word, score in ranked[:5]:
        print(f"  {word:>8}  similarity={score:.4f}")

    print()
    print("Example vector shape:", vectors[0].shape)
    print("First 8 numbers for 'cat':", np.round(vectors[0][:8], 4).tolist())
    print()
    print("What happened:")
    print("- The Hugging Face model turned each word into a high-dimensional vector.")
    print("- We compared the query vector to stored vectors with cosine similarity.")
    print("- A vector database does the same search, but at larger scale and with indexes.")


if __name__ == "__main__":
    main()