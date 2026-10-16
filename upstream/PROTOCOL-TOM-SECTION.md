# Proposed Protocol section: Target Operating Model, the second stage

> **Superseded, 16 October 2026.** Merged in a revised form as §19 of the 49GAION Operating Protocol (`49GAION-protocol` pull request #36; `49GAION/DR-0016`). This draft is kept unedited below as history; the merged text governs.

**Draft for the 49GAION Operating Protocol · from `[ORG]AIOC-OCO` · blueprint `v0.4.0` · 15 October 2026 · not yet proposed.** Generalised: no organisation's name or data. If adopted, it would follow §13 as a new §14, under an unreleased version row of the Protocol CHANGELOG, with its Library card (`target-operating-model.part-card.json`, `DRAFT`, `last_result` `NOT_RUN`) and one TEST-TOM case for every rule. It changes no rule of §13; it names what §13, item 6 calls "the next stage". The full text of the part is the blueprint of `[ORG]AIOC-TOM` (`blueprint/TOM-BLUEPRINT.md` of its writing repository).

---

## 14. Target Operating Model: the second stage

**Addition (GOV, `<date of decision>`).** 49GAION Target Operating Model is a Library part (`library/cards/target-operating-model.part-card.json`). In an `[ORG]AION` it is the AIOC `[ORG]AIOC-TOM` (Naming Standard R2).

1. **The second part.** It is the stage after Source Lifecycle (§13, item 6). It designs the target operating model of an organisation of any shape: one person's work, a single entity, a group of entities, or a group with independent institutions inside it. Like every other part, it enters through OCO.
2. **What it takes.**
   - It takes only sources served by reference: by Source Lifecycle's output socket (§13, item 4), and by any other source through its own adapter, read only. Its Input socket hands the engine one versioned Input Pack (§5).
   - Nothing typed or spoken to it is a source, and nothing that arrives through a human port is a source.
   - A run starts only from a Design Request: a source in Source Lifecycle approved by the Requesting Authority. The Requesting Authority is the Cell carrying `[ORG]HOAC-GOV`, or a human Cell to which it has delegated the design decisions (Standard §4.4, item 8).
   - How fine the model is (light, standard or deep) is the Requesting Authority's to state in the Design Request, within a limit the TM Cell sets for cost.
3. **What it asks.**
   - What the sources do not answer, it asks of the Chief of Staff of `[ORG]AIOC-SL`, as a needs request: a sub-item of the run's Work Item (§4.6). A request is for a document, an explainer, a confirmation, a status, an export or a decision.
   - It never asks any person anything about the organisation, and a request never names a person.
   - One decision per row; at most 12 rows per pass. Silence, or approval of a whole pass, decides nothing.
   - A row only the Requesting Authority may decide is answered only by its Cell.
   - A row of a listed type is decided only with a valid signature at the tool gateway (§4.9; §4.10, items 7-10).
   - With every pass, it reports what is still missing, in the organisation's language.
4. **What it gives.**
   - A TOM Release: an operating model that names roles and what each decides. It does not say who fills a role, or how many people are needed. It covers capabilities, value streams, decision rights, interfaces, and the hand-offs between parts and with outside parties.
   - A role register: every role of the model, once, with what it decides, what it answers for and what it hands to whom. The next stage reads it first.
   - The release says nothing about how it was made, beyond its quality checks.
   - Every element is traced to its sources, and the release is decided element by element by the Requesting Authority.
   - The release is frozen and content-addressed. It is filed into Source Lifecycle as a source, and the next stage reads it there, never from the part.
5. **Its connection.**
   - It connects to Source Lifecycle under §13, item 5, with three scopes: unrestricted read; write only for its own filed releases and design reports; and needs requests.
   - Revocation cuts the connection at the gateway at once. The run is held, and no copy of a source's text is kept in its records.
6. **Assurance.**
   - Every stage's output is checked under a review rule of several independent engines from more than one family: each first alone, then in a short debate held to quotes, settled by code without a vote, with a human ruling on what stays contested. The frame and each part's design are written twice, separately, by authors of two families, and their differences are settled on the sources or put to the organisation. The model is walked through sealed situations. No unit grades its own work (Standard §2.3, item 9).
   - A material finding stops the release. It is put to the Requesting Authority with its choices; none is adopted until that decision.
7. **Other sources.** A source of another type may stand beside Source Lifecycle, read only, through its own adapter. Asking and filing stay with Source Lifecycle.
8. **Standing alone.** The release is a product on its own: an organisation may run it with people only, and stop there.
9. **The fixed test.** Every rule of this section has a case in TEST-TOM (v3). The card stays `DRAFT`, with `last_result` `NOT_RUN`, until the test has run once with recorded evidence (§10, item 3).

---

**What §13 would need beside this section.** The connection of item 5 relies on twelve additions to Source Lifecycle (`docs/INTAKE-WITH-SOURCE-LIFECYCLE.md` §9 of the writing repository). They are proposed to the Source Lifecycle part and its fixed test, not to this section.

*Powered by 49GAION*
