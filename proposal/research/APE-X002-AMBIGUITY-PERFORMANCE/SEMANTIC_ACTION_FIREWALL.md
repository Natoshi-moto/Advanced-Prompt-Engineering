# Semantic Action Firewall (SAF) — minimal reference model

**State:** `CANDIDATE`  
**Relationship to HAPCL:** HAPCL-like structured commands may be one compiler
surface. They are not, alone, the firewall.

## Security claim

SAF aims to prevent a model-generated interpretation from silently inheriting
authority to produce a consequential external effect.

It does not claim to solve alignment, malicious authorized users, compromised
tools, incorrect policies, all social engineering, or all ambiguity.

## Pipeline

```text
UNTRUSTED UTTERANCE
  -> OBSERVATION RECORD
  -> INTERPRETATION SET
  -> RESOLVED ACTION DRAFT
  -> POLICY AND AUTHORITY GATE
  -> USER-BOUND ACTION CONTRACT
  -> EXECUTION ADAPTER
  -> EFFECT RECEIPT
```

### 1. Observation record

Preserve exact bytes, speaker/channel identity, timestamp, conversation
reference, visible tool state, and a hash. Do not summarize away the source.

### 2. Interpretation set

Represent plausible speech acts and unresolved variables. Include a null
interpretation (`INFORMATION_ONLY` or `NO_ACTION`) and record why alternatives
were included or excluded.

### 3. Resolved action draft

Resolve opaque nouns to stable identifiers. A draft must name:

- operation and tool;
- target and recipient identifiers;
- fields or resources affected;
- quantity, cost, and time bounds;
- reversibility and rollback path;
- preconditions and expected postconditions;
- policy basis and requested authority;
- remaining unknowns and defaults.

### 4. Policy and authority gate

Evaluate capability, user authority, system policy, risk, novelty, and whether
confirmation is permitted to authorize the act at all. Clarification is not a
bypass around policy.

### 5. User-bound action contract

Show the resolved human-readable effect and bind confirmation to a digest of
the machine action. Generic replies such as "yes," old confirmations, or a
confirmation obtained before target resolution do not authorize changed
arguments.

### 6. Execution adapter

The tool receives the authorized contract, not the free-form conversation.
Reject argument drift, stale state, changed recipients, expanded scope, or
expired authorization.

### 7. Effect receipt

Record attempted action, tool response, observed external state, divergence
from expected postconditions, reversibility window, and unresolved uncertainty.
`TOOL_OK` is not equivalent to `INTENDED_EFFECT_CONFIRMED`.

## Why structured language is insufficient

`USER >> SEND >> EMAIL >> JOHN` still leaves ambiguity in `USER`, `EMAIL`,
`JOHN`, the meaning of `SEND`, permissions, version, attachments, timing,
audience, and success. Structure relocates ambiguity; it does not necessarily
remove it.

## First test matrix

| Axis | Paired case |
|---|---|
| speech act | question vs instruction |
| lexical | kill process vs harm person |
| entity | John Smith A vs John Smith B |
| scope | delete matching files vs delete container |
| quantity | close position vs reduce position |
| quotation | quoted instruction vs active instruction |
| context | prior technical frame vs sudden domain pivot |
| temporality | current state vs stale confirmation |
| authority | owner request vs relayed or coerced request |
| outcome | tool accepted vs intended postcondition obtained |

Compare SAF against: direct execution, simple confirmation, risk-only gating,
permission-only gating, and structured-command-only gating. Measure false
actions, missed safe actions, clarification burden, target drift, authorization
replay, and false confidence.

