"""Command-line interface for the retrieval prototype."""

from __future__ import annotations

import argparse

from hadith_companion.retrieval import DatasetError, load_records, search_records


def main() -> int:
    parser = argparse.ArgumentParser(description="Search a curated Hadith metadata dataset.")
    parser.add_argument("--data", required=True, help="Path to a JSON dataset")
    parser.add_argument("--query", required=True, help="Topic or situation to search for")
    parser.add_argument("--top-k", type=int, default=5, help="Maximum number of results (default: 5)")
    args = parser.parse_args()

    try:
        records = load_records(args.data)
        results = search_records(records, args.query, args.top_k)
    except (DatasetError, ValueError) as exc:
        parser.error(str(exc))

    if not results:
        print("No records found. Add verified records to your JSON dataset first.")
        return 0

    for rank, record in enumerate(results, start=1):
        print(f"\n{rank}. {record['collection']} — {record['reference']}")
        print(f"   Relevance score: {record['relevance_score']}")
        print(f"   Language: {record['language']} | Topics: {', '.join(record['topics'])}")
        print(f"   Text: {record['text']}")
        print(f"   Source: {record['source_url']}")
        if record.get("grade"):
            print(f"   Grade (dataset-provided; not independently verified): {record['grade']}")
        if record.get("translation_credit"):
            print(f"   Translation credit: {record['translation_credit']}")
    print("\nReminder: relevance ranking does not verify authenticity or provide a religious ruling.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
