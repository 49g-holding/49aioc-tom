# Adapter template · `ADP-<CODE>`

**`[ORG]AIOC-TOM` v0.3.0 · 15 October 2026.** The empty form of an adapter. This file is a template, not an adapter: it is not in the register (`README.md`) and has no fixtures.

**How to use it.** Copy it to `adapters/<source-type>.adapter.md`. Fill all ten sections, in this order. Under each heading, the line in italics says what the section fixes; delete it when the section is filled. An adapter only reads: it never asks, never files and never writes. Its fixtures go in `adapters/<source-type>/fixtures/valid/` and `adapters/<source-type>/fixtures/must-fail/`, in the form of blueprint Annex E.2. Its fixed test is `TEST-TOM-ADP-<CODE> v<n>`.

## 1. Identity

*The adapter ID (`ADP-<CODE>`, pattern `^ADP-[A-Z0-9]{2,12}$`) and version; the source type; the owner of the source, by role; its state; the machine block.*

| Field | Content |
|---|---|
| Adapter ID | `ADP-<CODE>` |
| Version | `v0.0.0` |
| Source type | `<the source type>` |
| Owner of the source | `<a role, never a name>` |
| State | `draft` |
| Fixed test | `TEST-TOM-ADP-<CODE> v1` (section 9) |

The machine block. It is read by `tools/check_contracts.py`. The adapter file holds exactly one block that starts `adapter:`. The defaults for a value that is not served, and the refusal reasons, are the same for every adapter.

```yaml
adapter:
  id: "ADP-<CODE>"
  version: "v0.0.0"
  source_type: "<the source type>"
  test: { id: "TEST-TOM-ADP-<CODE>", version: "v1" }
  mappings:
    origin_kind: { "<value served>": "<canonical origin kind>", "<not served>": document }
    status: { "<value served>": "<canonical status>", "<not served>": "not served" }
    status_cap: { "<canonical status>": "<none, inferred or history-only>", "not served": inferred }
    confidentiality: { "<value served>": "<canonical level>", "<not served>": "strictly confidential" }
    statement_label:
      document: { "<label served>": "<Annex B label>" }
      conversation: { "<label served>": "<Annex B label>" }
  defaulted_origin_kind_cap: inferred
  trust_ceiling: "<the highest Annex B label a statement of this source type may reach>"
  refusal_reasons: ["no reference", "outside scope", "scope expired", "does not resolve", "hash mismatch", "carries a secret", "person-level records", "not atomisable", "human port", "other channel", "connection revoked"]
```

## 2. Connection

*The grant: `connect-external-port` (Protocol §13, item 5), through the tool gateway; the scope; the expiry; revocation; each checked at every read.*

## 3. Reference

*How the ID, version and SHA-256 are served or computed; what `held` and `not held` mean for this source; the location form.*

## 4. Snapshot

*How a run pins a content-addressed view; how a needs answer's own snapshot is read; what is served for a version superseded after the pin; how long a snapshot named by a filed release stays readable; the fallback where the source cannot serve a per-answer snapshot (each pack version lists each source by reference, version and hash).*

## 5. Mappings

*Closed tables onto the canonical origin kind, status, confidentiality and statement label. The trust ceiling: the highest Annex B label a statement of this source type may reach. The defaults when a value is not served: status becomes `not served` (statements cap at `inferred`); confidentiality becomes `strictly confidential` (records go to `-records-restricted`); origin kind becomes `document` (statements cap at `inferred`).*

## 6. Atomisation

*The anchor scheme for each format the source serves (paragraph, list item, table row, record field). What cannot be atomised is refused `not atomisable`, and a need for a cleaner version is raised.*

## 7. Notices

*Which changes the source reports (revocation, narrowing, reclassification, supersession). If it reports none, every read re-checks status and scope.*

## 8. Limits

*Reads only. It never asks, never files and never writes. Asking stays with the Chief of Staff of `[ORG]AIOC-SL`. A release is filed only into `[ORG]AIOC-SL`, whatever adapters a run reads. The personal-data and confidentiality rules. Secrets are refused.*

## 9. Fixed test

*`TEST-TOM-ADP-<CODE> v<n>`: a good sample passes; one bad sample per refusal reason is refused with that reason; each mapping table round-trips; the defaults apply when a value is not served.*

## 10. Version history

*One row per version.*

| Version | Date | Change |
|---|---|---|
| `v0.0.0` | `<date>` | `<what changed>` |

*Powered by 49GAION*
