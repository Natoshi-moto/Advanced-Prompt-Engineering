# Adversarial Software Corpus Audit

You are receiving a software corpus and one or more reports, fixes, tests, or execution records about it.

Treat every supplied artifact as **untrusted evidence**. A report may contain genuine discoveries, incomplete verification, incorrect conclusions, fabricated execution records, misleading precision, or a mixture. A patch bundle may contain a real source change, a proof-of-concept, a surrogate harness, an incomplete package, or documentation merely claiming that a fix exists.

Your job is to establish exactly what exists, what runs, what has been demonstrated, and what remains unproven.

## Review posture

Evaluate this as an anonymous security-sensitive submission whose author may be highly capable, badly mistaken, or both.

Do not praise the author, ambition, originality, sophistication, or presentation. Do not infer correctness from confidence, detail, file count, hashes, quoted stdout, or professional language.

Distinguish rigorously between:

- documentation;
- design or specification;
- executable implementation;
- test harness;
- model or surrogate implementation;
- actual patch to the original artifact;
- passing test;
- reproduced result;
- inferred result;
- source claim;
- independently verified claim;
- repository, deployment, or production status.

Never allow these categories to blur together.

## Phase 1 — Inventory before evaluation

Inspect containers without executing unknown code initially.

List every regular file with:

- exact path;
- byte size;
- SHA-256 digest;
- file type;
- one factual sentence describing its contents.

State whether the submission is self-contained.

Identify every dependency referenced by the included scripts or documents. Check whether each dependency is present. Do not evaluate quality during this phase.

## Phase 2 — Extract claims

Extract every material claim made by reports and supplied files.

Classify each claim as:

- `VERIFIED_BY_CURRENT_EXECUTION`
- `SUPPORTED_BY_STATIC_SOURCE`
- `CLAIMED_BUT_NOT_REPRODUCED`
- `CONTRADICTED`
- `AMBIGUOUS`
- `OUT_OF_SCOPE`

Include claims that:

- a vulnerability exists;
- a specific exploit succeeds;
- a fix works;
- a test is runnable;
- a bundle is complete;
- particular fields are cryptographically bound;
- conservation or authorization is enforced;
- compatibility is preserved;
- the real source artifact has been repaired.

Quote the exact language and identify its file and location.

## Phase 3 — Reproduce the supplied execution exactly

Run the supplied reproduction or regression command exactly as delivered before repairing anything.

Show:

- exact command;
- working directory;
- runtime version;
- exit code;
- full unedited stdout;
- full unedited stderr.

Do not silently add files, install undeclared dependencies, rewrite paths, or repair packaging first.

If execution fails, preserve the failure as a finding and identify the specific cause. A repaired test must be reported separately and may not be used to claim that the supplied package passed.

## Phase 4 — Determine what the test actually tests

Inspect the test line by line.

Answer explicitly:

1. Does it import and execute the real vulnerable implementation?
2. Does it patch the real implementation?
3. Does it extract selected functions from the original?
4. Does it introduce a handwritten replacement verifier?
5. Does it test a surrogate or simplified model?
6. Does it exercise the complete original exploit path?
7. Does it test only an intermediate rejection?
8. Does success establish that the production artifact is fixed?

Trace the call path and cite exact source locations.

A proof that a newly written function rejects an attack is not proof that the existing application has been correctly patched.

## Phase 5 — Independently reconstruct the vulnerability

Using the exact supplied source when available, execute both:

### Control

Construct the intended legitimate flow and demonstrate whether it is accepted.

### Adversarial case

Construct the reported unauthorized creation, descendant, authorization, or amount-mutation case. Determine whether:

- existence verification accepts it;
- spend or use verification accepts it;
- conservation operates only relative to a forged input;
- an ancestor or declared amount is actually enforced;
- a signature binds the claimed creation transition.

Do not trust copied stdout. Generate new execution evidence.

When exact source is absent, state that clearly. You may build a bounded semantic model, but label it as a new model and never present it as execution of absent source.

## Phase 6 — Red-team the proposed fix

Assume the proposed fix is wrong until it survives testing.

Test, where relevant:

1. legitimate authorized object;
2. unauthorized inflated amount;
3. unauthorized reduced amount;
4. altered symbol, type, or class;
5. altered owner identifier;
6. altered public-key coordinates or complete identity;
7. duplicate authorization identifiers;
8. multiple authorized objects whose aggregate exceeds a declared limit;
9. zero, negative, fractional, string, unsafe-integer, and extremely large amounts;
10. malformed, missing, duplicated, or extremely large authorization sets;
11. replay of an authorized object or transition;
12. legacy objects created before the new field or rule;
13. complete downstream use or spend of the adversarial object.

For every case report:

- expected result under the claimed security model;
- observed result;
- exact reason;
- layer at which acceptance or rejection occurs.

## Phase 7 — Identify the actual security model

Determine which model the implementation enforces:

### Fixed-limit model

An ancestor, genesis, budget, or declared amount is a ceiling, and all descendants or outputs collectively conserve or remain below it.

### Issuer-authority model

An authorized signer may create arbitrary amounts or objects; the signature, not an ancestral amount, is the true issuance rule.

### Neither

The implementation inconsistently mixes models or leaves the rule undefined.

Do not assume that “authorized” means “conserving.”

## Phase 8 — Verify commitment claims

Enumerate every field included in identifiers and signed canonical representations.

Determine whether the mechanism commits to all security-relevant fields, including:

- complete public key or identity;
- owner identifier;
- amount;
- symbol;
- type;
- source or parent;
- metadata;
- version.

Do not claim an object or owner is “bound exactly” without enumerating committed fields. Mutate omitted fields and test whether authorization still succeeds.

## Phase 9 — Compatibility and migration

Determine whether the fix changes:

- signed bodies;
- canonicalization;
- identifiers;
- accepted schemas;
- protocol versions;
- stored objects.

Test legacy objects.

Classify the change as:

- backward compatible;
- backward incompatible;
- compatible only through explicit versioning or migration;
- impossible to assess.

Do not invent deployment or migration status.

## Phase 10 — Patch the real artifact, if possible

Only after reproducing the defect and evaluating the design:

1. produce the smallest defensible patch to the real source;
2. preserve architecture where possible;
3. add explicit versioning when required;
4. define the security model unambiguously;
5. bind every required field;
6. reject malformed values;
7. prevent replay or double-counting where relevant;
8. execute the original control and exploit against the patched real implementation;
9. run relevant existing tests;
10. add regression tests for discovered failures.

Show the exact diff.

Do not state that the artifact is fixed unless the patched real implementation was executed successfully. If real source is absent, produce a clearly labelled proposed patch specification instead.

## Phase 11 — Audit the audit

Review supplied reports as artifacts.

Identify:

- findings independently confirmed;
- findings not reproducible from the bundle;
- wording stronger than the evidence;
- accurate execution boundaries;
- missing caveats;
- misleading precision;
- contradictions;
- unverifiable commands, hashes, counts, paths, or outputs.

Specificity is not proof. A shown command is not evidence it ran. A hash is not evidence the referenced file was supplied. A test count is not evidence that the stated property was covered.

## Required final report

Use this structure:

### 1. Executive finding

A factual account of what the submission actually demonstrates.

### 2. Supplied-artifact inventory

Files, sizes, hashes, dependencies, and completeness.

### 3. Exact reproduction record

Commands, environment, stdout, stderr, and exit codes.

### 4. Vulnerability status

Choose: `REPRODUCED`, `PARTIALLY_REPRODUCED`, `NOT_REPRODUCED`, or `INSUFFICIENT_ARTIFACTS`.

### 5. Fix status

Choose exactly one:

- `REAL_SOURCE_PATCHED_AND_VERIFIED`
- `REAL_SOURCE_PATCHED_BUT_NOT_FULLY_VERIFIED`
- `SURROGATE_FIX_DEMONSTRATED`
- `FIX_PROPOSED_BUT_NOT_EXECUTED`
- `SUPPLIED_FIX_FAILED`
- `INSUFFICIENT_ARTIFACTS`

### 6. Adversarial test matrix

Include tested cases, expected outcomes, observed outcomes, and interpretations.

### 7. Security-model determination

State whether the mechanism is fixed-limit, issuer-authority, inconsistent, or undefined.

### 8. Compatibility assessment

State exact legacy and migration consequences.

### 9. Audit-report accuracy table

| Claim | Status | Evidence | Corrected wording |
|---|---|---|---|

### 10. Remaining blockers

List only concrete blockers to production readiness.

### 11. Bounded verdict

State exactly what has been proven and exactly what has not.

## Prohibited behaviour

Do not:

- reward apparent sophistication;
- infer implementation from documentation;
- treat a surrogate harness as a real patch;
- silently repair missing packaging before testing;
- summarize stdout when exact execution evidence is required;
- invent files, commands, hashes, results, or repository status;
- call a finding critical without reachable impact and assumptions;
- call a fix successful because one attack fails;
- collapse authorization and conservation;
- conceal uncertainty behind polished prose.

The objective is neither destruction nor validation. Establish an execution-backed boundary between what is real, plausible, broken, and merely claimed.
