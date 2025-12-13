# Research: Book RAG Chatbot

## Research Summary

This research document addresses the technical decisions and investigations required for implementing the Book RAG Chatbot system using OpenAI Agent SDK and Qdrant vector database.

## Decision: OpenAI Agent SDK Integration
**Rationale**: The feature specification explicitly requires using the OpenAI Agent SDK for the RAG system. This provides a structured way to orchestrate the query interpretation, retrieval, and answer generation workflow as specified in the rules.

**Alternatives considered**:
- Direct OpenAI API calls: Less structured, more manual orchestration required
- LangChain: More complex for this specific use case, potential over-engineering
- Custom agent framework: Higher development time, maintenance burden

## Decision: Qdrant Vector Database
**Rationale**: The feature specification explicitly requires using Qdrant for storing the book content embeddings. Qdrant is a high-performance vector database optimized for semantic search, which is ideal for RAG applications.

**Alternatives considered**:
- Pinecone: Cloud-only, potential cost concerns for development
- Weaviate: Good alternative but specification specifically mentions Qdrant
- FAISS: Lower-level, requires more implementation work for production use

## Decision: FastAPI for Web Framework
**Rationale**: FastAPI provides excellent performance, automatic API documentation (OpenAPI/Swagger), built-in validation with Pydantic, and async support which is important for I/O-bound operations like vector database queries.

**Alternatives considered**:
- Flask: Simpler but lacks automatic validation and documentation
- Django: Too heavy for this API-focused use case
- Starlette: Lower-level than needed, FastAPI provides better developer experience

## Decision: Content Ingestion from Sitemap.xml
**Rationale**: The feature specification explicitly mentions that book content is ingested from sitemap.xml. This provides a structured way to discover and parse all pages of a book's published website.

**Technical approach**:
- Use requests/beautifulsoup4 to fetch and parse sitemap
- Extract content from each URL in the sitemap
- Process content into chunks suitable for embedding
- Generate embeddings using OpenAI's text-embedding-ada-002 model
- Store embeddings in Qdrant with metadata for retrieval

## Decision: Response Format and Schema
**Rationale**: The feature specification requires a specific JSON response schema with evidence citations, confidence levels, and follow-up questions. This provides transparency about the source of information and allows for verification.

**Schema**:
```json
{
  "answer": "<answer text>",
  "evidence": [
    {
      "doc_id": "<document ID>",
      "chunk_id": "<chunk identifier>",
      "quote": "<verbatim quote or excerpt ≤200 chars>"
    }
  ],
  "confidence": "<High|Medium|Low>",
  "follow_up": {
    "ask": <true|false>,
    "question": "<follow-up question if applicable>"
  }
}
```

## Decision: Handling Edge Cases
**Rationale**: The system must handle several specific edge cases as defined in the feature specification:

1. When no relevant passages are found: Return "No supporting text found in the book."
2. When selected text doesn't contain the answer: Return "Answer not available in the selected text."
3. When user requests external knowledge: The system should not provide it unless explicitly asked.

## Decision: Query Processing Workflow
**Rationale**: Following the exact operational order specified in the execution planner rules:
1. Interpret user query
2. Decide retrieval strategy (considering if selected text is provided)
3. Query Qdrant vector database
4. Pass retrieved passages to OpenAI Agent SDK for answer generation

## Decision: Security and Validation
**Rationale**: The system must prevent hallucination and ensure all responses are based on retrieved passages. This requires strict validation mechanisms:

- Validate that all content in responses originates from retrieved passages
- Implement checks to prevent using pretraining memory
- Ensure citations are accurate and verifiable
- Prevent disclosure of internal system details

## Implementation Considerations

### Performance
- Use async operations for I/O-bound tasks (database queries, API calls)
- Implement caching for frequently accessed content
- Optimize embedding retrieval with appropriate similarity thresholds

### Scalability
- Design for horizontal scaling of API services
- Consider partitioning of vector database for large book collections
- Implement proper connection pooling for database access

### Error Handling
- Graceful degradation when Qdrant is unavailable
- Proper error responses when content cannot be retrieved
- Fallback mechanisms for different failure scenarios