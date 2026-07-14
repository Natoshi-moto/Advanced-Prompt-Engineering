# Advanced Prompt Engineering

**An execution-backed laboratory for designing, testing, falsifying, and publishing advanced prompting methods.**

➡️ Start with [`README_START_HERE.md`](README_START_HERE.md).

## Repository contract

```text
one repository = one authoritative prompt-research corpus
branches       = proposal and experiment spaces
main           = accepted working state
tags           = exact prompt and benchmark anchors
raw inputs     = inert, untrusted evidence
receipts       = reconstructable records of work performed
audits         = append-only observations bound to exact targets
AI agents      = replaceable, attributed research seats
human          = sole canonical promotion authority
```

This repository separates prompt text, hypotheses, experiments, evidence, evaluation, disposition, and promotion. A persuasive report does not promote itself. A passing demonstration does not automatically establish generality, novelty, safety, or production readiness.

## First research object

`prompts/adversarial-software-corpus-audit/v0.1.0/` contains the initial candidate prompt and its manifest. `experiments/EXP-0001/` defines the first controlled evaluation programme around it.

## Core commands

```bash
python3 scripts/verify_repo.py
```

The verifier checks the agent entry files, status object, task routing, prompt manifests, and prompt-content hashes without third-party dependencies.
