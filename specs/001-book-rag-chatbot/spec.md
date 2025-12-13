# Feature Specification: Book RAG Chatbot

**Feature Branch**: `001-book-rag-chatbot`
**Created**: 2025-12-11
**Status**: Draft
**Input**: User description: "You are a book-content chatbot built on a Retrieval-Augmented Generation (RAG) system using the OpenAI Agent SDK. Your knowledge source consists only of the book content ingested from the sitemap.xml and embedded into Qdrant.

RULES:

1. Use only the ingested book content from the vector database. Never use outside knowledge unless explicitly asked.
2. For every user query, use the OpenAI Agent SDK's tool-calling flow:
   - First: interpret the query
   - Then: call the retrieval tool (Qdrant search)
   - Finally: generate the answer strictly from retrieved passages
3. Never produce an answer without retrieval unless the user asks for a meta/system explanation.
4. If user provides selected text, restrict retrieval only to those chunk IDs.
5. If no supporting passage exists in the selected text, answer exactly:
   'Answer not available in the selected text.'
6. If no passage is found in the database:
   'No supporting text found in the book.'
7. Never hallucinate, fabricate details, or use pretraining memory.
8. All answers must be concise, factual, and directly tied to retrieved passages.
9. When quoting, quote only from retrieved passages and keep excerpts ≤200 characters.
10. Always output in the defined JSON schema, followed by a short human-readable answer."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Query Book Content (Priority: P1)

As a user, I want to ask questions about the book content so that I can get accurate answers based only on the book's information.

**Why this priority**: This is the core functionality of the chatbot - allowing users to interact with the book content through natural language queries.

**Independent Test**: The system can respond to user queries with answers derived solely from the book content, following the required rules for accuracy and citation.

**Acceptance Scenarios**:

1. **Given** a user has access to the book RAG chatbot, **When** the user asks a question about book content, **Then** the system retrieves relevant passages from the vector database and generates an answer based only on those passages
2. **Given** a user asks a question not covered by the book content, **When** no relevant passages are found, **Then** the system responds with "No supporting text found in the book."

---

### User Story 2 - Get Selected Text Answers (Priority: P2)

As a user, I want to ask questions about specific selected text so that I can get answers restricted to that content.

**Why this priority**: This provides a more focused interaction mode for users who want answers only from specific parts of the book.

**Independent Test**: When a user provides selected text or chunk IDs, the system restricts its retrieval to only those specific content areas.

**Acceptance Scenarios**:

1. **Given** a user provides selected text or specific chunk IDs, **When** the user asks a question, **Then** the system retrieves answers only from the specified text segments
2. **Given** a user provides selected text, **When** no supporting passage exists in the selected text, **Then** the system responds with "Answer not available in the selected text."

---

### User Story 3 - Receive Structured Responses (Priority: P3)

As a user, I want to receive responses in a structured format with citations so that I can verify the source of information.

**Why this priority**: This enhances trust and usability by providing transparency about where the information comes from.

**Independent Test**: The system outputs responses in the required JSON schema with evidence citations and confidence levels.

**Acceptance Scenarios**:

1. **Given** the system generates an answer, **When** returning the response, **Then** it provides both JSON format with evidence citations and a human-readable answer
2. **Given** the system generates an answer, **When** citing sources, **Then** it includes document IDs, chunk identifiers, and relevant excerpts ≤200 characters

---

### Edge Cases

- What happens when the user asks for external information or general knowledge?
- How does system handle queries that are too vague to match specific book content?
- What happens when the query requires information from multiple book sections that may conflict?
- How does the system handle queries when the vector database is temporarily unavailable?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST use only ingested book content from the vector database as the knowledge source
- **FR-002**: System MUST never use outside knowledge unless explicitly asked by the user
- **FR-003**: System MUST follow the OpenAI Agent SDK's tool-calling flow: interpret query → call retrieval tool → generate answer
- **FR-004**: System MUST call the Qdrant search tool to retrieve relevant passages for each user query
- **FR-005**: System MUST generate answers strictly from retrieved passages, never from pretraining memory
- **FR-006**: System MUST respond with "Answer not available in the selected text." when no supporting passage exists in user-provided selected text
- **FR-007**: System MUST respond with "No supporting text found in the book." when no relevant passage is found in the database
- **FR-008**: System MUST never hallucinate, fabricate details, or use pretraining memory
- **FR-009**: System MUST provide concise, factual answers directly tied to retrieved passages
- **FR-010**: System MUST output responses in the defined JSON schema format followed by a human-readable answer
- **FR-011**: System MUST restrict retrieval to specific chunk IDs when user provides selected text
- **FR-012**: System MUST include citations with document ID, chunk identifier, and verbatim quotes (≤200 characters) in responses
- **FR-013**: System MUST provide confidence level (High|Medium|Low) for each response
- **FR-014**: System MUST allow users to request summaries based only on retrieved passages

### Key Entities

- **Book Content**: The source material ingested from the book's published website via sitemap.xml, embedded into Qdrant vector database
- **User Query**: Natural language questions from users seeking information from the book content
- **Retrieved Passages**: Relevant text segments from the book content retrieved from the vector database based on semantic similarity
- **Response**: Structured output containing both JSON schema and human-readable answer with citations
- **Chunk ID**: Unique identifiers for specific segments of book content in the vector database

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users receive accurate answers to book-related questions with 95% factual correctness based on retrieved passages
- **SC-002**: System responds to user queries within 5 seconds for 90% of requests
- **SC-003**: 90% of user queries that have relevant book content receive properly sourced answers with citations
- **SC-004**: 100% of queries without relevant book content receive the exact response "No supporting text found in the book."
- **SC-005**: 100% of queries with selected text restrictions that have no supporting content receive the exact response "Answer not available in the selected text."
- **SC-006**: 0% of responses contain hallucinated information or external knowledge not present in the book content
- **SC-007**: 95% of responses include proper citations with document ID, chunk identifier, and relevant excerpts
- **SC-008**: Users report 80% satisfaction with the accuracy and relevance of responses compared to direct book consultation
