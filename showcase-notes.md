# Showcase notes

## One-sentence pitch

Hadith Companion AI is a Python research prototype that explores context-aware discovery of Hadith records through transparent text retrieval and source-preserving metadata.

## Problem being explored

People may know the situation or theme they want to explore without knowing a collection, chapter, or reference number. Keyword search can be restrictive when the wording in a query differs from the wording in a record.

## Current technical contribution

The repository implements a lightweight lexical retrieval baseline using TF-IDF and cosine similarity. It validates the shape of user-supplied JSON records and returns ranked records with their source metadata.

## What it does not claim

- It is not a generative AI assistant or deployed application.
- It does not include a verified Hadith corpus.
- It does not authenticate narrations or independently validate grading.
- It does not provide tafsir, fatwas, or religious rulings.
- A relevance score is not a measure of authenticity or correctness.

## Suggested portfolio walkthrough

1. Start with the README and the retrieval-flow diagram.
2. Open `src/hadith_companion/retrieval.py` to explain the retrieval baseline.
3. Show the JSON schema to explain source traceability.
4. Open `tests/test_retrieval.py` to show how input validation and ranking are tested.
5. Finish with the governance policy and future research directions.

This walkthrough can be done by browsing the source files on GitHub. Running or deploying the project is not required for a repository showcase.
