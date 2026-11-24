"""TF-IDF retrieval over a user-supplied, curated Hadith dataset.

This module ranks records for topical relevance. It does not verify authenticity
or generate religious explanations.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

REQUIRED_FIELDS = {"id", "collection", "reference", "language", "text", "topics", "source_url"}


class DatasetError(ValueError):
    """Raised when the supplied dataset is malformed or incomplete."""


def load_records(path: str | Path) -> list[dict[str, Any]]:
    """Load and validate records from a JSON file."""
    file_path = Path(path)
    try:
        records = json.loads(file_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise DatasetError(f"Dataset not found: {file_path}") from exc
    except json.JSONDecodeError as exc:
        raise DatasetError(f"Dataset is not valid JSON: {exc}") from exc

    if not isinstance(records, list):
        raise DatasetError("Dataset root must be a JSON array.")

    seen_ids: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise DatasetError(f"Record at index {index} must be an object.")
        missing = REQUIRED_FIELDS - record.keys()
        if missing:
            raise DatasetError(f"Record at index {index} is missing: {', '.join(sorted(missing))}")
        if not all(isinstance(record[field], str) and record[field].strip() for field in
                   ("id", "collection", "reference", "language", "text", "source_url")):
            raise DatasetError(f"Record at index {index} has an empty or invalid required text field.")
        if not isinstance(record["topics"], list) or not all(isinstance(t, str) for t in record["topics"]):
            raise DatasetError(f"Record at index {index}: topics must be a list of strings.")
        if record["id"] in seen_ids:
            raise DatasetError(f"Duplicate record id: {record['id']}")
        seen_ids.add(record["id"])

    return records


def search_records(records: list[dict[str, Any]], query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """Return records ranked by TF-IDF cosine similarity."""
    if not query or not query.strip():
        raise ValueError("Query must not be empty.")
    if top_k < 1:
        raise ValueError("top_k must be at least 1.")
    if not records:
        return []

    documents = [record["text"] + " " + " ".join(record["topics"]) for record in records]
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(documents + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).ravel()
    ranked_indices = sorted(range(len(records)), key=lambda i: float(scores[i]), reverse=True)

    results = []
    for index in ranked_indices[:top_k]:
        result = dict(records[index])
        result["relevance_score"] = round(float(scores[index]), 4)
        results.append(result)
    return results
