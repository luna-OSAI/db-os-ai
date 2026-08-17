---
id: source-register
title: Source register — what exists, where it lives, how far to trust it
type: source
status: approved
confidence: verified
source: Direct inspection of ~/Desktop/OS AI (33 files), ~/1-Tumai-Second-Brain/1-projects/oscale ai - Terms and Conditions, Privacy Policy and more (6 files), and https://www.oscale.ai (fetched 2026-08-18)
as_of: 2026-08-18
owner: Tumai
tags: [source-register, provenance, intake, s1]
---

# Source register

Every source inspected during S1 intake, with an honest authority rating. **Authority is not
about how long the document is.** It is about whether the claims inside it can be traced to
Oscale A.I's own words, systems or contracts.

| Rating | Meaning |
|---|---|
| **A — Primary** | The company's own binding or published material. Quote-safe. |
| **B — Internal** | Written by the team about the team. True as intent; not proof of results. |
| **C — Derived** | Assembled by an AI or from a template. Useful shape, unreliable facts. |
| **D — Foreign** | Belongs to a different vertical or a generic pack. **Not OS A.I material.** |

---

## A — Primary sources

| Source | Location | Covers | Date |
|---|---|---|---|
| Terms and Conditions | `1-projects/oscale ai - .../TERMS AND CONDITIONS.md` | Legal entity, ABN, address, phone, email, site, service description, subscription terms | Last updated 2024-11-17 |
| Privacy Policy | same folder | Data handling, jurisdictions, contact | 2026-08-17 export |
| Acceptable Use Policy | same folder | Prohibited customer conduct | 2026-08-17 export |
| Cookie Policy | same folder | Tracking disclosure | 2026-08-17 export |
| Affiliate Policy | same folder | Partner program terms | 2026-08-17 export |
| Refund Policy | same folder | No-refund posture, 7-day trial auto-conversion | 2026-08-17 export |
| **Live website** | `https://www.oscale.ai` | **Current plans and prices, partner tiers, published claims, agent names, nav** | Fetched 2026-08-18 |

These are the only sources that can support a `verified` claim about what Oscale A.I sells,
charges, or promises.

---

## B — Internal company documents

| Source | Covers | Authority note |
|---|---|---|
| `6_Business_Plan_OS_AI.md` | Problems, solutions, money model, SWOT, vision, goals | Competitors / USP / competitive-advantage sections are **unfilled template placeholders** |
| `7_Marketing_Plan_OS_AI.md` | ICP demographics + psychographics, capture/nurture/convert strategy, campaign planner | Richest ICP source. "Learnings / Roadblocks" left blank — no campaign has run |
| `8_Sales_Plan_OS_AI.md` | Sales model, stages, targets, metrics | All "Current /m" fields are `[0000]` — **no baseline exists** |
| `9_Operations_Plan_OS_AI.md`, `10_Client_Partner_Plan_OS_AI.md`, `11_Training_Admin_Plan_OS_AI.md` | Department plans | Intent, not performance |
| `13_Onboarding_SOP.md` | 10-step onboarding, value-add features, named owners | Confirms GoHighLevel sub-account provisioning |
| `12_AutomationOS_List.md` | The live automation/workflow inventory across 5 departments | Strong evidence of what is actually built |
| `4_OS_AI_Platform_OS_Feature_Reference_Consolidated.md` | Full platform capability map, feature → benefit → what-it-replaces | **Best product source in the set.** Describes the GHL feature surface |
| `3_Team_OS_Leadership_Profiles_Consolidated_OS AI.md` | Five leadership profiles, roles, locations | Contains extensive psychometric and personal-history material — see privacy note below |
| `2_Roles and Responsibilities_OS AI.md` | Org structure and accountabilities | — |
| `1_OS AI_Mind Map.md` | Six-department business map | Structural only |
| `OS_AI_Second_Brain_ChatGPT_8K.md` | **Distilled operating brief** — brand, platform, avatar, KPIs, hard rules | Highest signal-per-word document in the set |
| `OS_AI_Second_Brain_Claude_Anthropic_Instructions_V1_22032026.md`, `..._Gemini_Gem.md`, `..._Perplexity_Space_Trimmed.md` | Same content at other lengths | Redundant with the above |

---

## C — Derived / assembled

| Source | Covers | Authority note |
|---|---|---|
| `0_OS_AI_Master_KB_File_V1_22032026.md` (8,418 lines) | Everything, in eight parts | **Partially contaminated — see the quarantine note below** |
| `5_OS_AI_Full Company.md` | Company summary | Duplicates the business plan almost verbatim |
| `26_OS_AI_Bran_Archetype_..._Magician_Ruler.md` | Magician-Ruler archetype, 70/30 blend, language clusters, visual identity | Well-researched brand theory. The archetype decision is a **real company decision**; the surrounding research is external and should be cited as such |
| `15–18_Framework_Book Library_Part_1–4.md` | 37-book framework library (Hormozi, EOS, etc.) | Third-party frameworks. Reference material, not company fact |
| `14_Founder_Leadership_Identity_FinanceOS.md` | Founder identity | **Filename says FinanceOS.** Belongs to a different brand |

---

## D — Foreign / generic — do not treat as OS A.I voice

| Source | Why it is disqualified |
|---|---|
| `19_Welcome_SMS_Templates.md` | Generic pack. Explicitly scoped to "physical product welcome sequences, coaching program check-ins" |
| `20_Nurture Email Templates.md` | Generic pack, 12 email types, no OS A.I specificity |
| `21_Product_Launch_Email_Templates.md` | Generic pack |
| `22_Sales Email Templates.md` | Generic pack, 13 promo types incl. flash sale / scarcity |
| `23_Webinar Email Templates.md` | Generic pack |
| `24_Welcome Email Templates Markdown.md` | Generic pack |

**These six files total ~230KB and look like the biggest content asset in the set. They are not.**
They are an off-the-shelf template library. Copying their voice into OS A.I output would produce
exactly the generic, scarcity-driven marketing the brand claims to be against. They belong in
`99-source-material/` as structural reference for *sequence architecture only* — never for voice,
never for claims.

---

## Quarantine — the master KB positioning contamination

`0_OS_AI_Master_KB_File_V1_22032026.md` § "Brand Positioning & Core Messaging" is written for a
**mortgage broking** audience, not for OS A.I's stated market. Verbatim evidence:

- "Aggregator Software Not Getting Your Leads?"
- "Manual Lead Generation vs. Auto-Pilot **Settlements**"
- "Empty Pipeline vs. Full Calendar. It's Your **Brokerage**"
- "OS A.I. fixes the gap between enquiry and **funded loan**"
- "Bonus #1: The X5 **BrokerGPT** Business Bundle"

It also carries an offer structure — "OS A.I. — Monthly: $297 USD/Month" with five funnels and
BrokerGPT bonuses — that matches **neither** the live website **nor** the business plan.

**Ruling:** this section is quarantined. It is Finance OS material that was pasted into the OS A.I
knowledge base. No claim, hook or offer detail may be drawn from it. Everything else in the master
KB is usable at C-grade with its facts re-verified against an A or B source.

---

## The pricing conflict — three incompatible offer structures

This is the single most important finding of S1.

| Source | Structure | Date |
|---|---|---|
| **Live website** | Pro **$97/m** · Partner **$297/m** · Platinum **$497/m** — self-serve SaaS with 3-tier partner payouts (40% / 45%+5% / 50%+30%+10%) | 2026-08-18 |
| **Business plan** | Pro Chat Agent **$2,500 setup + $297/m** · Platinum Chat **$6,800 + $497/m** · Pro Voice **$5,500 + $297/m** · Platinum Voice **$11,100 + $497/m** · Automation Library $99 · Prompting Library free | 2026-03-22 |
| **Master KB** | "OS A.I. Monthly $297" bundle with funnels + BrokerGPT bonuses | quarantined |

These are not versions of one offer. They are a **self-serve software subscription** and a
**done-for-you services business** with coincidentally matching monthly numbers. The database must
model them as two distinct revenue lines with one shared subscription spine, and the routing layer
must state which one wins in copy. Proposed ruling in [`../00-start-here/SCHEMA.md`](../00-start-here/SCHEMA.md).

---

## Privacy note — leadership profiles

`3_Team_OS_Leadership_Profiles_Consolidated_OS AI.md` contains MBTI, Enneagram, Human Design,
numerology and astrology readings, stress and burnout patterns, family relationships, and personal
history including homelessness and religious exile — for five named people, four of whom are not
the requester.

**Only role, title, location at city level, accountabilities and publicly-tellable story material
are carried into this database.** Psychometric profiles, stress patterns and personal history stay
out. They are not needed to write marketing copy, and a marketing database is the wrong home for
them. See [`../00-start-here/GAP-LIST.md`](../00-start-here/GAP-LIST.md) if any of it is later
judged necessary.

---

## Sources that do not exist

Checked and confirmed absent:

- **No call recordings or transcripts.** No Granola, Fathom or Zoom exports for OS A.I.
- **No customer testimonials, reviews or case studies** in any file.
- **No campaign performance data.** Every metric field in the sales plan reads `[0000]`.
- **No competitor research.** The business plan's competitor section is an unfilled template.
- **No CRM export.** Pipelines, forms and workflows are described but never enumerated with IDs.
- **No brand or design assets** — no logo files, palette, or typography specification.
