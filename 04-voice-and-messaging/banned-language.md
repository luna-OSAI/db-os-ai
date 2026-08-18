---
id: banned-language
title: Banned language
type: voice
status: approved
confidence: verified
source: OS_AI_Second_Brain_ChatGPT_8K.md · 07-compliance-and-guardrails/guardrails.md · 26_OS_AI_Bran_Archetype (phrases to avoid) · category convention analysis
as_of: 2026-08-18
owner: Tumai
tags: [voice, banned-language, compliance, critical]
---

# Banned language

**Read before writing anything.** This file outranks the voice guide and every playbook — only
[guardrails](../07-compliance-and-guardrails/guardrails.md) sits above it.

A banned-word list does more work than a voice guide, because generic AI copy fails by reaching for
the category's exhausted vocabulary, and a list of forbidden words is a constraint a model can
actually obey.

---

## Tier 1 — legal and company rules. Never, under any circumstance.

| Banned | Why |
|---|---|
| **GoHighLevel**, HighLevel, GHL, LeadConnector | Company rule, stated FIRM. Never client-facing |
| "our proprietary platform", "we built from scratch", "our own AI", "developed in-house" | False provenance. See [white-label disclosure](../07-compliance-and-guardrails/white-label-disclosure.md) |
| "guaranteed results", "guaranteed leads", "we guarantee" | No guarantee exists. ACL s29(1)(m) |
| "risk-free", "no risk", "nothing to lose" | The trial auto-converts and fees are non-refundable |
| "no refunds", "all sales final" **in marketing copy** | Cannot imply the buyer has no ACL rights |
| Any **partner income figure**, "passive income", "replace your salary", "financial freedom" | No earnings data. ACL exposure. See [partner and income claims](../07-compliance-and-guardrails/partner-and-income-claims.md) |
| "It's easy", "simple as that", "anyone can do it" | Company rule. Insults the reader and is untrue |
| Invented client counts, revenue figures, results, retention rates | See [what we cannot claim](../05-proof-and-evidence/what-we-cannot-claim.md) |

---

## Tier 2 — category-exhausted. Every competitor uses these.

Using them makes OS A.I sound like everyone else, which is a positioning failure even when it is not
a compliance one.

**Nouns:** solutions · game-changer · secret sauce · silver bullet · powerhouse · one-stop shop ·
Swiss army knife · rockstar · ninja · guru · hack · blueprint *(exception: "Free Blueprints" is a
live product name)*

**Verbs:** leverage *(as a verb)* · unlock *(overused into meaninglessness)* · supercharge ·
turbocharge · skyrocket · crush it · dominate · 10x *(as a verb — the site's "10× Faster" claim is
registered and permitted; new uses are not)* · revolutionise · disrupt

**Adjectives:** seamless · cutting-edge · best-in-class · world-class · innovative · robust ·
powerful · comprehensive · bespoke · tailored · turnkey · frictionless

**Phrases:** take your business to the next level · work smarter not harder · in today's fast-paced
world · now more than ever · the future of X is here · imagine a world where · what if I told you ·
here's the thing · let that sink in

---

## Tier 3 — AI writing tells

These make copy read as generated. They are the fastest way to lose a technical reader.

- **The rule of three used as a rhythm device** — "faster, smarter, and more efficient." Occasionally fine; as a default cadence it is a signature
- **"Not just X — it's Y"** and every variant ("more than just", "isn't merely")
- **Negative parallelism** — "It's not about the tools. It's about the system." Once per piece, maximum
- **Em-dash overuse.** Two per piece is plenty
- **Superficial -ing analysis** — "reshaping how businesses operate", "highlighting the importance of"
- **Vague attribution** — "experts say", "studies show", "it's widely known". Every stat needs a URL and a date
- **Inflated significance** — "stands as a testament to", "plays a vital role in", "serves as a cornerstone"
- **Conjunctive throat-clearing** — "Moreover", "Furthermore", "Additionally", "In conclusion"
- **Uniform paragraph length.** Three sentences each, every time, is a tell
- **Hedge stacking** — "may potentially help to possibly improve"
- **Closing summary** that restates what was just said

---

## Tier 4 — tonally wrong for this brand

| Avoid | Because |
|---|---|
| Exclamation marks | Confidence does not shout |
| Emoji in copy | Not the register. *(Internal docs are fine)* |
| "Hey there!", "Hope this finds you well" | Filler openers |
| Rhetorical-question openers | "Tired of losing leads?" — the most exhausted opener in the category |
| Manufactured urgency, countdowns, fake scarcity | The generic template packs are full of this. It is not the brand |
| "Dear valued customer" | Corporate distance |
| American spelling | Australian English, always |

---

## Words to use instead

| Instead of | Use |
|---|---|
| solution | system · platform · setup · the thing that does X |
| leverage | use · run on · put to work |
| seamless | connected · in one place · nothing to sync |
| bespoke / tailored | built for your business · configured around how you work |
| unlock | get · turn on · switch on |
| game-changer | *name the actual change* |
| take it to the next level | *say what actually improves* |
| effortless | done for you *(if true)* · handled |

The pattern: **every banned word is a placeholder where a specific fact should go.** If you cannot
replace it with something concrete, the sentence has no content.

## Related

- [Brand voice](brand-voice.md) · [Guardrails](../07-compliance-and-guardrails/guardrails.md)
