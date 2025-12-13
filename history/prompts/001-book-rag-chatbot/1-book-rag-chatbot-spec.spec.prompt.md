---
id: 1
title: Book RAG Chatbot Spec
stage: spec
date: 2025-12-11
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-book-rag-chatbot
branch: 001-book-rag-chatbot
user: Claude
command: /sp.specify
labels: [spec,rag,book,chatbot,openai-agent]
links:
  spec: specs/001-book-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-book-rag-chatbot/spec.md
 - specs/001-book-rag-chatbot/checklists/requirements.md
tests:
 - none
---

## Prompt

```text
You are a book-content chatbot built on a Retrieval-Augmented Generation (RAG) system using the OpenAI Agent SDK. Your knowledge source consists only of the book content ingested from the sitemap.xml and embedded into Qdrant.

RULES:

1. Use only the ingested book content from the vector database. Never use outside knowledge unless explicitly asked.
2. For every user query, use the OpenAI Agent SDK's tool-calling flow:
   - First: interpret the query
   - Then: call the retrieval tool (Qdrant search)
   - Finally: generate the answer strictly from retrieved passages
3. Never produce an answer without retrieval unless the user asks for a meta/system explanation.
4. If user provides selected text, restrict retrieval only to those chunk IDs.
5. If no supporting passage exists in the selected text, answer exactly:
   "Answer not available in the selected text."
6. If no passage is found in the database:
   "No supporting text found in the book."
7. Never hallucinate, fabricate details, or use pretraining memory.
8. All answers must be concise, factual, and directly tied to retrieved passages.
9. When quoting, quote only from retrieved passages and keep excerpts ≤200 characters.
10. Always output in the defined JSON schema, followed by a short human-readable answer.
```

## Response snapshot

Created a comprehensive specification for the book-content chatbot built on a RAG system using the OpenAI Agent SDK. The specification includes:

- Three prioritized user stories covering core functionality:
  1. Query Book Content (P1) - Primary functionality to answer questions from book content
  2. Get Selected Text Answers (P2) - Focused queries on specific text segments
  3. Receive Structured Responses (P3) - JSON responses with citations and confidence

- 14 functional requirements covering all specified rules including:
  - Using only ingested book content as knowledge source
  - Following OpenAI Agent SDK tool-calling flow
  - Providing specific responses for edge cases
  - Outputting in JSON schema with citations
  - Preventing hallucination and external knowledge use

- Success criteria with measurable outcomes including 95% factual correctness, 5-second response times, and 0% hallucination rate

- Key entities defined: Book Content, User Query, Retrieved Passages, Response, and Chunk ID

## Outcome

- ✅ Impact: High - established complete functional specification for RAG chatbot
- 🧪 Tests: None needed - specification document created
- 📁 Files: 2 files created (spec.md and requirements checklist)
- 🔁 Next prompts: Ready for planning phase with `/sp.plan`
- 🧠 Reflection: Specification comprehensively covers all requirements with testable acceptance criteria

## Evaluation notes (flywheel)

- Failure modes observed: None - successful specification creation
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin planning implementation with `/sp.plan`