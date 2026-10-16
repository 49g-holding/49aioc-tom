# The output: a TOM Release

**`[ORG]AIOC-TOM` v0.4.0 · draft · 15 October 2026; v0.6.0, 16 October 2026, adds four parts and what the model also states (blueprint Annex H).** Exactly what the Target Operating Model AIOC delivers. The manifest's machine contract is `contracts/tom-release.schema.json`; the filing receipt's is `contracts/tom-filing-receipt.schema.json`.

## 0. What you receive, in plain words

When a run ends well, you receive one package, the **TOM Release**. Read it in this order:
1. **The Decision Package.** In your own language: what the model is, why, what is still unknown, and what you decided. This part is written for you.
2. **For each part of your organisation:** what it must be able to do, how each capability is delivered and how mature it is, how its main work flows and which flows are critical, who decides what (by role, never by name), and where it hands work to other parts and to outside parties.
3. **The hand-offs between parts and with outside parties,** each outside party's journey through your organisation, and the legal questions for a lawyer.
3a. **Your strategy on one page,** as your documents state it or as you decided it; **the value case**: for each change, how it is measured, where it starts and what it aims at; **the priority** of each element; and **how the work runs today**, where you gave records of it.
4. **The role register:** every role in the model, once, with what it decides, what it answers for, and what it hands to whom.
5. **The test against realistic situations,** and the quality checks made at each stage by checkers who did not make the work.
6. **What is still open:** unknowns, assumptions, deferred items, anything you accepted as a known defect, and what is missing.

If only part of the organisation was designed, the release says which part.

It names roles and what each decides. It does not say what fills a role. You can stop here and run the model, carrying each role in a position of your own.

### Glossary

| Term | Meaning |
|---|---|
| Requesting Authority | the seat that asked for the design and decides it |
| Capability | something a part of the organisation must be able to do, whoever does it |
| Value stream | the path the main work takes from start to finish, in a few phases |
| Decision rights | who decides what, by role |
| Role-type | a kind of accountable role, never a person or a job description |
| Role register | every role-type of the model, listed once, with what it decides, what it answers for and what it hands to whom |
| Run depth | how fine the model is: `light` (each part's main capabilities only), `standard` (as fine as your documents support), or `deep` (one level finer where your documents support it, and tested more); you stated it in your design request |
| General pattern | a widely known way to organise, from a published catalogue; it may suggest a structure, but it is never evidence about your organisation |
| Crossing, or interface | a point where work, information or obligation passes between a part and another part or an outside party; each part declares its own |
| Hand-off | a crossing between two parts, paired from both sides: what crosses, each side's obligation and trigger, the role at each end, and the decision on the crossing |
| Counterparty | an outside party, recorded by class (for example regulator, bank, supplier, customer), never designed from its own side |
| Design Brief | the agreed statement of what the design is for: the frame for the whole request, then one brief per part |
| Readiness Report | what is delivered instead of a brief when the evidence cannot yet support one: what was established, what blocks, and what would unblock it |
| Quality checks | for each stage, whether an independent check took place, what it found and what became of each finding |
| Child | a piece of the organisation designed on its own: a whole entity, or a bounded part of one |
| `source-backed` | one of your documents says it |
| `inferred` | worked out from your documents; it may be wrong |
| `organisation-stated` | you said it, in an approved explanation or correction recorded in Source Lifecycle |
| `assumed` | carried without evidence; what breaks if it is false is written beside it |
| `unknown` | not established; why, and whether it blocks, is written beside it |
| Honesty ceiling | the weakest support any important part of the model rests on; it tells you how far to trust the whole |
| Walkthrough | a desk test of the design through realistic situations; not a test of how people really work |
| Deliberately undecomposed | the documents do not show enough to split it further, so the model does not guess |
| Known defect | a material finding you decided to accept and proceed with; it is stated in the release's headline |
| Frozen and content-addressed | every file has a fingerprint; any change is a new release |
| Input Pack | the sealed, numbered set of passages from your documents that the design was made from; an answer or a decision you gave later is added as a new version |
| Strategy frame | your strategy on one page: purpose, values, long-range target, three-year picture, one-year goals with their measures, and critical numbers; each from your documents or your decision, or marked `not given` |
| Delivery model | how a capability is delivered: in-house, as a shared service, outsourced, or by a partner; never who the provider is |
| Make or buy | `make` for in-house or a shared service; `buy` for outsourced or a partner |
| Maturity | how established a capability is, on five levels: ad hoc, repeatable, defined, measured, improving; today's level only from your documents, the target only from your documents or your decision |
| Critical value stream | a value stream marked critical for a stated reason: revenue, customers, legal or regulatory, safety, or continuity |
| Journey | the moments where one outside party meets your organisation, in order; nothing on the party's own side |
| Value case | for each change the design is for: its measures, where each starts and what it aims at, from your documents or decisions only |
| Priority | `must`, `should` or `could`, proposed by a fixed rule and decided by you with each element |
| Activity profile | how the work runs today, by role-type and process, from records you approved; never about a person |
| Organisation dictionary | your own terms and what each means; where you have one, the model uses your words in your meaning |

## 1. In one paragraph

A run delivers one **TOM Release**: the organisation's target operating model, decided element by element by its own Requesting Authority, frozen and content-addressed. For each child in scope, and for the hand-offs between children and with outside parties, it says:
- what capabilities there are;
- how the work flows, at the level of phases;
- who decides what, as accountable role-types, never people, with every role listed once in the role register;
- where it hands work to other children and to outside parties;
- how each capability is delivered and how mature it is, and which flows are critical;
- what is still unknown or deferred.

With them come your strategy on one page, each outside party's journey, the value case, the priority of each element, and how the work runs today where you gave records of it. It says why, with every element traced to the organisation's own sources. It has been walked through realistic situations and independently checked at every stage. It names roles and what each decides. It does not say what fills a role. It covers one slice of the organisation, and says which. The release is filed into Source Lifecycle as a source of origin kind `operating model`. The next stage, Process and Position Design, is told of it at once and reads it there.

## 2. The parts of a release

| # | Part | For whom | Section |
|---|---|---|---|
| 1 | Release manifest | machines and auditors | §3 |
| 2 | Design Brief (frame and child briefs, decided) | the Requesting Authority; every later step | §4 |
| 3 | Decided structure and slice | the Requesting Authority; every later step | §5 |
| 4 | Per child: TOM Blueprint (Output A) | the organisation | §6.1 |
| 5 | Per child: Rationale and Evidence Brief (Output B) | the organisation; auditors | §6.2 |
| 6 | Per child: design ledger (machine-readable) | the next design stages | §6.3 |
| 7 | Hand-offs register | the organisation; the next stages | §7.1 |
| 8 | Counterparty register | the organisation; the next stages | §7.2 |
| 9 | Legal and regulatory perimeter | the organisation's lawyers | §7.3 |
| 10 | Deferred-boundary register | the organisation; the next stages | §7.4 |
| 11 | Seam findings | the organisation; auditors | §7.5 |
| 12 | Role register | the organisation; the next stage, first | §7.6 |
| 13 | Walkthrough report | the Requesting Authority | §8 |
| 14 | Quality checks | the Requesting Authority; auditors | §9 |
| 15 | Decision Package and decision references | the Requesting Authority | §10 |
| 16 | Registers | everyone | §11 |
| 17 | Trace | auditors; the next stages | §12 |
| 18 | Strategy frame | the Requesting Authority; the next stages | §4a |
| 19 | Outside-party journeys | the organisation; the next stages | §7.7 |
| 20 | Value case | the Requesting Authority; the next stages | §10a |
| 21 | Current-state activity profile | the next stages | §11a |

- **Files.** Parts 2-21 are each a file named in the manifest by hash.
- **Run records** are not part of the release: read plans, round logs, the lens record, the party register, child packages, packaging ledgers, gate reports, the pairing table, the walk input, walkthrough hop traces, review records, ruling sheets, the run preview, the two drafts and the difference registers of the Frame and of each part's Design, the lint report and the carry-forward record. They are kept in the organisation's records repository and referenced from the manifest by hash. They hold atom IDs and hashes, never the text of a source.
- **The filing receipt** is kept beside the manifest, never inside it.

## 3. Release manifest

| Field | Content |
|---|---|
| `release_id` | `TOMR-` + SHA-256 of the canonical manifest body without `release_id`. Filing never changes it |
| `org_aion` | the `[ORG]AION` |
| `scope` | the organisation's shape; the committed and context entities; the **slice**: the children designed, those not yet designed, and those withdrawn; the **subject**: the whole organisation, or one unit of it (named) |
| `blueprint_version` | the version of this AIOC that made it |
| `standard_versions` | the 49GAION Standard, Protocol and Library versions |
| `depth` | the run depth: `light`, `standard` or `deep` (§4, frame item 19) |
| `input_packs` | every version of the Input Pack the run read, from P0, each with its snapshots; and those of any carried release |
| `parts` | each part: path, SHA-256, size, and its child where the part is per child; and, for a part carried from an earlier release, that release |
| `run_records` | every run record, by kind and hash; none is a part |
| `release_lint` | the lint result (pass), the deny-list version, and any exemption by part, rule, count and source passages, never the word |
| `carries` | the earlier releases this one carries forward, if any |
| `reference_models` | the catalogue of general patterns read, by version and hash, or `unavailable`; and each pattern used, by its plain name, with the parts it informed and how many elements rest on it alone |
| `decisions` | each decision reference in Source Lifecycle, with its subject, value, deciding Cell, date taken, date recorded, for an element its decided priority, and for a listed type its `signature_ref` |
| `final_status` | `ACCEPT`, or `ACCEPT WITH CORRECTIONS` (before or after the next stage) |
| `honesty_ceiling` | the release ceiling, the per-entity ceilings, and the ceilings of the present state, the outcome and each criterion; each named with its claim and its label distribution; and the reliance on general patterns |
| `known_defects` | any material finding the Requesting Authority accepted as a known defect, with the element and the decision reference |
| `confidentiality` | the highest confidentiality level of anything the release quotes |
| `supersedes` | the release it replaces, or none |
| `attestation` | the reference of the TOM Design Lead's attestation of gates T0-T7 |

**The filing receipt** (`contracts/tom-filing-receipt.schema.json`) records:
- the Source Lifecycle reference of the filed release;
- the Cell it was filed on behalf of;
- the write scope used;
- the final-status decision cited as its approval;
- the status Source Lifecycle set from that decision.

## 4. Design Brief

**The frame** (decided at gate T1). Each row is labelled (blueprint Annex B):
1. Identity and requesting authority, per entity: `committed` or `context`; the evidence of authority to commit; the veto-holders (a co-owner, board, partner or other party). No obligation falls on a context entity.
2. The request as interpreted.
3. Scope in.
4. Named exclusions (or "no material exclusions", with a reason).
5. Present state, with label, standing and source status.
6. Outcomes, as differences from today that two independent readers would judge the same.
7. Criteria the sources state, each with its admissibility result (blueprint Annex C.3).
8. Constraints, hard or preference.
9. Assumptions, with what breaks if false and when to re-check.
10. Unknowns, carried or blocking, with how they might be obtained.
11. Contradictions, with status and what they block.
12. Obligations of the organisation.
13. The Gate A record for the whole request: eight questions with reasons, and the floor.
14. Open items. This is a normal section: an empty table on a non-trivial brief is a warning sign.
15. Evidence basis: sources served, read in full, sampled, not opened; requested and not provided.
16. Honesty ceiling.
17. Version and change control: later steps may extend the brief, never rewrite it.
18. The request kind, with its reason: a reading that may be revised.
19. The run depth: `light`, `standard` or `deep`, as the design request states it, or `standard`.
20. The strategy frame, filed as its own part (§4a).

With the frame, the organisation also answered: whether this is how it reads its own request (the understanding check); whether each finding the sources hold, and the request did not state, was known; and whether each load-bearing assumption and obligation stands. With the frame, the organisation also answered, where two separate readings of its request differed and the documents did not settle it, which reading it meant. Each answer is a source, by reference.

**The child briefs** (decided at gate T3), one per decided child:
- the child's Gate A record and floor;
- its success criteria, as decided by the Requesting Authority. Each names the observable state read, the method (sample, decision rule, window) and a measurer independent of the measured party; states what it is a proxy for, where it is not the outcome itself; can be re-run by a third party; and is frozen at the decision;
- the contradictions decided for it.

**A Readiness Report** takes the place of a child brief whose floor cannot hold, or of the whole brief when no frame can be decided. It contains:
- the current interpretation;
- why it is not a brief (which floor question failed);
- whether a brief is reachable as framed. If it is not, the next step says what the organisation would have to change in the request, and never gives a path to a brief as framed;
- blockers, and who can unblock them;
- missing evidence; contradictions;
- what was established anyway;
- the honesty ceiling;
- the stop reason and the residue;
- the suggested next step.

It is a deliverable, not a rejection slip. It is filed into Source Lifecycle as a source of origin kind `design report`, with the ID `TOMD-` + SHA-256 of its body and a filing receipt. A Held Report, after a CLOSE choice (blueprint §5.8), is filed the same way.

## 4a. Strategy frame

Your strategy on one page, decided with the frame: the purpose; the values; the long-range target; the three-year picture; the one-year goals, each with its measure; the critical numbers, each with its definition. Each element is quoted from your documents, with its label, or marked `not given`, with what was asked and the answer. Nothing here was written for you, and nothing was worked out from other material: what your organisation wants comes only from you. Purpose and values are those of a document in force, or those the Cell carrying `[ORG]HOAC-GOV` signed. The next stage starts its objectives from the goals and the critical numbers.

## 5. Decided structure and slice

- The parent statement.
- Per child: its subject; its boundary in and out; its intended outcome; why it is separable; its dependencies; what it does not deliver without its sibling; its inherited ceiling; the unknowns positioned in it; its startability; the four-leg answers; and the decision reference.
- The orphan mapping table and the exclusion matrix.
- The rejected alternatives.
- The dependency order (an ordering, not a dispatch).
- The slice: the children designed in this release, and those carried from an earlier release.

## 6. Per child

### 6.1 TOM Blueprint (Output A)
- **A0 Framing.**
- **A1 Entity type used**, with provenance, confidence, basis and what would change it.
- **A2 Capability map.** Each capability with its description, provenance, confidence and basis. A capability whose finer shape the evidence cannot tell apart is shown "deliberately undecomposed"; the candidates for its finer shape appear only in the brief, never here. How fine the map is follows the run depth (§3, `depth`): at `light`, each part's main capabilities only; at `deep`, one level finer where the documents support it. Where a general pattern suggested part of the map, it is named, and each element that rests on it alone is marked as an assumption.
- **A2, also**, for each capability: its **delivery model** (`in-house`, `shared service`, `outsourced`, `partner`, or `not decided`), never naming a provider, with the crossings that deliver it where it is not in-house; its **make or buy**; and its **maturity**, today's level and the target, each with where it comes from, or `unknown` and `not set`.
- **A3 Value streams**, at capability-level phases only, each phase labelled. A stream ends at its boundary crossing. A stream that cannot be described locally is marked `interface-dependent`. Each stream is marked **critical** or not; a critical stream names its reasons (revenue, customers, legal or regulatory, safety, continuity), each with its sources.
- **A4 Decision rights and governance skeleton**: decision domains, accountable role-types and interfaces. No policy text, no meeting cadence, no procedure.
- **A5 Expected interface map**, in two separate parts: **stated interface points**, which are authoritative; and **inferred or unresolved interface candidates**, which are not authoritative and satisfy no dependency.
- **A6 Run status**: `complete`, with the stated reason why the grain is enough; or `incomplete-design`, naming the element and the missing fact-type.

### 6.2 Rationale and Evidence Brief (Output B)
- B1 why this structure.
- B2 evidence ledger: claim, label, confidence, atom references, reasoning, what would flip it.
- B3 classification basis and flip conditions, and any general pattern considered.
- B4 alternatives rejected, and why.
- B5 non-authoritative candidate structures; where the two separate designs differed and the documents did not settle it, both versions.
- B6 assumptions, unknowns and limitations, including each element resting on a general pattern alone.
- B7 demand signals, by type only.
- B8 revision record, with no verdicts.
- B9 what future evidence would change the design.
- Run statistics, computed by the renderer.

### 6.3 Design ledger
The machine-readable record both outputs are rendered from. Every element has its ID, type, claim, provenance (`stated`, `inferred`, `unresolved`, or `assumed` where it rests on no passage of your documents), confidence, basis references and class (`authoritative`, `candidate`, `narrative`); where a general pattern informed it, the pattern and the catalogue version. A decision domain names its decision and its accountable role-type. A capability carries its delivery model, make or buy, the crossings that deliver it, and its maturity now and target; a value stream carries whether it is critical, and why. The next stages read the ledger. An entry of class `candidate` or `narrative` is never consumed as designed content.

## 7. Hand-offs and outside parties

There is no model of the whole beyond the children and the hand-offs between them: no capability, value stream, decision domain or body above the children. A shared service is a hand-off like any other. A relationship between independent entities is never a body above them.

### 7.1 Hand-offs register
One entry per clean pair of crossings between two children, including two children of one entity: what crosses; the direction; each side's obligation and trigger; the accountable role at each end; the decision on the crossing and the role that takes it, as one field; its support and sources. Where the release has one child, the register is empty and says why, and §7.2 to §7.5 still apply.

### 7.2 Counterparty register
Every outside party, by class, for every shape of organisation: what crosses, the obligation and trigger on the child's side, and the role. The far side is never designed. A class the sources are silent on, but that the organisation's shape normally has, was asked about.

### 7.3 Legal and regulatory perimeter
Each item listed and flagged for human legal review. Each item names the part of the organisation, the matter, its kind, its sources and the question for legal review. Nothing is decided by this AIOC.

### 7.4 Deferred-boundary register
Every boundary class not yet designed, with its durable ID, its evidence by atom, the run that surfaced it, the reason for deferral and its destination. Nothing is dropped.

### 7.5 Seam findings
Every crossing that did not pair, or paired with a contradiction, and how it was resolved: upstream, by decision, or by registration. None was bridged.

### 7.6 Role register
One entry per role-type named anywhere in the release: what it decides; what it is accountable for; where it appears, by part and element; and the hand-offs it sends and receives, with what crosses. It is built by a code check from the decided designs and registers, never written by hand. It lists roles only: never a person or a position. Two names are one role only where you decided so. Where roles conflicted (one role named two ways; one decision held by two roles; a decision with no role; a hand-off with no role at one end), the conflict and how it was settled are listed. The next stage reads this part first: positions and job descriptions are made from it.

### 7.7 Outside-party journeys
For each outside party of the counterparty register, its journey: the moments where it meets your organisation, in order, each a crossing already in the counterparty register, with the value stream and phase it meets. The order is as your documents state it, or `order not stated`. Nothing is designed on the party's own side, and no crossing is added: a moment your documents describe that no crossing carries was routed back as a seam finding. Each journey was decided with its counterparty class.

## 8. Walkthrough report

- What the walkthrough is and is not: a test of the design, not evidence about operations.
- How to read the findings.
- The headline result by class. A reduced-catalogue walk says "reduced: value streams not walked" here. Any accepted known defect is stated here.
- What was walked; the situations and why that set; whether the situation mix was met, or its shortfall.
- Where the model closes; where it stops; what it cannot honestly determine.
- Every finding, with what would be needed to close it (the gap, never the fix).
- What was refused, and why.
- Coverage, with named gaps; the termination profile.
- The fixed identities that reproduce the report: the model, the situation set and the rules, by hash.
- After a correction: the sealed closure test, and the regression result against the earlier failures.
- In a continuation: every earlier failing situation, re-run as regression, with its result.

## 9. Quality checks

For each stage, one short section:
- whether an independent check took place (`done`), or a check that was not fully independent of the authors (`reduced`), in which case it reads exactly: "The checks at this stage were not fully independent of the authors.";
- for the Frame and for each part's Design: whether the work was written twice, separately, and compared (`done`); where it was written once, it reads exactly: "The work at this stage was written once, not twice independently.";
- for each part's Design: each general pattern used, by its plain name, with how many elements it informed and how many rest on it alone, and then exactly: "A general pattern suggested part of this design. It is not evidence about your organisation; each element that rests on it alone is an assumption, listed with what breaks if it is false.";
- each finding on the operating model: material or minor; what it was about; and what became of it: corrected, withdrawn, accepted by you as a known defect, dismissed by ruling, or open;
- each ruling of the TOM Design Lead on a disputed finding, with its reason.

One more section covers the questions put to your organisation. The quality checks say nothing about how the checks were made. The full records of every check are kept in the organisation's records repository and named in the manifest by hash.

## 10. Decision Package and decision references

**The Decision Package** (blueprint §5.9) contains:
- an executive summary;
- for each element: its purpose, what it owns and does not own, why it exists, and its main evidence;
- value streams in plain language;
- the decision model;
- the boundary as inside, outside and deferred, visibly separated;
- the rationale;
- the open items in five blocks: A, evidence gaps; B, instrument gaps; C, deferred cross-child scope; D, remaining design uncertainty; E, items needing a decision now. Only E asks anything;
- the missing-evidence signal, in plain words;
- risks and limitations;
- the walkthrough summary;
- findings of the quality checks, only where they help the decision, never wording hygiene;
- the elements carried from an earlier release, listed apart, as decided in that release;
- the sources superseded since they were read, and what rests on them, in plain words;
- how fine the model is (the run depth), in plain words, and where your documents stopped a part earlier;
- the general patterns used, and each element that rests on a pattern alone, with what breaks if it is false;
- the role register in plain words, with each role conflict and how it was settled;
- the strategy frame, with each element `not given`;
- each capability's delivery model and maturity, and each critical stream with its reasons;
- each outside party's journey;
- the value case (§10a);
- how the work runs today, or that no record of it was given;
- each element's proposed priority, and the rule that gave it;
- the number of rows and passes the decision will take.

Every statement in the package traces to a reviewed part of the release and claims no more than that part (checked before any decision row is sent).

**The decision references** are those, in Source Lifecycle, of every decision taken on the package:
- the strategy frame, decided with the frame;
- per element, `ACCEPT`, `CORRECT` with comment, or `REJECT`, with its priority (`must`, `should`, `could`): the proposed priority on `ACCEPT`, yours on `CORRECT`; each role of the role register is an element;
- the value case;
- the final status;
- the purpose-and-values rows signed at the gateway by the Cell carrying `[ORG]HOAC-GOV`;
- any choice on a material finding notice;
- your answers on two readings of your request, and on two names for one role.

## 10a. Value case

One entry for each outcome of the frame: the change, as the outcome states it; its measures, which are the criteria you decided and the critical numbers of your strategy frame; for each measure, where it starts (the baseline, from your documents, with its date, or `unknown`) and what it aims at (the target, from your documents or your decision, or `not set`); the elements it rests on; and the assumptions it rests on, each with what breaks if it is false. It is put together by a code check from the decided parts and your decisions, and holds no figure that is not quoted from your documents or decided by you. You decided it as one row, and you could set a target by correcting it. The stage that carries the model into your organisation starts its register of value from it.

## 11. Registers

| Register | Each row holds |
|---|---|
| Needs log | the request (by its ID; never its raising unit's code), its type, pass and row, its versions, its state history, its answer reference |
| Missing Reports | one per pass, by reference |
| Unknowns | the unknown, carried or blocking, why the sources cannot answer it, how it might be obtained, what would resolve it |
| Contradictions | both sides with their sources; status; how it was resolved; the precedence source; impact if wrong; decisions blocked |
| Assumptions | the assumption, what breaks if false, the re-check trigger |
| Open items | the item, which later stage will likely own it, why it was not resolved here |
| Demand signals | the missing capability or fact-type, by type only, and what raised it |
| Known defects | the finding, the element, the decision that accepted it |
| Superseded since read | the source and version, the date it was superseded, the elements resting on it |

## 11a. Current-state activity profile

How the work runs today, where you gave records of it: for each role-type and each process, as your records name them, the share of time or the volume your records state, with their date. The records were exported from your own systems by role-type and process, with nothing that says who did the work; your organisation approved each export, after its data-protection review, before it was recorded in Source Lifecycle. The profile describes today. It designs nothing and sets no workload. Where you gave no such records, it reads `no observation`, and nothing is put in its place.

## 12. Trace

Every element of every Blueprint, of the hand-offs register, of the counterparty register and of the role register traces to:
- its ledger entry;
- its basis entries;
- the source passages (atoms, by ID and hash) those rest on, and the Input Pack version that holds each, with its snapshot;
- where a general pattern informed it, that pattern, with the catalogue version and hash;
- the decision that accepted it.

A code check confirms that no element is orphaned, and that every cited passage still resolves by hash at its snapshot, in an Input Pack version of this run or of a carried release. A code check also rebuilds the role register from the decided parts and confirms that it is the same.

## 13. What a release is not

- Not a job description, a position list, a workload, a process manual, a policy, a choice of systems, or an assignment of work to anything other than an accountable role. Those are later stages, and each is a product in its own right.
- Not evidence that the model works in practice. The walkthrough tests the design, not operations.
- Not a record of how any person works. The activity profile is by role-type and process only.
- Not a legal determination.
- Not final for ever: a change is a new release that supersedes it.

## 14. How the next stage uses it

- **The next stage**, Process and Position Design, is told of each decided release at once, by a release notice that names it by reference. It reads the filed release from Source Lifecycle: the role register first, and the design ledgers as its machine input.
- **Returning a release.** Process and Position Design, and Delivery and Implementation after it, return a release only by naming the parts and elements it concerns, using one of: accepted · cannot use, missing X · contradiction found · assumption invalid · request kind unsupported. A return comes back to this stage directly and is put to you. It never changes the release. It ends in one of four ways: answered by a new release; answered by your decision; set aside by your decision and carried forward as a known defect or a decided assumption; or withdrawn by the stage that sent it. Each round has a deadline; past it, the return comes to you for a decision. None is left open.
- **What the next stages start from.** Process and Position Design starts its objectives from the strategy frame, designs the critical streams first, gives a capability that is outsourced or delivered by a partner a hand-off to the outside party, reads the activity profile as today's workload, and orders its work by priority. Delivery and Implementation starts its register of value from the value case.
- **The next slice.** It is designed in a continuation run that carries this release forward: its decided parts are kept by hash and not asked again; only the children named for change, or whose sources changed, are designed again. The new release supersedes this one and contains every slice designed so far.
- **Used on its own.** The release names accountable role-types and what each decides. An organisation may stop here and carry each role in a position of its own.
- **Smaller stops.** An organisation may also stop after the decided Design Brief, or take a Readiness Report on its own. Each is filed into Source Lifecycle.

*Powered by 49GAION*
