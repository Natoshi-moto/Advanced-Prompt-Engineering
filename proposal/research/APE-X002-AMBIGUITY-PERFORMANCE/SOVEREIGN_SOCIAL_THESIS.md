# Sovereign social computing thesis

**State:** `CANDIDATE`  
**Ambition:** A smooth, economically capable social environment whose identity,
history, reasoning tools, and exchange rules remain usable without dependence
on a single platform operator.

## Precise target

The target is not "no network." IRC, dial-up links, relays, local meshes, and
Nostr are networking systems. The target is:

> No mandatory centralized social-media operator, no platform-owned identity,
> no single canonical server, and no requirement for frontier-scale inference
> to participate meaningfully.

## Vision

A person owns a local archive and cryptographic identity. Their client can:

- read and write durable signed social objects;
- communicate through interchangeable transports such as local files, delay-
  tolerant bundles, IRC gateways, Nostr relays, Bluetooth/Wi-Fi meshes, or
  ordinary internet links;
- use a small local language model for indexing, summarization, filtering,
  translation, and bounded assistance;
- carry reputation and provenance as inspectable claims rather than a platform
  score;
- make bounded economic agreements without issuing a speculative public token;
- recover, migrate, fork, and continue when a relay, host, or community fails.

## Existing neighbors

This cannot be called the first decentralized or sovereign social system
without a prior-art review. Existing components already cover substantial
territory:

- IRC provides a simple text-based conferencing protocol and distributed
  server architecture.
- ActivityPub specifies decentralized client/server and federated server/server
  social networking.
- Nostr uses signed events and interchangeable relays without a trusted central
  server.
- Briar supports peer-to-peer communication over Bluetooth, Wi-Fi, and Tor,
  including offline-resilient forums.

The candidate novelty must therefore live in a tested composition: local-first
intellectual workspace, transport independence, semantic action firewall,
portable provenance, bounded local AI, and non-speculative economic contracts
with a low-resource operating envelope.

## Minimum architecture

1. **Local object store:** content-addressed events, threads, annotations,
   receipts, claims, and redactions.
2. **User-held identity:** signing keys with rotation, delegation, recovery, and
   explicit device authority.
3. **Transport adapters:** the same signed envelope over file bundle, IRC,
   Nostr, mesh, or HTTP; transport is not authority.
4. **Semantic Action Firewall:** no conversational inference directly invokes a
   consequential tool.
5. **Local cognition:** search and small-model assistance with declared limits;
   remote models are optional accelerators.
6. **Community policy:** forkable moderation and membership rules with no claim
   of globally objective reputation.
7. **Economic object layer:** offers, acceptances, invoices, delivery receipts,
   disputes, and settlement references; value issuance is optional and gated.
8. **Replication and recovery:** exportable state, deterministic validation,
   partial sync, and explicit conflict semantics.

## Low-resource claim to test

Define an operating envelope before implementation:

- functional text interface on commodity or legacy hardware;
- graceful operation on intermittent, high-latency, low-bandwidth links;
- no mandatory GPU for ordinary social participation;
- local models optional and replaceable;
- bounded storage and partial replication;
- energy and bandwidth measured per useful social/economic operation.

"Runs on dial-up" requires a declared bitrate, latency, reconnect behavior,
sync backlog, object sizes, and test trace. It is not established by using a
text protocol.

## Prior-art sources

- [IRC client protocol, RFC 2812](https://datatracker.ietf.org/doc/html/rfc2812)
- [IRC server protocol, RFC 2813](https://datatracker.ietf.org/doc/html/rfc2813)
- [ActivityPub, W3C Recommendation](https://www.w3.org/TR/activitypub/)
- [Nostr protocol repository](https://github.com/nostr-protocol/nostr)
- [Briar: how it works](https://briarproject.org/how-it-works/)

