---
id: research-readme
title: Research and market — how this folder works
type: market
status: approved
confidence: verified
source: Folder convention derived from SCHEMA.md three-way separation
as_of: 2026-08-18
owner: Tumai
tags: [research, market, convention, sourcing]
---

# Research and market

**External research only.** Nothing in this folder is a fact about OS A.I. Nothing about OS A.I
belongs in here.

This is the "external research" third of the three-way separation the database is built on
([SCHEMA](../00-start-here/SCHEMA.md)) — kept apart from company facts (`01`–`05`, `07`) and from
editorial ideas (`11`, `12`) so that a reader can always tell which is which.

## The rule for every file here

Every claim carries:

1. **A source URL** — the actual page, not "according to research"
2. **A `researched:` date** in frontmatter
3. **The publisher named in the text**, so a reader can weigh it
4. **The original study named** where a statistic is being relayed second-hand

**No URL and no date means it does not ship.** Guardrail 7.

## What is in here

| File | Holds |
|---|---|
| [competitor-hubspot.md](competitor-hubspot.md) | The primary named comparison, with verified 2026 pricing |
| [competitor-landscape.md](competitor-landscape.md) | The wider category — all-in-one, point tools, agencies |
| [market-context-au.md](market-context-au.md) | Australian SMB context |
| [stats-bank.md](stats-bank.md) | **Every external statistic, one row each, with source and date** |
| [glossary.md](glossary.md) | Terms the audience uses |

## Using competitor material

It exists to shape **how we say things**, never **who we attack**. Guardrail 8.

- ✅ Explain the category and where OS A.I sits
- ✅ Quote a competitor's own published pricing, dated
- ❌ Name a competitor in a hostile frame
- ❌ Characterise a competitor's product from memory rather than their published material

## Staleness

**Competitor pricing changes without notice.** Anything with a `researched:` date more than six
months old is re-verified before use, not assumed. Re-check the whole folder annually, or whenever a
competitor visibly relaunches.

## Related

- [Stats bank](stats-bank.md) · [Claims policy](../07-compliance-and-guardrails/claims-policy.md)
