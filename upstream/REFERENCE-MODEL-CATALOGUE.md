# The reference-model catalogue

**Draft for the 49GAION Library · from `[ORG]AIOC-OCO` · blueprint `v0.4.0` · 15 October 2026 · not yet proposed.** Generalised: no organisation's name or data. Plain descriptions of widely known ways to organise; no text is copied from any source.

## 1. What it is

A catalogue of operating-model patterns: widely known ways to organise, each with its typical capabilities, its decision rights by role-type, its typical hand-offs, when it fits and when it does not, and its known risks. A design may read it as a method, never as evidence about an organisation. It is read by version and hash, and it changes only by a new version.

## 2. The format

The field list of blueprint Annex E.19. The machine form is `reference-model-catalogue.seed.json` in this folder, valid against `contracts/reference-model-catalogue.schema.json` of the writing repository.

| Field | Type | Req | Meaning |
|---|---|---|---|
| `catalogue` | const `49GAION Reference-Model Catalogue` | yes | |
| `version` | `^v[0-9]+\.[0-9]+\.[0-9]+$` | yes | |
| `status` | enum `draft`, `released` | yes | |
| `rules` | array of string, minItems 1 | yes | the use rules every reader keeps |
| `patterns` | array, minItems 1 | yes | |
| pattern.`pattern_id` | `^RMP-[A-Z0-9-]{2,24}$` | yes | stable; never reused |
| pattern.`name` | string, 1 to 80 characters | yes | plain; the only part of a pattern that reaches a release |
| pattern.`summary` | string | yes | |
| pattern.`typical_capabilities` | array of string, minItems 1 | yes | |
| pattern.`decision_rights` | array of `{decision, role_type}`, minItems 1 | yes | by role-type, never a person |
| pattern.`typical_hand_offs` | array of `{from, to, what_crosses}`, minItems 1 | yes | |
| pattern.`fits_when`, `does_not_fit_when`, `known_risks` | arrays of string, minItems 1 | yes | |
| pattern.`never_evidence` | const "This pattern is never evidence for an organisation." | yes | |

## 3. The rules

1. A pattern is a method. It may suggest a structure; it never states a fact about an organisation.
2. Every element a pattern suggests still needs the organisation's own evidence. Without it, the element is an assumption, with what breaks if it is false.
3. A pattern never raises the label of a statement, never closes an unknown and never settles a contradiction.
4. A pattern names role-types, never persons, holders or numbers of people.
5. This catalogue holds no organisation's data and no copied text. Each pattern is a plain description of a widely known way to organise.

## 4. The seed (v0.1.0, draft)

### 4.1 Functional organisation (`RMP-FUNCTIONAL`)

Work is grouped by kind of expertise, such as sales, operations, finance and people. Each function has one accountable lead, and the top role joins the functions together.

**Typical capabilities.**
- Direction and governance
- Sales and customer relations
- Operations or delivery
- Finance
- People
- Support services, such as legal, premises and information

**Decision rights, by role-type.**

| Decision | Role-type |
|---|---|
| Overall direction and priorities | the top role |
| The budget across functions | the top role, advised by the finance lead |
| Methods and standards inside a function | the function lead |
| Hiring inside an approved budget | the function lead |

**Typical hand-offs.**

| From | To | What crosses |
|---|---|---|
| sales | operations | a confirmed order or commitment to deliver |
| operations | finance | delivery records for billing |
| every function | finance | spending requests inside the budget |
| people | every function | new staff ready to work |

**When it fits.**
- There is one main line of products or services.
- The organisation serves one market or a few similar ones.
- Depth of expertise matters more than speed across functions.

**When it does not.**
- There are several distinct product lines or markets that need their own priorities.
- Most work needs fast coordination across many functions every day.

**Known risks.**
- Each function serves its own goals before the whole.
- Decisions that cross functions are slow and pile up at the top role.
- No one owns a customer's whole experience.

*This pattern is never evidence for an organisation.*

### 4.2 Divisional organisation (`RMP-DIVISIONAL`)

The organisation is split into divisions by product, market, customer group or region. Each division holds most of the functions it needs and answers for its own results, under a small centre.

**Typical capabilities.**
- Direction of the whole and allocation of capital, at the centre
- Rules for the whole, such as financial reporting, risk and legal, set at the centre
- In each division: its sales, its delivery and its management
- Review of each division's results

**Decision rights, by role-type.**

| Decision | Role-type |
|---|---|
| The strategy of the whole, and capital between divisions | the top role at the centre |
| A division's plan and operations, inside its targets | the division lead |
| Policies that bind every division, such as finance, risk and legal | the centre's function leads |
| Prices and offers inside a division | the division lead |

**Typical hand-offs.**

| From | To | What crosses |
|---|---|---|
| the centre | a division | targets, capital and the policies that bind it |
| a division | the centre | results and forecasts |
| a division | another division | shared customers or internal supply, on agreed terms |

**When it fits.**
- Products, markets or regions differ enough to need their own priorities.
- Each division is large enough to carry its own functions.
- Results can be measured division by division.

**When it does not.**
- The organisation is too small to repeat functions in each division.
- The products share most of their customers and their ways of working.

**Known risks.**
- Functions are repeated in every division, at a cost.
- Divisions compete for customers or resources.
- The centre loses sight of risks that cross divisions.
- Practices drift apart between divisions.

*This pattern is never evidence for an organisation.*

### 4.3 Matrix organisation (`RMP-MATRIX`)

Two lines of accountability cross: one by function or expertise, one by product, project, market or region. Many roles answer to both, so the decision rights must say which line decides what.

**Typical capabilities.**
- Function leadership: standards, expertise and people
- Product, project or market leadership: priorities and results
- Joint planning of people's time
- Settling conflicts between the two lines

**Decision rights, by role-type.**

| Decision | Role-type |
|---|---|
| What is delivered, and when | the product, project or market lead |
| How the work is done, and its quality standards | the function lead |
| How people's time is shared | the two leads jointly, under a rule agreed in advance |
| A conflict the two lines cannot settle | a named role above both lines |

**Typical hand-offs.**

| From | To | What crosses |
|---|---|---|
| a function | a product, project or market | people and expertise assigned |
| a product, project or market | a function | demand and priorities |
| both lines | the role above both | conflicts they could not settle |

**When it fits.**
- The work needs both deep expertise and a strong focus on products, projects or markets.
- Scarce experts must be shared.
- The organisation can afford the effort of coordination.

**When it does not.**
- The decision rights of the two lines cannot be written down clearly.
- The organisation is small, and a second line adds effort without benefit.

**Known risks.**
- Accountability becomes unclear.
- Decisions slow down, and the two lines come into conflict.
- Coordination takes a large share of everyone's time.
- People are caught between two leads.

*This pattern is never evidence for an organisation.*

### 4.4 Shared-service centre (`RMP-SHARED-SERVICE`)

Common support work, such as finance processing, people administration, purchasing or information services, is done once, in one centre, for several units, under agreed service terms.

**Typical capabilities.**
- Delivery of the shared services to the units served
- Service terms and demand
- Reporting on service against its terms
- Improvement of the shared ways of working

**Decision rights, by role-type.**

| Decision | Role-type |
|---|---|
| Which services are shared, and their scope | the role with authority over all the units served, or, between independent entities, their agreement |
| Service terms: levels, charges and priorities | the centre lead and the units served, agreed under that authority |
| How a service is delivered | the centre lead |
| Whether a unit may leave a shared service | the same authority that decided the service is shared |

**Typical hand-offs.**

| From | To | What crosses |
|---|---|---|
| a unit | the centre | requests, and the information the service needs |
| the centre | a unit | the completed service and its records |
| the centre | the deciding authority | service results against the agreed terms |

**When it fits.**
- Several units need the same support work, and most of it is standard.
- Gains in scale or consistency are worth the extra hand-offs.
- Service terms can be stated and checked.

**When it does not.**
- The support work differs a great deal between units, or must sit close to each unit's daily work.
- Too few units share the work to gain from scale.

**Known risks.**
- The centre drifts away from the units' needs.
- Disputes arise over service terms and charges.
- Units build their own hidden copies of the service.
- One failure in the centre reaches every unit at once.

*This pattern is never evidence for an organisation.*

### 4.5 Holding with independent subsidiaries (`RMP-HOLDING`)

A parent owns several subsidiaries. Each runs as an independent entity, with its own management and its own governing body. The parent acts as owner, not as operator.

**Typical capabilities.**
- Ownership and allocation of capital, at the parent
- Appointing and overseeing each subsidiary's governing body, as owner
- Reporting and accounts for the whole group
- In each subsidiary: its own complete operating model

**Decision rights, by role-type.**

| Decision | Role-type |
|---|---|
| Buying, selling or funding a subsidiary | the parent's governing body |
| Appointing a subsidiary's governing body | the parent, as owner, through the subsidiary's own rules |
| A subsidiary's strategy and operations | that subsidiary's own governing body and management |
| Reporting rules for the whole group | the parent, within what the law and each subsidiary's own rules allow |

**Typical hand-offs.**

| From | To | What crosses |
|---|---|---|
| a subsidiary | the parent | results and the reports owed to the owner |
| the parent | a subsidiary | capital and owner decisions, through the subsidiary's own governing body |
| a subsidiary | another subsidiary | dealings on agreed terms, as between independent parties |

**When it fits.**
- The businesses differ enough to need their own management.
- Legal, regulatory or risk separation between them is needed.
- The owner wants to be able to buy or sell a business as a whole.

**When it does not.**
- The businesses depend on each other every day and need shared operations.
- The parent wants to direct operations itself.

**Known risks.**
- The parent directs operations informally and blurs the separation.
- Costs are repeated in each subsidiary.
- The owner's oversight of each subsidiary's risks is weak.
- Dealings between subsidiaries drift away from agreed terms.

*This pattern is never evidence for an organisation.*

### 4.6 Platform with business units (`RMP-PLATFORM`)

A central platform provides common capabilities, such as customer access, technology, data, payments or brand, and several business units build their own offers on it. The units own their markets and results; the platform owns the shared capabilities.

**Typical capabilities.**
- The platform's capabilities, offered to the units
- The platform's plan and priorities
- In each unit: its offer, its customers and its results
- Rules for using the platform: access, standards and charges

**Decision rights, by role-type.**

| Decision | Role-type |
|---|---|
| What the platform offers, and in what order | the platform lead, after hearing the units' demand under an agreed rule |
| A unit's offer and market | the unit lead |
| The standards a unit must meet to use the platform | the platform lead |
| A dispute over the platform's priorities | a named role with authority over both, or, between independent entities, their agreement |

**Typical hand-offs.**

| From | To | What crosses |
|---|---|---|
| the platform | a unit | a platform capability ready to use |
| a unit | the platform | demand, feedback and use |
| a unit | the platform | charges or contributions, where agreed |

**When it fits.**
- Several units need the same core capabilities and gain from sharing them.
- The units serve different markets.
- The shared capability would be costly to build twice.

**When it does not.**
- The units need very different underlying capabilities.
- The platform cannot be run as a service to the units.
- Using the platform would turn the units into internal functions of the platform, against their own autonomy.

**Known risks.**
- The platform becomes a bottleneck.
- The units lose their autonomy to the platform's priorities.
- Charges for the platform are unclear.
- One failure of the platform stops every unit.

*This pattern is never evidence for an organisation.*

### 4.7 Single-person practice (`RMP-SOLO`)

One person does or directs all the work, with clients, suppliers, advisers and authorities at the boundary. The roles are hats the one person wears, so the model names each role-type the person holds and what each decides.

**Typical capabilities.**
- Finding and agreeing work with clients
- Doing the work
- Administration and finance
- Keeping skills and permissions current
- Managing outside suppliers and advisers

**Decision rights, by role-type.**

| Decision | Role-type |
|---|---|
| Which work to accept, and on what terms | the practitioner, as owner |
| How the work is done | the practitioner, as professional |
| Prices and spending | the practitioner, as owner |
| What is passed to outside suppliers and advisers | the practitioner, within agreed terms |

**Typical hand-offs.**

| From | To | What crosses |
|---|---|---|
| a client | the practitioner | a request and the information needed |
| the practitioner | a client | the delivered work and the invoice |
| the practitioner | a supplier or adviser | a defined task |
| the practitioner | an authority | the filings and reports owed |

**When it fits.**
- The work is one person's, with occasional outside help.
- A few client relationships or one profession define the work.

**When it does not.**
- The work needs several people acting in different roles at the same time.
- Others hold decision rights over the work.

**Known risks.**
- Nobody covers when the person is away.
- One person holds every decision, so conflicts between the roles go unseen.
- Outside dependencies are not written down.

*This pattern is never evidence for an organisation.*

## 5. How it changes

A pattern is added, changed or retired by a new catalogue version, merged by the governing seat of 49GAION. A `pattern_id` is never reused.

*Powered by 49GAION*
