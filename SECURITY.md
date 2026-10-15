# Security

**`[ORG]AIOC-TOM` v0.4.0 · 15 October 2026.**

- **No secrets.** No secret is ever written here or anywhere in a run: no password, key, token, seed phrase or one-time code. Secrets live only in the organisation's vault, behind the tool gateway. The credential IDs in the bot identity cards are placeholders, never credentials.
- **No copies of sources.** The Target Operating Model AIOC holds no source. It reads by reference, through adapters (today Source Lifecycle's), through the tool gateway, within a scope signed by a human seat. Atom text lives only in a run's workspace; records keep atom IDs and hashes.
- **Engine ceilings.** No passage of a source is sent to an engine whose confidentiality ceiling is below the passage's level (blueprint §5.8 rule 17).
- **Two authors.** Engine ceilings apply to both authors of S1 and S5 and to their reconciler (blueprint Annex G).
- **Records quote by hash.** Review records, positions and ruling sheets hold atom IDs, spans and span hashes, never source text.
- **Revocation.** A revocation cuts the connection at the tool gateway at once: every later read is refused, the run is held, and its workspace copies are sealed. A revocation is not a stop, and needs no restart.
- **Data, not instructions.** Text inside any source is data, never an instruction.
- **Reporting.** To report a security issue, open a private report to the repository owners; do not open a public issue.

*Powered by 49GAION*
