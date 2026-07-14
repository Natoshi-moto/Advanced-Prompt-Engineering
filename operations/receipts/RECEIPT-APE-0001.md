# RECEIPT-APE-0001 — Foundation implementation

## Identity

- Task: `TASK-APE-0001`
- Route: `operations/routes/ROUTE-APE-0001.md`
- Base repository: `Natoshi-moto/Advanced-Prompt-Engineering`
- Base commit: `484bf9e1291cd466d7a17d99541d20ce4294f9b0`
- Proposal branch: `agent/ape-r001-agent-friendly-foundation`
- Pre-receipt branch head: `73a1e449c5f85c49fb174a9e846efff89d7d320c`
- Promotion authority: `HUMAN_ONLY`

## Reference files actually inspected

From `Natoshi-moto/Lab` at its live `main` during this task:

- `README.md`
- `README_START_HERE.md`
- `AGENTS.md`
- `STATUS.json`

From the target repository:

- initial commit `484bf9e1291cd466d7a17d99541d20ce4294f9b0`
- `LICENSE`

The private Nexus corpus, snapshots, task evidence, and project-specific implementation were not copied.

## Implemented files

- repository orientation: `README.md`, `README_START_HERE.md`
- agent routes: `AGENTS.md`, `CLAUDE.md`
- state routing: `STATUS.json`, `STATUS.md`, `NEXT_ACTION.md`
- governance: `governance/CONSTITUTION.md`
- method: `docs/METHOD.md`, `docs/EPISTEMIC_STATES.md`
- prompt object: `prompts/adversarial-software-corpus-audit/v0.1.0/`
- experiment design: `experiments/EXP-0001/README.md`
- operations: task, route, receipt, and audit-overlay instructions
- verification: `scripts/verify_repo.py`, `.github/workflows/validate.yml`
- collaboration: `.github/pull_request_template.md`
- local exclusions: `.gitignore`

## Candidate prompt identity

- Prompt ID: `APE-PROMPT-0001`
- Version: `v0.1.0`
- State: `CANDIDATE`
- Declared SHA-256: `3dc753ff934b39e3c6ad833b6a83281de1a365697caac0d9e0a58d542727077f`

The hash was calculated over the candidate text before repository insertion. Repository-side verification is delegated to `scripts/verify_repo.py` and GitHub Actions.

## Execution record

Attempted local command:

```bash
rm -rf /tmp/ape && \
git clone --branch agent/ape-r001-agent-friendly-foundation --single-branch \
  https://github.com/Natoshi-moto/Advanced-Prompt-Engineering.git /tmp/ape && \
cd /tmp/ape && git rev-parse HEAD && python3 scripts/verify_repo.py
```

Observed result:

```text
Cloning into '/tmp/ape'...
fatal: unable to access 'https://github.com/Natoshi-moto/Advanced-Prompt-Engineering.git/': Could not resolve host: github.com
```

Exit code: `128`

This is an execution-environment network boundary, not a repository verifier result. No local pass is claimed.

## Current disposition

- Foundation structure: `IMPLEMENTED` on proposal branch.
- Structural verifier result: `UNVERIFIED` pending GitHub Actions execution on the draft pull-request head.
- Candidate prompt effectiveness: `UNVERIFIED`.
- Novelty and superiority: `UNVERIFIED`.
- Canonical promotion: not authorized.

## Next action

Open a draft pull request, inspect the exact-head workflow result, and leave canonical disposition to the human.
