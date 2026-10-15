# Contributing

**`[ORG]AIOC-TOM` v0.4.0 · 15 October 2026.**

1. **One change, one pull request**, reviewed by someone other than its writer.
2. **Positions, never people.** No person's name in any file; holders are kept only in an organisation's private holders register.
3. **No organisation data.** This repository is written for any organisation. An organisation's values, sources and run records live in its own records repository. The register of any earlier, private texts lives in the organisation's code project.
4. **Cite every rule** to its source: a 49GAION text by section and version, a carried rule by `docs/CARRIED-RULES.md` section. Never invent a fact, a version, a score or an appointment. `NOT_RUN` is never PASS.
5. **The blueprint governs the cards.** Edit the card data block of blueprint §17 only, then run `python3 tools/make_cards.py <49GAION-protocol/spec/schemas>`. It must report 0 errors: 26 unit cards and 18 bot cards.
6. **Contracts are schemas.** A change to `contracts/` keeps every example as expected and adds a valid or must-fail example for any new case. `python3 tools/check_contracts.py --signature-list <path> [--catalogue <path>]` must report 0 failures. A new must-fail example has its entry in `contracts/examples/MUST-FAIL-REASONS.json`.
7. **Decided texts are never edited.** A change is a new version that names what it supersedes.
8. **English only, plain and short.**
9. **A new source type** is a new adapter file, its fixtures and its test, and a row in `adapters/README.md`. No stage text changes.
10. **The release lint deny-list** gains a word by a tested change; a word is removed only as `change-fixed-test-or-threshold`.
11. **A reference-model catalogue version** is taken into use only by changing its pin in `contracts/PINS.json`, as a tested change made through OCO (blueprint §13, H-34).

*Powered by 49GAION*
