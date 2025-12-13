# Implementation Plan: Book RAG Chatbot

**Branch**: `001-book-rag-chatbot` | **Date**: 2025-12-11 | **Spec**: [specs/001-book-rag-chatbot/spec.md](specs/001-book-rag-chatbot/spec.md)
**Input**: Feature specification from `/specs/001-book-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a book-content chatbot using Retrieval-Augmented Generation (RAG) with OpenAI Agent SDK. The system will ingest book content from sitemap.xml, store it in Qdrant vector database, and respond to user queries with answers strictly based on retrieved passages. The system will follow constitutional principles of source-based answering, no hallucination, and factual accuracy.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: OpenAI Agent SDK, Qdrant client, Pydantic, FastAPI
**Storage**: Qdrant vector database (for embeddings), local files (for sitemap ingestion)
**Testing**: pytest with unit and integration tests
**Target Platform**: Linux server (web-based API)
**Project Type**: Single project (web-based API)
**Performance Goals**: 90% of queries respond within 5 seconds, support 1000 concurrent users
**Constraints**: <200ms p95 latency for retrieval, <500MB memory usage, offline-capable for cached content
**Scale/Scope**: Support up to 10,000 book content chunks, handle 100 queries per minute

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

1. **Source-Based Answering (Constitution I)**: System MUST answer ONLY from book's retrieved passages. Implementation will ensure all responses are generated from retrieved content, with "No supporting text found in the book" when no relevant passages exist.

2. **Selected Text Compliance (Constitution II)**: When user selects text, system MUST answer STRICTLY from that text. Implementation will include functionality to restrict retrieval to specific chunk IDs when provided.

3. **No Outside Knowledge (Constitution III)**: System MUST NOT use outside knowledge unless explicitly requested. Implementation will prevent use of pretraining memory and external APIs except for the specified Qdrant retrieval.

4. **No Hallucination Policy (Constitution IV)**: System MUST never guess, invent facts, or hallucinate. Implementation will include strict validation to ensure all responses are grounded in retrieved passages.

5. **Factual Accuracy Requirement (Constitution V)**: System MUST keep answers short, factual, and based only on retrieved text. Implementation will include citation requirements and excerpt validation.

6. **System Transparency Limitation (Constitution VI)**: System MUST NOT reveal internal system details. Implementation will ensure no internal mechanics are exposed in responses.

## Project Structure

### Documentation (this feature)

```text
specs/001-book-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   ├── chatbot.py           # Core chatbot model and response schema
│   ├── content.py           # Book content data models
│   └── query.py             # Query processing models
├── services/
│   ├── rag_service.py       # Main RAG service orchestrating query flow
│   ├── qdrant_service.py    # Qdrant vector database operations
│   ├── ingestion_service.py # Content ingestion from sitemap.xml
│   └── openai_service.py    # OpenAI Agent SDK integration
├── api/
│   ├── main.py              # FastAPI application entry point
│   ├── routes/
│   │   └── chat.py          # Chat endpoint definitions
│   └── middleware/
│       └── validation.py      # Request validation middleware
└── utils/
    ├── embedding_utils.py   # Text embedding utilities
    └── validation_utils.py  # Response validation utilities

tests/
├── unit/
│   ├── models/
│   ├── services/
│   └── utils/
├── integration/
│   ├── api/
│   └── services/
└── contract/
    └── chatbot_contract.py

data/
├── embeddings/              # Vector embeddings storage
└── content/                 # Ingested book content
```

**Structure Decision**: Single project web-based API structure selected, with clear separation of concerns between models, services, API routes, and utilities. The structure supports the RAG flow with dedicated services for each component of the system.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
