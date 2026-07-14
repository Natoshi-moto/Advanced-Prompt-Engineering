# Noted as the destination: sovereign work and capacity exchange

**State:** `CANDIDATE`  
**Source proposition — user:**

> People will do creative work, rent their mining power, rent their AI reasoning
> power, sell their own Nexus OS kernels. The noted app is where everything ends
> up.

## Interpretation status

The source establishes Noted as the intended integration destination and names
four economic objects. It does not yet settle their exact legal, technical, or
settlement mechanisms.

`mining power` remains an unresolved typed term:

- proof-of-work mining capacity;
- CPU/GPU/ASIC capacity currently operated by miners;
- general compute capacity;
- a project-specific useful-work or verification mechanism.

No one interpretation inherits authority until adopted in a later route.

The resource market is broader than mining. Candidate resource types include:

| Resource | Commercial unit | Important boundary |
|---|---|---|
| storage | byte-time plus replication level | content policy, deletion, durability, encryption |
| RAM | byte-time inside a declared execution lease | normally not separable from the compute job using it |
| CPU | core-time or verified job | sandboxing, architecture, benchmark, side channels |
| GPU/accelerator | device-time, memory class, or verified job | model/data isolation, thermal and energy accounting |
| bandwidth | direction-specific bytes at measured service levels | abuse, jurisdiction, privacy, congestion, exit-node liability |
| relay service | availability, retention, and delivery window | censorship policy, spam, data loss, operator visibility |
| archival replication | object-time with challenge proofs | availability is not correctness or legality |
| AI inference | bounded job, tokens, or evaluated deliverable | privacy, model identity, tool authority, quality variance |

Every resource offer needs a unit, locality, availability window, measurement
method, verification method, isolation promise, data policy, price, cancellation
rule, and failure remedy. A resource should not be listed merely because it is
physically present; it must be safely allocatable and its delivery must be
measurable.

## System shape

```text
NOTED LOCAL HOST
  ├─ private archive and relational workspace
  ├─ identity, keys, pacts, permissions, and receipts
  ├─ creative-work studio and provenance
  ├─ capacity and reasoning marketplace
  ├─ Nexus kernel registry and sandbox
  └─ transport adapters: bundle / IRC / Nostr / mesh / web
```

Noted is not merely a client for a remote platform. It is the user's local
authority surface: the place where offers are composed, external objects are
inspected, permissions are granted, work is received, receipts are preserved,
and portable history remains usable if a market or relay disappears.

## Four market object classes

### 1. Creative work

Examples include research, editing, design, code, prompts, teaching, analysis,
media, moderation, and collaborative synthesis.

A creative-work offer should bind deliverables, license, attribution,
provenance, acceptance tests, revision limits, confidentiality, price,
deadlines, and dispute procedure.

### 2. Compute or mining capacity

A capacity offer should declare hardware class, benchmark method, runtime,
energy or price basis, availability window, geographic/legal constraints,
allowed workloads, isolation level, data-retention policy, and proof of work
performed. A claimed benchmark is not capacity until independently challengeable.

### 3. AI reasoning capacity

A reasoning offer may expose a model, agent workflow, evaluation service, or
specialized local corpus without exposing private model weights or source data.
It must declare provider/model provenance, tool access, context policy,
retention, output license, safety limits, reproducibility limits, and whether a
human participates.

Reasoning quality is not a single scalar. Buyers request a bounded job and
receive the raw output, declared procedure, receipt, and any evaluator result
as separate objects.

### 4. Nexus OS kernels

A kernel is a portable, versioned package of behavior, schemas, policies,
interfaces, tests, and declared capabilities. It may be sold, licensed,
forked, or shared.

Installing a kernel does not grant it authority. Noted must show a permission
diff, verify signatures and hashes, run conformance tests, isolate execution,
and require explicit pacts for external effects.

The intended kernel carrier is a `.html` file. The same exact bytes may be
opened locally, served as a website, distributed as a peer-to-peer object, or
mounted in Noted. Distribution mode does not change artifact identity, and
artifact identity does not grant capabilities. See `HTML_KERNEL_DISTRIBUTION.md`.

## Minimal shared economic vocabulary

| Object | Purpose |
|---|---|
| `IdentityManifest` | user-held keys, rotation, delegation, and recovery |
| `Offer` | exact good, service, capacity, or license proposed |
| `CapabilityManifest` | what a worker, model, machine, or kernel can attempt |
| `WorkOrder` | accepted scope, price, deadline, inputs, and outputs |
| `ExecutionPact` | permissions and constraints for actions or computation |
| `DeliveryEnvelope` | deliverable bytes plus provenance and license |
| `EffectReceipt` | what was attempted and what was observed |
| `AcceptanceRecord` | buyer's result against frozen criteria |
| `DisputeRecord` | bounded disagreement and cited evidence |
| `SettlementReference` | payment or accounting proof without prescribing currency |
| `ReputationAttestation` | signed contextual observation, never a universal score |

## Settlement neutrality

The market does not require a new speculative token. A `SettlementReference`
may point to direct payment, invoice settlement, barter, community credit, an
existing payment rail, or another declared mechanism. Each adapter owns its
trust, finality, reversal, fee, and legal assumptions.

## Non-negotiable safety boundary

```text
PURCHASED != TRUSTED
SIGNED != SAFE
POPULAR != CANONICAL
PAID != ACCEPTED
TOOL_OK != DELIVERED
DELIVERED != CORRECT
```

External kernels, creative artifacts, model outputs, and job instructions enter
Noted as inert objects. Authority is granted only through local policy and an
action contract bound to exact identities, versions, permissions, and scope.

## First vertical slice

The smallest end-to-end proof should avoid public currency and arbitrary code:

1. a creator publishes a signed bounded analysis offer;
2. a buyer accepts with frozen deliverables and criteria;
3. a local or remote model performs a sandboxed reasoning job;
4. Noted receives raw output, metadata, and receipt;
5. the buyer records acceptance or dispute;
6. settlement is referenced through an external test adapter;
7. both parties can export the complete transaction as a portable bundle.

Only after this works should the proof expand to compute leasing and third-party
kernel execution.
