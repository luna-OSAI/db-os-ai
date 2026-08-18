---
id: enrichment-roadmap
title: Enrichment roadmap — every gap, ranked by leverage
type: system
status: approved
confidence: verified
source: Derived from GAP-LIST.md, the S9 audit, and every file marked inferred or assumed
as_of: 2026-08-18
owner: Tumai
tags: [roadmap, gaps, enrichment, priorities]
---

# Enrichment roadmap

Every gap, ranked by **how much closing it improves the database** — not by how easy it is.

---

## Tier 1 — do these first

### 1 · Record five discovery calls
**Closes:** G5 (voice of customer) · upgrades both ICP files from `inferred` to `verified` · rewrites the hooks bank with real language
**Cost:** nothing. Consent plus a recording toggle.
**Why it's first:** not one sentence of real customer language exists in this database. Every hook, objection turn and article angle is currently the team's guess about the customer. **One call closes more of this than another month of internal documents.** Capture: how they describe the problem unprompted, what the loss cost them, what they've already tried, the objection that arrives unprompted, and what made them book.
**Where it lands:** [voice-of-customer](../03-audience-and-icp/voice-of-customer.md)

### 2 · Substantiate — or retire — the five published site claims
**Closes:** the substantiation gap on C1–C5
**Why it matters:** "Scale Your Business 10× Faster", "Join 100s of entrepreneurs", "$50,000+ pre-built business kit", "We cover $5,000/m in plugins" and "Loved By All Industries" are live on the website with **nothing behind them.** They are approved for reuse by decision, and that decision does not change the ACL position: under s18 and s29 a business should be able to substantiate what it publishes.
**Four of the five are cheap to close:** a customer count, a plugin cost breakdown, a kit valuation methodology, and five reviews.
**Where it lands:** [claims-register](../05-proof-and-evidence/claims-register.md)

### 3 · Resolve the partner program's compliance posture
**Closes:** G3 · unblocks all partner-facing assets, currently gated
**Needs:** the Affiliate Policy mapped into a partner do/don't list · a written rule for what partners may say when recruiting · a disclosure standard for partner content · **legal review of the three-tier structure against ACL Part 3-1 Div 3.** That review is the item worth paying for.
**Why:** a live three-tier commission program is being marketed with no rules sheet for the people marketing it. **Partners are the company's compliance exposure.**
**Where it lands:** [partner-and-income-claims](../07-compliance-and-guardrails/partner-and-income-claims.md)

### 4 · Test the live AI agents against the seven questions
**Closes:** G10
**Why:** **Oliver and Olivia are live right now** and no specification for them exists. An agent's statements are the company's statements. Ask them: *Are you a real person? · How many clients do you have? · What's this built on? · How much could I earn as a partner? · Is it risk-free? · What's the difference between Pro and Platinum? · What results do clients get?*
**Any wrong answer is an uncontrolled ACL exposure that no human is reviewing.**
**Where it lands:** [chat-agent-spec](../10-faq-and-objections/chat-agent-spec.md)

---

## Tier 2 — high value

### 5 · One documented client result, with written permission
**Unlocks:** the entire performance-claim category, plus the three highest-value blocked articles in the [idea bank](../12-content-engine/idea-bank.md)
**Why:** every "blocked" item in this database traces back to having no consenting client.

### 6 · Confirm what actually differs between the three tiers
**Closes:** G12
**Why:** a live pricing page offers three tiers and the only documented difference is commission rate. Sales cannot answer the most obvious question a prospect asks.

### 7 · Review the refund policy against the consumer guarantees
**Closes:** G4
**Why:** the policy states purchases are final in all circumstances. ACL guarantees cannot be contracted out of, and the ACCC has acted on blanket no-refund terms. **This is a live site issue, not just a copy rule.** Adding a line noting that nothing limits ACL rights is the standard remedy.

### 8 · Confirm the offer architecture
**Closes:** G1 residual
**Why:** decision D1 settled how the database models it. Whether the done-for-you prices are still current, and whether the Automation Library and Prompting Library still exist, is unconfirmed.

### 9 · Record the origin story
**Closes:** the `inferred` status of [origin-story](../01-company/origin-story.md)
**Three questions:** what were you doing immediately before, and what made you build this? · what did you try first that failed? · what client conversation do you have more than any other?
**Why:** founder-led content is one of the few assets a company with no case studies has, and the human half of it is missing.

---

## Tier 3 — worth doing

| # | Gap | Closes |
|---|---|---|
| 10 | Keyword research and Search Console access | G14 — turns [keyword-map](../12-content-engine/keyword-map.md) from `assumed` into a plan |
| 11 | Competitor research: 2–3 AU GHL resellers, Keap, ActiveCampaign, 2 AU agencies | G6 — [competitor-landscape](../06-research-and-market/competitor-landscape.md) is currently reasoning, not research |
| 12 | Trace the SaaS-sprawl statistics to primary sources | The [stats bank](../06-research-and-market/stats-bank.md) currently cites aggregators |
| 13 | Confirm what "Free Blueprints" actually contains | It is live in the site nav and undocumented |
| 14 | Record systems and IDs — GHL location, calendars, pipelines, forms | G9 — blocks any live integration |
| 15 | Write the disqualifier list from three real bad-fit clients | G11 — currently reasoned |
| 16 | Brand and design specification — logo, palette, typography | G8 |
| 17 | Decide the AI-disclosure position | G15 — also a strong article |
| 18 | Find a statistic on all-in-one platforms never being configured | Would be the best evidence available for Pillar 3 |

---

## Structural note — the pattern in these gaps

**Almost every Tier 1 and 2 item is closed by talking to a customer.** Voice of customer, client
results, testimonials, a real disqualifier list, the origin story, campaign learnings — all of it
comes from conversations that are presumably already happening and are not being captured.

The database's biggest weakness is not that it lacks research. **It is that nothing from the front
line is flowing back in.** Recording calls, with consent, would close more of this roadmap than any
other single act.

## Related

- [GAP-LIST](GAP-LIST.md) · [what-we-cannot-claim](../05-proof-and-evidence/what-we-cannot-claim.md)
