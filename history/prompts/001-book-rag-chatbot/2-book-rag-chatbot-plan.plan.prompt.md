---
id: 2
title: Book RAG Chatbot Plan
stage: plan
date: 2025-12-11
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-book-rag-chatbot
branch: 001-book-rag-chatbot
user: Claude
command: /sp.plan
labels: [plan,rag,book,chatbot,openai-agent,qdrant]
links:
  spec: specs/001-book-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-book-rag-chatbot/plan.md
 - specs/001-book-rag-chatbot/research.md
 - specs/001-book-rag-chatbot/data-model.md
 - specs/001-book-rag-chatbot/quickstart.md
 - specs/001-book-rag-chatbot/contracts/chatbot-api.yaml
 - .specify/memory/constitution.md
 - CLAUDE.md
tests:
 - none
---

## Prompt

```text
You are the execution planner for a RAG chatbot system built with OpenAI Agent SDK, using book content ingested from a sitemap.xml and stored in Qdrant.

Your role: For each user query, create a detailed, actionable execution plan that specifies steps, tools, and branching logic. Do NOT generate answers — only plan the workflow.

RULES:

1. Always produce a step-by-step plan before any tool is called.
2. Use this operational order:
   a. Interpret user query.
   b. Decide retrieval strategy.
   c. Query Qdrant vector database (consider selected text if provided).
   d. Pass retrieved passages to OpenAI Agent SDK for answer generation.
3. If the query is outside the book content, include a branch:
   "Return: No supporting text found in the book."
4. If user provides selected text, retrieval must be restricted to those chunk IDs.
5. Specify tool calls with parameters before they are executed.
   Example: "Step 3: Call qdrant.search(query_embedding, top_k=5)".
6. Include conditional logic if retrieval returns zero hits:
   - "If no hits → produce: 'No supporting text found in the book.'"
7. Do not hallucinate or generate content outside retrieved passages.
8. Output format:
PLAN:
1. …
2. …
3. …
4. …
5. …
No JSON, only normal text.
```

## Response snapshot

Created a comprehensive implementation plan for the Book RAG Chatbot feature, including:

- Detailed technical context specifying Python 3.11, OpenAI Agent SDK, Qdrant client, FastAPI, and other dependencies
- Constitution check ensuring all constitutional principles are satisfied:
  * Source-Based Answering (Constitution I)
  * Selected Text Compliance (Constitution II)
  * No Outside Knowledge (Constitution III)
  * No Hallucination Policy (Constitution IV)
  * Factual Accuracy Requirement (Constitution V)
  * System Transparency Limitation (Constitution VI)

- Well-defined project structure with clear separation of concerns:
  * Models for chatbot, content, and query processing
  * Services for RAG, Qdrant, ingestion, and OpenAI integration
  * API layer with FastAPI
  * Utilities for embeddings and validation

- Research document addressing technical decisions:
  * OpenAI Agent SDK integration rationale
  * Qdrant vector database selection
  * FastAPI framework choice
  * Content ingestion from sitemap.xml approach
  * Response format and schema definition

- Data model defining all key entities:
  * Book Content, User Query, Retrieved Passages, Response, Evidence, and Chunk ID
  * Validation rules and state transitions
  * API contract specifications

- Quickstart guide for easy setup and usage
- API contract in YAML format defining endpoints, request/response formats, and error handling
- Agent context updated to include new technologies (Python 3.11, OpenAI Agent SDK, Qdrant client, FastAPI)

## Outcome

- ✅ Impact: High - established complete implementation architecture for RAG chatbot
- 🧪 Tests: None needed - planning artifacts created
- 📁 Files: 7 files created/updated (plan.md, research.md, data-model.md, quickstart.md, contracts/chatbot-api.yaml, constitution.md, CLAUDE.md)
- 🔁 Next prompts: Ready for task generation phase with `/sp.tasks`
- 🧠 Reflection: Plan comprehensively covers all constitutional requirements with proper architecture and implementation guidance

## Evaluation notes (flywheel)

- Failure modes observed: None - successful planning phase completion
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Generate implementation tasks with `/sp.tasks`