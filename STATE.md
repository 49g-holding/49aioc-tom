# State

| Item | State |
|---|---|
| Blueprint | `v0.6.0`, draft (16 October 2026): closed at v0.4.0, which added four features to v0.3.0 (`decisions/DR-0003`); v0.4.1 changed wording only: no natural person, positions only (`decisions/DR-0004`); v0.5.0 links it directly to the stages after it, and every return ends (`decisions/DR-0005`); v0.6.0 adds what the model also states and reads: the strategy frame, delivery model and maturity, critical streams, journeys, the value case, priority, and records of the work as it runs, never about a person (`decisions/DR-0006`; Annex H) |
| Template | 49GAION AIOC Blueprint Template `v1.5.0` at `06b00d9` |
| 49GAION versions | Standard `v1.5.0`; Protocol `v1.5.0`, with §13 (Source Lifecycle), §17 (Process and Position Design), §19 (this part) and §20 (Delivery and Implementation) on main under the unreleased `v1.6.0` row; signature list and the design return contract pinned in `contracts/PINS.json` |
| Protocol section on this AIOC | merged in a revised form as Protocol §19 (`49GAION-protocol` pull request #36; `49GAION/DR-0016`); the draft stays in `upstream/` as history |
| Library card | merged: `library/cards/target-operating-model.part-card.json` v1, `DRAFT`, `NOT_RUN`; this blueprint is its mother |
| Fixed test | TEST-TOM v5: 123 cases, TDL v5 (TDL-1 to TDL-8), path qualification, the walkthrough battery, the reviewer battery · `NOT_RUN` |
| Adapter | `ADP-SL` v1.1.0; TEST-TOM-ADP-SL v2 · `NOT_RUN` |
| Walkthrough instrument battery | not built · `NOT_RUN` (a build item; it gates the card's claim, never a run) |
| Reviewer battery | not built · `NOT_RUN` (a build item; it gates the card's claim, never a run) |
| Standard situation library | not built · `NOT_RUN` (a build item; it gates the card's claim, never a run) |
| Schemas between Pods | field lists closed (blueprint Annex E; `CARRIED-RULES.md`); JSON Schemas are build items |
| Contracts | 10 schemas, sound (2020-12). `tools/check_contracts.py --signature-list --design-return`, 16 October 2026: 32 valid and 56 must-fail examples, 20 adapter fixtures and 10 lint fixtures as expected; the catalogue seed (7 patterns) valid and with no lint hit, and its pin checked (check 10); the listed-type subset check against the pinned signature list run; 4 design return examples valid against the pinned Library contract (check 11); the release lint on `docs/OUTPUT.md` 0 hits; **0 failures** |
| Unit cards | 26 Pod and Cell cards, generated from blueprint §17. `tools/make_cards.py`, 16 October 2026: 26 unit cards written, the AIOC card checked, valid against `unit-card.schema.json` and the code rules; **0 errors** |
| Bot identity cards | 18 (one for each AI Cell). `tools/make_cards.py`, 16 October 2026: 18 written, valid against `bot-identity-card.schema.json`; no shared credential; none signs; **0 errors** |
| Engine register | held at the tool gateway; to be set by GOV and the TM Cell (blueprint §13, H-05: at least four families) |
| Reference-model catalogue | proposed to 49GAION (`upstream/REFERENCE-MODEL-CATALOGUE.md`); not in the Library; every run declares it unavailable until it is pinned (H-34) |
| Code project | started: the earlier chain's files kept under `legacy/` as a case study, read only; PRD v0.3 |
| Joining | blocked until Source Lifecycle accepts the thirteen additions of `docs/INTAKE-WITH-SOURCE-LIFECYCLE.md` §9 and declares them on its card (gate T0), and until the engine register holds eligible engines (T0 (g)) and two author families (T0 (j)) |
| Links to the stages after it | release notices to `[ORG]AIOC-PPD`; returns from `[ORG]AIOC-PPD` and `[ORG]AIOC-DI` (blueprint §5.10). Their connections are signed by this AIOC's `[ORG]HOAC-ACS` position (H-35); this AIOC stands alone without them |
| Installed in any `[ORG]AION` | no |

The four features proposed for later in v0.3.0 are in v0.4.0 (`decisions/DR-0003`).

*Powered by 49GAION*
