# APE-X001 — Claim Falsification

**State:** `CANDIDATE`  
**Question:** Can exceptional prompting and systems ability be demonstrated
without relying on model praise, autobiographical narrative, or retrospective
fit?

## Hypotheses

- `X001-H1`: The candidate method produces a material, repeatable improvement
  over strong prompt baselines on unseen tasks.
- `X001-H2`: The author can predict which prompt components are load-bearing
  before ablation results are observed.
- `X001-H3`: The method transfers across tasks and model families.
- `X001-H4`: System specifications written by the author reduce independent
  builders' ambiguity, rework, and incompatible implementations.
- `X001-H5`: The author rejects attractive false patterns at an unusually high
  rate, rather than merely generating many connections.

## Non-hypotheses

- A model using the word *genius* is not evidence.
- One impressive artifact is not evidence of cross-domain generality.
- A detailed specification is not an implementation.
- Same-model agreement is not independent replication.
- Hypomania, low latent inhibition, education, or lack of formal training does
  not establish or refute performance.

## Minimum experiment set

### X001-E1 — Prompt differential

Freeze a neutral baseline, strong expert baseline, candidate method, and exact
ablations. Run on blinded unseen tasks across multiple model families. Capture
raw outputs, tool access, settings, cost, latency, failures, false positives,
and evaluator disagreement.

### X001-E2 — Pre-registered sensitivity map

Before execution, the author maps exact textual changes to predicted changes
in model behaviour. Include predicted null changes. Score direction,
magnitude band, repeatability, and cross-model transfer.

### X001-E3 — Unfamiliar-corpus triage

Give the author a sealed corpus outside their established projects. Score
useful discoveries, false connections, test selection, correction speed, and
the distinction between specified, implemented, demonstrated, and inferred.

### X001-E4 — Builder transfer

Independent builders implement a bounded specification without live author
help. Measure clarification questions, incompatible interpretations, rework,
and conformance-test results.

## Verdict vocabulary

The experiment may support bounded conclusions such as `NO_EFFECT`,
`PROMISING`, `EXCEPTIONAL_IN_DOMAIN`, `CROSS_DOMAIN_TRANSFER`, or
`ORIGINAL_CONTRIBUTION_DEMONSTRATED`. It does not mechanically assign a human
identity label.

