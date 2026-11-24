import json
import tempfile
import unittest
from pathlib import Path

from hadith_companion.retrieval import DatasetError, load_records, search_records


# Fictional test-only text. These are not Hadith and must never be used as religious content.
FIXTURES = [
    {
        "id": "TEST-1", "collection": "Fictional test collection", "reference": "Test 1",
        "language": "en", "text": "FICTIONAL TEST TEXT about patience and perseverance.",
        "topics": ["patience", "perseverance"], "source_url": "https://example.invalid/test-1"
    },
    {
        "id": "TEST-2", "collection": "Fictional test collection", "reference": "Test 2",
        "language": "en", "text": "FICTIONAL TEST TEXT about generosity and helping others.",
        "topics": ["generosity", "helping"], "source_url": "https://example.invalid/test-2"
    }
]


class RetrievalTests(unittest.TestCase):
    def test_search_ranks_relevant_record_first(self):
        results = search_records(FIXTURES, "patience during a difficult time", top_k=2)
        self.assertEqual(results[0]["id"], "TEST-1")
        self.assertIn("relevance_score", results[0])

    def test_empty_dataset_returns_empty_list(self):
        self.assertEqual(search_records([], "patience"), [])

    def test_empty_query_is_rejected(self):
        with self.assertRaises(ValueError):
            search_records(FIXTURES, "   ")

    def test_invalid_dataset_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps([{"id": "missing-fields"}]), encoding="utf-8")
            with self.assertRaises(DatasetError):
                load_records(path)

    def test_duplicate_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(json.dumps([FIXTURES[0], FIXTURES[0]]), encoding="utf-8")
            with self.assertRaises(DatasetError):
                load_records(path)


if __name__ == "__main__":
    unittest.main()
