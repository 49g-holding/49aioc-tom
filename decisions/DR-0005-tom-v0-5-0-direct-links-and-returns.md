# DR-0005 · TOM v0.5.0: direct links to the stages after it; every return ends

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV), in conversation with `[ORG]AIOC-OCO` (the decider is a position)
- **Source:** the directions of GOV of 15 October 2026, recorded at 49GAION as `49GAION/DR-0016` (items 4 and 5) and `49GAION/DR-0018`: Process and Position Design "is linked to the target operating model itself, because it may have defects and go back and forth"; and "whatever is returned must have a back-and-forth process until it is answered and finalised: a loop until a decision is made, not left open; either it leads to a decision, or it is set aside and carried forward so that the output arrives" (translated). The approval of Delivery and Implementation as a Library part, whose returns also reach this stage (`49GAION/DR-0017`, item 8). And the direction of GOV of 16 October 2026 to connect the chain in this order, so that the blueprints, engineering and documents of the human cycle are complete (translated).
- **Relation:** builds on DR-0001 to DR-0004; it supersedes nothing. It completes DR-0004, item 2, at gate T0.

## Decision

1. **Told directly.** On every filing of a decided release, this AIOC also sends a release notice to `[ORG]AIOC-PPD`, by reference: the release ID, version and manifest hash, the filed reference, the final-status decision reference, the release it supersedes and the returns it answers (`contracts/release-notice.schema.json`; blueprint §5.9, step 8a). The release itself lives only in Source Lifecycle.
2. **Returns come back directly.** This AIOC receives the returns of `[ORG]AIOC-PPD` and `[ORG]AIOC-DI` on elements of its releases, under the Library's design return contract, pinned by commit and hash in `contracts/PINS.json` (blueprint §5.10). It keeps no copy of the contract.
3. **Every return ends.** A return is answered by a new decided release (a continuation run), or by a decision of the Requesting Authority, or set aside by that decision and carried forward as a known defect or a decided assumption, or withdrawn by its sender. It has rounds, a deadline for each, and escalation to the Requesting Authority and the Cell carrying `[ORG]HOAC-TM`. Silence never ends it. A filed release is never edited.
4. **No self-grading.** The return brief is made by code. The Chief of Staff never answers or classifies a return; the Requesting Authority answers it, and the TOM Design Lead classifies it as a defect of this AIOC or as normal discovery.
5. **The mother.** This blueprint is the mother blueprint of the Library part 49GAION Target Operating Model (`49GAION/DR-0016`, item 7).
6. **Wording, under `49GAION/DR-0015`.** Two positions are two parties: gate T0 checks that the Requesting Authority's Cell is not the TOM Design Lead's Cell, and nothing reads who occupies either. No text of this AIOC states a number of people, even to deny one.
7. **What changes.** Blueprint §0, §1, §2, §4.2, §4.4, §5.0, §5.9, §5.10 (new), §6, §8 to §10, §12 to §15, §17, Annexes C, D and E (E.20 to E.22, new); `docs/OUTPUT.md`, `docs/CARRIED-RULES.md` §4.4, `docs/DESIGN-BASIS.md`, `docs/INTAKE-WITH-SOURCE-LIFECYCLE.md`; the release notice contract and its examples; the pin and check 11 of the design return contract; TEST-TOM v4 (cases 100–108, TDL-8); the cards.

*Powered by 49GAION*
