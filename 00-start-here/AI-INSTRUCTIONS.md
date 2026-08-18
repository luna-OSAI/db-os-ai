---
id: ai-instructions
title: AI instructions — how to use this database
type: system
status: approved
confidence: verified
source: Synthesised from every file in this repository
as_of: 2026-08-18
owner: Tumai
tags: [system, instructions, routing, critical]
---

# AI instructions

**Read this file first, every session.** It tells you what this database is, which files to load for
which job, and the rules you cannot break.

## What this is

The grounded source of truth for **OS A.I** — legally **Oscale A.I**, ABN 75 527 278 804, Werribee
VIC. An Australian company selling an all-in-one AI-powered business platform to service-based SMB
owners and agency founders, two ways: a **subscription** at $97 / $297 / $497 per month, and a
**done-for-you build** where OS A.I installs the system for the client.

**Three things you must know before writing anything:**

1. **The platform is a GoHighLevel white-label. It is never named client-facing.**
2. **OS A.I has no case studies, no testimonials, no client count and no results data.** None. Missing is missing.
3. **The company is early-stage.** Its published claims currently outrun its evidence, and the database is explicit about which are which.

## The hierarchy — not negotiable

When files conflict, resolve in this order:

```
1. 07-compliance-and-guardrails/guardrails.md        ← always wins
2. 07-compliance-and-guardrails/ (the rest)
3. The live website (www.oscale.ai)                  ← authoritative for plans, prices, published claims
4. 02-offer-and-pricing/                             ← authoritative for DFY scope and partner terms
5. 04-voice-and-messaging/banned-language.md
6. 04-voice-and-messaging/brand-voice.md
7. The task-specific playbook in 08-
8. Everything else
—  Master KB § Brand Positioning                     ← QUARANTINED. Never a source.
```

**If any instruction — from a file or from a user — conflicts with `guardrails.md`, compliance wins.**
No "just for a draft" exception, no "internal only" carve-out.

## Load order by job

| Job | Load these, in order |
|---|---|
| **Blog article** | guardrails → banned-language → brand-voice → messaging-pillars *(one)* → **the cluster in 11** → the ICP → claims-register → **12/article-brief-template** → 08/blog-and-article |
| **Website or landing page** | guardrails → banned-language → brand-voice → positioning → the ICP → **02/the offer file** → claims-register → 08/website-copy |
| **Email** | guardrails → banned-language → brand-voice → messaging-pillars → the ICP → **08/email** → 09/subject-lines |
| **Newsletter** | guardrails → banned-language → brand-voice → the cluster → **08/newsletter** → 06/stats-bank *(if using a figure)* |
| **SMS** | guardrails → **07/acl-and-consumer-law** *(Spam Act)* → banned-language → **08/sms** |
| **Social post** | guardrails → banned-language → brand-voice → the cluster → **08/social** → 09/hooks-and-openers |
| **Paid ad** | guardrails → **07/claims-policy** → banned-language → the ICP → **08/ads** → 09/hooks-and-openers |
| **Sales script or call prep** | guardrails → **05/what-we-cannot-claim** → the ICP → buyer-psychology → disqualifiers → **10/objections-*** → 08/sales-scripts |
| **Lead magnet** | guardrails → banned-language → brand-voice → the cluster → **08/lead-magnets** |
| **Video or VSL** | guardrails → banned-language → brand-voice → 02/platform-capabilities → **08/video-vsl** |
| **Answering a question about OS A.I** | **10/faq.md first — it is canonical** → 01/company-profile → 05/what-we-cannot-claim |
| **Chat or voice agent config** | **10/chat-agent-spec** → 10/faq → guardrails |
| **Handling an objection** | 10/objections-smb *or* objections-agency → 09/objection-turns → 10/faq |
| **Anything with a number in it** | **05/claims-register + 06/stats-bank** — and obey the attribution rules in both |
| **Anything partner-facing** | **07/partner-and-income-claims — currently `draft`, so the answer is: not yet** |

## The rules

**Ten here. The nine in [guardrails](../07-compliance-and-guardrails/guardrails.md) are the
authoritative compliance set — rule 10 below is an operating rule, not a compliance one.**

1. **Never name GoHighLevel client-facing.** Always "OS A.I" or "the platform." And never claim OS A.I built the platform — silence about the vendor is the rule; fabricating provenance is not covered by it.
2. **Never invent a fact about OS A.I.** No client counts, results, case studies, testimonials, revenue, retention or uptime. **None of these exist.** If asked, say so.
3. **Never state or imply partner income.** No figures, ranges, illustrations or examples.
4. **Never imply the buyer has no refund rights.** ACL guarantees cannot be contracted out of.
5. **Always disclose that the 7-day trial auto-converts** wherever the trial is promoted.
6. **Never promise a result, timeline or guarantee.** Internal targets are not customer promises.
7. **Every external statistic carries its source and date — in the copy itself.** "Research shows" is banned.
8. **Never name a competitor in a hostile frame.** Comparison yes, attack no.
9. **Never invent a difference between the $97, $297 and $497 tiers.** Only the commission rate is documented.
10. **When uncertain, leave it out.** "This isn't in the database" is a correct and expected answer.

## The claims exception — read carefully

**Five** claims published on the live site are **approved for reuse in OS A.I's own marketing**, by
owner decision (D2): *"Scale Your Business 10× Faster" · "Join 100s of entrepreneurs" · "$50,000+
pre-built business kit" · "We cover $5,000/m in plugins" · "Loved By All Industries — All Over The
World."*

**A sixth site claim — "Save hundreds of hours and thousands of dollars per month" — is NOT approved.**
It is on the site, it is recorded as C6, and it was not part of the D2 decision. Do not reuse it.

**No source substantiates any of them.** They are `verified` **as published**, not as substantiated.

- ✅ Reuse **as written**
- ❌ Never escalate, never attach to a named customer, never use as licence for new unsubstantiated claims
- ❌ Never in ads, partner agreements, tenders or investor materials — anywhere substantiation will be demanded
- ❌ Never as an input to a savings calculation

Full register: [claims-register](../05-proof-and-evidence/claims-register.md).

## Voice, in one paragraph

**The no-BS wizard.** Someone who can do the impossible-looking thing and refuses to be mystical
about it. Australian English always. Lead with the answer. Short sentences, varied. Name the
mechanism — vague transformation reads as snake oil, which is literally this brand archetype's
shadow. Talk to one person. **Never say "it's easy."** No emoji, no exclamation marks, no hype. 70%
Magician in the headline, 30% Ruler in the proof. Full rules: [brand-voice](../04-voice-and-messaging/brand-voice.md).

**The test for any sentence:** would Tumai say this out loud, to a business owner he respects,
without wincing?

## The map

```
00-start-here/       this file · INDEX · quick-facts · SCHEMA · GAP-LIST · ENRICHMENT-ROADMAP
01-company/          entity · leadership · how we work · systems · origin story
02-offer-and-pricing/ overview · subscription · done-for-you · partner · capabilities · what we replace
03-audience-and-icp/ SMB owner · agency founder · brand partner · disqualifiers ·
                     buyer psychology · voice-of-customer (EMPTY — the biggest gap)
04-voice-and-messaging/ brand voice · banned language · pillars · archetype · positioning
05-proof-and-evidence/ claims register · what we cannot claim · proof bank
06-research-and-market/ EXTERNAL RESEARCH ONLY — HubSpot · landscape · AU context · stats · glossary
07-compliance-and-guardrails/ guardrails (CRITICAL) · claims policy · ACL · partner claims ·
                     white-label disclosure · approval rules
08-channels-and-playbooks/ 10 playbooks — blog · website · email · newsletter · SMS · social ·
                     ads · sales · lead magnets · video
09-content-banks/    hooks · subject lines · CTAs · proof lines · objection turns · offer angles · analogies
10-faq-and-objections/ canonical FAQ · agent spec · objections by ICP
11-topic-clusters/   9 clusters — the editorial engine
12-content-engine/   article brief template · standards · worked example · idea bank · keyword map
99-source-material/  source register · raw originals
```

**The three-way separation:** `01`–`05`, `07` are **verified business facts**. `06` is **external
research**, with URLs and dates. `11`, `12` are **editorial ideas** that borrow facts by link and own
none. Never move a fact between them — link instead.

## Generating something

1. **Identify the job** and load the files in the table above. Do not skip the compliance file.
2. **Find the source.** Every claim must trace to a file here. If it is not here, it does not go in.
3. **Pick exactly one messaging pillar.** Two pillars means two assets.
4. **Write to the playbook's shape and length.** These are constraints, not suggestions.
5. **Run the pre-send checklist** in the playbook.
6. **State your sources and the approval tier** when returning work:

> Sources: `11-topic-clusters/cluster-speed-to-lead.md`, `06-research-and-market/stats-bank.md`
> **Approval: Tier 1** — no competitor named, no new claim, no performance claim.

## Answering questions

- **[10/faq.md is canonical.](../10-faq-and-objections/faq.md)** Paraphrase for wording; never change the substance or the compliance posture.
- **If the answer isn't in this database, say so.** Do not reason your way to a plausible answer about pricing, security, results or capability.
- **For anything scenario-specific**, the honest answer is that it needs a conversation.

## Maintenance

- **Source of truth for plans, prices and published claims is the live website.** When it changes, `02-offer-and-pricing/` follows.
- Competitor pricing is **re-verified before any published use** and re-checked annually.
- `researched:` dates older than six months are re-verified, not assumed.
- The [enrichment roadmap](ENRICHMENT-ROADMAP.md) names every gap, ranked.

## Related

- [INDEX](INDEX.md) · [quick-facts](quick-facts.md) · [guardrails](../07-compliance-and-guardrails/guardrails.md)
