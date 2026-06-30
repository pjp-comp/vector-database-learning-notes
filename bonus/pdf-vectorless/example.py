"""
PDF VECTORLESS RAG — answer questions about the SAME PDF, with NO embeddings.

This is the PageIndex idea (Phase 7) applied to a real file:
    1. Read the PDF and build a TREE of its headings (its table of contents).
    2. REASON over the headings to pick the section that answers the question.
    3. Read that section's text and answer.

Notice: no embedding model, no vector database, no FAISS imported. Retrieval is
reasoning over structure, not similarity over numbers.

The "reasoning" step is faked with simple keyword matching over headings so it
runs with no API key. A real system would ask an LLM "which heading answers this?"

Run (from project root, venv active):
    python bonus/pdf-vectorless/example.py
"""

import os
import re
import sys

from pypdf import PdfReader

HERE = os.path.dirname(__file__)
PDF_PATH = os.path.abspath(os.path.join(HERE, "..", "handbook.pdf"))
PDF_MAKER_DIR = os.path.abspath(os.path.join(HERE, "..", "pdf-rag"))

HEADING_RE = re.compile(r"^\d+(\.\d+)*\s")  # lines like "1.1 Refunds"


def ensure_pdf():
    if not os.path.exists(PDF_PATH):
        print("Sample PDF not found — creating it...")
        sys.path.insert(0, PDF_MAKER_DIR)
        from make_sample_pdf import build_pdf
        build_pdf()


def parse_sections(path):
    """Turn the PDF into a list of (heading, body-text) pairs by spotting numbered
    headings like '1.1 Refunds'. This is our lightweight 'table of contents'."""
    reader = PdfReader(path)
    lines = []
    for page in reader.pages:
        lines.extend((page.extract_text() or "").splitlines())

    sections, current_heading, current_body = [], None, []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if HEADING_RE.match(line):
            if current_heading is not None:
                sections.append((current_heading, " ".join(current_body).strip()))
            current_heading, current_body = line, []
        elif current_heading is not None:
            current_body.append(line)
    if current_heading is not None:
        sections.append((current_heading, " ".join(current_body).strip()))
    return sections


def reason_pick(question, sections):
    """FAKE 'reasoning'. A real system asks an LLM which heading fits.
    Here: score each heading by how many question words it shares."""
    q_words = set(re.findall(r"[a-z]+", question.lower()))

    def score(heading):
        h_words = set(re.findall(r"[a-z]+", heading.lower()))
        return len(q_words & h_words)

    best = max(sections, key=lambda s: score(s[0]))
    print("Table of contents found in the PDF:")
    for heading, _ in sections:
        marker = "  ->" if heading == best[0] else "    "
        print(f"{marker} {heading}")
    print(f"\nReasoning: '{best[0]}' best matches the question.")
    return best


ensure_pdf()
sections = parse_sections(PDF_PATH)

question = "How many days do I have to refund an annual plan?"
print(f'Question: "{question}"\n')

heading, body = reason_pick(question, sections)
print(f"\nOpened section: {heading}")
print(f"Answer text: {body}")

print(
    "\nSame PDF, same question as bonus/pdf-rag/example.py — but here we used"
    "\nNO embeddings and NO vector DB. We navigated the document's structure by"
    "\nreasoning, the way you'd flip to the right section of a manual."
)
