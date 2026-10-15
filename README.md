# Target Operating Model · `[ORG]AIOC-TOM`

> **TOM in one page**
>
> TOM (Target Operating Model) turns an organisation's own documents into a written model of how it should work. For each part of the organisation, the model sets out what the part must be able to do, how its main work flows, who decides what, and where it hands work to other parts and to outside parties. It names roles and what each decides. It does not say what fills a role.
>
> It serves one person's work, a unit, a company, a group of companies, or a group with independent institutions inside it. Where there are several companies, it designs only the hand-offs between them and with outside parties.
>
> **What goes in**
> 1. An approved design request, recorded in Source Lifecycle, the organisation's library of sources: who asks, what the design is for, what should be different, and how fine the model should be (light, standard or deep).
> 2. The organisation's own documents, read only by reference. The input socket checks them, cuts them into numbered passages, labels each passage with how far it can be trusted, and hands the engine one sealed Input Pack.
> 3. Answers to what the documents do not say. TOM never asks a person. It asks the Chief of Staff of Source Lifecycle, who gets the answer from the right person, has it approved and recorded, and returns it. Each answer arrives as a new version of the Input Pack.
>
> Today Source Lifecycle is the only source. Other kinds of source plug into the same socket, each through its own adapter file, and only to be read.
>
> **What the engine does, in nine stages**
> 1. Admit: check the request and the connection, and make the Input Pack.
> 2. Frame: work out what is asked, who may decide it, what exists today, what should change, and what is unknown or in conflict.
> 3. Structure: split the work into parts, and propose which to design first.
> 4. Child briefs: for each part, what it must achieve and how anyone would know.
> 5. Package: gather each part's own evidence, and nothing about the other parts.
> 6. Design: design each part's model, and write down why. A general pattern may suggest a structure, but it never counts as evidence.
> 7. Hand-offs: pair every hand-off between parts and with outside parties, list every role once with what it decides, and flag legal questions for a lawyer.
> 8. Walk: test the model against realistic situations, and record where it holds and where it stops.
> 9. Decide and release: the organisation decides each element; the decided model is frozen and filed back in Source Lifecycle, and Process and Position Design is told at once.
>
> Each stage has one input, one output and one test that says when it is done. The frame and each part's design are written twice, separately, by two AI engines of different families; their differences are settled on the sources or put to the organisation. Inside every stage, three or more other independent AI engines check the output: each alone first, then in a short debate held to quotes. They do not vote. A person, the TOM Design Lead, rules on what they still dispute.
>
> **What comes out: the TOM Release**
> 1. The Decision Package: a plain summary, what is still unknown, and the choices to make.
> 2. For each part: what it must be able to do, its main flows, who decides what, and where it hands work over, each with its reasons and sources.
> 3. The hand-offs between parts and with outside parties, and the legal questions for a lawyer.
> 4. The role register: every role in the model, what it decides, what it answers for, and what it hands to whom.
> 5. The test against situations, and the quality checks made at each stage.
> 6. What is still open: unknowns, assumptions, deferred items, and any defect the organisation chose to accept.
> 7. The record: the sources used, and the trace from each statement back to its source.
>
> **Who uses it**
> - The decision-maker who asked for the design decides each element: accept, correct or reject. Silence decides nothing.
> - The positions that lead each part check its model against how the work runs.
> - Process and Position Design, the next stage, is told of each decided release directly and reads it, starting with the role register. It sends back what it cannot use, and so may Delivery and Implementation, the stage after it.
> - Every return goes back and forth until it ends: answered by a new release, answered by a decision, or set aside by decision and carried forward as a known defect or a decided assumption. None is left open.
> - Auditors and lawyers use the sources, the trace and the record.

The writing repository of **`[ORG]AIOC-TOM`, Target Operating Model**: the AIOC that designs an organisation's target operating model from its own documents. It is the second stage of an organisation's design under 49GAION, after Source Lifecycle: the Library part 49GAION Target Operating Model (Operating Protocol §19; `49GAION/DR-0016`), whose mother blueprint this is. In each organisation this repository is named `<org>aioc-tom` (49GAION Naming Standard R9).

**Status: draft `v0.5.0`, 16 October 2026: closed at v0.4.0; v0.4.1 changed wording only (`decisions/DR-0004`); v0.5.0 links this AIOC directly to the stages after it (`decisions/DR-0005`). Nothing here has run; every fixed test reads `NOT_RUN`.** Version 0.4.0 added four features to the closed v0.3.0 and removed nothing (`decisions/DR-0003`).

## Where to read

| File | What it is |
|---|---|
| [`docs/OUTPUT.md`](docs/OUTPUT.md) | **start here** after the page above: what you receive, in plain words, with a glossary; then exactly what a TOM Release contains |
| [`blueprint/TOM-BLUEPRINT.md`](blueprint/TOM-BLUEPRINT.md) | the blueprint, on the 49GAION AIOC Blueprint Template `v1.5.0`: identity, card, placement, positions, the four standard and nine functional capabilities, the nine stages, each with its input, output and done-test (§5.0), the Review Panel rule (§5.8), run states, gates, labels, decision rules, the field lists of the new objects (Annex E), the run depth (Annex F), the two authors (Annex G), Cells and Pods |
| [`docs/INTAKE-WITH-SOURCE-LIFECYCLE.md`](docs/INTAKE-WITH-SOURCE-LIFECYCLE.md) | how it learns anything: only documents; the Design Request; needs requests to the Chief of Staff of `[ORG]AIOC-SL`; the Missing Report; what Source Lifecycle is asked to add |
| [`docs/ASKING-CATALOGUE.md`](docs/ASKING-CATALOGUE.md) | the document kinds, explainer templates, request kinds and row forms it asks with, and why |
| [`docs/CARRIED-RULES.md`](docs/CARRIED-RULES.md) | the full text of every rule carried from an earlier organisation-design chain |
| [`docs/DESIGN-BASIS.md`](docs/DESIGN-BASIS.md) | why each rule is here, and which test case checks it |
| [`tests/TEST-TOM.md`](tests/TEST-TOM.md) | the fixed test, written before use: 108 cases, the Design Lead's seat test, path qualification, the walkthrough battery and the reviewer battery |
| [`tests/release-lint/`](tests/release-lint/) | the words a release may not hold, and their fixtures |
| [`adapters/`](adapters/) | one file per source type that plugs into the Input socket; today Source Lifecycle |
| [`contracts/`](contracts/) | the machine contracts, with valid and must-fail examples; `tools/check_contracts.py` checks them |
| [`cards/`](cards/) | the unit cards of its seven Pods and nineteen Cells, and the bot identity cards of its eighteen AI Cells, generated from the blueprint by `tools/make_cards.py` |
| [`upstream/`](upstream/) | the proposals to 49GAION: the Protocol section and Library card, now merged in a revised form (Protocol §19; `49GAION/DR-0016`), a reference-model catalogue, and the other proposals with their state |
| [`decisions/`](decisions/) | the decision records of this repository |

## Where things live

- **Writing** (this repository): the blueprint, adapters, contracts, tests, decisions, design basis and carried rules. It is written for any organisation, with `[ORG]` placeholders. An organisation's own values and run records are kept in its records repository, never here.
- **Code**: the code project of the same name on the organisation's code platform (Naming Standard R9). It holds:
  - the code steps, written new against the blueprint, and their tests;
  - the PRD;
  - the private register of the earlier chain;
  - and, unchanged under `legacy/`, the earlier chain's files, kept as a case study and never wired in (blueprint §0).
- **The 49GAION Library** holds this AIOC's part card (`library/cards/target-operating-model.part-card.json` of `49GAION-protocol`) and points here for its mother blueprint.

## Checks

```
python3 tools/check_contracts.py --signature-list <49GAION hub>/upstream/human-floor-signature-types.json --design-return <49GAION-protocol at the pinned commit>/library/contracts/design-return.schema.json
python3 tools/make_cards.py <49GAION-protocol>/spec/schemas
```

Both must report 0 failures and 0 errors. `check_contracts.py` also checks the adapter fixtures, runs the release lint, and checks this AIOC's return examples against the Library's design return contract at the pinned commit.

## How a change is made

A change is a pull request: a tested change to the blueprint or a contract, reviewed by someone other than its writer. A decided text is never edited; a change is a new version that names what it supersedes.

*Powered by 49GAION*
