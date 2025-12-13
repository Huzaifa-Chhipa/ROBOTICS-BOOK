# Implementation Tasks: Book RAG Chatbot

**Feature**: Book RAG Chatbot with OpenAI Agent SDK, Gemini API, Cohere embeddings, Qdrant vector database
**Branch**: `001-book-rag-chatbot` | **Date**: 2025-12-11
**Spec**: [specs/001-book-rag-chatbot/spec.md](specs/001-book-rag-chatbot/spec.md)

## Dependencies

User stories must be implemented in priority order:
- US1 (P1) must complete before US2 (P2)
- US1 (P1) must complete before US3 (P3)

## Parallel Execution Examples

Per story parallelization opportunities:
- **US1**: [P] Create models in parallel → [P] Create services in parallel → [P] Create API routes in parallel
- **US2**: [P] Extend models → [P] Extend services → [P] Update API routes
- **US3**: [P] Update response models → [P] Update service logic → [P] Update API responses

## Implementation Strategy

**MVP Scope**: Complete US1 (Query Book Content) with basic functionality:
- Environment setup
- Qdrant connection
- Cohere embedding function
- Basic agent with retrieve tool
- Query endpoint that returns answers from book content

**Incremental Delivery**: Each user story builds on the previous with additional capabilities:
- US1: Core RAG functionality
- US2: Selected text restriction capability
- US3: Structured response with citations and confidence

---

## Phase 1: Setup

**Goal**: Initialize project structure and configure required dependencies

- [X] T001 Create project directory structure per implementation plan in src/, tests/, data/
- [X] T002 Create requirements.txt with dependencies: agents, openai, cohere, qdrant-client, python-dotenv, fastapi, uvicorn, pydantic
- [X] T003 Create .env file template with GEMINI_API_KEY, COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY placeholders
- [X] T004 Create main application entry point in src/api/main.py with basic FastAPI setup
- [X] T005 [P] Install and configure pytest for testing framework
- [X] T006 Set up gitignore for Python project with .env, __pycache__, .env, .venv exclusions

## Phase 2: Foundational Components

**Goal**: Implement core infrastructure components required by all user stories

- [X] T010 Create embedding utilities in src/utils/embedding_utils.py with get_embedding function using Cohere
- [X] T011 Create Qdrant service in src/services/qdrant_service.py with connection and query methods
- [X] T012 Configure environment variables loading in src/config.py
- [X] T013 Create OpenAI service in src/services/openai_service.py with Gemini API configuration
- [X] T014 [P] Create validation utilities in src/utils/validation_utils.py for response validation
- [X] T015 Create base data models in src/models/base.py for common model definitions

## Phase 3: [US1] Query Book Content

**Goal**: Implement core functionality to answer questions based on book content

**Independent Test**: The system can respond to user queries with answers derived solely from the book content, following the required rules for accuracy and citation.

- [X] T020 Create User Query model in src/models/query.py with validation rules
- [X] T021 Create Retrieved Passages model in src/models/retrieved_passages.py with validation rules
- [X] T022 Create Response model in src/models/response.py with JSON schema validation
- [X] T023 [P] Create RAG service in src/services/rag_service.py implementing query interpretation and retrieval strategy
- [X] T024 [P] Implement retrieve function as an agent tool in src/services/rag_service.py with Qdrant vector database search
- [X] T025 Create agent configuration in src/agents/chatbot_agent.py using OpenAI Agent SDK with Gemini model
- [X] T026 [P] Create chat endpoint in src/api/routes/chat.py with POST /api/v1/query
- [X] T027 [P] Implement query endpoint logic that calls retrieve tool and passes to agent
- [X] T028 Handle edge case: when no relevant passages found, return "No supporting text found in the book."
- [X] T029 [P] Add response validation to ensure answers are based only on retrieved passages
- [X] T030 [P] Create basic test suite for US1 in tests/unit/test_us1_query_content.py
- [X] T031 [P] Create integration test for US1 in tests/integration/test_us1_integration.py

## Phase 4: [US2] Get Selected Text Answers

**Goal**: Implement functionality to restrict answers to specific selected text chunks

**Independent Test**: When a user provides selected text or chunk IDs, the system restricts its retrieval to only those specific content areas.

- [X] T040 [P] Update User Query model to support selected_chunks field validation
- [X] T041 [P] Update retrieve function to accept and filter by specific chunk IDs when provided
- [X] T042 Update RAG service to implement selected text restriction logic
- [X] T043 [P] Update agent instructions to handle selected text scenarios
- [X] T044 Handle edge case: when selected text doesn't contain answer, return "Answer not available in the selected text."
- [X] T045 [P] Update query endpoint to accept selected_chunks parameter
- [X] T046 [P] Add validation to ensure selected chunk IDs exist in database
- [X] T047 [P] Create test suite for US2 in tests/unit/test_us2_selected_text.py
- [X] T048 [P] Create integration test for US2 in tests/integration/test_us2_integration.py

## Phase 5: [US3] Receive Structured Responses

**Goal**: Implement structured response format with citations and confidence levels

**Independent Test**: The system outputs responses in the required JSON schema with evidence citations and confidence levels.

- [X] T060 [P] Update Response model to include evidence array with doc_id, chunk_id, and quote fields
- [X] T061 [P] Update Evidence model with validation for ≤200 character quotes
- [X] T062 Update RAG service to extract and format evidence from retrieved passages
- [X] T063 [P] Implement confidence calculation logic based on similarity scores
- [X] T064 [P] Update agent to include citations with document ID, chunk identifier, and excerpts ≤200 characters
- [X] T065 [P] Update API response format to match required JSON schema with evidence and confidence
- [X] T066 [P] Add validation to ensure all quotes are verbatim from source passages
- [X] T067 [P] Create test suite for US3 in tests/unit/test_us3_structured_responses.py
- [X] T068 [P] Create integration test for US3 in tests/integration/test_us3_integration.py

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Complete the implementation with error handling, performance optimization, and documentation

- [ ] T080 [P] Add comprehensive error handling for Qdrant connection failures
- [ ] T081 [P] Add comprehensive error handling for Cohere API failures
- [ ] T082 [P] Add comprehensive error handling for Gemini API failures
- [ ] T083 [P] Implement caching for frequently accessed embeddings to improve performance
- [ ] T084 [P] Add request validation middleware in src/api/middleware/validation.py
- [ ] T085 [P] Add logging for debugging and monitoring purposes
- [ ] T086 [P] Add health check endpoint in src/api/routes/health.py
- [ ] T087 [P] Update documentation with API usage examples
- [ ] T088 [P] Add performance monitoring for query response times
- [ ] T089 [P] Implement rate limiting to prevent API abuse
- [ ] T090 [P] Add comprehensive contract tests for all API endpoints
- [ ] T091 [P] Perform final integration testing of all user stories together
- [ ] T092 [P] Update quickstart guide with complete usage instructions
- [ ] T093 [P] Add deployment configuration files (Dockerfile, docker-compose.yml)