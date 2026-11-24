# Evaluation plan

Use a manually reviewed query set with relevance judgments created by qualified reviewers. Do not evaluate religious correctness using similarity scores alone.

Suggested retrieval metrics:

- **Precision@K:** proportion of the top K results judged relevant.
- **Recall@K:** proportion of all judged-relevant records retrieved in the top K.
- **MRR:** reciprocal rank of the first relevant result.
- **nDCG@K:** ranking quality when relevance has graded labels.

Also audit reference completeness, source-link validity, translation attribution, duplicate records, and unsupported claims. Keep the evaluation corpus separate from training or tuning data where applicable.
