# Dataset instructions

`hadith.example.json` is intentionally an empty JSON array. This repository does not ship real Hadith text or translations, and it must not invent narrations to make the demo appear populated.

Create your own `hadith.json` after checking source reliability, reuse permissions, translation rights, and scholarly review. Keep one JSON object per record.

Required fields:

| Field | Meaning |
|---|---|
| `id` | Unique stable identifier |
| `collection` | Hadith collection name |
| `reference` | Exact book/chapter/number reference |
| `language` | Language code or label |
| `text` | Verified text or translation |
| `topics` | List of topical keywords |
| `source_url` | Direct source link |

Optional fields: `grade`, `translation_credit`, `edition`, `reviewed_by`, `review_date`.

See `hadith-schema.json` for the JSON Schema. Do not treat the schema as evidence of authenticity.
