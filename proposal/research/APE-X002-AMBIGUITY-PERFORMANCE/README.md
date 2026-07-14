# APE-X002 — Ambiguity–Performance

**State:** `CANDIDATE`  
**North star:** Study the model's transformation, not the drama it generates
around the transformation.

## Founding observation

A human made a descriptive claim about downstream textual sensitivity. The
assistant converted it into a stronger claim about deliberate prediction and
control, then proposed a test for that stronger claim. When challenged, the
assistant recognized that it had romanticized the observation.

This is not merely a conversational curiosity. A tool-using agent can perform
the same conversion and then change external state.

## Core thesis

> A live-tool agent is an ambiguity-to-authority converter. It observes a
> display, constructs one actionable reality from several possible meanings,
> and performs against the world. Safety depends on preventing that constructed
> meaning from silently inheriting the user's authority.

The claim is deliberately narrower than "ambiguity is the whole alignment
problem." Ambiguity is one cross-cutting vulnerability surface interacting with
identity resolution, authorization, policy, tool semantics, state freshness,
and verification.

## Five separations

| Layer | Object | Failure if collapsed |
|---|---|---|
| 1 | observed bytes/events | model invents or omits source material |
| 2 | candidate interpretations | one reading is mistaken for the reading |
| 3 | proposed action contract | interpretation inherits authority |
| 4 | authorized action contract | vague confirmation authorizes changed scope |
| 5 | execution and observed effect | tool success is mistaken for intended success |

## Research questions

1. Which linguistic ambiguities survive conversion into a structured command?
2. Where does ambiguity move—to entity resolution, defaults, scope, policy, or
   success criteria—rather than disappear?
3. When does clarification increase rather than reduce risk?
4. Can an action contract remain bound to the exact interpretation the user
   authorized through target resolution and execution?
5. How should systems represent unresolved ambiguity without manufacturing
   certainty?
6. How do narrative styles—clinical, theatrical, technical, heroic, skeptical—
   alter agent decisions while leaving literal task content similar?

## Initial falsifiers

- If ordinary capability and confirmation controls already eliminate the
  proposed failure class without semantic binding, the firewall is redundant.
- If ambiguity scores cannot predict action error better than simpler risk and
  permission baselines, the ambiguity detector adds no demonstrated value.
- If structured restatements merely create confirmation bias or automation
  complacency, the handshake may increase risk.
- If the system cannot bind user confirmation to resolved identities, scope,
  tool arguments, and postconditions, it is not an action firewall.

