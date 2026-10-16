# Proposals to 49GAION from the Target Operating Model work

**From `[ORG]AIOC-OCO` · 15 October 2026 · drafts.** State on 16 October 2026: item 1 is merged in a revised form (Protocol §19, the Library card and Standard §3.1, item 4; `49GAION-protocol` pull request #36, `49GAION` pull request #68, `49GAION/DR-0016`). Items 3 to 9 are merged in a revised form: item 3 as Naming Standard R9 (`49GAION/DR-0021`); items 4, 5 and 8 as Protocol §13, items 9 and 10, and the reading note on connectors in `unit-card.schema.json`; items 6 and 7 as Standard §4.4, item 11 (`49GAION/DR-0020`); item 9 as Standard §3.1, item 1, and `library/reference-models/` (`49GAION/DR-0022`) (`49GAION` pull request #69; `49GAION-protocol` pull requests #38 and #39). Item 2 is held: bound to HF-03 under Standard §4.4, item 8, it would make the Design Lead's position sign instead of the Requesting Authority; until its own decision, H-04 stands. Item 10 is proposed with v0.6.0. Generalised: no organisation's name or data. Each proposal reaches 49GAION only as a pull request, merged on the decision of the governing seat (GOV) of 49GAION.

## 1. The Target Operating Model as a Library part and a Protocol section

- **Current text.** Protocol §13, item 6: "Then the next stage starts." No part is named as that stage. The Library has no Target Operating Model part.
- **Proposed text.** A new Protocol §14 and the Library card `library/cards/target-operating-model.part-card.json` (`DRAFT`, `NOT_RUN`), both drafted in this folder (`PROTOCOL-TOM-SECTION.md`, `target-operating-model.part-card.json`). Also a reading note under §13, item 6: "The next stage is proposed in §14."
- **Reason and evidence.** Every organisation needs a decided target operating model before positions and job descriptions, and the stages after them, can be designed. The blueprint of `[ORG]AIOC-TOM` has been reviewed in two rounds by independent seats and closed at v0.3.0.
- **Parts and tests affected.** Protocol §13, §14; the Library cards README; TEST-TOM v3. The card schema check (`card-schema-test`) must pass on the new card.

## 2. A listed type for accepting an operating model

- **Current text.** The Standard's signature list (`upstream/human-floor-signature-types.json`) has no type for accepting a design stage. Only `set-purpose-or-values` (HF-04) covers part of what the Requesting Authority decides on a TOM Release.
- **Proposed text.** Add `accept-operating-model`, `human_floor` HF-03, with the note: "the final-status decision on a TOM Release, by the Requesting Authority's Cell". Until it is listed, an `[ORG]AION` adds it under `decision_types` in its own list (Protocol §4.9, item 4). Until it is listed, the TOM contracts carry it as `org_listed_type`; the `listed_type` enums hold only types a TOM decision can be (a subset of the pinned list, checked in CI).
- **Reason and evidence.** The decision binds the organisation's operating model, and mandatory human oversight (HF-03) applies to it. Without a listed type, the gateway cannot require a signature for it.
- **Parts and tests affected.** The signature list; `signature-types-floor`; Standard §4.4, item 10 (coverage); TEST-TOM case 36.

## 3. Naming Standard R9: three gaps

- **Current text.** "AIOC | `<org>aioc-<abbr>`, with `-records` and `-records-restricted` as needed … A repository is recorded before it is created."
- **Proposed text.**
  - (a) **Visibility.** "The writing repository of an AIOC may be public only when it holds no organisation data; `-records` and `-records-restricted` are never public."
  - (b) **Where it is recorded.** "A repository is recorded before it is created, as an event on the AIOC's entry in the unit register, with its name, its visibility and its platform."
  - (c) **A mother and an instance.** "Where an AIOC's writing repository is also proposed as a Library mother, the Library card points to it; the mother carries no organisation data, and the organisation's own copy of its values lives in its records repository."
- **Reason and evidence.** The rule says a repository is recorded first, but not where. Nothing says whether a writing repository may be public. And nothing separates a mother text, written for any organisation, from an organisation's instance of it. All three questions arose in this work.
- **Parts and tests affected.** Naming Standard R9; `registers/HOAC-REGISTER.md` (an event type for a repository); `no-org-names` (unchanged).

## 4. Where a connection's access is managed

- **Current text.** `unit-card.schema.json`, `anatomy.connectors[].access_managed_in`: `{"const": "panel"}`, "access managed in the Panel".
- **The conflict.** Protocol §13, item 5 and Standard §4.4, item 7 have a connection signed at the tool gateway, as `connect-external-port`, by a labelled human seat.
- **Proposed text.** A reading note in the schema description: "The Panel shows the connection and requests it; the grant itself is signed at the tool gateway as `connect-external-port` (Standard §4.4, item 7; Protocol §13, item 5)." Optionally, widen the value to `{"enum": ["panel", "tool gateway"]}`.
- **Reason and evidence.** The blueprint of `[ORG]AIOC-TOM` must write `panel` to pass the schema, although its grant is signed at the gateway.
- **Parts and tests affected.** `unit-card.schema.json`; `card-schema-test`; the template §1 card.

## 5. Twelve additions to Source Lifecycle

- **Current text.** Protocol §13, items 4-6 and TEST-SOURCE-LIFECYCLE cases 1-16.
- **Proposed text.** The twelve additions SL-A1 to SL-A12 of `docs/INTAKE-WITH-SOURCE-LIFECYCLE.md` §9, each with its acceptance test:
  - needs-request intake;
  - routing;
  - outcomes and states;
  - explainer templates as configuration;
  - confirmation, status and decision rows;
  - listed-type rows at the gateway;
  - reference fields (SL-A7: an export carries its date);
  - snapshot pinning (SL-A8 as amended: a needs answer is read at its own snapshot, and a snapshot named by a filed release stays readable);
  - filing by a connected part;
  - the organisation-design grant;
  - notices to connected parts;
  - the published sockets contract.
- **Reason and evidence.** Without them, the next stage cannot ask through Source Lifecycle in a way that keeps the Protocol's status list, the signature rules and the statement labels. The reviews of the TOM blueprint found each gap.
- **Parts and tests affected.** The Source Lifecycle Library card and its README; TEST-SOURCE-LIFECYCLE (one new case per addition); Protocol §13.

## 6. Binding an engine is not a change of filler

- **Current text.** Standard §4.4, item 3 (`change-filler`) and item 8 (bots). Neither says anything about the engine behind a bot.
- **Proposed text.** A reading note under §4.4: "The engine a bot's calls run on is bound by the tool gateway under its engine register (§4.4 item 11). Binding or changing that engine is gateway policy, not a change of filler. An engine may serve a Cell only after passing that Cell's fixed test at its current version (§3.2 item 2; §4.4 item 4)."
- **Reason and evidence.** A seat that draws a different engine for each review would otherwise need a signature for each review, and would lose its memory each time.
- **Parts and tests affected.** Standard §4.4; the bot-identity-card schema description; TEST-TOM cases 53 and 59.

## 7. The engine register at the tool gateway

- **Current text.** Standard §4.4, item 11: the tool gateway holds its policy, its map from tool calls to decision types and its keys, changed only under `change-gateway-policy`. Protocol §10, item 6: the gateway meters every call. No text names a register of engines, their families or their confidentiality ceilings. UNVERIFIED: the Standard and Protocol texts at `v1.5.0` were not read again for this draft; the copies and notes of the 49GAION texts held by `[ORG]AIOC-OCO` mention no such register.
- **Proposed text.** The fields of blueprint Annex E.12 as the gateway's register of engines, changed only under `change-gateway-policy`.
- **Reason and evidence.** Several parts need eligible engines by family and by confidentiality ceiling, and the gateway already holds the keys and meters the calls (Protocol §10, item 6).
- **Parts and tests affected.** Standard §4.4, item 11; Protocol §10; a gateway test.

## 8. Protocol §13, item 7: the asking route

- **Current text.** "…replace it or stand beside it".
- **Proposed text.** "An equivalent source may stand beside Source Lifecycle, read only, through the reading part's own adapter. Asking and filing stay with Source Lifecycle. If a part ever replaces Source Lifecycle, this section must name the new asking route."
- **Reason and evidence.** A part that reads several sources still needs one route to the organisation's people.
- **Parts and tests affected.** Protocol §13; the GOV list (H-08).

## 9. A reference-model catalogue in the Library

- **Current text.** Standard §3.1, item 1: "The 49GAION Library holds all ready-made AIOC blueprints and part cards." No Library text holds operating-model patterns.
- **Proposed text.** (a) Standard §3.1, item 1: "The 49GAION Library holds all ready-made AIOC blueprints and part cards, and the method catalogues that blueprints read, such as the reference-model catalogue. A method catalogue holds no organisation's data and is never evidence about an organisation." (b) The catalogue, `library/reference-models/reference-model-catalogue.json` of `49GAION-protocol`, with a plain README, in the format and with the seed of `REFERENCE-MODEL-CATALOGUE.md` and `reference-model-catalogue.seed.json` in this folder; `status` `draft`, version `v0.1.0`. Its format is the field list of blueprint Annex E.19.
- **Reason and evidence.** The blueprint of `[ORG]AIOC-TOM` lets Design use a known pattern only as a labelled method held by the Library. Without a Library text, an organisation either invents patterns or uses none. The case study named such a catalogue as a concept and never built it.
- **Parts and tests affected.** Standard §3.1; the Library cards README; a CI check that the catalogue validates against its format and holds no organisation name (`no-org-names`); TEST-TOM v3 cases 96–99.

## 10. What a decided operating model also states, and records of the work as it runs

- **Current text.** Protocol §19 names the parts of a Target Operating Model release and its links; it says nothing of the strategy the model serves, how each capability is delivered, how mature it is, which streams are critical, outside parties' journeys, a value case, a priority per element, or records of the work as it runs. Standard §3.1, item 4, names the part.
- **Proposed text.** (a) Standard §3.1, item 4, a sentence: "A Target Operating Model release also states the organisation's strategy on one page, how each capability is delivered and how mature it is, which value streams are critical, each outside party's journey, a value case and a priority per element: each from the organisation's sources or decisions, never written by the part; and it may read records of the work as it runs, by role-type and process only, never about a person." (b) Protocol §19, new items: the strategy frame, decided in one row and never blocking; delivery model and make-or-buy, never naming a provider; criticality on a closed list of reasons; maturity now from sources only, target from sources or decisions; journeys from declared crossings only; the value case by code; priority by a fixed rule, decided with each element; records of the work admitted only as the organisation's projection, after its impact assessment and its data-protection decision (HF-17), with the refusal `person-level records`. (c) Protocol §13, a new item: Source Lifecycle records such an export only as that projection, and may serve an organisation dictionary by reference. (d) Protocol §17 and §20: the next stages read these parts.
- **Reason and evidence.** A study of comparable products found each feature in common use; the stages after this one need them to start (their objectives, their order, their workload reading, their register of value). Each is placed where it belongs, from sources and decisions only.
- **Parts and tests affected.** Standard §3.1, item 4; Protocol §13, §17, §19, §20; the Library cards of Target Operating Model, Process and Position Design, Delivery and Implementation and Source Lifecycle; TEST-TOM v5 cases 109–123.

*Powered by 49GAION*
