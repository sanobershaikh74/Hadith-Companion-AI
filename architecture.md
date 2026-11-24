# System architecture

```mermaid
flowchart TD
    A[User topic or situation] --> B[CLI input]
    B --> C[Load curated JSON records]
    C --> D[Validate required metadata]
    D --> E[TF-IDF vectorization]
    B --> E
    E --> F[Cosine similarity ranking]
    F --> G[Top-k results]
    G --> H[Show text, reference and source]
```

The current implementation is a local retrieval baseline. It does not call an LLM, generate commentary, authenticate narrations, or infer religious rulings. A future architecture may add multilingual embeddings and human-reviewed explanations, but source-grounded retrieval should remain independently testable.
