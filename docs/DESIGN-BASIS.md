# Design basis: why each rule of `[ORG]AIOC-TOM` is here

**`[ORG]AIOC-TOM` v0.4.0 · draft · 15 October 2026; v0.6.0, 16 October 2026, adds §9a.**

This register says, for every rule of `[ORG]AIOC-TOM`, why it is here, where the blueprint states it, where its full text is, and which case of TEST-TOM v5 checks it. Each rule either comes from an earlier organisation-design chain (and is then marked kept, changed, moved, restored or dropped) or is new in this AIOC. The earlier chain is described here only generically. The private register that maps each rule to the earlier texts, their versions and the decision records behind them is kept in the organisation's code project (`docs/LINEAGE.md` there), and the earlier texts themselves are kept unchanged there under `legacy/`. Nothing in this file needs those texts: the full text of every carried rule is in `docs/CARRIED-RULES.md`. The earlier chain is a case study: blueprint §0. No earlier test result or run outcome is given here as a reason.

**Marks:** **kept** (carried as written, adapted only in wording) · **changed** (carried with a stated change) · **moved** (now held by another AIOC) · **restored** (not carried in v0.2.0, carried again in v0.3.0) · **kept, split** (one half carried here, the other held by another AIOC) · **dropped** (not carried, with the reason) · **new** (not in the earlier chain).

**Columns:** *Here* is the section of `blueprint/TOM-BLUEPRINT.md`. *Rule text* is the section of `docs/CARRIED-RULES.md`; "—" means the blueprint states the rule in full. *Test case* is the case number in TEST-TOM v5 (`tests/TEST-TOM.md`); "—" means no case covers it yet.

---

## §0 The seven earlier capabilities, and where they went

| Earlier capability | What it did | Where it is now | Mark |
|---|---|---|---|
| Requester stewardship | captured the request; talked to the person asking; carried every question and decision between the design steps and people | split: the Chief of Staff of `[ORG]AIOC-SL` does all asking of people and records the answers as sources; this AIOC captures the request (§5.1), tracks what is missing (§5.2) and carries the decision rows (§5.9) | **kept, split** |
| Request reconstruction | reconstructed the request as completely as the captured material allowed, before any burden on a person | Pod `[ORG]POD-TRR` Request Reconstruction (§5.1) | kept |
| Commission decomposition | proposed the children of a decided request, without designing them | Pod `[ORG]POD-TS` Structuring (§5.3) | kept |
| Entity work packaging | prepared an isolated package of one entity's own evidence, with every crossing declared and every counterparty anonymised | Pod `[ORG]POD-TEP` Entity Packaging (§5.4) | kept |
| Single-entity design | designed one entity's architecture-level operating model together with its rationale | Pod `[ORG]POD-TEM` Entity Model Design (§5.5) | kept |
| Cross-entity assembly | mandated to join the entity models and handle every outside relationship; never designed | Pod `[ORG]POD-TH` Hand-offs (§5.6) | kept as a mandate, narrowed to the hand-offs (`decisions/DR-0002`); **new** as a design |
| Operational walkthrough | walked a model structurally through realistic situations | Pod `[ORG]POD-TW` Operational Walkthrough (§5.7) | kept |

The gates, the sufficiency standard, the evaluator's questions (restored: §5.8; `CARRIED-RULES.md` §11.1) and the decision rules that joined the first three capabilities are carried into Annex C of the blueprint and §5.1, §5.2, §5.8 and §5.9 (below, §1, §2 and §8). The standing doctrines of the earlier chain are in §9.

---

## §1 Reading and asking

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Only one seat talks to people; every other capability reaches a person only through it | Asking from several places multiplied the burden and lost track of what had been asked | **moved**: to the Chief of Staff of `[ORG]AIOC-SL` | §4.2; §5.2; §11 item 1 | §1.4 | 13 |
| This AIOC asks no person anything about the organisation; its only human contact is its Design Lead, about the run | Spoken words cannot be the basis of an operating model (the direction recorded in `decisions/DR-0001`) | new | §4.2; §11; Annex D 1 | — | 13, 29 |
| Nothing that arrives through a human port is a source; a run request is admitted only as a Design Request reference | Words typed or spoken to the AIOC cannot be traced or re-checked | new | §4.3 | — | 2, 29 |
| Sources only by reference (ID, version, hash), through an adapter | One home for each source; a run can be re-checked by hash | new | §4.3; §7 | — | 1 |
| The Input Pack: one versioned, content-addressed object; the engine reads nothing else | One sealed input makes every step re-checkable by hash, and every answer visible as a new version | new | §4.3; Annex E.1 | — | 44, 49, 51 |
| Atomising and labelling once, in the socket | Labels need atoms; one place to assign them gives each passage one label | new (moved from Packaging) | §4.3; Annex B.1 | §7.1 | 45 |
| The pack report | What the pack covers and lacks is known before framing | new | §4.3; Annex E.1a | — | 46 |
| One adapter file per source type, read only | A new source type must change no stage | new | §4.3; Annex E.2 | — | 47, 48 |
| Answers make new pack versions; a re-base only by decision | Answers arrive after the pin; a silent re-pin would change what earlier steps read | new | §4.3 | — | 49, 50 |
| Answer by reference only; an answer that does not resolve the question becomes a new request | A typed answer cannot be traced; a guess launders a gap | new | §4.3; §5.2 steps 9, 10 | — | 11 |
| The eight-check acceptance test of a needs answer | `done` must mean a checked answer | new | §4.3 | — | 11 |
| The run preview | The Design Lead knows the level and cost of the checks before work starts | new | §4.2 step 2; Annex E.13 | — | 81 |
| Read before asking; a question a held source answers is waste | The organisation is not the memory of its own documents | kept | §5.1 step 1; §5.2 limits | §1.1 | 8 |
| The read plan is declared before reading; unopened material is never treated as read; no claim may cite a source the read plan marks as not opened | Without a declared plan, coverage is claimed rather than shown | changed: the plan is always declared, not only when the sources exceed what can be read; "never treat unopened material as read" is carried as a rule | §5.1 step 1; §5.1 limits | §1.1 | 8 |
| The selection basis of the read plan carries its own label | The sources' own markings are claims, not facts | kept | §5.1 step 1 | §1.1 | 8 |
| Coverage adequacy is judged independently; declared narrow coverage is no defence | A run can make its work easy by reading little | changed: judged at RP1 under the Review Panel rule | §5.1 step 11; §5.8 | §1.1 | 15 |
| Currency screen: recency is never authority; presence is never adoption | A newer or present document is not thereby in force | kept | §5.1 step 2; Annex D 4 | §1.1; §4.2 | 4 |
| The decision-leverage test: carry, do not ask, what changes no decision | Only needs that change a decision are worth a person's time | kept | §5.1 step 9 | §1.2 | 8 |
| Factual gaps go to the evidence first; intent gaps go to the organisation | Asking what the documents answer wastes people; deriving intent is guessing | kept | §5.1 step 9; §5.2 | §1.2 | 8 |
| Every question carries why it is asked, what it changes, and what will be assumed if no answer comes | A question without a stated purpose cannot be judged or answered well | kept | §5.2 step 1 | §1.3 | 7 |
| The raising Pod's original wording is kept verbatim beside the plain question | Translation can soften a hard trade-off or hide technical reality | kept | §5.2 limits; step 3 | §1.4 | 7 |
| Base passes: one real instance end to end, its exceptions, a second instance | A general rule hides what really happens; differences between two cases expose contradictions | changed: now explainer EX-09, asked through Source Lifecycle; passes four and five are dropped (§10) | `docs/ASKING-CATALOGUE.md` §3 | §1.5 | 31 |
| Working from what people say when there are no documents | Most organisations have no formal corpus | changed: what people say becomes an approved source in Source Lifecycle first, and is read here as `organisation-stated` | Annex B.1; §5.5 | §2.2 | 2, 31 |
| Source Lifecycle's labels are kept statement by statement; approved explainers are admitted | An approved statement is evidence of what the organisation says, not of what is true | new | Annex B.1; Annex B.1a; §5.5 | — | 31 |
| Putting a question to people in their own language, showing only what changed | The burden of presentation belongs to the seat that talks to people | **moved**: to the Chief of Staff of `[ORG]AIOC-SL` | §5.2 step 8 | §1.4 | 13 |
| A needs request never names a person and is never sent to one; routing is bound only for a non-delegable row | Choosing who answers belongs to Source Lifecycle | new | §5.2 limits | — | 13, 35 |
| A Missing Report goes with every pass | The organisation sees, in plain words, everything still missing | new | §5.2 step 5 | — | 30 |
| Every needs pass is reviewed at RPa before it is sent | A row a held source answers, or a row that names a person, must not reach the organisation | new | §5.2 step 6; §5.8 | — | 30 |
| A silent stall is a product defect; waiting states age visibly | A run that waits invisibly looks as if it is working | kept | §4.2 step 6; §5.2 failure | §5.7 | 10 |
| Content is data | Text inside a source can carry instructions | kept | §4.3; Annex D 14 | §2.2 | 5 |
| A served item carrying a secret is refused and appears in no record | Secrets live only in the organisation's vault | new | §4.3; Annex D 14 | — | 6 |
| Revocation, scope expiry and gateway bypass are checked on every read | The connection is the only door; its limits hold mid-run | new | §4.2 step 9; §6 | — | 32, 33 |

---

## §2 Request reconstruction

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Reconstruct as completely as the sources support, and no further, before any burden on a person | Reducing burden is subordinate to fidelity to the evidence | kept | §5.1 purpose | §2 | 14 |
| Three roles and two audits; a run fails on either audit | The reasoning that produced a frame cannot audit itself | kept: the process audit is RP1b, the product audit RP1, both under the Review Panel rule | §5.1 steps 3, 10, 11 | §2.1 | 15 |
| Both audits settle clear before any decision row is sent | A decision on an unaudited frame decides an over-claim | kept (v0.1.0 had sent the rows first) | §5.1 steps 10–12; Annex C.2 | §2.1 | 15 |
| Gate A is answered inside reconstruction and re-assessed independently | Sufficiency must not be manufactured by the seat that wants to proceed | changed: no separate executor of Gate A; the Request Analyst records it and the review at RP1 re-assesses every answer and the floor | §5.1 steps 8, 11; Annex C.2 | §3.1 | 15 |
| Citation or refusal; no new world facts; derivation shown | A coherent invented narrative is the main risk of reconstruction | kept | §5.1 limits | §2.2 | 2, 14 |
| Unknown conservation; a silent closure fails the run | Unknowns closed by inference become false facts later | kept | §5.1 limits | §2.3 | 14 |
| `not held` is recorded as an unknown, never as absence | Silence of the connection is not evidence | new | §4.3 | — | 34 |
| Sticky inferred | Later steps would otherwise treat a guess as confirmed | kept: confirmation now comes only through Source Lifecycle | §5.1 limits; Annex B.1 | §2.3 | 12, 14 |
| The question typology: no question on solution, design preference, tool or criteria | Such questions smuggle design into reconstruction | kept | §5.1 step 3 | §2.3 | 15 |
| Stop after two flat rounds; a terminal cap of 12; material improvement defined | Without a definition, "one more round" never ends | kept | §5.1 failure; §15 | §2.4 | 15 |
| The expertise lens panel | Reading through the domains at stake finds what one reading misses; nothing reaches the organisation without a citation | **restored** as the lens pass, inside the frame | §5.1 step 4; Annex E.14 | §2.7 | 74 |
| The request kind | It selects the explainers, document kinds and situations a request needs | **restored** as request kinds, as configuration | §5.1 step 6; `docs/ASKING-CATALOGUE.md` §3b | §2.8 | 73 |
| The party register | Every name of every party must be known before identities are replaced | new | §5.1 step 6; Annex E.3 | — | 83 |
| The set of needs for people, each with its leverage proof | Only needs that change a decision reach people | changed: the set becomes needs requests to Source Lifecycle | §5.1 step 9; §5.2 | §1.2; §1.3 | 8 |
| The do-not-ask list is bounded | An unbounded list inflates the burden-spared figure shown to the organisation | kept (v0.1.0 had gone back to an unbounded wording) | §5.1 outputs, measures | §2.5 | 8 |
| The do-not-use-as-fact list | Weak items must not become facts later | kept | §5.1 outputs | §2.5 | 14 |
| Honest emptiness | A thin result is not a failure; padding is | kept | §5.1 measures | §2.5 | 8 |
| Reconstruction is kept apart from mapping | A consumer contract would bend the reconstruction toward what the consumer wants | kept | §5.1 limits | §2.6 | — |
| Labels, their order, and standing; a confirmation recorded apart from the label | Confirming an inference must never lower the ceiling | changed: the organisation's statements are `organisation-stated`; `observed` is reserved; a draft, in-review or not-yet-in-force source caps at `inferred`; a confirmation never lowers a label | Annex B.1 | §2.2; §2.3 | 4, 12 |
| No label laundering; evidence of the destination's class; changes of scope of a claim recorded | A label that rises by repetition is the commonest silent defect | kept | Annex B.1; Annex D 3 | §2.2 | 4 |
| Load-bearing by default, with a recorded reason for any exception | Two earlier definitions each covered cases the other left out | kept (both lists combined) | Annex B.3 | — | 15 |
| Honesty ceiling: the weakest load-bearing label, per committed entity; context entities stated separately | The ceiling must show the weakest point, never an average | kept | Annex B.3 | §4.1 item 16 | 15 |
| Gate A: the eight questions with reasons, and the floor | "Sufficient" means a later step can start responsibly | kept | Annex C.3 | §3.1 | 15 |
| S1 standing: committed or context; veto-holders; no obligation on a context entity | Authority to commit must be shown wherever someone could veto | kept | Annex C.3 | §3.1 | 15 |
| Admissible criteria | A criterion that the decider judges is a satisfaction score, not a measure | kept | Annex C.3 | §3.2 | 15 |
| Contradiction precedence: a cited rule from a held source, or a decision for this brief only; a shared-source row is not closed by decision; a decision for a draft upgrades nothing; the losing side stays | Deciding which source governs must not change the standing of the sources beyond this brief | kept | Annex B.2 | §4.2 | 15, 35 |
| Which source governs is a decision, never a status question | A status record says what is in force, not which of two sources governs | kept (v0.1.0 had routed it as a status request) | Annex B.2; Annex C.4 item 8 | §4.2 | 35 |
| The Design Brief's sections; the Readiness Report | The brief is a starting contract; the report is a deliverable, not a rejection slip | kept, adapted to a design brief | §5.1; `docs/OUTPUT.md` §4 | §4.1; §4.3 | 15 |
| Not reachable as framed: the next step says what to change in the request, never a path to a brief as framed | A path to an unreachable brief misleads | kept | §5.1 failure; `docs/OUTPUT.md` §4 | §4.3 | 15 |
| The return vocabulary of a later stage | A return is a learning input, not a complaint | kept, with `request kind unsupported` restored beside it; a return is filed as a source and re-enters through a new run | `docs/OUTPUT.md` §14; §5.9 | §4.4 | 27 |
| Findings offered as new | The organisation sees what its sources hold that its request did not say | **restored** as "found, not said" confirmation rows through Source Lifecycle | §5.1 step 12 | §4.5 | 75 |
| The organisation's own verdict on how well its request was understood | The organisation confirms or corrects the reading of its request, through Source Lifecycle | **restored** as the understanding-check confirmation row | §5.1 step 12 | §4.5 | 75 |
| Gate B of the case study, mapped | Its parts are carried; its two delegable parts are restored as confirmation rows | kept, mapped; two parts restored | §5.1 step 12; Annex C.4 item 9 | §4.5 | 76 |
| An independent evaluator of the brief, with its question set and verdicts | Its questions serve the job; the Review Panel asks them | **restored** as the question set of RP1 and RP3; no separate capability | §5.8 | §11.1 | 72 |
| A run starts only on an approved Design Request, through gate admission | A run needs a defined, approved request to start | new | §4.2 step 1; §4.3; Annex C.2 | — | 3 |
| The TOM Design Lead is not a source, and its Cell is never the Requesting Authority's Cell | The seat that runs the method must not also decide the design; two positions are two parties, and who occupies them is never read (`49GAION/DR-0015`) | new; reworded in v0.5.0 | §2.1; §4.3; Annex C.2 T0 (d) | — | 29 |

**Gate B, mapped.** The source is the case study's interpreted-request gate (Gate B): the requester's item-by-item decision gate on the interpreted request. It maps to nothing removed:

| Gate B part | Carried as |
|---|---|
| Part 0, decomposition proposal (non-delegable, before the parent's Gate A) | the S2 structure rows; gate T2; decomposition before the parent floor (`CARRIED-RULES.md` §3.1, §6.10) |
| Mandatory header: Gate A record; the floor; "if the floor fails, the template is void" | Gate A at T1 and T3; no pass is sent with the floor failed (`CARRIED-RULES.md` §5.7 item 6) |
| Part 1, what you are asking (non-delegable) | the frame's non-delegable rows: scope, exclusions, roster (T1) |
| Part 2, what this means in practice (delegable) | **restored**: the understanding-check confirmation row and its consequences (`CARRIED-RULES.md` §4.5) |
| Part 3, how we will know (non-delegable) | the S3 criteria rows (T3; Annex C.3) |
| Part 4, assumptions, unknowns, obligations (delegable) | **restored**: delegable confirmation rows for load-bearing assumptions and obligations (`CARRIED-RULES.md` §4.5) |
| Part 5, what your documents disagree about (non-delegable) | contradiction rows (Annex B.2; Annex C.4 item 8) |
| Honesty ceiling | Annex B.3 |
| Approval record: meaning shown verbatim; per-part weak approval; global assent as non-approval; delegated items; dissent; Gate A re-runs | `CARRIED-RULES.md` §5.1 item 4; §5.2; §5.3; §5.5; §5.6; §3.1 floor item 4 |
| Two authors write the frame, blind; code compares; a reconciler settles only on the sources or puts the reading to the organisation | One author's reading of a request has blind spots that another, independent reading finds; the differences are kept visible, never averaged | new (v0.4.0) | §5.1 steps 1–9, 9a, 9b; Annex G | §2.1 item 7 | 92–95 |

---

## §3 Structuring

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Structure the work, never the solution | Design smuggled into structure escapes review | kept | §5.3 | §6.1 | 16 |
| The child description holds subject, boundary in and out, and intended outcome, and nothing else | Any other content is design | kept | §5.3 limits | §6.1 | 16 |
| Axes from evidence; citation discipline extends to child titles | An uncited axis is the structurer's preference | kept | §5.3 step 1 | §6.1 | 16 |
| The four-leg test, with "owner role"; the smallest passing set wins | Prevents fragmentation; "owner role" keeps the test to roles, never to who fills them | kept | §5.3 step 2 | §6.2 | 16 |
| An attempted-split table for a single child; a vague "inseparable" note fails the run | Prevents a monolith by default | kept | §5.3 step 3 | §6.3 | 16 |
| The orphan check and the exclusion check, shown | Silent dropping of scope; silent crossing of exclusions | kept | §5.3 step 4 | §6.4 | 16 |
| At least one rejected alternative | Anchoring on the first structure | kept | §5.3 step 5 | §6.5 | 16 |
| Ordering is not dispatch; a live cycle fails | An ordering that starts work bypasses the decision | kept | §5.3 step 6; failure | §6.6 | 16 |
| Per-child acceptance; a rejected child returns as an issue; a dependent sibling is not startable | Each child is a separate commitment | kept, decided in Source Lifecycle | §5.3 step 8; states | §6.7 | 16, 35 |
| A contradiction touching a child's boundary, ownership or startability holds that child | Starting on a contested boundary builds on sand | kept | §5.3 limits | §6.7 | 16 |
| Coordination between independent entities is named as relationships, never as a governing layer | A coordinating child can read as a new body over autonomous entities | kept | §5.3 limits; §5.6 limits | §6.8 | 16, 42 |
| An entity aligned to a group platform keeps its operational autonomy | Alignment must not turn an entity into an internal function of the platform | kept, generalised; how the alignment is delivered is a hand-off like any other (`decisions/DR-0002`) | §5.3; §5.6 | §6.8 | 16, 65 |
| The loop cap of 8 | Bounded rounds | kept | §5.3 failure; §15 | §6.9 | 16 |
| Decomposition before the parent floor; the floor per child; the paired set of briefs and reports | Otherwise a request too large for one brief could never be designed | kept (v0.1.0 had made Structuring wait for a decided parent brief) | §5.1 steps 13–15; §5.3 trigger | §3.1; §6.10 | 15, 16 |
| No narrowing by this AIOC alone | Shrinking a large request alone takes the decision from its owner | kept | §5.3 | §6.10 | 16 |
| Demand signals by capability type only, never sequenced | Naming a missing capability is not designing it | kept | §5.3; §5.5 outputs | §6.1 | 16 |
| Child, not entity: a child is a whole entity or a bounded part of one | One entity may be split into children whose crossings still need pairing | new | §5 ("Child, not entity"); §5.6 | — | 42 |
| The first slice | A large request needs an honest first slice; the earlier chain removed sequencing because it slid into dispatch | new: brings back a sequencing proposal that the earlier chain had removed; it binds only as a decision row, and the dependency order stays an ordering; the next slice is a continuation run | §5.3 steps 6, 8; §5.9 | §6.11 | 16, 69 |
| The party register is extended with the sibling children | A sibling is a party whose name must be swept before packaging | new | §5.3 step 6; Annex E.3 | — | 83 |

---

## §4 Packaging

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| The child package is the only thing the Designer sees | A designer who sees the far side designs it | kept | §5.4 | §7.1 | 17 |
| Six sections; the seven-field register; closed vocabularies; the completeness flag | Crossings become data that code can check at both ends | kept | §5.4 | §7.1 | 17 |
| Per-field provenance; one `unresolved` entry for a contested crossing | A strong crossing must not lend its strength to a weak obligation | kept | §5.4 | §7.1 | 17 |
| Rules 1 to 12 (no far side; four disclosure cases; class not name; crossing completeness; no design judgement; contradictions preserved; verbatim evidence; deterministic anonymisation; one child per job; no contact or research; stop as `incomplete-package`; no self-certification) | Isolation without declaration blinds the designer; declaration without isolation leaks the far side; the two are one rule | kept | §5.4 limits; Annex D 7 | §7.2 | 17 |
| Disclosure: the exact bar for a regime (its concrete internal requirements quoted; the regime disclosed, not the organisation); the per-run declaration; coherence is never a ground | A decorative mention of a regulator is not a requirement; the stable marker already keeps a party recognisable | kept (v0.1.0 had widened case (b) and lost the declaration) | §5.4 limits | §7.2 | 17 |
| Gates G1 to G5, with their full clauses | Leaks and omissions are caught by code, not by reading | kept | §5.4 step 4; Annex C.2 | §7.3 | 17 |
| The two-step method: code first, then an engine that selects and never retypes | Paraphrase and identity leakage become structurally impossible | kept | §5.4 steps 1–3 | §7.4 | 17 |
| Auditable judgement: reason code, references, confidence, "could be wrong because" | Judgement without a recorded reason cannot be reviewed | kept | §5.4 limits | §7.2; §7.4 | 17 |
| Review of every package, and bounded repair | Gates check form; only a reading from outside the run checks substance (Standard §2.3 item 9) | kept; at RP4 | §5.4 step 5; §5.8 | §7.5 | 41 |
| Sources are cut into atoms by a code step | No earlier capability owned atomisation; the work fell between three | changed: atomisation is a code step of the Input socket, once per source (§1); earlier it was left to curation upstream | §4.3; Annex E.1 | §7.1 | 17, 45 |
| Each atom carries its status, its label and its confidentiality | Without them the ceiling cannot pass through packaging | changed: atoms carried only a confirmation status before; they are now labelled in the socket | §4.3; Annex E.1 | — | 4, 17 |
| Records and releases hold atom IDs and hashes, never atom text | A record must not become an uncontrolled copy of a source | new | §5.4 records; §7 | — | 43 |
| The marker map is built from the party register | One register of names, aliases and descriptors serves the sweep and the gate | new | §5.4 step 1; Annex E.3 | — | 83 |
| A malformed input goes back to its owner, never repaired here | A silent repair hides the upstream defect | kept | §5.4 failure | §7.5 | 17 |
| Two failed schema validations stop the step | Bounded retries | changed: the earlier method allowed three retries | §5.4 failure | — | 17 |

---

## §5 Model design

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Two outputs, captured together: the Blueprint and the Rationale and Evidence Brief | Rationale written afterwards becomes a justification essay | kept | §5.5 | §8.1 rule 4 | 18 |
| Rule 1 one child; rule 2 architecture level only; rule 3 no success criteria | Scope creep below architecture | kept | §5.5 limits | §8.1 | 18 |
| Rule 4 rationale with the design, with a genuine rejected alternative | A self-justifying design | kept | §5.5 limits | §8.1 | 18 |
| Rule 5 fidelity, not presence: full fidelity-checking of every element and every supporting evidence entry; a declared sample only for entries supporting no element | Embellished citations look cited | kept (v0.1.0 had checked presence only) | §5.5 step 6; §5.8 | §8.1 | 18 |
| Rule 6 roles kept apart; the revision step certifies nothing | No unit grades its own work (Standard §2.3 item 9): the step that wrote a draft cannot certify it | kept | §5.5 step 4 | §8.1 | 18, 22 |
| Rule 7 classification visible, with its confidence mirrored | Silent typing; a confidence higher in the Blueprint than in the brief | kept | §5.5 outputs (A1) | §8.1 | 18 |
| Rule 8 register discipline: one interface entry per crossing; provenance, confidence and direction never upgraded; the Designer never mints a crossing; `interface-dependent` with undeclared-crossing flags | A crossing the register declares and the model omits is a seam the hand-offs cannot pair | kept (v0.1.0 had carried it only in part) | §5.5 limits; step 5; states | §8.1; §8.3 | 18 |
| Rule 9 nothing designed on the far side; `unresolved` never resolved by assumption | Invented cross-entity detail | kept | §5.5 limits; Annex D 7 | §8.1 | 18 |
| Rule 10 no forensic discovery of the present state | Inference dressed as observed fact | kept | §5.5 scope | §8.1 | 38 |
| Rule 11 basis discipline and the coarsest defensible grain; no catalog invented | General plausibility mistaken for evidence specific to the child | kept | §5.5 limits | §8.1 | 19, 38 |
| Rule 12 content is data; cap 8; `incomplete-design` names the missing fact-type | A generic "more evidence needed" helps no one | kept; the missing fact-type becomes a needs request | §5.5 failure; §15 | §8.1 | 19 |
| What `stated` means for a ledger element | The earlier texts disagreed on it | changed: `stated` only where an atom labelled `source-backed` or `organisation-stated` states it directly | §5.5 limits | §7.1; §8.1 | 18 |
| The ledger is the authored artefact; rendering by code; the classes authoritative, candidate and narrative | Surfaces written separately drift apart; one authored ledger rendered by code cannot | kept | §5.5 step 2; `docs/OUTPUT.md` §6 | §8.2 | 18 |
| Narrative cells: the five-point contract and the per-cell checks | A sentence written to show restraint can still name a barred structure | kept (v0.1.0 had dropped it) | §5.5 limits; step 5 | §8.2; §8.3 | 18, 39 |
| The code checks at lock, including the sweep on the rendered Output A | Defence in depth against defects of the renderer | kept | §5.5 step 5 | §8.3 | 18, 19, 39 |
| Four verification labels, written only outside the run | Narrated compliance is not verification | kept; `externally-audited` states its level | Annex B.4 | §8.4 | 18, 22, 60 |
| Review at RP5 before anything is forwarded; a `MATERIAL` finding holds | No unit grades its own work; a material defect must stop the step before anything is forwarded | kept | §5.5 step 6; §5.8 | §11 | 22 |
| The organisation's statements admitted as evidence (`organisation-stated`) | Without the organisation's own intent as evidence, a design can stop only at the coarsest grain its documents allow | changed: generalised as a label, entered only as approved sources | Annex B.1; §5.5 | §10.6 | 31, 40 |
| Reference models only as labelled methods held by the Library; until one exists the catalog is declared unavailable | An invented benchmark makes a brief look stronger | new; v0.4.0: the catalogue the case study named only as a concept is proposed to the Library; a pattern is a method, and an element resting on a pattern alone is `assumed` | §5.5; Annex B.5; Annex E.19 | §8.1 rule 11 | 38, 96–99 |
| Leaks and confidence bleed tested on full-length runs | Rule checks on short fixtures do not show behaviour on output of ordinary length | kept | §5.5; §9 | §8.3 | 39 |
| A child that ends `incomplete-design` is put to the Requesting Authority as a WITHDRAW choice | The rest of the slice can go on | new | §5.5 failure; §5.8 | — | 40 |
| Two authors design each child, blind; the Ledger Reviser reconciles; an unsettled difference keeps only the shared, coarser grain | Two reasonable designs that the evidence cannot tell apart are what rule 11 keeps out of the Blueprint | new (v0.4.0) | §5.5 steps 2–4; Annex G | §8.2 item 5 | 92–95 |

---

## §6 Hand-offs

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| A separate capability after model design: restore identities, pair crossings, detect seams, record the hand-offs, keep the counterparty register even for a standalone organisation | Cross-entity work inside model design could never exceed placeholders, because its inputs were undesigned siblings | kept as a mandate, narrowed to the hand-offs (`decisions/DR-0002`); **new** as a design | §5.6 | §9.1 | 20 |
| No model of the whole; the hand-offs register of clean pairs | The direction recorded in `decisions/DR-0002` | changed | §5.6 | §9.1, §9.3 | 65 |
| Reconciliation of locally designed models | Reconciling by the Hand-off Analyst's own choice would redesign a decided child | changed: reconciliation is done only by routing back; Hand-offs never edits a child's model | §5.6 limits | §9.1 | 20 |
| An unmatched or contradictory seam is a seam finding, never bridged | Bridging hides a decomposition, packaging or evidence defect | kept (v0.1.0 had dropped contradictory seams) | §5.6 step 2; limits | §9.1 | 20 |
| A boundary class is never dropped: durable ID, evidence by atom, the run that surfaced it, reason for deferral, destination; it leaves only when incorporated at the correct level, recorded against its ID | Deferred scope must not be lost | kept | §5.6 limits; step 6; Annex E.7 | §9.1 | 37 |
| A child's own accountability is in; the counterparty relationship is recorded or deferred | Keeps model design single-child | kept | §5.6 limits | §9.1 | 37 |
| The eight known deferred classes; a capability that cannot place or register them has not met its mandate | The earlier chain set this as the acceptance condition of its cross-entity assembly capability | kept | §5.6 limits | §9.2 | 37 |
| A counterparty register for every shape | Every shape has outside parties | kept | §5.6 step 4 | §9.1 | 66 |
| A need is raised where the sources are silent on an expected counterparty class | Silence about a regulator or a customer class is what must be probed | kept | §5.6 step 4; Annex E.5 | §9.1 | 20, 66 |
| The legal and regulatory perimeter is flagged for human legal review | This AIOC makes no legal determination | new | §5.6 step 5 | — | 20 |
| Crossings between children of one entity are paired like those between entities | A split entity has internal seams too | new | §5 ("Child, not entity"); §5.6 | — | 42 |
| Seams with a carried child go to the new side | A carried child is decided | new | §5.9 | — | 70 |
| The role register: every role-type of the release, made by code from the decided ledgers and registers; conflicts are role findings, never merged | The next stage needs one list of who decides what; a conflict between children must never be merged silently | new (v0.4.0) | §5.6 step 6a; Annex E.17 | — | 85–88 |

---

## §7 Walkthrough

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Not a simulation; no numeric performance claim, ever | The model holds no evidence of volume, time or cost | kept | §5.7 | §10 | 21 |
| The six-section input; never fill an unknown; a claimed path through an unknown is `MATERIAL` | A refusal must not hide a claimed path that cannot close | kept | §5.7 inputs | §10 | 21 |
| The walk input and the blind brief, compiled by code | The walk reads one checked input; the author of situations never sees the design | new | §5.7 step 0; Annex E.8, E.9 | §10.5 | 84 |
| The binding rules and their precedence; unbindable prose halts; the validator wins | Every "deterministic" hop hides a classification of prose | kept | §5.7 step 1; limits | §10.1 | 21 |
| Actors derived, never invented | An invented role is a design change | kept | §5.7; Annex D 10 | §10 | 21 |
| The licensed terminal states, including `halts-excluded-scope` | Anything else is a structural defect | changed: `halts-excluded-scope` added (I-1) | §5.7 | §10.2 | 21 |
| The per-hop and per-walk fields | Every finding must be re-derivable from the trace | kept | §5.7 step 4 | §10.3 | 21 |
| The five known defects I-1 to I-5, fixed | Five gaps in the earlier instrument's rules would void or misclass findings; each is closed here | changed: all five applied | §5.7 | §10.4 | 21; the walkthrough battery |
| W1 to W6, and the mandatory negatives | Each type targets named finding classes | kept, W6 narrowed (I-4) | §5.7 | §10.5 | 21 |
| The mix: library at least 60%, blind pack at least 30%, the organisation's situations additive only; the designer never authors situations | An author tests what it designed | kept | §5.7 limits; step 2 | §10.5 | 21 |
| A library shortfall is declared, and the mix reported as not met | A mix that is silently not met hides a weaker walk | new | §5.7 | — | 21 |
| The seal before the walk; determinism; regression after a correction | Re-running is the audit | kept | §5.7 limits; step 3 | §10.5 | 21 |
| Regression across slices | A fresh situation set never erases a recorded failure | kept | §5.9 | §10.6 | 71 |
| Outside events of a supported class may be injected where the model is silent | A closed world never tests what the model omits | kept (it had been left out of the earlier standard) | §5.7 limits | §10.5 | 21 |
| Joint ownership, where declared, is not a W6 defect | Avoids false multi-claim findings | kept (likewise) | §5.7 limits | §10.5 | 21 |
| "Not declared" is a finding, never a compile failure | The walkthrough must not force a schema on the design | kept | §5.7 limits | §10.5 | 21 |
| The reduced catalogue, and its grade | A model thin in streams must still be walked; refusing it would test only the models that least need it | changed: adopted with its grade, which the earlier standard had left out | §5.7 | §10.5 | 21 |
| The five finding classes; the gap, never the fix | A fix-shaped finding is hidden redesign | kept | §5.7 | §10.6 | 21 |
| Per-walk assurance: the walked model is the reviewed model, confirmed by hash; one or two traces replayed | Findings must be checked against the right model | kept | §5.7 step 6 | §10.6 | 21, 22 |
| The findings review is mandatory, at RP7 under the Review Panel rule | A walkthrough's own classification of its findings can run toward leniency; a check outside it corrects that | kept, in a stronger form | §5.7 step 6; §5.8 | §10.6; §11 | 21, 22 |
| The correction path is chosen by the Requesting Authority; the closure test is sealed first; a clarification is evidence, not closure; a fresh set never erases a failure | A finding is against a design, not against an intention | kept (v0.1.0 had sent the model back without the authority's choice) | §5.7 failure; §5.8 | §10.6 | 21, 40 |
| The instrument battery: it sets the card's claim and the wording of a clean report; no walk or release waits for it | A walk's sensitivity must be measured before the card claims it | kept; changed: it gates the claim, never the work | §5.7 fixed test; §9 | §10.6 | the walkthrough battery |

---

## §8 Review, decision and release

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Blind pass, fresh context, no tools | An engine that saw the dialogue inherits its errors | kept | §5.8 rule 5 | §11 | 22, 53 |
| The Review Panel rule: 3–5 engines, at least 2 families, none of an author's family in normal mode; reduced level only with the TM Cell's permission and the Design Lead's acceptance | Engines of one family share blind spots; several independent engines that debate on quotes find more and dismiss less | changed (D5) | §5.8 | §11 | 53–64 |
| The served-engine check; a mismatch voids the call | A silent substitution of engine breaks the diversity | kept | §5.8 rule 17; §8 | §11 | 62 |
| Settlement by code, without a vote | A count can let a true finding fall | new | §5.8 rule 13 | §11 | 57 |
| Rulings on contested `MATERIAL` findings only | The human load stays bounded; an upheld finding needs no ruling | changed | §5.8 rule 15 | §11 | 58 |
| Engine ceilings and the served engine | No passage goes where it may not; the engine that answered is the one drawn | new | §5.8 rule 17; Annex E.12 | — | 61, 62 |
| The review budget | Cost is bounded without lowering a review | new | §5.8 rule 16 | — | 63 |
| Bounded repair: fresh reviser, smallest change, versions kept, all checks re-run, full re-review, at most 2 cycles, then hold | Unbounded repair patches prose for ever | kept | §5.8 rule 19 | §11 | 22 |
| The class sweep after repair | A repair of the named findings alone leaves their siblings in place | kept | §5.8 rule 19 | §11 | 22 |
| Findings ruled on rule text and evidence, never by counting engines or families | Votes are not evidence | kept | §5.8 rule 15 | §11 | 22, 58 |
| The seat that rules on findings | The Chief of Staff must not rule on findings about its own run | changed: the TOM Design Lead rules, not the orchestrator | §5.8 rule 15 | §11 | 22 |
| Quality checks in the release; review records outside it | The release is about the operating model only (D1) | new | §5.9; Annex E.11 | — | 64, 80 |
| The release lint | The release says nothing about how it was made | new | §5.9 step 6a; Annex E.15 | — | 67 |
| The material finding notice, with the choices SUPPLY, WITHDRAW, REDESIGN, ACCEPT AS KNOWN DEFECT and CLOSE | The Requesting Authority, not the engine, chooses the correction path | changed: five fixed choices; ACCEPT AS KNOWN DEFECT is kept from the earlier notice as a non-delegable row and stated in the release's headline; CLOSE files a Held Report | §5.7 failure; §5.8 failure | §10.6 | 40 |
| One decision per row; at most 12 rows per pass; the cap never met by packing | Bundled rows produce approvals nobody gave | kept | §5.2 limits; Annex C.4 item 1 | §5.1 | 9 |
| Global assent is never approval | Silence and "looks fine" are not decisions | kept | Annex C.4 item 1 | §5.2 | 10, 23 |
| Row dependencies | A corrected row silently invalidates the rows that rest on it | kept (v0.1.0 had dropped it) | §5.2 step 10; Annex C.4 item 2 | §5.3 | 9 |
| "Don't know" is legitimate, and blocks scope, exclusion, criterion and contradiction rows | Turning "don't know" into yes manufactures a decision | kept | Annex C.4 item 3 | §5.4 | 9, 10 |
| The weak-approval signal per part; cosmetic corrections do not clear it | Ceremony approval | **moved**: computed by Source Lifecycle; this AIOC keeps that a pass with an uncleared signal on non-delegable rows decides nothing | Annex C.4 item 4 | §5.5 | 10 |
| Delegated, not decided; non-delegable rows answered only by the Requesting Authority | Delegation must not stand in for the decider on scope, criteria and contradictions | kept | Annex C.4 items 5, 6, 9 | §5.6 | 35 |
| The non-response stop; the narrowest honest brief, built only from non-delegable rows already decided; residue `safe-to-carry` or `blocking` | Work must never be left open indefinitely, or silent | kept (v0.1.0 had lost it) | §5.1 failure; §5.3 states; §5.9 states; Annex C.1 | §5.7 | 28 |
| The stop vocabulary | Every stop states why | kept (`round-cap` joined from reconstruction) | §5.1 failure | §5.8 | 28 |
| One run at a time; the slot is released only by the decision or the run's closure, never by a review verdict | Parallel runs hide failures between them; assurance must not free the slot | changed: a second run with the TOM Design Lead's approval | §4.2 step 4; Annex C.1 | §5.9 | — |
| A row of a listed type is decided only with a gateway signature; purpose and values signed by the GOV Cell | A listed decision is valid only when signed at the gateway | new | §5.9 limits; Annex C.4 item 7 | — | 36 |
| Listed types: a subset of the Standard's list | A decision on an operating model is never an engine or gateway decision | new | §13; `contracts/PINS.json` | — | 68 |
| The Decision Package contents | The decider must not have to read any technical file | kept; the platform-alignment item is withdrawn (`decisions/DR-0002`); carried elements and superseded sources are listed | §5.9 step 1 | §12.1 | 23 |
| Inside, outside and deferred made visually obvious; prose hygiene never put before the decider; five open-item blocks, where only E asks | Evidence gaps and instrument gaps are not the decider's questions | kept | §5.9 step 1 | §12.1 | 23 |
| The review of the Decision Package at RP8 | The package must claim no more than the reviewed parts | new | §5.9 step 2 | — | 23 |
| The decision-sheet values per element, and the final status values | One fixed vocabulary for the decision | kept | §5.9 step 4 | §12.2 | 23 |
| The release is frozen, content-addressed and filed into Source Lifecycle; a change is a new release | Later stages read one decided model from the source of record | new | §5.9 steps 6, 7 | §4.4 | 24 |
| Carry-forward of earlier slices | A decided slice is not asked again | new | §5.9 | §4.4 | 69 |
| A unit as the subject | A unit of an organisation can ask for its own model | new | §2.2 | — | 82 |
| The release names roles and what each decides, and stands alone | What fills a role, and the workload of each position, are matters of later stages | new; reworded in v0.5.0 | §2.2; §5.9 | — | 27 |
| The next stage is told of each decided release directly, by reference | A later stage that only reads Source Lifecycle learns late, and a release that nobody is told of waits unused (`49GAION/DR-0016`, item 4) | new in v0.5.0 | §5.9 step 8a; Annex E.20 | — | 100 |
| Returns arrive directly, and each ends in one of four ways | A return that only waits in Source Lifecycle is not heard, and a return without an end can block the stage after it (`49GAION/DR-0016`, item 5; `DR-0018`) | new in v0.5.0 | §5.10; Annex E.21, E.22 | §4.4 | 101–107 |
| Each ended return is classified by the Design Lead | A return for what this AIOC should have obtained is its defect; no unit grades its own work | new in v0.5.0 | §5.10 limit 8 | §4.4 item 3 | 108 |
| An Office is proposed, never self-created | A unit never enlarges itself | new | §4.1 | — | 25 |
| A stop through the stop door halts every part at once | The human seat can always stop the AIOC | new | §4.2 step 8; Annex C.1 | — | 26 |
| Two authors never lower a review: four families; one author at S5 only with the TM Cell's permission, declared | The several-engine review (D5) comes first; an added check must not weaken it | new (v0.4.0) | Annex G.3, G.7; §13 H-05, H-32 | — | 94, 95 |

---

## §9 Standing doctrines

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Small, narrow capabilities | A narrow responsibility can be checked from outside; a broad one cannot | changed: the capabilities stay narrow, as Pods of one AIOC, so that one unit carries one product | §17 | — | 27 |
| Nine stages, each with one input, one output and one done-test | Each stage is defined by what it takes and what it gives | new | §5.0 | — | 78 |
| Closure, and one list of human decisions | A closed blueprint holds no open design question | new | §0; §13 | — | 77 |
| The case study, not evidence | Earlier results are not reasons here | new | §0 | — | 79 |
| Schema-first contracts between steps | Prose is commentary on a schema, never the contract itself | changed: the external contracts and the Input Pack have schemas; every other object has a closed field list (blueprint Annex E; `CARRIED-RULES.md`), from which its schema is a build item that may add nothing | §8; §10; `contracts/` | — | 7, 24, 44 |
| Path qualification with a named owner | Qualifying each part is necessary, never sufficient | kept: the path owner is the TOM Design Lead; it gates the card's `qualified` claim, never a run | §3; §9 | — | path qualification |
| Rate evidence: at least three full-length runs; failures kept, never averaged away | A battery shows that a capability can; reliability is a rate | kept | §9 | — | path qualification |
| A compatibility register of qualified version tuples | A change to any part invalidates the tuples that contained it | kept, in the code project | §7; §9 | — | path qualification |
| The null default: no tools, no outside access, no memory, a fresh context; any grant justified | Every grant is a degree of freedom that must be qualified | kept | §8 | — | — |
| The two-gate engine, the derivation rule, and runners kept unaware of the tests | A capability is its logic and its configuration together; hand-paraphrased instructions drift; a runner that sees the test games it | kept; the reviewer battery is hidden from the runners too | §8 | — | — |
| Preservation: earlier records kept unchanged | Silent retrofitting rewrites history | kept: under `legacy/` in the code project, read only, never wired in | §7; §8 | — | 79 |
| Technical clearance is not permission | A clear review means only "clear to present to the Requesting Authority" | kept | §5.8 limits; §5.9 | §11 | 23 |
| The starting contract | "Sufficient" means startable, not complete; a return for specialist-found information is normal | kept | Annex C.3 | §3.1; §4.4 | 15 |
| Demand signals surfaced, never absorbed | A missing capability hidden inside another is never built | kept | §5.3; §5.5 | §6.1; §8.1 | 16, 38 |
| Inputs from people kept apart from sources | Direction about method must never become content about the organisation | changed: the earlier tagging of each input's role becomes "nothing through a human port is a source" | §4.3; §11 | — | 2, 29 |
| The run depth: grain and volume only, stated by the Requesting Authority within the TM Cell's permission | How fine a model is needed is the decider's need, and its cost the TM Cell's; neither may cut a stage, a check or a review | new (v0.4.0); not the case study's depth setting (§10) | Annex F; §15 | §2.7; §10.5 | 89–91 |

---

## §9a What the model also states, and the organisation as it runs today (new in v0.6.0)

Each rule below is new, under the direction recorded in `decisions/DR-0006`. Its source is a study of comparable products (each feature taken as a method, never as evidence) and the governing seat's direction that the stages after this one must find in the release what they need to start.

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| The strategy frame, from sources and decisions only, asked once through EX-10, never blocking | The next stages' objectives, the priority of each element and the value case start from the organisation's strategy; what the organisation wants is never inferred | new | §5.1 steps 7, 9, 12; Annex H.1 | §4.1 section 22; §4.5 | 109–111 |
| Delivery model and make-or-buy per capability, never a provider; carried by a crossing | How a capability is delivered decides where the next stage designs a process and where a hand-off; naming a provider is a choice of supplier, which this AIOC never makes | new | §5.5; §5.6 step 4b; Annex H.2 | §8.2; §8.3 item 11 | 112, 113 |
| Critical value streams, each on a cited reason from a closed list | The next stage designs the critical streams first; a stream made critical by judgement alone would order the work on nothing | new | §5.5; Annex H.3 | §8.2; §8.3 item 12 | 114 |
| Maturity now only from a source; the target only from a source or a decision | Assessing a level is forensic discovery of the present state, which the design never does; a target is the organisation's ambition | new | §5.5; Annex H.4 | §8.2; §8.3 item 12 | 115 |
| Outside parties' journeys, from crossings already declared | The path an outside party takes shows gaps between the parts it meets; adding a crossing or designing the party's side would invent what the evidence does not hold | new | §5.6 steps 4a, 4b; Annex H.5 | §9 | 116 |
| The value case, compiled by code, with no figure of its own | The stage that carries the model into the organisation needs where each change starts and what it aims at; a figure this AIOC made up would be an estimate presented as a fact | new | §5.9 step 1b; Annex H.6 | §12.1 item 23; §12.2 | 117 |
| Priority proposed by a fixed rule, decided with each element | Priority is the organisation's trade-off (§1.2 item 4); a rule proposes it so that no author's preference does | new | §5.9 steps 1b, 4; Annex H.7 | §12.2 | 118 |
| Records of the work as it runs today: exports by role-type and process only; `person-level records` refused; the activity profile by code, or `no observation` | The governing seat directed this input; positions only, and the personal-data floor (HF-17), mean that a record of who did the work never enters | new | §4.3; Annex H.8; Annex E.1, E.2 | — | 119–121 |
| Twenty release parts; a decided priority on each element decision | The new parts are read by reference like every part, and each is required, so that a release without one is visibly incomplete | new | `contracts/tom-release.schema.json`; Annex H | — | 122 |
| The organisation dictionary read where served | The stages use the organisation's words in its own meaning; a difference of meaning between sources is a contradiction, never a silent choice | new | §5.1 step 1; Annex H.9 | §4.2 | 123 |

---

## §10 Dropped or replaced

| Rule (short) | Why | Mark | Here | Rule text | Test case |
|---|---|---|---|---|---|
| Prose critic passes that certify their own run | No unit grades its own work (Standard §2.3 item 9); code checks and the Review Panel do this work | replaced by a stronger form | §5.5 step 4; §5.8 | §8.1 rule 6 | 18, 22 |
| Free conversation with people inside the design chain | The direction recorded in `decisions/DR-0001`: this AIOC works only from documents | dropped | §11 | — | 2, 13 |
| Outside research by the design steps | Unchanged prohibition; only cited sources are used | dropped | Annex D 2 | §2.2 | 2 |
| The depth setting (light, standard, deep) | Burden is set by leverage, passes and rows; review effort by the slots `review_engines` and `review_budget_per_run`. The run depth of v0.4.0 (§9) is a different setting: it changes only how much is designed and checked above the floors, never how anyone is asked. | replaced | §5.2; §15 | — | — |
| The run's self-critique of its own inferred rows | Sticky inferred, the process audit (RP1b) and the review at RP1 do this work | replaced | §5.1 | §2.1; §2.3 | 14, 15 |
| Base passes four and five (boundary and consequence probes), and the prediction recorded before the second instance | They were probes of a conversation; boundary and consequence tests are done by the structuring checks and the walkthrough | dropped | `docs/ASKING-CATALOGUE.md` §3 | §1.5 | — |
| The `externally-researched` label | No research is done | dropped | Annex B.1 | — | — |
| The `observed` label, and closing a contradiction by cited observation | This AIOC never watches work. GOV directed records of the work as it runs as an input (`decisions/DR-0006`); they enter as exports by role-type and process, labelled as exports, never as observation (§9a) | not used | Annex B.1; Annex H.8 | §3.1 (S8) | 119–121 |
| "Treat unopened material as read" (a prohibition) | Examined with the drops | kept: carried as a rule, not dropped | §5.1 limits | §1.1 | 8 |
| Up to two scope questions before reading | The approved Design Request sets the scope | dropped | §4.3 | — | 3 |
| Simulation as a channel for facts | The walkthrough is not a simulation, and nothing simulated is a fact | dropped | §5.7 | §10 | 21 |

The rows restored in v0.3.0 (the evaluator's question set, the request kind, the expertise lens, findings offered as new, and the organisation's own verdict on how its request was understood) are in §2.

*Powered by 49GAION*
