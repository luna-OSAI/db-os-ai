---
id: stats-bank
title: Stats bank — every external statistic, sourced and dated
type: market
status: approved
confidence: verified
source: Individual sources named per row
researched: 2026-08-18
as_of: 2026-09-01
owner: Tumai
tags: [research, statistics, bank, evidence]
---

# Stats bank

**Every external statistic OS A.I is permitted to cite.** One row each, with its source and date.
If a figure is not here, it does not go in an asset.

**Attribution is mandatory in the copy itself**, not just in this file. "Research shows" is banned —
name the study.

---

## Speed to lead — evidence for Pillar 1

The strongest external evidence OS A.I has, and it maps directly onto the core argument.

| Stat | Source | Researched |
|---|---|---|
| Contacting a web lead **within 5 minutes** makes qualification **21× more likely** than waiting 30 minutes | Dr James Oldroyd, MIT / InsideSales.com **Lead Response Management Study (2007)** | 2026-08-18 |
| Lead quality **drops ~80% after the first 5 minutes** | Oldroyd, McElheran & Elkington, *"The Short Life of Online Sales Leads"*, **Harvard Business Review (2011)** | 2026-08-18 |
| Average first-response time across 2,241 audited US companies: **42 hours** | HBR (2011), same audit | 2026-08-18 |
| **23% of audited companies never responded at all** | HBR (2011), same audit | 2026-08-18 |
| Responding within an hour makes meaningful qualification **~7× more likely** than the hour after | HBR (2011) | 2026-08-18 |

**Attribution rules for these:**

- The 21× figure is **MIT/InsideSales (Oldroyd, 2007)** — it is frequently misattributed to HBR. Do not repeat that error.
- The 42-hour, 23% and 7× figures are the **separate HBR 2011 audit**.
- **Both studies are old** — 2007 and 2011. They are still the canonical citations in this field, and being upfront about their age is more credible than hiding it. If a reader checks, they should find exactly what you said.

**Why they matter:** the "23% never responded" figure is the single most useful statistic in this
database. It makes Pillar 1's invisible loss visible with third-party evidence, and it does not
require any OS A.I performance data.

---

## Tool sprawl and SaaS consolidation — evidence for Pillar 2

| Stat | Source | Researched |
|---|---|---|
| Average company runs **106 SaaS applications**, down from 112 in 2024 and 130 in 2022 | BetterCloud, *State of SaaS* / 2026 SaaS statistics compilations | 2026-08-18 |
| **25–30% of SaaS licences are unused or significantly underutilised** | 2026 SaaS statistics compilations | 2026-08-18 |
| Lines of business own **~70% of SaaS spend** and about half of all apps; IT controls **~26%** | 2026 SaaS statistics compilations | 2026-08-18 |

**Handle with care.** These figures come from aggregator articles rather than the primary reports,
and they describe **companies at large**, not the 1–10 staff service businesses OS A.I sells to.
An SMB running 106 apps is not credible.

**Rules:**

- **Never present these as SMB figures.** Say "the average company", not "the average small business".
- **Prefer the direction to the number** — SaaS counts peaked in 2022 and are falling as businesses consolidate. That trend is the argument, and OS A.I is on the right side of it.
- **Trace to the primary source before publishing.** These need upgrading from aggregator to original report. Logged in the [enrichment roadmap](../00-start-here/ENRICHMENT-ROADMAP.md).
- The 25–30% unused-licence figure is the most useful of the three, because waste is checkable by the reader against their own stack.

---

## Competitor pricing

| Stat | Source | Researched |
|---|---|---|
| HubSpot Marketing Hub **Professional: $800/mo monthly, $890/mo annual**, 3 seats, plus **$3,000 one-time onboarding** | hubspot.com/pricing/marketing | 2026-08-18 |
| HubSpot **Enterprise: from $3,600/mo**, plus **$7,000 onboarding** | same | 2026-08-18 |
| Additional HubSpot seats: **$45/mo** (Pro), **$75/mo** (Enterprise) | same | 2026-08-18 |

Full context: [competitor-hubspot](competitor-hubspot.md).

---

## Australian AI adoption — evidence for Pillar 4

| Stat | Source | Researched |
|---|---|---|
| **~12% of Australian businesses** reported using AI in the workplace in **2024–25** | ABS, *Business adoption of Artificial Intelligence accelerates in 2024–25*, released 25 June 2026 | 2026-09-01 |
| **Small and micro businesses: ~11%.** Medium: **22%** (from 3%). Large: **35%** (from 9% in 2021–22) | same | 2026-09-01 |
| Innovation-active small businesses: **19%** vs **4%** for non-innovation-active | same | 2026-09-01 |
| Top industries: Information, media and telecommunications **38%**; Professional, scientific and technical services **24%**; Financial and insurance services **24%** | same | 2026-09-01 |

URL: <https://www.abs.gov.au/media-centre/media-releases/business-adoption-artificial-intelligence-accelerates-2024-25>
Sample: nearly 7,000 Australian businesses.

**Population note — step 4 of [Adding a stat](#adding-a-stat).** This counts *any* AI use by *any*
Australian business, from a generative-text tool upward. **It is not a measure of AI agents**, and it
must never be presented as one. The right use is scale-setting: most Australian small businesses have
not adopted AI at all yet.

**Rules:**

- Attribute as **ABS**, with the **2024–25** reference period and the **25 June 2026** release date, in the copy itself.
- **Never round 11% up to "one in eight"** or otherwise restate it into a bigger-sounding figure.
- Vendor and industry trackers reporting Australian SMB AI adoption in the **40–70%** range are self-selecting samples measuring "used AI in some form". **They are not interchangeable with this figure and must not be blended with it.** Where the contrast is useful, name both and say why they differ.
- This is a primary source from a national statistical agency, which makes it the strongest external evidence in this database after the speed-to-lead set.

---

## Gaps — statistics that would strengthen the argument but have not been researched

- Australian SMB software spend specifically
- Cost of context-switching, with a primary source
- SMB churn attributable to poor onboarding
- Missed-call statistics for service businesses
- What proportion of all-in-one platform buyers never complete configuration — **this would be the single best stat for Pillar 3, and no source has been found for it**

---

## Adding a stat

1. Find the **primary source**, not an article citing it
2. Record the publisher, the study name and the year
3. Add the URL and a `researched:` date
4. Note who the population actually is — this is where most statistical misuse happens
5. Then it may be cited, with attribution in the copy

## Related

- [Claims policy](../07-compliance-and-guardrails/claims-policy.md) · [Speed-to-lead cluster](../11-topic-clusters/cluster-speed-to-lead.md)
