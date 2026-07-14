# Next action

## `ACT-APE-0002_PREPARE_EXP0001_CONTROLLED_RUNS`

Prepare the first executable run package for `experiments/EXP-0001` without yet claiming that the candidate prompt is superior.

The proposal should:

1. freeze exact `C0`, `C1`, and `C2` prompt variants;
2. define at least one section-level ablation;
3. select or construct a compact software corpus with independently established ground truth;
4. include one real defect, one misleading claim, one incomplete bundle, one safe suspected issue, and one second-order fix defect;
5. specify randomization, blinding, model/runtime metadata, tool access, stop conditions, and evaluator criteria;
6. record raw outputs and execution receipts without reconstruction;
7. measure false positives as well as successful discoveries;
8. keep prompt effectiveness, novelty, and generality `UNVERIFIED` until results justify narrower states.

Work must begin on a new proposal branch from canonical commit `7da81fe1ce365703ab25ad044826944b45fbbb66`. No agent may merge or promote the resulting experiment without fresh human authorization.
