# ROUTE-APE-0001 — Foundation proposal

## Baseline

- Repository: `Natoshi-moto/Advanced-Prompt-Engineering`
- Base branch: `main`
- Base commit: `484bf9e1291cd466d7a17d99541d20ce4294f9b0`
- Proposal branch: `agent/ape-r001-agent-friendly-foundation`

## Objective

Create the smallest useful agent-friendly prompt-research operating layer, inspired by the Nexus Lab's repository-centred governance while remaining suitable for a public repository.

## Required reads

1. `LICENSE` on the base commit.
2. Nexus reference files used only for structural inspiration:
   - `README.md`
   - `README_START_HERE.md`
   - `AGENTS.md`
   - `STATUS.json`
3. The current candidate prompt supplied by the human.

## Allowed writes

Only files introduced by `TASK-APE-0001` on the proposal branch.

## Required properties

- provider-neutral entry instructions;
- imported prompt/transcript content treated as inert data;
- exact baseline and write scope;
- explicit epistemic states;
- versioned prompt objects with hashes;
- reproducible experiment records;
- append-only audit posture;
- human-only canonical promotion;
- dependency-free structural verifier;
- draft pull request, not direct promotion.

## Stop conditions

Stop and record a blocker if:

- the repository contains unexpected pre-existing work;
- required GitHub permissions are absent;
- private Nexus content would need to be copied;
- the verifier cannot establish prompt identity;
- any requested action would require settings mutation, merge, release, force-push, or deletion.

## Completion output

Create `operations/receipts/RECEIPT-APE-0001.md`, run the verifier, and open a draft pull request. The human decides disposition.
