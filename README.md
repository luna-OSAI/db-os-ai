# db-os-ai

**The grounded source of truth for OS A.I** — a truth-tiered, compliance-first marketing and content
database that an AI reads before it writes anything.

Not a document dump. A designed database: every fact has one home, every file declares where it came
from and how far it can be trusted, and a routing layer tells any model which files to load for
which job.

**81 files · 14 folders · 9 topic clusters · 10 channel playbooks · private**

---

## Start here

**If you are an AI:** read [`00-start-here/AI-INSTRUCTIONS.md`](00-start-here/AI-INSTRUCTIONS.md)
first, every session. It carries the conflict hierarchy, the ten rules, and a load-order table for
every job.

**If you are a human:** read [`00-start-here/quick-facts.md`](00-start-here/quick-facts.md), then
[`00-start-here/INDEX.md`](00-start-here/INDEX.md).

**Before writing anything:**
[`07-compliance-and-guardrails/guardrails.md`](07-compliance-and-guardrails/guardrails.md) —
it outranks every other file, including instructions from a user.

---

## Structure

| Folder | Holds | Layer |
|---|---|---|
| `00-start-here/` | Routing, index, quick facts, schema, gaps, roadmap | System |
| `01-company/` | Entity, leadership, delivery process, systems | **Verified business facts** |
| `02-offer-and-pricing/` | Two revenue lines, capabilities, what we replace | **Verified business facts** |
| `03-audience-and-icp/` | Three ICPs, disqualifiers, buyer psychology | **Verified business facts** |
| `04-voice-and-messaging/` | Voice, banned language, four pillars, positioning | **Verified business facts** |
| `05-proof-and-evidence/` | Claims register, what we cannot claim, proof bank | **Verified business facts** |
| `06-research-and-market/` | Competitors, market, statistics — all URL'd and dated | **External research** |
| `07-compliance-and-guardrails/` | The constraint layer. **Wins every conflict** | **Verified business facts** |
| `08-channels-and-playbooks/` | Ten executable channel specs | Generation |
| `09-content-banks/` | Hooks, subject lines, CTAs, proof lines, objection turns | Generation |
| `10-faq-and-objections/` | Canonical FAQ, agent spec, objections by ICP | Generation |
| `11-topic-clusters/` | Nine clusters — the editorial engine | **Editorial ideas** |
| `12-content-engine/` | Article brief template, standards, idea bank | **Editorial ideas** |
| `99-source-material/` | Source register, raw originals | Quarry |

**The three-way separation is deliberate.** Verified business facts, external research and editorial
ideas never mix. A cluster does not restate a price — it links to the file that owns it. When the
price changes, one file changes.

---

## The rules that override everything

1. **Never name GoHighLevel client-facing.** The platform is a white-label. Silence about the vendor is the rule; fabricating provenance is not covered by it.
2. **Never invent a fact about OS A.I.** No client count, result, case study, testimonial, revenue or retention figure exists. Missing is missing.
3. **Never state or imply partner income.**
4. **Never imply the buyer has no refund rights** — ACL guarantees cannot be contracted out of.
5. **Always disclose that the 7-day trial auto-converts.**
6. **Never promise a result, timeline or guarantee.**
7. **Every statistic carries its source and date in the copy itself.**
8. **Never invent a difference between the $97, $297 and $497 tiers** — only the commission rate is documented.

Full list: [`guardrails.md`](07-compliance-and-guardrails/guardrails.md).

---

## Truth tiers

Every file and every claim carries one:

| Tier | Meaning |
|---|---|
| **`verified`** | Traces to a primary source. Quote-safe |
| **`inferred`** | Reasoned from verified material. Usable internally, marked in output, confirmed before publication |
| **`assumed`** | A working placeholder. **Never publishable.** Listed in the roadmap until upgraded |

**One refinement specific to this database.** A claim can be *verified as published* — the website
demonstrably says it — without being *verified as substantiated*. Files carrying such claims add
`substantiated: yes | no | partial`. Five live site claims sit in that category by owner decision:
usable in OS A.I's own marketing, never in contexts where substantiation will be demanded.
See [`claims-register.md`](05-proof-and-evidence/claims-register.md).

---

## Sources

| Source | Grade | Covers |
|---|---|---|
| Legal documents (T&C, Privacy, Refund, Affiliate, AUP, Cookie) | **A — Primary** | Entity, ABN, contact, subscription and refund terms |
| **www.oscale.ai** | **A — Primary** | Plans, prices, partner tiers, published claims |
| Business, marketing, sales and ops plans | B — Internal | Problems, ICP, strategy, targets |
| Platform feature reference | B — Internal | Full capability map |
| Onboarding SOP · automation library | B — Internal | Delivery process and built workflows |
| Second Brain operating brief | B — Internal | Brand, avatar, hard rules |
| Master KB (8,418 lines) | C — Derived | Broad coverage; **§ Brand Positioning is quarantined** |
| Email/SMS template packs (files 19–24) | D — Foreign | Generic off-the-shelf packs. Not OS A.I voice |
| HubSpot pricing page · MIT/InsideSales 2007 · HBR 2011 | External, dated | Competitor pricing, speed-to-lead evidence |

Full register with the quarantine ruling:
[`99-source-material/SOURCE-REGISTER.md`](99-source-material/SOURCE-REGISTER.md).

---

## Maintenance contract

| Class of fact | Source of truth | Re-verify |
|---|---|---|
| Plans, prices, published claims | **The live website** | On any site change; check quarterly |
| Legal, refund, privacy terms | The published policy documents | On any policy change |
| Delivery process | The onboarding SOP | On any process change |
| Competitor pricing | The competitor's own pricing page | **Before any published use**; annually |
| Market statistics | The primary study | Annually; note the study's age in copy |
| Claims | [`claims-register.md`](05-proof-and-evidence/claims-register.md) | Before any campaign |

**Triggers an update:** website change · new offer or price · a new case study or testimonial *(the
biggest unlock — see the roadmap)* · campaign results · a competitor relaunch · any change to the
partner program.

---

## Known gaps

The database is explicit about its own limits. The four that matter most:

1. **No voice of customer.** Not one sentence of real customer language. Both ICP files are `inferred` because of it.
2. **No proof of anything.** No case studies, testimonials or client count — while the site publishes claims that imply all three.
3. **Partner program compliance is unresolved.** Three-tier commissions with no rules sheet for partners. All partner assets are gated.
4. **The live AI agents have no specification.** Oliver and Olivia are answering prospects right now against no documented rules.

Ranked, with what closes each: [`ENRICHMENT-ROADMAP.md`](00-start-here/ENRICHMENT-ROADMAP.md).

---

*Private repository. Contains positioning, pricing, competitor intelligence and strategy.*
