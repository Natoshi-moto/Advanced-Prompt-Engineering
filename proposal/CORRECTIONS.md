# Correction ledger

This ledger is append-only. It records cases where an agent attributed,
implied, strengthened, narrowed, or reframed a user's claim beyond the source
language.

## CORR-APE-0001 — Observation strengthened into predictive control

**Source statement — user**

> Every single letter I type holds consequence downstream in magnitudes and I
> know that.

**Assistant transformation**

> The decisive result would be not merely that wording changes output—it
> obviously does—but that you can predict which small changes produce which
> systematic downstream effects before seeing them.

**Finding**

The user made an observation about consequence or sensitivity. The assistant
introduced a stronger proposition about pre-specified predictive control over
small changes. The proposed experiment may be useful, but it tests the
assistant's strengthened claim unless the user separately adopts it.

**Status:** `ACKNOWLEDGED_AGENT_OVERREACH`

## CORR-APE-0002 — Etymological inquiry framed as attempted proof

**Source instruction — user**

> Also look into the multiple meanings of the word grandiosity, also look at
> the etymology of the words act, play, performance, drive, observe, reality,
> theater acting, spectate, spectacle, observe, display

and:

> And the thesis that ties it all together and I want to (ambitious and
> grandiose I am aware) do my ted talk about.

**Assistant framing**

> The etymology produces a useful structure, but I'm treating it as a lens
> rather than proof.

The drafted lexicon repeated:

> Etymology can reveal inherited semantic collisions and suggest experiments.
> It does not prove a philosophical or engineering thesis.

**Finding**

The user did not state that etymology proved the thesis. The user requested
etymological research and a thesis connecting the concepts. By volunteering a
proof/non-proof correction, the assistant implied an epistemic error that the
user had not made.

The caveat remains useful as document methodology, but it must be attributed to
the assistant's research discipline, not presented as a correction of the
user.

**Status:** `ACKNOWLEDGED_AGENT_OVERREACH`

## General control derived from both incidents

Before strengthening or correcting a proposition, an agent should preserve:

```text
SOURCE_PROPOSITION
AGENT_PARAPHRASE
ADDED_COMMITMENTS
REMOVED_AMBIGUITIES
USER_ADOPTION_STATUS
```

An agent-generated clarification is `PROPOSED_INTERPRETATION` until adopted.
It cannot be cited later as something the user originally claimed.

