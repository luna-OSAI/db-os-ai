---
id: schema
title: Entity model and schema design
type: system
status: approved
confidence: verified
source: Derived from 99-source-material/SOURCE-REGISTER.md and the project brief's ASSETS list
as_of: 2026-08-18
owner: Tumai
tags: [schema, entity-model, s3, design]
---

# Entity model — db-oscale-ai

**Status: APPROVED 2026-08-18.** Decisions D1, D2, D3 and D6 confirmed by Tumai. D4 and D5 were not
adopted as hard rules and remain guidance only.

---

## The business in five sentences

Oscale A.I, trading as **OS A.I**, is an Australian company (ABN 75 527 278 804, Werribee VIC) that
sells an all-in-one AI-powered business platform to service-based SMB owners and agency founders
across Australia, New Zealand and North America. The platform is a **GoHighLevel white-label** —
CRM, marketing automation, funnels, websites, courses and communities — fronted by AI chat and voice
agents that capture, qualify and book leads around the clock. It is sold two ways: a **self-serve
subscription** at $97 / $297 / $497 per month, and a **done-for-you build** where OS A.I designs and
installs the client's system for a setup fee. Growth is intended to come substantially through a
**three-tier brand-partner commission program**. It competes by consolidating a sprawling tool stack
into one system at a fraction of enterprise CRM pricing, under the promise **"The Magic Is In The
System."**

---

## The nouns, and what each becomes

| Noun in the business | Entity | Home |
|---|---|---|
| The company | `company` | `01-company/` |
| The people who run it | `company` | `01-company/leadership.md` |
| The systems it runs on | `system` | `01-company/systems-and-ids.md` |
| A plan someone can buy | `offer` | `02-offer-and-pricing/` — one file per line |
| A capability the platform has | `offer` | `02-offer-and-pricing/platform-capabilities.md` |
| The partner program | `offer` | `02-offer-and-pricing/partner-program.md` |
| A kind of buyer | `icp` | `03-audience-and-icp/` — one file per ICP |
| How the brand sounds | `voice` | `04-voice-and-messaging/` |
| Something that makes a claim credible | `proof` | `05-proof-and-evidence/` |
| A competitor or market fact | `competitor` / `market` | `06-research-and-market/` |
| A rule the content may not break | `compliance` | `07-compliance-and-guardrails/` |
| How to write for a channel | `playbook` | `08-channels-and-playbooks/` |
| A reusable line | `bank` | `09-content-banks/` |
| A question that recurs | `faq` | `10-faq-and-objections/` |
| **A subject the brand owns** | **`cluster`** | **`11-topic-clusters/`** |
| **A planned article** | **`brief`** | **`12-content-engine/`** |
| Raw unedited material | `source` | `99-source-material/` |

---

## The three-way separation the brief asks for

> *"separate folders for verified business information, external research, and editorial content
> ideas, so facts, sources, and drafts remain clearly distinct"*

| Layer | Folders | Rule |
|---|---|---|
| **Verified business information** | `01` – `05`, `07` | Primary sources only. Nothing enters without an A- or B-grade source |
| **External research** | `06-research-and-market/` | Every file carries a source URL and a `researched:` date. Never mixed into company files |
| **Editorial content ideas** | `11-topic-clusters/`, `12-content-engine/` | Angles, briefs and drafts. **Nothing here is a fact.** It borrows facts by linking to `01`–`07` |

A statistic about the market lives in `06` and is *linked* from a cluster. A price lives in `02` and
is *linked* from a brief. **A cluster file never restates a number** — it points at the file that
owns it. That is the whole normalisation discipline in one rule.

---

## Topic clusters — the reusable unit

Nine clusters. Seven named in the brief, plus two that the source material shows are actually the
dominant pains and deserve their own home.

| id | Cluster | Why it exists |
|---|---|---|
| `cluster-ai-for-small-business` | AI for small business | The category the brand sells into |
| `cluster-software-sprawl` | Software sprawl & subscription creep | Named customer problem #2 |
| `cluster-duct-taped-systems` | Duct-taped systems & the integration tax | The brief's own phrase; the sharpest angle in the set |
| `cluster-automation` | Automation — what to automate and what not to | Core capability |
| `cluster-workflows` | Workflows & process design | Core capability |
| `cluster-crm` | CRM — why they fail small businesses | The competitive battleground |
| `cluster-cost-savings` | Stack consolidation economics | Carries the HubSpot comparison |
| `cluster-speed-to-lead` *(added)* | Missed leads & follow-up speed | The #1 stated problem across every source. Too central to be a sub-topic |
| `cluster-founder-bottleneck` *(added)* | Founder dependency & time freedom | The emotional register the ICP actually buys on — burnout, 60–80 hour weeks |

**Every cluster file carries these seven headings, in this order, always:**

1. **The customer pain** — in the customer's words where we have them, marked when we do not
2. **OS A.I's viewpoint** — the argument, including what the brand refuses to say
3. **The solution** — which capabilities apply, linked to `02`
4. **Supporting evidence** — every item tiered and sourced, linked to `05` or `06`
5. **Common objections** — with the turn, linked to `10`
6. **Keywords** — primary, secondary, and the questions people actually ask
7. **Article ideas** — titles with angle and intent, feeding `12`

Fixed headings are what make a cluster queryable rather than an essay. An article brief selects a
cluster and inherits all seven.

---

## The article-brief template

Lives at `12-content-engine/article-brief-template.md`. A writer picks a cluster, and the brief
resolves to: the approved business facts they may use (by link), the dated research they may cite
(by link), the relevant proof (or an explicit statement that none exists), the voice constraints,
the pre-publish checklist, and the compliance gate. **It is a spec, not a suggestion.**

---

## Relationships

```
offer ──────── serves ────────▶ icp
  │                              │
  │                              ├── has ──▶ objection ──▶ faq
  ▼                              ▼
capability ─── answers ────▶ cluster ◀─── evidences ─── proof
                               │  ▲                       │
                               │  └──── contextualises ── research
                               ▼
                            brief ──── writes to ────▶ playbook
                               │                          │
                               └──── constrained by ──▶ compliance
```

**Compliance sits above everything and is not on the graph as a peer.** It is a gate every path
passes through.

---

## Proposed conflict hierarchy

The pricing contradiction forces this to be decided now, not improvised later.

```
1. 07-compliance-and-guardrails/          ← always wins, no exceptions
2. The live website (www.oscale.ai)       ← authoritative for plans, prices, published claims
3. 02-offer-and-pricing/                  ← authoritative for DFY scope and partner terms
4. 04-voice-and-messaging/banned-language.md
5. 04-voice-and-messaging/brand-voice.md
6. The task-specific playbook in 08-
7. Everything else
—  0_Master_KB § Brand Positioning        ← QUARANTINED. Never a source.
```

**Ruling on the offer conflict** (needs your confirmation — this is decision D1 below):

- The **$97 / $297 / $497 monthly plans are the product.** They are what the site sells today.
- The **$2,500–$11,100 setup fees are a separate done-for-you services line** — the same platform, installed for the client rather than by them.
- They get **two files**, not one merged file, because they are sold to different buyers with different objections.
- The master KB's "$297 with BrokerGPT bonuses" is **quarantined** as Finance OS contamination.

---

## Full folder map

```
00-start-here/           AI-INSTRUCTIONS · INDEX · quick-facts · SCHEMA · GAP-LIST · ENRICHMENT-ROADMAP
01-company/              profile · leadership · how-we-work · systems-and-ids · origin-story
02-offer-and-pricing/    offer-overview · subscription-plans · done-for-you-services ·
                         partner-program · platform-capabilities · what-we-replace
03-audience-and-icp/     icp-smb-owner · icp-agency-founder · icp-brand-partner ·
                         disqualifiers · buyer-psychology · voice-of-customer (stub — G5)
04-voice-and-messaging/  brand-voice · archetype · messaging-pillars · banned-language · positioning
05-proof-and-evidence/   proof-and-evidence-bank · claims-register · what-we-cannot-claim
06-research-and-market/  competitor-* · comparison-matrix · market-context-au · glossary · stats-bank
07-compliance-and-guardrails/  guardrails · claims-policy · acl-and-consumer-law ·
                         partner-and-income-claims · white-label-disclosure · approval-rules
08-channels-and-playbooks/  website-copy · blog-and-article · email · newsletter · sms ·
                         social · ads · sales-scripts · lead-magnets · video-vsl
09-content-banks/        hooks-and-openers · subject-lines · ctas · proof-lines ·
                         objection-turns · offer-angles · analogies
10-faq-and-objections/   faq · objections-smb · objections-agency · objections-partner · chat-agent-spec
11-topic-clusters/       README + 9 cluster files
12-content-engine/       article-brief-template · content-standards · idea-bank ·
                         keyword-map · editorial-calendar · worked-example-brief
99-source-material/      SOURCE-REGISTER + raw/ (unedited originals, dated)
```

---

## Assessment against the ASSETS list

Walking each asset the brief demands, and confirming the map can produce it:

| Asset | Producible? | Path through the model |
|---|---|---|
| Blog / article from a topic cluster | **Yes** | `11/cluster-*` → `12/article-brief-template` → `08/blog-and-article` |
| Website / landing page copy | **Yes** | `02` → `03` → `04` → `08/website-copy` |
| Email sequence | **Yes** | `03` → `04` → `08/email` → `09/subject-lines` |
| Newsletter | **Yes** | `11` → `06` → `08/newsletter` |
| SMS | **Yes** | `08/sms` → `07` (Spam Act) |
| Social post | **Yes** | `11` → `09/hooks-and-openers` → `08/social` |
| Ad copy | **Yes** | `02` → `09/offer-angles` → `08/ads` → `07/claims-policy` |
| Sales script | **Yes** | `03` → `10/objections-*` → `08/sales-scripts` |
| Lead magnet | **Yes** | `11` → `08/lead-magnets` |
| Chat/voice agent behaviour | **Yes** | `10/chat-agent-spec` → `10/faq` → `07` |
| Partner recruitment asset | **Gated** | Blocked on G3 until the partner claims rule exists — **by design** |
| Anything citing a result | **Gated** | Blocked on G2. `05/what-we-cannot-claim` will say so plainly |

Two assets are deliberately gated rather than enabled. That is the schema working: it refuses to
produce copy the evidence cannot support.

---

## Decisions needed before build

| # | Decision | Ruling |
|---|---|---|
| **D1** | Offer model | **ADOPTED.** Two lines, two files. The live site is authoritative for price |
| **D2** | The five published site claims | **ADOPTED — reuse permitted.** Recorded as `verified` **as published**, with `substantiated: no`. See the claims register |
| **D3** | Leadership psychometric and personal-history material | **ADOPTED.** Role, title, city and public story only |
| **D4** | Generic template packs (files 19–24) | **Not adopted as a rule.** They stay in source material, graded D, as guidance rather than prohibition |
| **D5** | Brand naming rule | **Not adopted as a rule.** "OS A.I" is used in copy because every source and the live site does; "Oscale A.I" appears in legal contexts. Descriptive, not enforced |
| **D6** | The two added clusters | **ADOPTED.** Nine clusters |

### The published-vs-substantiated distinction (from D2)

D2 forces one refinement to the truth-tier system, and it is worth stating precisely because the
rest of the database depends on it.

A claim can be **verified as published** — the live site demonstrably says it, and that is a fact
with a traceable source — without being **verified as substantiated**, which would require evidence
that the claim is true. The five site claims are the first category, not the second.

Files carrying such claims therefore add one frontmatter field:

```yaml
substantiated: yes | no | partial
```

`confidence: verified` + `substantiated: no` means: *the brand says this, you may say it too, and
no evidence has been produced for it.* Copy may reuse these lines per D2. The
[claims register](../05-proof-and-evidence/claims-register.md) is the single home for all five, and
the [enrichment roadmap](ENRICHMENT-ROADMAP.md) keeps the substantiation gap visible until it closes.
