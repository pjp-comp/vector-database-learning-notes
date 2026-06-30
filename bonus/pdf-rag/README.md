# PDF RAG — classic RAG over a real PDF

**Big idea:** take an actual PDF, chunk it, embed the chunks, and answer questions
by retrieving the most relevant pieces. This is Phases 1–4 applied to a real file.

## Run
```bash
python bonus/pdf-rag/example.py
```
It auto-creates a small sample PDF (`bonus/handbook.pdf`) the first time. You
can also create it explicitly:
```bash
python bonus/pdf-rag/make_sample_pdf.py
```

## What you'll see
The PDF is split into chunks; a refund question retrieves the right chunk and an
answer is built from it. (The LLM step is a labeled fake — no API key needed.)

## Compare
Run [bonus/pdf-vectorless/example.py](../pdf-vectorless/) to answer the **same
PDF and question without embeddings** — a side-by-side of the two approaches.

## Words to know
- **PDF text extraction** — pulling the words out of a PDF (here with `pypdf`).
- **Chunking** — splitting the text into searchable pieces.
- **RAG** — retrieve relevant chunks, then let an LLM answer from them.

→ Full explanation: [learning_notes.md](../../learning_notes.md#deep-dive-phase-4--building-real-rag)
