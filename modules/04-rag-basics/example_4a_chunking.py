"""
PHASE 4a — Chunking: splitting a document into searchable pieces.

Why:
    Real documents are too long to embed as one vector — you'd lose detail.
    So we split them into smaller "chunks", and embed each chunk separately.

This example shows two simple chunking styles so you can SEE the difference:
    1. By paragraph (natural boundaries).
    2. By fixed size with overlap (so an idea split across a boundary isn't lost).

No model needed — this is just about cutting text into pieces.

Run:
    python modules/04-rag-basics/example_4a_chunking.py
"""

document = (
    "Vector databases store data as embeddings. "
    "An embedding is a list of numbers that captures meaning. "
    "Similar meanings get similar numbers.\n\n"
    "To search a long document, you split it into chunks. "
    "Each chunk is embedded separately. "
    "At query time you retrieve the most relevant chunks.\n\n"
    "Chunk size matters. Too big loses detail; too small loses context. "
    "Overlap helps keep ideas together across chunk boundaries."
)


def chunk_by_paragraph(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def chunk_by_size(text, size=80, overlap=20):
    text = text.replace("\n\n", " ")
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end].strip())
        start += size - overlap  # step back by 'overlap' so chunks share edges
    return chunks


print("=== Chunking by paragraph ===")
for i, chunk in enumerate(chunk_by_paragraph(document), 1):
    print(f"[{i}] {chunk}\n")

print("=== Chunking by fixed size (80 chars, 20 overlap) ===")
for i, chunk in enumerate(chunk_by_size(document), 1):
    print(f"[{i}] {chunk}")

print(
    "\nTakeaway: chunking decides what 'a result' is. Good chunks = good retrieval."
    "\nReal projects also chunk by sentences or by meaning (semantic chunking)."
)
