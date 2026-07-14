# EXP-0001 — Adversarial audit framing evaluation

## Status

`CANDIDATE`

No run is recorded by this file. It defines the experiment only.

## Research question

Does `APE-PROMPT-0001` improve execution-backed software auditing compared with simpler instructions, without merely increasing verbosity, suspicion, or false positives?

## Conditions

Use the same corpus, tool access, time budget, and output requirements across randomized fresh sessions.

### C0 — Bare task

Ask the model to inspect the corpus, reproduce the reported issue, and assess the fix.

### C1 — Conventional expert frame

Add a standard senior security-engineer role and instruction to be critical and evidence-based.

### C2 — Candidate prompt

Use `prompts/adversarial-software-corpus-audit/v0.1.0/PROMPT.md` unchanged.

### C3+ — Ablations

Remove one mechanism-bearing section at a time, including:

- anonymous-review frame;
- untrusted-evidence declaration;
- exact category separation;
- execute-as-delivered requirement;
- surrogate-versus-real-patch questions;
- adversarial test matrix;
- security-model determination;
- audit-the-audit phase;
- prohibited-behaviour section.

Do not claim every token is load-bearing from section-level ablation. Token-level claims require a separate design.

## Primary outcomes

- true defects reproduced;
- true defects missed;
- false defects asserted;
- supplied execution reproduced exactly;
- missing dependencies detected before repair;
- surrogate tests incorrectly described as real patches;
- unsupported security claims;
- complete attack paths tested;
- exact commands and outputs preserved;
- boundedness of final conclusions.

## Secondary outcomes

- tokens and wall-clock cost;
- unnecessary work;
- refusal or tool-use failure;
- evaluator disagreement;
- clarity and usability of the report.

## Blinding

The evaluator should not know which condition produced an output. Remove condition-identifying preambles where possible without changing substantive evidence.

## Ground truth

Seed or select corpora with known properties, including:

- one obvious defect;
- one subtle invariant violation;
- one misleading comment or report;
- one incomplete test bundle;
- one suspected issue that is actually safe;
- one plausible fix with a second-order defect.

Ground truth must be established independently of the model responses being scored.

## Success criterion

The candidate must improve correct, independently checkable findings over C0 and C1 without a disproportionate increase in false positives or unsupported claims.

A single impressive run is exploratory evidence, not a demonstration of general superiority.

## Required run record

Each run should preserve:

- condition identifier stored separately from blinded output;
- exact prompt hash;
- corpus hashes;
- model/provider/interface and date;
- tool availability;
- parameters when exposed;
- raw response;
- files created;
- commands, stdout, stderr, and exit codes;
- evaluator scores and rationale;
- anomalies and missing metadata.
