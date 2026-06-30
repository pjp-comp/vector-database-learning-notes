"""
PHASE 7 — Vectorless RAG (PageIndex style): reason over structure, no embeddings.

The newest direction: instead of turning everything into vectors and searching by
similarity, give the model the document's STRUCTURE (its table of contents) and
let it REASON about which section to open — like a human using a manual's index.

Notice: this file imports NO embedding model and NO vector library at all.
Retrieval here is reasoning over a tree, not similarity over numbers.

About the "reasoning":
    A real system uses an LLM to pick the right section. To run with no API key,
    we fake the LLM with simple keyword matching over the section titles. The
    point is the SHAPE: navigate a structure instead of comparing vectors.

Run:
    python modules/08-vectorless-rag/example.py
"""

# A document represented as a tree (table of contents), like PageIndex builds.
document = {
    "title": "Company Handbook",
    "sections": [
        {
            "title": "Billing",
            "subsections": [
                {"title": "Refunds", "text": "Annual plans are refundable within 30 days."},
                {"title": "Invoices", "text": "Invoices are emailed on the 1st of each month."},
            ],
        },
        {
            "title": "Accounts",
            "subsections": [
                {"title": "Passwords", "text": "Reset your password in account settings."},
                {"title": "Login Issues", "text": "Use the forgot-password link to recover access."},
            ],
        },
    ],
}


def reason_pick_section(question, doc):
    """FAKE 'reasoning'. A real system asks an LLM: 'which section answers this?'
    Here we score titles by how many question words they share, and walk the tree.
    """
    q_words = set(question.lower().replace("?", "").split())

    def title_score(title):
        return len(q_words & set(title.lower().split()))

    # Step 1: pick the best top-level section by its title.
    best_section = max(doc["sections"], key=lambda s: title_score(s["title"]))
    print(f"Reasoning: this question looks like '{best_section['title']}'.")

    # Step 2: within it, pick the best subsection.
    best_sub = max(best_section["subsections"], key=lambda s: title_score(s["title"]))
    print(f"Reasoning: drilling into '{best_section['title']} > {best_sub['title']}'.")
    return best_sub


question = "What is the refund window for annual plans?"
print(f'Question: "{question}"\n')

picked = reason_pick_section(question, document)
print(f"\nOpened section: {picked['title']}")
print(f"Answer text: {picked['text']}")

print(
    "\nTakeaway: NO embeddings, NO vector DB were used. We navigated the document's"
    "\nstructure by reasoning, the way you'd use a table of contents. Real systems"
    "\nput an LLM in the 'reasoning' step for much smarter navigation."
)
