# Audit overlays

Audits are observations bound to an exact target. They do not edit the target and do not automatically become repository truth.

Store audits as:

```text
operations/audits/<audit-id>/
├── TARGET.json
├── METHOD.md
├── observations.jsonl
├── evidence/
└── DISPOSITION.md
```

## `TARGET.json`

Record the exact repository commit, prompt hash, experiment/run identifiers, evaluator version, and any external artifact hashes.

## `observations.jsonl`

Append one JSON object per observation. Each should include:

- observation ID;
- target identity;
- claim or defect;
- evidence location;
- status (`SUPPORTED`, `CONTRADICTED`, `UNABLE_TO_VERIFY`, or `OUT_OF_SCOPE`);
- severity rationale where relevant;
- authoring seat and date.

## Authority

An audit may identify a defect or support a claim. It may not rewrite locked prompt bytes, experiment outputs, prior receipts, or promotion history. Repairs occur on new proposal branches. Human review determines disposition.
