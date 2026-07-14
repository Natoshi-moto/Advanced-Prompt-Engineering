# ROUTE-APE-0002 — Prepare EXP-0001 controlled runs

## Baseline

- Repository: `Natoshi-moto/Advanced-Prompt-Engineering`
- Base branch: `main`
- Base commit: `7da81fe1ce365703ab25ad044826944b45fbbb66`
- Required proposal branch pattern: `agent/ape-r002-exp0001-*`

## Objective

Produce an execution-ready, blinded comparison package for the first candidate prompt without performing or claiming the experiment unless the active proposal explicitly includes execution.

## Required reads

1. `README_START_HERE.md`
2. `AGENTS.md`
3. `STATUS.json`
4. `NEXT_ACTION.md`
5. `governance/CONSTITUTION.md`
6. `docs/METHOD.md`
7. `experiments/EXP-0001/README.md`
8. `prompts/adversarial-software-corpus-audit/v0.1.0/MANIFEST.json`
9. `prompts/adversarial-software-corpus-audit/v0.1.0/PROMPT.md`

## Required outputs

- exact `C0`, `C1`, and `C2` condition artifacts;
- at least one exact ablation artifact;
- independently established ground-truth fixture manifest;
- model/runtime and tool-access record schema;
- randomization and blinding procedure;
- evaluator rubric covering false positives and unsupported claims;
- raw-output storage layout;
- bounded preparation receipt.

## Constraints

- Do not edit `APE-PROMPT-0001` v0.1.0.
- Do not reconstruct absent outputs.
- Do not use the model responses being scored to establish ground truth.
- Do not treat same-model repetition as independent replication.
- Do not merge or promote without fresh human authorization.

## Stop conditions

Stop and record a blocker if ground truth cannot be established independently, fixtures cannot be published safely, condition parity cannot be maintained, or required model/runtime metadata is unavailable.
