# HTML kernel distribution contract

**State:** `CANDIDATE`  
**Source proposition — user:**

> It's .html files they can be served as websites or p2p

## Core object

A Nexus kernel is a portable HTML artifact whose identity is the hash of its
exact bytes. The same artifact may travel through multiple channels:

```text
SIGNED HTML BYTES
  ├─ local file/archive
  ├─ ordinary web server
  ├─ static website host
  ├─ content-addressed peer-to-peer exchange
  └─ Noted kernel mount
```

The transport is not the authority. A copy received from a trusted peer still
requires hash, signature, manifest, and capability checks. A file served over
HTTPS is not thereby safe. A signature establishes an author's key, not code
quality or benign behavior.

## Document/program ambiguity

HTML can be:

- a passive document;
- a visual interface;
- an executable JavaScript application;
- a network client;
- a storage client;
- a wrapper around imported code;
- a control surface for privileged host operations.

Therefore Noted must record three separate events:

```text
INSPECTED_ARTIFACT
EXECUTED_IN_SANDBOX
GRANTED_CAPABILITY_SET
```

Viewing must not imply execution, and execution must not imply authority.

## Sidecar manifest

Before installation, a kernel declares:

```text
kernel_id
version
html_sha256
author_key
signature
license
entry_mode
external_dependencies
network_origins
storage_namespaces
requested_host_capabilities
message_protocol_version
expected_outputs
tests
known_limitations
update_predecessor
```

For a strictly single-file kernel, `external_dependencies` is empty and all
code/assets are embedded. If remote resources are permitted, every origin and
integrity expectation must be explicit; the retrieved application is no longer
identified solely by the original HTML hash.

## Execution modes

### `PASSIVE_PREVIEW`

Render a sanitized or inert representation. No scripts, network, storage, host
messages, downloads, popups, or navigation.

### `SANDBOXED_APP`

Run under an isolated origin or sandboxed frame with no ambient Noted secrets.
Host interaction occurs through a versioned, allowlisted message protocol.

### `HOSTED_SITE`

Serve the exact artifact as an ordinary website. The site has only browser and
server capabilities separately configured for that deployment. A hosted copy
cannot claim Noted-local authority.

### `P2P_OBJECT`

Exchange exact bytes plus manifest and signature. Peers verify before indexing
or offering execution. P2P availability does not imply global discoverability,
moderation immunity, or trusted authorship.

## Capability rule

The Noted host owns keys, private archives, economic authorization, filesystem
access, network credentials, and external tools. A kernel receives narrow RPC
capabilities such as:

```text
archive.read(query, bounds)
draft.write(namespace, object)
offer.propose(unsigned_offer)
job.submit(authorized_job_contract)
receipt.read(receipt_id)
```

High-consequence operations are never raw JavaScript calls. They require a
host-rendered action contract bound to resolved identities, arguments, cost,
scope, expiry, and user authorization.

## Update and fork semantics

- Any byte change produces a new hash.
- Updates are explicit successor objects, not silent mutation.
- A fork may retain ancestry without inheriting the predecessor author's
  endorsement.
- Revocation is a signed warning or policy decision; it cannot erase already
  distributed bytes.
- Historical receipts continue to identify the exact executed version.

## First conformance tests

1. passive preview cannot execute inline or imported scripts;
2. kernel cannot read host storage without a granted capability;
3. kernel cannot expand an authorized message after confirmation;
4. same HTML bytes verify identically over web, bundle, and P2P transport;
5. altered bytes fail the original hash/signature identity;
6. external dependency mutation is detected or prohibited;
7. denied network origins remain unreachable;
8. update cannot impersonate predecessor identity;
9. receipt names artifact hash, capability set, host version, and effect;
10. closing or revoking a kernel terminates outstanding capability leases.

