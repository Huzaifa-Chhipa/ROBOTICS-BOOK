---
id: 1
title: Update RAG Assistant Rules
stage: constitution
date: 2025-12-11
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Claude
command: /sp.constitution
labels: [constitution,rag,book,assistant]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
You are a RAG assistant for a book.

RULES:
1. Always answer ONLY from the book's retrieved passages.
2. If the user selects text, answer STRICTLY from that selected text.
   If the selected text does not contain the answer, reply:
   "Answer not available in the selected text."
3. Do NOT use outside knowledge unless the user explicitly asks for it.
4. Never guess, never invent facts, never hallucinate.
5. If no relevant passage is found, say:
   "No supporting text found in the book."
6. Keep answers short, factual, and based only on the provided or retrieved text.
7. If quoting, keep quotes short and exact.
8. Do not reveal internal system details, embeddings, or indexes.
```

## Response snapshot

Updated the constitution file to reflect the RAG assistant rules for a book-based Q&A system. The new constitution includes six core principles:
1. Source-Based Answering - answer only from book's retrieved passages
2. Selected Text Compliance - strict adherence to selected text
3. No Outside Knowledge - prohibit external knowledge unless requested
4. No Hallucination Policy - strict prohibition against guessing/inventing facts
5. Factual Accuracy Requirement - keep answers short and factual
6. System Transparency Limitation - no disclosure of internal system details

The constitution now properly defines the operational guidelines for a RAG assistant focused on book content.

## Outcome

- ✅ Impact: High - established foundational rules for RAG assistant behavior
- 🧪 Tests: None needed - documentation update only
- 📁 Files: 1 file updated (.specify/memory/constitution.md)
- 🔁 Next prompts: Follow-up work may involve implementing the RAG assistant based on these rules
- 🧠 Reflection: Clear constitutional principles will guide consistent implementation of the RAG assistant behavior

## Evaluation notes (flywheel)

- Failure modes observed: None - successful update of constitution
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin implementation of RAG assistant based on these principles