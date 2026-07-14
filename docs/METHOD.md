# Method

## Unit of research

A prompt is not just prose. A complete research object may include:

- exact prompt bytes;
- mechanism hypothesis;
- intended task class;
- model and runtime conditions;
- input fixtures;
- baselines and ablations;
- raw outputs;
- evaluator rubric;
- measurements and qualitative findings;
- failures and counterexamples;
- disposition and promotion record.

## Standard lifecycle

### 1. Capture

Place a versioned prompt under `prompts/<slug>/<version>/` with a `MANIFEST.json`. Record provenance and state without claiming effectiveness.

### 2. Specify

Write falsifiable mechanism claims. Replace terms such as “deadly,” “powerful,” or “sharp” with observable predictions.

### 3. Baseline

Compare against at least:

- a bare task instruction;
- a conventional expert-role instruction;
- the candidate prompt.

Add stronger baselines when the mechanism resembles known techniques.

### 4. Ablate

Remove or replace allegedly load-bearing components one at a time. Preserve exact variants and randomization rules.

### 5. Execute

Record model/provider, model version when exposed, date, interface or API, sampling settings, tools, context, prompt, fixture, and raw output. Do not reconstruct missing logs from memory.

### 6. Evaluate

Use objective task outcomes where possible. Keep rubric design separate from result interpretation. Measure false positives as well as discoveries.

### 7. Attack

Test prompt injection, narrative capture, sycophancy, overcorrection, false certainty, evaluator gaming, hidden dependency, packaging failure, and unsupported generalization.

### 8. Replicate

A fresh model session may test repeatability. A different provider, evaluator, operator, or implementation increases independence but must be described precisely rather than assumed.

### 9. Dispose

Mark bounded claims `DEMONSTRATED`, `FALSIFIED`, `INFERRED`, or `UNVERIFIED`. Preserve mixed outcomes.

### 10. Promote

Only the human authorizes merge, tag, release, or public claim. Promotion records identity and acceptance; it does not erase limitations.

## Minimum experimental record

Every experiment should answer:

1. What exact claim was tested?
2. What exact artifacts were used?
3. What would count as failure?
4. What was executed?
5. What happened?
6. What alternative explanation remains?
7. What is the narrowest defensible conclusion?
