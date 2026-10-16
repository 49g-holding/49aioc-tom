# Design return examples of this AIOC

Examples of returns as this AIOC receives and answers them (blueprint §5.10). They are checked against the Library's design return contract at the version pinned in `contracts/PINS.json` (`tools/check_contracts.py`, check 11). The contract and its must-fail examples live only in `49GAION-protocol`; this AIOC keeps no copy of it.

| File | What it shows |
|---|---|
| `answer.accepted.json` | an `accepted` return, ended at once as `answered by release` by the release it names (§5.10, limit 3) |
| `answer.set-aside.json` | a return set aside by decision in its second round, carried forward on a decided assumption |
| `answer.by-release.json` | a return from Delivery and Implementation answered by a new release |
| `return.from-di-open.json` | a return from Delivery and Implementation, open in its first round, filed in Source Lifecycle |

*Powered by 49GAION*
