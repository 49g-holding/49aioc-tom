# Asking catalogue

**`[ORG]AIOC-TOM` v0.4.0 · draft · 15 October 2026; v0.6.0, 16 October 2026: EX-10, EX-11, records of the work, and priority on element rows (blueprint Annex H).** What the Target Operating Model AIOC asks the Chief of Staff of `[ORG]AIOC-SL` for, in what form, and why. Each entry names the design decision it feeds, so no question is asked for its own sake. The catalogue is configuration: an organisation may add entries as tested changes; it never removes the rules of `INTAKE-WITH-SOURCE-LIFECYCLE.md`.

## 1. Choosing the form

1. If a document of a known kind would hold the answer: ask for that **document** (§2).
2. If no such document exists, or it was declared absent: offer an **explainer** (§3).
3. If this AIOC already inferred the answer from the sources: ask for a **confirmation** of that one item; or where the frame needs the organisation to confirm how its request was read (§4.1).
4. If a load-bearing source has no status: ask for a **status** (§4.2). If two held sources disagree, put a **decision** row (§4.4), non-delegable, unless a held source states the precedence rule, which is then cited.
5. If the fact lives in a system, not a document: ask for an **export** (§4.3).
6. If only the Requesting Authority can choose: put a **decision** row (§4.4).

## 2. Document kinds

The kinds most often needed, by what the design uses them for. A kind that does not exist for an organisation is answered `not applicable` once and never asked again.

| Need (design use) | Document kinds to ask for | Feeds |
|---|---|---|
| Who the organisation is and who may commit it | constitutional documents (articles, charter, statutes, partnership agreement); register of entities and ownership; shareholder or member agreements; powers of attorney | Design Brief frame, item 1 (standing, committed or context); structure |
| What it is for | purpose or mission statement; strategy or business plan; founding documents | outcomes; purpose and values (GOV) |
| How decisions are made | delegation of authority; approval matrix; board and committee terms of reference; minutes recording governing decisions; signing rules | decision rights and governance skeleton |
| What it does today | organisation chart; descriptions of functions or teams; earlier operating model or review reports; process documents | present state; capability map; value streams |
| Rules it follows | policies in force; internal standards; codes of conduct | constraints; governance skeleton |
| Who it deals with outside | key contracts and service agreements (by counterparty class); licences and regulatory permissions; correspondence with regulators | boundary register; counterparty register; legal and regulatory perimeter |
| Limits it works within | budgets and financial limits; regulatory obligations; staffing or capacity limits stated in documents | constraints |
| What should change | a revised Design Request (§3a); board or owner resolutions; transformation briefs | outcomes; success criteria |

**For a single person's work** the kinds are simpler: a statement of goals, a list of commitments and roles held, recurring activities, the people and organisations dealt with, any agreements in force.

## 3. Explainer templates

An explainer is the organisation's own account, given in a guided conversation through Source Lifecycle and recorded only after the person approves the exact text, item by item. It is recorded as a source of origin kind `explainer`, with the template ID and version and each statement's own Source Lifecycle label. This AIOC admits a statement labelled `stated` as `organisation-stated`, and keeps `inferred`, `assumed` and `unknown` as they are (`adapters/source-lifecycle.adapter.md` §5). Each question carries why it is asked; "don't know" is always allowed; questions come one at a time. An explainer counts as three rows toward the pass limit.

| ID | Explainer | Plain questions (abridged) | Why it is asked | Feeds |
|---|---|---|---|---|
| EX-01 | Purpose and scope | What is this organisation, or this work, for? Whom does it serve? What must it never do? What should this design cover, and what should it leave out? | No design can start without a scope and an outcome two people would judge the same way | Design Brief: scope, exclusions, outcomes; purpose and values (GOV) |
| EX-02 | Shape and entities | Which legal entities, units or institutions are there? Who owns or controls whom? Which of them is this design about, and which are only context? | Each committed entity needs its own standing and its own model | Design Brief frame, item 1; structure |
| EX-03 | What is done today | For each entity in scope: what work is actually done, where, and by which part of the organisation (roles, not names)? | The present state, labelled, is the base of the model | present state; capability map |
| EX-04 | How decisions are made today | Who decides what, today? What needs whose approval? Where are decisions recorded? | Decision rights must start from what is real, not assumed | decision rights and governance skeleton |
| EX-05 | Rules actually followed | Which rules are followed in practice, written or not? Where do practice and documents differ? | Unwritten rules and gaps against documents shape the governance skeleton and the contradiction register | constraints; contradictions |
| EX-06 | Outside relationships | Which kinds of outside party does the work depend on or answer to: regulators, banks, suppliers, customers, partners, platforms? What crosses with each? | Every crossing must be declared; the counterparty register is needed even for a standalone organisation | boundary register; counterparty register; perimeter |
| EX-07 | The change wanted | What should be different after this design? How would anyone tell, by looking at the world, that it worked? | Outcomes and at least one observable criterion are the floor of the brief | outcomes; success criteria (decided by the Requesting Authority) |
| EX-08 | Limits and obligations | What limits apply: legal, regulatory, money, time, people? What must the organisation itself provide or decide during the design? | Hard limits and obligations bound the design | constraints; obligations |
| EX-09 | One real case, end to end | Take one real recent case of the main work. Walk it from start to finish: what happened, in what order, who handed what to whom, what went differently from the rule? Then one exception, and a second case. | Value streams and walkthrough situations need a real instance, not the general rule; differences between cases become candidate contradictions, not corrections | value streams; walkthrough situations |
| EX-10 | Strategy on one page | Only the elements the sources lack, one at a time: What is this organisation for? What does it hold to? Where does it mean to be in the long run? What should it look like in three years? What must be true in one year, and how would anyone tell? Which few numbers show how it is doing, and what does each count? | The strategy frame is the organisation's own; it is never inferred. The priority of each element, the value case and the next stage's objectives start from it (blueprint Annex H.1) | strategy frame; purpose and values (GOV) |
| EX-11 | How mature each capability is | For each capability of one part, as the model names it: how established is it today, on five levels (done differently each time; done the same way each time; written down and followed; measured; improved on its measures)? Is there a level it should reach? Asked once per part, only where a level would change a design choice | Today's level is a fact only the organisation holds; the target is its decision (blueprint Annex H.4) | maturity now; maturity target (decided by the Requesting Authority) |

The full question set of each template, its order and its wording are kept as configuration of the Chief of Staff of `[ORG]AIOC-SL` (proposed addition SL-A4, `INTAKE-WITH-SOURCE-LIFECYCLE.md` §9). This catalogue fixes their IDs, purpose and what they feed.

## 3a. The Design Request template (DRQ-01)

A run starts only from an approved Design Request (`INTAKE-WITH-SOURCE-LIFECYCLE.md` §1, item 4). Where the organisation has no written brief, the Chief of Staff of `[ORG]AIOC-SL` makes one with the Requesting Authority through EX-01 and EX-07, on this template. This AIOC supplies the template, never the content.

| # | Field | In the organisation's own words |
|---|---|---|
| 1 | The requesting seat | which seat asks for the design (by role, never by name), and on whose behalf |
| 2 | The entities in view | which entities, units or institutions the design is about, and which are only context |
| 3 | What should be different | what should be different after the design, as the organisation sees it |
| 4 | Why now | what prompted the request |
| 5 | Known limits | anything the organisation already knows must hold (money, time, law, people) |
| 6 | What is out | anything the organisation already knows it does not want designed |
| 7 | The request kind | the request kind, if known (§3b) |
| 8 | The earlier release | the earlier release this continues, if any, and what in it should change |
| 9 | How fine the model should be | `light`, `standard` or `deep`, and why. `light` designs each part's main capabilities only; `standard` designs as finely as the documents support; `deep` also tries one level finer for each main capability, and tests the model more. Left empty, it is `standard`. The deepest the organisation permits is set by the Cell carrying `[ORG]HOAC-TM` (blueprint Annex F) |

The Requesting Authority approves the whole Design Request in Source Lifecycle; its fields are then read like any other source. A later change to the request is a revised Design Request, a new version.

## 3b. Request kinds

The frame states one request kind, from this closed list.

| Kind | Meaning |
|---|---|
| `new organisation or unit` | designing what does not yet run |
| `reorganisation` | changing an organisation or unit that runs |
| `one person's work` | the operating model of one person's work |
| `group of entities` | several entities and the hand-offs between them |
| `group with an independent institution` | a group with an independent institution inside it |
| `next slice` | a continuation of an earlier release |

A profile per kind holds: the explainers offered first (EX IDs); the document kinds expected (§2); the situation-library pack; the counterparty classes usually present. The frame states the kind with its reason, as a revisable hypothesis, labelled like any claim. A re-classification is logged. Where no profile fits, the frame says so and uses the general profile, and the gap is a demand signal. A later stage may then return `request kind unsupported` (`CARRIED-RULES.md` §4.4). Profiles grow with the situation library; none is invented.

| Kind | Explainers first | Document kinds expected (§2) | Situation pack | Counterparty classes usually present |
|---|---|---|---|---|
| `new organisation or unit` | EX-01, EX-02, EX-07, EX-08 | founding documents; plans; the mandate | standard library: W1, W3, W5 | regulatory; commercial-counterparty |
| `reorganisation` | EX-03, EX-04, EX-05, EX-07, EX-09 | present structure; delegations; process documents | standard library: all types | as the present state shows |
| `one person's work` | EX-01, EX-03, EX-09 | the person's mandate; engagement documents | standard library: W1, W2, W4 | commercial-counterparty; public |
| `group of entities` | EX-02, EX-04, EX-06 | ownership records; inter-entity agreements | standard library: all types, hand-off weighted | group-internal; financial-infrastructure; regulatory |
| `group with an independent institution` | EX-02, EX-04, EX-06, EX-08 | the institution's founding and governance documents | standard library: all types, independence weighted | group-internal; regulatory; public |
| `next slice` | as the carried release's kind | the carried release; sources changed since it | the carried release's pack, plus regression | as the carried release |

These profiles are the first, offered by `[ORG]AIOC-OCO` on the evidence of the case study. They are configuration. A profile is changed or added as a tested change, and grows with the situation library; none is invented in a run.

## 4. The other forms

### 4.1 Confirmation row
`# · purpose · what we read or inferred, in plain words · from which sources · why it matters · confirm / correct (your wording) / don't know`. The row says plainly that this is something derived, not something the person said. A confirmed item keeps its label and gains the confirmation reference; it never becomes `source-backed`, and no answer ever lowers its label. A correction replaces the item, labelled `organisation-stated`.

The five purposes (`row_purpose`):
- `inferred item`: one item this AIOC inferred from the sources;
- `understanding check`: "This is how we read your request": the frame in plain words and its main consequences; one row per frame decision pass;
- `found, not said`: one finding the sources hold and the Design Request did not state; the answer records whether it was already known (`known_before`: yes, no, don't know);
- `assumption`: one load-bearing assumption, with what breaks if it is false;
- `obligation`: one obligation of the organisation, with its owner role and its date.

All five are delegable. An answer by delegation is recorded `delegated, not decided`. None of them decides a scope, exclusion, roster, criterion or contradiction row.

### 4.2 Status row
`# · document · version · the question (in force? draft? superseded?) · answer`. Answered by the document's approver in Source Lifecycle, with the approval evidence. A status row never asks which of two documents governs; that is a decision row (§4.4).

### 4.3 Export request
`# · the system of record (by role, never by tool name in central text) · what to export · as of which date · why`. An export is a snapshot; it is never a live read. The contract requires all three of what, from which system and as of which date.

**Records of the work as it runs today** (new in v0.6.0; blueprint Annex H.8). The request also states `aggregation: by role-type and process`, and says plainly that the export must carry no field that says who did the work. The organisation makes the projection and records its impact assessment and its data-protection decision (HF-17) before the export is recorded in Source Lifecycle (`INTAKE-WITH-SOURCE-LIFECYCLE.md`, SL-A13). An export that still says who did the work is refused at the socket (`person-level records`). Where none is given, nothing is put in its place.

### 4.4 Decision row
`# · the decision, in one line · what changes depending on it · options · the deciding seat · the rows it depends on · your decision`. One decision per row. Rows only the Requesting Authority may answer are marked, and only its Cell may answer them. Rows of a listed type (for example purpose and values) are signed at the tool gateway, never in Source Lifecycle's own screens.
- **Contradictions:** `A governs / B governs / both, in different cases / don't know`. The decision holds only for this brief; the losing side stays in the register; where both sides rest on the same source, the row is carried, not closed.
- **Elements of the model:** `ACCEPT / CORRECT (comment) / REJECT`. A fact in a correction is admitted as `organisation-stated`. Each row shows its proposed priority (`must / should / could`; blueprint Annex H.7): `ACCEPT` keeps it; `CORRECT` may change it.
- **The strategy frame** (blueprint Annex H.1) and **the value case** (H.6): `ACCEPT / CORRECT (comment) / REJECT`, one row each. A correction of the value case may set a target; nothing is set for the organisation.
- **Final status:** `ACCEPT / ACCEPT WITH CORRECTIONS (before or after the next stage) / RETURN FOR REDESIGN / REJECT`.
- **A material finding notice:** `SUPPLY / WITHDRAW / REDESIGN / ACCEPT AS KNOWN DEFECT / CLOSE`, each with its cost, and one recommended choice; none is adopted until the Requesting Authority decides.
- **Two readings of the request** (blueprint Annex G): `reading A / reading B / both readings / don't know`. Non-delegable. It asks what the organisation means, never which design is better.
- **Two names for one role** (blueprint Annex E.17): `same role / different roles / don't know`. Non-delegable. Only `same role` joins the two names.

## 5. What is never asked

- A question a held source answers.
- A design question: which structure, which solution, which tool, which success measure to invent.
- A question whose answer changes no decision.
- A secret: a password, key, token, seed phrase or one-time code (Source Lifecycle refuses it at intake).
- A question addressed to a person by name; requests name seats or roles.
- A question about an evidence gap or an instrument gap of this AIOC: those are reported in the Missing Report and the Decision Package, never asked.
- A question about how this AIOC checks its own work. The independence of its checks is accepted, where reduced, by the TOM Design Lead within the TM Cell's permission; the Requesting Authority is told in the quality checks, never asked (blueprint §5.8 rule 18).
- Which of two designs is better. Where two separate designs of a part differ, the difference is settled on the sources, by asking for the missing fact, or kept open at the coarser grain (blueprint Annex G); it is never asked.

*Powered by 49GAION*
