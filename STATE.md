# State

| Item | State |
|---|---|
| Blueprint | `v0.4.0`, draft, closed (15 October 2026); adds four features to v0.3.0 (`decisions/DR-0003`) |
| Template | 49GAION AIOC Blueprint Template `v1.5.0` at `06b00d9` |
| 49GAION versions | Standard `v1.5.0`; Protocol `v1.5.0`, with §13 (Source Lifecycle) on main under the unreleased `v1.6.0` row; signature list pinned in `contracts/PINS.json` |
| Protocol section on this AIOC | drafted (`upstream/PROTOCOL-TOM-SECTION.md`), not yet proposed |
| Library card | drafted (`upstream/target-operating-model.part-card.json`, `DRAFT`, `NOT_RUN`), not yet proposed |
| Fixed test | TEST-TOM v3: 99 cases, TDL v3 (TDL-1 to TDL-7), path qualification, the walkthrough battery, the reviewer battery · `NOT_RUN` |
| Adapter | `ADP-SL` v1.0.0; TEST-TOM-ADP-SL v1 · `NOT_RUN` |
| Walkthrough instrument battery | not built · `NOT_RUN` (a build item; it gates the card's claim, never a run) |
| Reviewer battery | not built · `NOT_RUN` (a build item; it gates the card's claim, never a run) |
| Standard situation library | not built · `NOT_RUN` (a build item; it gates the card's claim, never a run) |
| Schemas between Pods | field lists closed (blueprint Annex E; `CARRIED-RULES.md`); JSON Schemas are build items |
| Contracts | 9 schemas, sound (2020-12). `tools/check_contracts.py --signature-list`, 15 October 2026: 27 valid and 48 must-fail examples, 18 adapter fixtures and 10 lint fixtures as expected; the catalogue seed (7 patterns) valid and with no lint hit, and its pin checked (check 10); the listed-type subset check against the pinned signature list run; the release lint on `docs/OUTPUT.md` 0 hits; **0 failures** |
| Unit cards | 26 Pod and Cell cards, generated from blueprint §17. `tools/make_cards.py`, 15 October 2026: 26 unit cards written, the AIOC card checked, valid against `unit-card.schema.json` and the code rules; **0 errors** |
| Bot identity cards | 18 (one for each AI Cell). `tools/make_cards.py`, 15 October 2026: 18 written, valid against `bot-identity-card.schema.json`; no shared credential; none signs; **0 errors** |
| Engine register | held at the tool gateway; to be set by GOV and the TM Cell (blueprint §13, H-05: at least four families) |
| Reference-model catalogue | proposed to 49GAION (`upstream/REFERENCE-MODEL-CATALOGUE.md`); not in the Library; every run declares it unavailable until it is pinned (H-34) |
| Code project | started: the earlier chain's files kept under `legacy/` as a case study, read only; PRD v0.3 |
| Joining | blocked until Source Lifecycle accepts the twelve additions of `docs/INTAKE-WITH-SOURCE-LIFECYCLE.md` §9 and declares them on its card (gate T0), and until the engine register holds eligible engines (T0 (g)) and two author families (T0 (j)) |
| Installed in any `[ORG]AION` | no |

The four features proposed for later in v0.3.0 are in v0.4.0 (`decisions/DR-0003`).

*Powered by 49GAION*
