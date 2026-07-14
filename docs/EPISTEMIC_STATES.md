# Epistemic states

These labels describe repository disposition. They are not decorative confidence words.

| State | Meaning |
|---|---|
| `LATERAL` | Relevant material retained beside the active line of work without endorsement or dependency. |
| `CANDIDATE` | Proposed artifact or claim awaiting adequate evaluation. |
| `LOCKED` | Exact bytes are frozen and hashable. This says nothing about effectiveness. |
| `IMPLEMENTED` | The specified artifact exists in executable or directly usable form. |
| `DEMONSTRATED` | A bounded claim met declared criteria in a recorded execution. |
| `FALSIFIED` | A stated claim failed a valid counterexample or declared criterion. |
| `SUPERSEDED` | A newer artifact replaces this one for a declared purpose; history remains preserved. |
| `INFERRED` | Conclusion reasoned from evidence but not directly executed or observed. |
| `UNVERIFIED` | Evidence is absent, inaccessible, stale, or insufficient. |

## Non-implications

- `LOCKED` does not imply `DEMONSTRATED`.
- `IMPLEMENTED` does not imply correct, safe, novel, or useful.
- `DEMONSTRATED` does not imply generality or independent replication.
- `SUPERSEDED` does not mean deleted or false.
- `INFERRED` must never be rendered as observed fact.

## Claim progression

A typical path is:

```text
LATERAL -> CANDIDATE -> LOCKED -> IMPLEMENTED -> DEMONSTRATED
                                      |                |
                                      v                v
                                  FALSIFIED        SUPERSEDED
```

Progression is not automatic. Each transition requires a receipt naming the evidence and authority.
