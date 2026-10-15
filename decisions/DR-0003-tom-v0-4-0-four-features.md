# DR-0003 · TOM v0.4.0: four features added

- **Date:** 2026-10-15
- **Decided by:** the direction of the governing seat, given to `[ORG]AIOC-OCO`, that the four features proposed for later are added now, so that the whole is built at once (the decider is recorded in the private holders register); and `[ORG]AIOC-OCO`'s choices within that direction, below. This is a decision on this repository only, not a decision of 49GAION.
- **Recorded by:** `[ORG]AIOC-OCO`
- **Status:** in force for this repository's draft
- **Supersedes, in part:** the list "Proposed and not taken into v0.3.0" of `DR-0002`. Nothing else of `DR-0002`.

## Decision

1. **A role register.** One release part lists every role-type once: what it decides, what it is accountable for, where it appears, and the hand-offs it sends and receives. It is made by code at S6 from the decided ledgers and registers, reviewed at RP6 and decided by the Requesting Authority as elements. Conflicts are role findings, never merged. It names roles, never people, and is what the next stage reads first.
2. **A run depth.** `light`, `standard` or `deep`. It changes only grain and volume above the floors; it never removes a stage, capability, gate or check, never lowers a review, and never changes how the organisation is asked.
3. **Two authors at S1 and S5.** Two authors of two families write blind; code compares; a reconciler makes one version; differences are settled on the sources, put to the organisation, or held open at the coarser grain, and every material difference reaches the stage's review.
4. **Reference models.** A catalogue of operating-model patterns is proposed to the 49GAION Library. Design may use a pattern as a method, never as evidence: an element resting on a pattern alone is `assumed`, and the release shows the reliance in plain words.
5. **Nothing of v0.3.0 is removed or weakened.** TEST-TOM becomes v3 (cases 85–99 and TDL-7), before any use.

## Choices made by `[ORG]AIOC-OCO`

- **(a)** The Requesting Authority states the depth in the Design Request; the TM Cell limits it for cost (default `standard`); a depth above the limit fails T0 and is never lowered silently; the Design Lead neither sets nor changes it.
- **(b)** Three new Cells: the Second Request Analyst, the Frame Reconciler and the Second Designer. At S5 the Ledger Reviser reconciles before it revises.
- **(c)** The reconciler runs on one of the two author families, in turn, so an output has exactly two author families; the engine register needs four families (H-05 changed).
- **(d)** S1 always has two authors. S5 runs with one only where two would lower its review, with the TM Cell's permission (default `no`) and the Design Lead's acceptance, declared in the quality checks.
- **(e)** Every material difference is a checked item of its review; one held open is also a `MINOR` finding raised by code; one only the organisation can settle is a decision row; a design difference is never asked.
- **(f)** The role register is compiled at S6 and is not a model of the whole.
- **(g)** Until 49GAION holds a catalogue and it is pinned, every run declares it unavailable.
- **(h)** A contract whose content changes takes `:v0.4`; the others keep `:v0.3`.

## Source

The direction of the governing seat given to `[ORG]AIOC-OCO` on 15 October 2026; the four features proposed by the reviews of v0.2.0 (DR-0002); `[ORG]AIOC-OCO`'s change specification of 15 October 2026.

*Powered by 49GAION*
