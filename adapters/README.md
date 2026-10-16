# Adapters: the source types of the Input socket

**`[ORG]AIOC-TOM` v0.3.0 · draft · 15 October 2026.** The register of the adapters of `[ORG]AIOC-TOM`.

Every source type plugs into the Input socket of `[ORG]AIOC-TOM` through its own adapter file (blueprint §4.3; Annex E.2). An adapter only reads. Asking and filing stay with Source Lifecycle. Adding an adapter is a tested change: one file, its fixtures, its test, and a row here.

An adapter is the Standard's converter for one source type (`49GAION-aioc` `docs/STANDARD-CAPABILITIES.md` §4.3). The socket hands the engine one Input Pack, whatever adapters served it (blueprint §4.3; `contracts/input-pack.schema.json`).

## The adapter register

| Adapter ID | Source type | File | Version | Test | State |
|---|---|---|---|---|---|
| `ADP-SL` | Source Lifecycle | [`source-lifecycle.adapter.md`](source-lifecycle.adapter.md) | v1.1.0 | TEST-TOM-ADP-SL v2 · NOT_RUN | draft |

## What is in this folder

| Path | What it is |
|---|---|
| [`TEMPLATE.adapter.md`](TEMPLATE.adapter.md) | the empty form: the ten fixed sections, in order, and an empty machine block |
| `<source-type>.adapter.md` | one adapter: its identity, connection, reference, snapshot, mappings, atomisation, notices, limits, fixed test and version history |
| `<source-type>/fixtures/valid/` and `<source-type>/fixtures/must-fail/` | the adapter's fixtures, in the form of blueprint Annex E.2. A valid fixture is admitted as its `expect` says. A must-fail fixture is refused with exactly its reason |

## Three rules

1. **Adding an adapter is a tested change.** One new file, its fixtures and its test, and a row in this register. No stage changes.
2. **An adapter is never a precedence rule.** Two sources that disagree are a contradiction (blueprint Annex B.2), whichever adapters served them.
3. **The same bytes served by two adapters are one source,** with two references.

## How an adapter is added

1. Copy [`TEMPLATE.adapter.md`](TEMPLATE.adapter.md) to `adapters/<source-type>.adapter.md`, and fill its ten sections.
2. Write its fixtures: one valid fixture for each mapping and each default, and one must-fail fixture for each refusal reason.
3. Write its fixed test, `TEST-TOM-ADP-<CODE> v<n>`, in section 9 of the adapter file.
4. Have the connection signed by the seat over that source, as `connect-external-port`, at the tool gateway. An adapter uses only the read part of a connection.
5. Add the row to the register above. `tools/check_contracts.py` checks the fixtures against the adapter's machine block.

*Powered by 49GAION*
