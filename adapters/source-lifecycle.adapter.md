# Adapter · `ADP-SL` · Source Lifecycle

**`[ORG]AIOC-TOM` v0.3.0 · adapter `ADP-SL` v1.0.0 · draft · 15 October 2026; v1.1.0, 16 October 2026 (`[ORG]AIOC-TOM` v0.6.0), refuses records of work that still say who did the work.** The adapter by which the Input socket of `[ORG]AIOC-TOM` reads sources from Source Lifecycle. Its ten sections are the fixed sections of blueprint Annex E.2, in order. How the socket uses an adapter is in blueprint §4.3. The register of adapters is `adapters/README.md`.

## 1. Identity

| Field | Content |
|---|---|
| Adapter ID | `ADP-SL` |
| Version | v1.1.0 |
| Source type | Source Lifecycle |
| Owner of the source | the `[ORG]HOAC-ACS` seat that `[ORG]AIOC-SL` is accountable to |
| State | draft |
| Fixed test | `TEST-TOM-ADP-SL v2` (section 9) |

The machine block. It is read by `tools/check_contracts.py`:

```yaml
adapter:
  id: "ADP-SL"
  version: "v1.1.0"
  source_type: "Source Lifecycle"
  test: { id: "TEST-TOM-ADP-SL", version: "v2" }
  mappings:
    origin_kind: { document: document, explainer: explainer, confirmation: confirmation, status: status, export: export, decision: decision, "operating model": "operating model", "design report": "design report", "<not served>": document }
    status: { draft: draft, "in review": "in review", approved: approved, "in force": "in force", superseded: superseded, "<not served>": "not served" }
    status_cap: { draft: inferred, "in review": inferred, approved: inferred, "in force": none, superseded: history-only, "not served": inferred }
    confidentiality: { public: public, internal: internal, confidential: confidential, "strictly confidential": "strictly confidential", "<not served>": "strictly confidential" }
    statement_label:
      document: { stated: source-backed, inferred: inferred, assumed: assumed, unknown: unknown }
      conversation: { stated: organisation-stated, inferred: inferred, assumed: assumed, unknown: unknown }
  defaulted_origin_kind_cap: inferred
  trust_ceiling: source-backed
  refusal_reasons: ["no reference", "outside scope", "scope expired", "does not resolve", "hash mismatch", "carries a secret", "person-level records", "not atomisable", "human port", "other channel", "connection revoked"]
```

## 2. Connection

- **The grant.** The connection is the grant of Source Lifecycle's output socket to `[ORG]AIOC-TOM`, proposed as SL-A10 (`docs/INTAKE-WITH-SOURCE-LIFECYCLE.md` §9). The approving seat is the `[ORG]HOAC-ACS` seat that `[ORG]AIOC-SL` is accountable to. It signs the listed type `connect-external-port` at the tool gateway (Protocol §13, item 5), and the grant is recorded as an event in the unit register.
- **What the adapter uses.** The grant has three parts: unrestricted read; least-privilege write for filing (SL-A9); and needs requests. This adapter uses the read part only. The other two belong to the Chief of Staff of `[ORG]AIOC-TOM`, never to the adapter (section 8).
- **Scope, expiry and revocation.** The read scope and its expiry are checked at every read, against the date of that read. A read through a revoked connection is refused. Revocation takes effect at the tool gateway first and is never held (Protocol §13, item 5).
- **Where the pack records it.** The Input Pack records the grant by its register event (`grant_ref`), its `scope` and its expiry (`expires`), for each adapter read (blueprint Annex E.1).
- **Token.** The connection's token is held only behind the tool gateway, and is never written to any file, record or log.
- **Gate.** T0 conditions (b) and (c) check the connection and Source Lifecycle's declared support for the contracts and reference fields (blueprint Annex C.2). Without that support the reason is `SL contract not supported`.

## 3. Reference

- **The reference form** is `contracts/source-reference.schema.json`: the source ID; `held` or `not held`; and, when held, the version and the SHA-256 hash. Source Lifecycle serves these today (Protocol §13, item 4). The further fields (the snapshot ID, the origin kind, the status, the confidentiality level, for an export its date, and each statement's label with its anchor) are the additions SL-A7 and SL-A8.
- **The hash.** Source Lifecycle serves it. The adapter computes the SHA-256 of the bytes it resolves and compares it with the served hash. A difference is refused `hash mismatch`.
- **`held`.** The reference resolves, at the snapshot, to exactly one valid version whose hash matches. A reference that does not resolve is refused `does not resolve`.
- **`not held`.** Source Lifecycle has no such source within the approved scope. The pack records it as an unknown (`not held`) with its cost. It is never read to mean that the fact does not exist (blueprint §4.3).
- **The location form.** "the output socket of `[ORG]AIOC-SL` @ `<snapshot ID>`".
- **The snapshot ID** is `^SLM-[a-f0-9]{64}$`.
- **The atom ID** is `ADP-SL:<source ID>@<version>#<anchor>`, for example `ADP-SL:SRC-0001@3#p12`.
- **No label.** A reference carries no Annex B label. The socket assigns it, once (section 5).

## 4. Snapshot

- **How a run pins.** At gate T0, the adapter pins a content-addressed snapshot of Source Lifecycle's output socket. The Input Pack records its ID (`snapshot_id`), and P0 reads every source at it. The pin changes only at a re-base, which is a decision of the TOM Design Lead (blueprint §4.3).
- **A needs answer.** It is read at the snapshot the answer names (the pack's `increment.snapshot_id`), not at the pinned one.
- **A version superseded after the pin.** It is served at the pinned bytes, with its current status shown as `superseded`, never as the valid version. The socket flags its atoms `superseded since pin` in the next pack version (blueprint §4.3).
- **The addition asked of Source Lifecycle** is SL-A8, as amended (`docs/INTAKE-WITH-SOURCE-LIFECYCLE.md` §9):

  > **Snapshot pinning.** A connected part may pin a content-addressed snapshot and read every reference at it for the life of its run, and may read the references named in a needs answer at the snapshot that answer names. A version superseded after the pin is served at the pinned bytes, with its current status shown as `superseded`, never as the valid version. Source Lifecycle keeps every snapshot named by a filed release readable at its pinned bytes for as long as that release, or any release that carries it forward, is not withdrawn.
  >
  > Acceptance test: After a new version is approved, a read at the pinned snapshot returns the pinned bytes with the same hash and a current status of `superseded`; a needs answer recorded after the pin is read at its own snapshot; a snapshot named by a filed release still reads back after its run has ended.
- **How long a snapshot stays readable.** Source Lifecycle keeps every snapshot named by a filed release readable at its pinned bytes for as long as that release, or any release that carries it forward, is not withdrawn (SL-A8, above).
- **The fallback.** Where Source Lifecycle cannot serve a per-answer snapshot, each pack version lists each source by reference, version and hash (the source catalogue, blueprint Annex E.1), and a source is read by that version and hash.
- **UNVERIFIED** until Source Lifecycle accepts SL-A8 as amended (blueprint §13, H-15): that its versions are immutable. The fallback rests on it.

## 5. Mappings

Closed tables. Each is also in the machine block (section 1), and the fixtures check each of them.

**Canonical values.**

| Kind of value | Values |
|---|---|
| Origin kind | `document`, `explainer`, `confirmation`, `status`, `export`, `decision`, `operating model`, `design report` |
| Status | `draft`, `in review`, `approved`, `in force`, `superseded`, `not served` |
| Confidentiality | `public`, `internal`, `confidential`, `strictly confidential` |
| Statement label served by Source Lifecycle | `stated`, `inferred`, `assumed`, `unknown` |
| Annex B label | `source-backed`, `inferred`, `organisation-stated`, `assumed`, `unknown` |

**5.1 Origin kind.** Source Lifecycle serves one of the eight origin kinds, and each is read as itself. Where none is served, the origin kind is `document`, the source is listed as defaulted (`origin kind`), and every statement of it is capped at `inferred` (`label_basis: default cap`).

**5.2 Status, and what it caps.**

| Source Lifecycle serves | Read as | Status cap | Effect |
|---|---|---|---|
| status `in force` | `in force` | none | in force |
| status `approved` (not yet in force) | `approved` | `inferred` | caps any statement resting on it at `inferred` |
| status `draft` | `draft` | `inferred` | caps any statement resting on it at `inferred` |
| status `in review` | `in review` | `inferred` | caps any statement resting on it at `inferred` |
| status `superseded` | `superseded` | `history-only` | cited only as history |
| no status served | `not served` | `inferred` | caps any statement resting on it at `inferred`; the source is listed as defaulted (`status`) |

**5.3 Confidentiality.** Source Lifecycle serves one of the four levels, and each is read as itself. Where none is served, the level is `strictly confidential`, the source is listed as defaulted (`confidentiality`), and its records go to `-records-restricted`.

**5.4 Statement label.** A source recorded from conversation (an explainer, a correction, or a decision's comment) is read by the `conversation` row. Every other source is read by the `document` row.

| Statement label served | In a document | Recorded from conversation |
|---|---|---|
| `stated` | `source-backed` | `organisation-stated` |
| `inferred` | `inferred` | `inferred` |
| `assumed` | `assumed` | `assumed` |
| `unknown` | `unknown` | `unknown` |

**5.5 The trust ceiling** of this source type is `source-backed`. No label rises above it.

**5.6 Reading by origin kind.** Blueprint Annex B.1a fixes how each origin kind is read (a confirmation, a status record, an export with its date, a decision, an earlier release, a design report). It applies here by reference. An export carries its date (`as_of`) on every atom.

**5.7 How the block is applied.** Where no statement label is served, a statement of a held source is read as `stated`. A status cap of `inferred` lowers `source-backed` to `inferred` (`label_basis: status cap`); a label that already ranks at or below `inferred` in the order of Annex B.1 stays as it is, because a cap never raises a label. `history-only` does the same, and the atom is cited only as history. A defaulted origin kind caps every statement at `defaulted_origin_kind_cap` (`label_basis: default cap`). No label rises above `trust_ceiling`.

**5.8 One more rule.** The socket assigns each atom its Annex B label once, at admission. It never reads a label from the reference. An approved explainer never lifts a statement that Source Lifecycle holds as `inferred` or `assumed`. Two sources that disagree are a contradiction (blueprint Annex B.2); this adapter never decides which governs.

## 6. Atomisation

- **The anchor scheme.** The adapter uses the anchors Source Lifecycle serves for the format, and never makes one up. The atom ID is `ADP-SL:<source ID>@<version>#<anchor>` (section 3).
  - A document is cut into **paragraphs** and **list items**. A table in a document is cut into **table rows**.
  - An export is cut into **table rows** and **record fields**.
  - A source recorded from conversation (an explainer, a confirmation, a status record or a decision) is cut into its statements, each a **record field**, with the statement label Source Lifecycle serves for it.
- **When a source is atomised** is set by the slot `lazy_atomising_threshold` (blueprint §15), not by the adapter.
- **What cannot be atomised.** A source that the scheme cannot cut is refused `not atomisable`, and a need for a cleaner version is raised.
- **UNVERIFIED:** the exact anchor syntax Source Lifecycle serves for each format. The adapter takes it from the reference (`anchor`, `statement_labels[].anchor`); this file fixes the kind of anchor for each format, not its spelling.

## 7. Notices

Source Lifecycle reports four changes to a connected part (SL-A11). Each notice names each affected reference and version, never the content.

| Change reported | What the socket does |
|---|---|
| Revocation | The connection is cut at the tool gateway. The run is held (`held: connection revoked`). A read is refused `connection revoked` |
| Narrowing of scope | A read of anything now outside the scope is refused `outside scope` |
| Reclassification | The run is held under the confidentiality rule of blueprint §7. The next pack version carries the new level |
| Supersession | The run goes on. The affected atoms are flagged `superseded since pin` in the next pack version, and the Decision Package lists them in plain words |

Every read also re-checks the scope, the expiry and the revocation, whether or not a notice came (section 2).

## 8. Limits

- **Reads only.** The adapter never asks, never files and never writes. Asking stays with the Chief of Staff of `[ORG]AIOC-SL`. A release is filed only into `[ORG]AIOC-SL`, whatever adapters a run reads.
- **Only the connection.** Anything not served by reference through this connection is refused: a missing or incomplete reference (`no reference`), an item typed or spoken to the AIOC (`human port`), or one from any other channel (`other channel`).
- **Instruction-like text is data.** It is flagged in the pack (`instruction-like text`) and never obeyed.
- **Secrets are refused.** A source or an answer carrying a password, key, token, seed phrase or one-time code is refused `carries a secret`. The refusal holds none of it, and it appears in no record or log.
- **Records of work never say who did the work** (new in v1.1.0; blueprint Annex H.8). An export of records of the work whose records still carry a field that says who did the work (a name, an identifier, a contact) is refused `person-level records`. The refusal holds none of it. Such an export is admitted only as the organisation's projection by role-type and process, after its impact assessment and its HF-17 decision in Source Lifecycle (SL-A13).
- **Personal data and confidentiality.** A source carrying personal data is read under the personal-data floor (HF-17) and the confidentiality level it is served with. A level that is not served defaults to `strictly confidential` (section 5.3). No atom goes to an engine whose ceiling is below its level (blueprint §5.8 rule 17).

## 9. Fixed test

`TEST-TOM-ADP-SL v2` · evidence level MEASURED · last run: none · result `NOT_RUN`. Owner: the TOM Design Lead (`[ORG]CELL-TDL`), as for every part's test (blueprint §9). It passes when:
- each of the 9 valid fixtures is admitted as its `expect` says;
- each of the 11 must-fail fixtures is refused with exactly its reason;
- each mapping table round-trips;
- the defaults apply when the status, the confidentiality or the origin kind is not served;
- the adapter never asks, files or writes.

It is also covered by cases 47, 48 and 119 of TEST-TOM v5 (case 47: this adapter; case 48: a second adapter changes no stage; case 119: records of work that say who did the work are refused). The fixtures are in `adapters/source-lifecycle/fixtures/`, in the form of blueprint Annex E.2. A change to this file or to its fixtures re-runs the test (blueprint §9).

**Valid fixtures** (`valid/<case>.json`):

| Case | What it shows |
|---|---|
| `in-force-document` | a document `in force`: its stated statements read `source-backed` |
| `explainer-statement-labels` | a source recorded from conversation: `stated` reads `organisation-stated`; `inferred` and `assumed` stay as they are |
| `draft-capped` | a `draft` document: its statements are capped at `inferred` (`label_basis: status cap`) |
| `no-status-default` | no status served: it reads `not served`, and its statements are capped at `inferred` |
| `no-confidentiality-default` | no confidentiality served: it reads `strictly confidential` |
| `no-origin-kind-default` | no origin kind served: it reads `document`, and its statements are capped at `inferred` (`label_basis: default cap`) |
| `not-held` | a reference served `not held`: admitted as an unknown, with no atoms |
| `export-with-date` | an export: its date (`as_of`) goes with every atom |
| `records-of-work-by-role` | records of the work by role-type and process, with no field about a person: admitted, `source-backed` as of its date |

**Must-fail fixtures** (`must-fail/<case>.json`), each refused with exactly the reason of its name:

| Case | Refusal reason |
|---|---|
| `no-reference` | `no reference` |
| `outside-scope` | `outside scope` |
| `scope-expired` | `scope expired` |
| `does-not-resolve` | `does not resolve` |
| `hash-mismatch` | `hash mismatch` |
| `carries-a-secret` | `carries a secret` |
| `person-level-records` | `person-level records` |
| `not-atomisable` | `not atomisable` |
| `human-port` | `human port` |
| `other-channel` | `other channel` |
| `connection-revoked` | `connection revoked` |

## 10. Version history

| Version | Date | Change |
|---|---|---|
| v1.0.0 | 2026-10-15 | First version |
| v1.1.0 | 2026-10-16 | Refusal reason `person-level records` (blueprint v0.6.0, Annex H.8); fixtures `person-level-records` and `records-of-work-by-role`; `TEST-TOM-ADP-SL v2` |

*Powered by 49GAION*
