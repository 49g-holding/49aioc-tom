# Intake with Source Lifecycle

**`[ORG]AIOC-TOM` v0.4.0 · draft · 15 October 2026; v0.6.0, 16 October 2026, adds SL-A13 and the v0.6 sockets contract (§9); v0.6.1, 19 October 2026, gives the Chief of Staff its COS code `[ORG]CELL-COSTOM` in `raised_by`, and the needs-request contract takes the id `v0.6.1`.** How the Target Operating Model AIOC gets everything it knows. It reads only sources, and where the sources are silent it asks through the Chief of Staff of `[ORG]AIOC-SL`. The machine contracts are in `contracts/`:
- `source-reference.schema.json`;
- `input-pack.schema.json`;
- `needs-request.schema.json` and `needs-answer.schema.json` (`:v0.4`);
- `needs-status.schema.json`;
- `missing-report.schema.json`;
- `tom-release.schema.json`;
- `tom-filing-receipt.schema.json`;
- `reference-model-catalogue.schema.json` (the Library catalogue as read; never a source).

`tools/check_contracts.py` checks the contracts and their examples.

Every source type plugs into the Input socket through its own adapter file (`adapters/`). Source Lifecycle's adapter is `adapters/source-lifecycle.adapter.md` (`ADP-SL`).

## 1. The rule

1. **Only documents.** This AIOC reads only sources served by reference: by Source Lifecycle (§7), and by any other source through its own adapter, read only (blueprint §4.3). v0.4.0 has one adapter, for Source Lifecycle. Asking and filing stay with Source Lifecycle. Nothing typed or spoken to it is a source.
2. **Never a question to a person.** This AIOC asks no one in the organisation anything. When the sources do not answer something the design needs, it asks the **Chief of Staff of `[ORG]AIOC-SL`**. Its only human contact is its own TOM Design Lead, and only about the run (method, configuration, run control). Nothing that arrives through a human port is a source.
3. **What people say becomes a source first.** The Chief of Staff of `[ORG]AIOC-SL` gets the answer from the right person, as a document, an explainer, a confirmation, a status, an export or a decision. Source Lifecycle shows the person the exact text to approve, records only what they approve, and answers this AIOC by reference. Spoken words are never the basis of the design; an approved, recorded, versioned source is.
4. **The Design Request.** A run starts only from a Design Request, a source in Source Lifecycle:
   - **Kind.** Origin kind `document` or `explainer`, approved by the Requesting Authority.
   - **Content.** At least the requesting seat, the entities in view, and what should be different, in the organisation's own words; and, where known, the request kind and the earlier release it continues (DRQ-01 fields 7 and 8), and the run depth (field 9).
   - **Where there is no written brief.** An organisation with no such document makes one with the Chief of Staff of `[ORG]AIOC-SL`, through explainers EX-01 and EX-07, approved item by item. This AIOC supplies the template (DRQ-01, `ASKING-CATALOGUE.md` §3a) and never the content.
   - **The run request.** The Requesting Authority's Cell then opens the run as one Work Item to this AIOC, carrying only the Design Request's reference (§2a).
   - **Before the run.** No needs request exists before gate T0.

Why: an operating model is the basis of how an organisation, a company or even one person's work will run. A basis must be traceable, versioned and approved by the person whose word it is. Speech is none of these until Source Lifecycle has made it a source.

## 2. Who does what

| Step | This AIOC (`[ORG]AIOC-TOM`) | Chief of Staff of `[ORG]AIOC-SL` | The organisation's people |
|---|---|---|---|
| Read | reads every held source in its read plan first | — | — |
| Decide to ask | asks only what no held source answers and what changes a design decision | — | — |
| Ask | sends a needs request (one thing; one decision per row), with the pass's Missing Report | accepts it or returns it with a reason (`needs status`) | — |
| Reach the person | never | for a delegable row, chooses who can answer (this AIOC may only suggest a role the sources name); for a non-delegable row, asks only the Cell named in `answering_cell` (the Requesting Authority's, or for a listed type the Cell that signs it); asks in plain words, with this AIOC's original wording kept beside it | — |
| Answer | — | collects the document, runs the explainer as a guided conversation, or puts the confirmation, status or decision row; links a listed-type row to the tool gateway's signature surface | answer, correct, say "don't know", or decline; sign a listed-type row at the gateway |
| Approve | — | shows the exact text to approve, item by item | approve each item, or not |
| Record | — | records only what is approved, as a source with its origin kind, status, confidentiality and each statement's own label | — |
| Return | admits the answer only by reference, and sets the sub-item `done` only when its acceptance test passes | answers by reference, or `declared absent`, `not applicable`, `declined`, `dont know` or `returned`, each with its reason | — |

The Chief of Staff of `[ORG]AIOC-SL` is a connecting Chief of Staff: it connects the organisation's people with the parts that need them (`49GAION-aioc` `docs/STANDARD-CAPABILITIES.md` §4.2; Naming Standard R3). It never answers for a person, never records content the person has not approved, and never decides.

## 2a. The Work Item envelope

1. **The run.** A run is one Work Item (Protocol §4.1), opened by the Requesting Authority's Cell through this AIOC's HU input port:
   - sender: that Cell;
   - receiver: `[ORG]AIOC-TOM`;
   - requested output: a TOM Release under `contracts/tom-release.schema.json`;
   - acceptance test: the Requesting Authority's own (gate T8 decided; the manifest valid; the filed reference reads back by hash);
   - sources: the Design Request reference.
2. **Needs requests.** Each needs request is a sub-item of the run, with `parent_work_item` set to the run and chain depth 1:
   - receiver: `[ORG]AIOC-SL`;
   - requested output: a needs answer under `contracts/needs-answer.schema.json`;
   - acceptance test: TEST-TOM v5, case 11 (the eight checks of blueprint §4.3);
   - sources: the references of `minimality_proof.searched`, each with its location (the output socket, at the snapshot of the pack version the request was raised from).

   Source Lifecycle answers the sub-item. It never opens a new item back to this AIOC, so the chain never loops (Protocol §4.6, item 2).
3. **Other messages.** The Missing Report and the status messages travel with the pass and the sub-items they concern.
4. **Waiting and bounces.** Overdue items follow `waiting_deadlines` and its escalation (Protocol §4.6, item 1). Re-sending follows `bounce_limit` (Protocol §4.4).

## 3. Before asking

A needs request is sent only after all of these:

1. **Read first.** Every held source in the run's read plan has been read. A question that a held source answers goes on the **do-not-ask list**, with the answering citation, and is never sent. The list is bounded: it covers only the needs candidates raised in this run, the fields of the published contracts this run must fill, and the answers already received; it is never an unbounded enumeration.
2. **Reconstruct first.** The Request Analyst and the Source Proxy have taken everything they can from the sources (blueprint §5.1).
3. **Decision leverage.** The answer changes a scope boundary, a constraint, a criterion or a design decision. If no decision changes, the item is carried as an assumption, with what breaks if it is false, and is not asked.
4. **Minimality proof.** The request lists the source references searched (at least one), and why none of them answers it.
5. **Not a design question.** The organisation is never asked to do the design it asked for: no question about which solution, which structure, which tool or which success measure to invent. It is asked for facts, for its own intent, and for decisions only it can make.
6. **Reviewed.** The pass has settled clear at review point RPa (blueprint §5.8): each row is one decision; no row is answered by a held source, leads the answer or names a person; each row's delegability is right; and the Missing Report equals the needs log.

## 4. The six types of request

| Type | Ask for | When | What comes back |
|---|---|---|---|
| `document` | a named kind of document believed to exist (`ASKING-CATALOGUE.md` §2) | the design needs what that document governs, and it is not held | the document, registered and approved in Source Lifecycle, with its status |
| `explainer` | the organisation's own account of something no document records, through a set explainer template (`ASKING-CATALOGUE.md` §3) | no document exists, or the documents are silent | an approved explainer, recorded as a source of origin kind `explainer`, with each statement's own Source Lifecycle label (§7.1). A statement labelled `stated` is admitted as `organisation-stated`; `inferred` and `assumed` stay as they are; `unknown` stays `unknown` |
| `confirmation` | confirm, correct (in the person's own words) or "don't know", on one item this AIOC inferred from the sources, or on how it read the request (`ASKING-CATALOGUE.md` §4.1) | an inferred item is load-bearing, or the frame needs the organisation to confirm how its request was read | an approved confirmation record. The item stays `inferred` and gains its confirmation reference; or it is replaced by the correction, labelled `organisation-stated`; or it stays `inferred`, with "don't know" recorded |
| `status` | whether one held document is in force, a draft, or superseded | a load-bearing source has no status | a status record by the source's approver in Source Lifecycle, with the approval evidence (who, when). A status record never says which of two sources governs |
| `export` | an export from a system of record (never a live read): for example a list of entities, an approval matrix, a register | the fact lives in a system, not in a document | the export, registered as a source with its date |
| `decision` | a choice only the Requesting Authority can make: what is in and out; which entity is committed; how anyone will know it worked; which of two disagreeing sources governs; accept, correct or reject each child and each element; the choice on a material finding | gates T1, T2, T3 and T8 (blueprint Annex C.2); or two held sources disagree and no held source states a precedence rule (non-delegable); or a material finding notice | a decision recorded in Source Lifecycle, with the deciding Cell's code, the date taken, the date recorded and evidence of a fresh live sign-in; for a listed type, its `signature_ref` from the tool gateway |

Observation of real work is not a type of request. Admitting it would be a decision of GOV (blueprint §13, H-07).

## 5. The fields of a needs request

| Field | Content |
|---|---|
| `request_id`, `version` | stable ID; a changed request is a new version, which supersedes the earlier one |
| `run_id`, `parent_work_item` | the design run and its Work Item |
| `raised_by` | the code of the Pod that raised it (`[ORG]POD-TRR`, `-TS`, `-TEP`, `-TEM`, `-TH`, `-TW`, `-TR`), or of the Chief of Staff (`[ORG]CELL-COSTOM`) for decision-sheet and notice rows |
| `type` | one of the six types |
| `question_plain` | the question in the organisation's language, short, one thing |
| `question_original` | the raising Pod's own wording, verbatim; Source Lifecycle keeps it beside the plain question and records any simplification |
| `asking_form` | the document kind; the explainer template; the confirmation row (the inferred item and the sources it came from); the status row (the source); the export (what, from which system by role, as of which date); or the decision row (the decision and its options); for a confirmation row, its purpose (`row_purpose`: inferred item, understanding check, found not said, assumption or obligation; `ASKING-CATALOGUE.md` §4.1); the decision options include, from v0.4, `reading A`, `reading B`, `both readings`, `same role` and `different roles` |
| `why_it_matters` | one sentence |
| `blocks` | the brief section, child, element or gate the answer blocks |
| `effect_of_answer` | what changes depending on the answer |
| `if_unanswered` | what will be carried instead (an assumption or an unknown) and what that costs |
| `minimality_proof` | the source references searched (at least one), and why none answers |
| `leverage` | breadth, irreversibility and cost of being wrong, each low, medium or high |
| `suggested_seat` | only for a delegable row: the role the held sources suggest can answer, with the citation; never a person's name. The Chief of Staff of `[ORG]AIOC-SL` chooses who answers |
| `non_delegable`, `answering_cell` | `non_delegable` is true only on a decision row that only the Requesting Authority may answer. `answering_cell` is then the Requesting Authority's Cell code; for a row of a listed type it is the code of the Cell that signs that type (for `set-purpose-or-values`, the Cell carrying `[ORG]HOAC-GOV`). Source Lifecycle returns the request if anyone else answers |
| `listed_type` or `org_listed_type` | for a decision of a listed type: it is decided only with a valid signature at the tool gateway |
| `depends_on` | the rows it depends on; a `correct` or `don't know` on one of them returns this row to undecided |
| `pass_id`, `row` | the pass it belongs to and its row number (at most the configured rows per pass; one decision per row) |
| `due` | the planned start date of the step the answer blocks, from the run plan in the run record |
| `missing_report_ref` | the Missing Report sent with its pass |

## 6. States and ageing

**The states are a view over the one status list of Protocol §4.2:**

| Status | Meaning here |
|---|---|
| `received` | sent |
| `in-progress` | accepted by Source Lifecycle, or asked |
| `rejected` | returned by Source Lifecycle, with its reason; withdrawn by this AIOC, with the reason "withdrawn by requester"; or superseded by a new version |
| `done` | answered, declared absent, not applicable, declined, or "don't know"; set only when this AIOC's acceptance test passes (Protocol §4.5) |

The run item shows `needs-input` while any needs request is open. The finer states travel as **needs status** messages (`contracts/needs-status.schema.json`):
- Source Lifecycle sends `accepted`, `returned` and `asked`;
- this AIOC sends `withdrawn` and `superseded`, and Source Lifecycle stops asking on either.

**Rules.**
- **Silence is never an answer.** An overdue request stays open and is reminded, then escalated, under the waiting deadlines; it shows on both Panels. The blocked item is carried as `unknown`, with its cost.
- **Never left open.** After the configured number of passes past their deadline with non-delegable rows unanswered, the step stops as `non-response`. It emits a Readiness Report, or the narrowest honest brief built only from rows already decided (blueprint §5.1).
- **"Don't know" is an answer.** It is recorded and never turned into a yes. On a scope, exclusion, criterion or contradiction row, it keeps the step awaiting decision.
- **A general approval is no answer.** "Looks fine", silence, or approval of a whole pass decides no row. A pass with an uncleared weak-approval signal decides nothing (blueprint Annex C.4).
- **Declared absent** (the document does not exist): the item becomes a named unknown with its owner and date, and Source Lifecycle records it as a gap. An explainer may then be offered.
- **Re-opening.** An answer re-opens only the work that depends on it, never the whole run.

## 7. The answer

An answer is admitted only by reference (`contracts/source-reference.schema.json`):
- **Served today** (Protocol §13, item 4): the source ID, version and SHA-256 hash, and `held` or `not held`, within the approved scope.
- **Asked of Source Lifecycle** (§9): the snapshot ID, the origin kind, the status, the confidentiality level, for an export the date it is as of, and each statement's own label with its anchor.

A pasted or typed answer is refused. An answer that does not resolve the question becomes a new request, never a guess. A `not held` answer is recorded as an unknown with its cost; it is never taken to mean that the fact is absent.

An admitted answer passes the eight checks of blueprint §4.3, and makes a new version of the Input Pack, read at the snapshot the answer names. It re-opens only the work that cites an affected passage.

### 7.1 Mapping from Source Lifecycle

How each value Source Lifecycle serves is read, with the defaults where a value is not served, is fixed in the adapter file, `adapters/source-lifecycle.adapter.md` §5, and checked by its fixtures.

This AIOC assigns its Annex B label on admission. It never reads a label from the reference, and an approved explainer never lifts a statement that Source Lifecycle holds as `inferred` or `assumed`.

## 8. Passes and burden

- At most the configured number of rows per pass (default 12), one decision per row, ranked by leverage. An explainer counts as three rows toward the limit. Rows that only the Requesting Authority may answer are marked and come first in their pass.
- Passes are sequenced: a new pass is sent only when the previous one is answered, or past its waiting deadline (blueprint §15).
- The measure of this intake is not how few questions reach people. It is that every question that does reach them is material and provably unanswerable from what they already hold.

### 8.1 The Missing Report

With every pass, this AIOC sends the Chief of Staff of `[ORG]AIOC-SL` one **Missing Report**, versioned and by reference (`contracts/missing-report.schema.json`). It lists:
1. What was answered from the organisation's own sources: the count and the list, bounded as in §3, item 1.
2. Every open need, grouped by kind (documents, explainers, confirmations, statuses, exports, decisions). Each need shows what it blocks, and what will be carried if no answer comes.
3. What is carried as an assumption without asking, and what that costs.
4. What is past its waiting deadline.

It is written in the organisation's language and names seats, never people. Source Lifecycle shows it to the organisation as "what is missing for your operating model". Its open needs always equal the open entries of the needs log.

## 9. What Source Lifecycle needs for this

Protocol §13 already gives most of it:
- intake for every input and every contributor;
- the contributor agreement, preview and approval;
- statement labels and gap finding;
- connections approved, scoped and revoked by a labelled human seat, through the tool gateway;
- the output socket that answers by reference.

This AIOC needs thirteen additions. They are proposed to Source Lifecycle, not decided here. Gate T0 fails with the reason `SL contract not supported` until Source Lifecycle's card declares them.

| ID | Addition | Acceptance test (one line) |
|---|---|---|
| SL-A1 | **Needs-request intake.** A needs request from a connected part is accepted only as a Work Item on the published, versioned contract, within the part's grant. It is accepted, or returned with a stated reason: malformed, outside the grant, duplicate, asks for a secret, or names a person. A `document` or `export` request becomes a gap; a `confirmation`, `status` or `decision` request is tracked as a question. | A malformed request, a request naming a person and a request for a password each come back `returned` with their reason; a valid `document` request appears as a gap linked to its ID and version. |
| SL-A2 | **Routing.** For a delegable row, Source Lifecycle chooses who answers (the suggested role is advice only). For a non-delegable row, it addresses only the position named in `answering_cell` (the Requesting Authority's Cell, or for a listed type the Cell that signs it), through its HU port; the tool gateway checks that the answering sign-in belongs to a current occupant of that position, and an answer from any other position is refused. Source Lifecycle reads no occupancy entry (Standard §1.1, item 9, proposed by `49GAION/DR-0013`). Every answering sign-in has a current contributor agreement. No occupant's name ever reaches the requesting part. | An answer to a non-delegable row from another position is refused; no occupant's name appears in any needs answer. |
| SL-A3 | **Outcomes and states.** Each request ends as `answered` (by reference), `declared absent`, `not applicable` (asked once), `declined`, `dont know` or `returned`. Every outcome except `answered` carries a reason. The states follow the one status list of the Protocol, and the finer states travel as needs status messages. `done` is set only by the requester's acceptance test. Overdue items follow the waiting deadlines and escalation; silence closes nothing. | Each outcome produces a needs answer valid against the contract; an unanswered request past its deadline is reminded and escalated, never closed. |
| SL-A4 | **Explainer templates as configuration.** Versioned templates (ID, version, questions in order, why each is asked) are configuration, run through preview and approval. The recorded source carries the template ID and version, each statement's label and the approval hash per item. | Adding a template needs no engine change; a recorded explainer carries its template ID and version and per-statement labels; an unapproved item is never served. |
| SL-A5 | **Confirmation, status and decision rows.** One item per row. A confirmation row offers confirm, correct (in the person's own words) or don't know. A status row asks only whether one document is in force, draft or superseded; which of two sources governs is a decision row, never a status row. A decision row shows its options. Each answer is recorded as a source of the matching origin kind, with the deciding Cell's code, both dates and evidence of a fresh live sign-in. Approving a whole pass decides no row; a weak-approval signal is computed per pass and per part. | "Approve all" on a 12-row pass records 0 decided rows; each decided row resolves to one source carrying the deciding Cell's code and both dates. |
| SL-A6 | **Listed-type rows go to the gateway.** A row whose decision is a listed type is never captured in Source Lifecycle's own screens or by its Chief of Staff. The person is linked to the tool gateway's signature surface, and the decision is recorded only with a valid `signature_ref`. | A purpose-and-values row answered without a gateway signature of the GOV Cell stays undecided; with one, the source carries its `SIG-` reference. |
| SL-A7 | **Reference fields.** Beyond ID, version, hash and held or not held, a reference carries: the snapshot ID; the origin kind (document, explainer, confirmation, status, export, decision, operating model, design report); the status from Source Lifecycle's own list; the confidentiality level; for an export, the date it is as of (`as_of`); and, for an item derived from conversation, each statement's label with its anchor. | For one sample of each origin kind, every field is present and matches the record; an export carries its date; an inferred statement in a conversation-derived item is served as `inferred`. |
| SL-A8 | **Snapshot pinning.** A connected part may pin a content-addressed snapshot and read every reference at it for the life of its run, and may read the references named in a needs answer at the snapshot that answer names. A version superseded after the pin is served at the pinned bytes, with its current status shown as `superseded`, never as the valid version. Source Lifecycle keeps every snapshot named by a filed release readable at its pinned bytes for as long as that release, or any release that carries it forward, is not withdrawn. | After a new version is approved, a read at the pinned snapshot returns the pinned bytes with the same hash and a current status of `superseded`; a needs answer recorded after the pin is read at its own snapshot; a snapshot named by a filed release still reads back after its run has ended. |
| SL-A9 | **Filing by a connected part.** A part holding a write scope limited to named origin kinds (`operating model`, `design report`) may file a source, on behalf of a named human Cell whose position has a current contributor agreement. The filed source is content-addressed and records what it supersedes. Its status is set from the approval decision the filing cites. | A filing with no write scope, or with no contributor Cell, is refused; an accepted filing reads back byte-identical, with its status set from the cited decision. |
| SL-A10 | **The organisation-design grant.** The approving seat is the `[ORG]HOAC-ACS` seat that `[ORG]AIOC-SL` is accountable to, signing `connect-external-port` at the gateway, recorded in the unit register. The grant has three parts: unrestricted read; least-privilege write for SL-A9 only; and needs requests. Scope expiry is checked on every read. | A grant made without that seat's gateway signature does not work; a read after expiry is refused; a write outside the named origin kinds is refused. |
| SL-A11 | **Notices to connected parts.** On a revocation, a narrowing of scope, a reclassification or a supersession affecting references a part has read, Source Lifecycle sends that part a notice naming each affected reference and version, never the content. | After revocation, the test part receives a notice naming every reference it read under the grant, and its next read is refused. |
| SL-A12 | **The sockets contract, published.** The needs-request, needs-answer, needs-status, Missing Report and source-reference contracts are versioned JSON Schemas with fixtures. A change names every connected part it affects and re-runs the cross-AIOC test (Protocol §11, item 2). | The contract fixtures pass in CI; a breaking change without a list of affected parts fails the check. |
| SL-A13 | **Records of the work, never about a person** (new in v0.6.0; blueprint Annex H.8). An export of records of the work as it runs (work queues, case logs, workflow and time records) is recorded only as the organisation's projection by role-type and process: the organisation's own mechanism removes who did the work, and any line that would still point to whoever did it; the seat that holds data protection (HF-17) records an impact assessment of the export and its decision on it (where the projection moves personal data, the listed type `export-share-or-purge-personal-data`). It is served as origin kind `export`, with its `as_of` date. | An export offered with a field that says who did the work is not recorded; an export recorded without its impact assessment and its HF-17 decision is not served; an admitted one is served as `export` with its date. |

**The v0.4 decision options.** The options `reading A`, `reading B`, `both readings`, `same role` and `different roles` are a change of the published sockets contract under SL-A12. Source Lifecycle shows them as it shows every option (SL-A5), and declares support for the v0.4 needs-request and needs-answer contracts on its card (gate T0, condition (c)). No new addition is asked.

**The v0.6 sockets contract** (blueprint Annex H.7, H.8). The needs-request contract adds `asking_form.proposed_priority` (on an element row) and `asking_form.aggregation` (on an export of records of the work); the needs-answer contract adds `decision.priority`. Source Lifecycle shows the proposed priority with the row, records the priority decided with the decision, and states the aggregation on the export request. It declares support for the v0.6 contracts on its card (gate T0, condition (c)); with SL-A13, that is the whole change.

*Powered by 49GAION*
