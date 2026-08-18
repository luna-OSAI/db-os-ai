---
id: article-brief-template
title: Article brief template
type: playbook
status: approved
confidence: verified
source: Derived from 11-topic-clusters/README.md, 04-voice-and-messaging/* and 07-compliance-and-guardrails/*
as_of: 2026-08-18
owner: Tumai
tags: [content, brief, template, articles, engine]
---

# Article brief template

**The core deliverable of the content engine.** A writer — human or AI — picks a topic cluster and
fills this in. The completed brief is a specification, not a suggestion: everything needed to write
the piece, and nothing that is not approved.

## How to use it

1. **Pick one cluster** from [11-topic-clusters](../11-topic-clusters/README.md)
2. **Pick one article idea** from that cluster's section 7
3. **Copy the template below** into `12-content-engine/briefs/YYYY-MM-DD-slug.md`
4. **Fill every field.** A field you cannot fill is a signal — usually that the evidence does not exist
5. **Write to the brief**, then run the pre-publish checklist
6. **Route for approval** per the tier the brief identifies

---

## The template — copy from here

```markdown
---
id: brief-<slug>
title: Brief — <working title>
type: brief
status: draft
confidence: verified
source: <cluster id> + the files listed in Load order
as_of: YYYY-MM-DD
owner: <writer>
tags: [brief, <cluster>, <intent>]
---

# Brief — <working title>

## 1 · The job

| | |
|---|---|
| **Cluster** | [cluster-x](../../11-topic-clusters/cluster-x.md) |
| **Messaging pillar** | Pillar N — *exactly one* |
| **Outcome** | Get More Leads / Make More Sales / Keep More Customers |
| **Reader** | [ICP file](../../03-audience-and-icp/) |
| **Awareness stage** | Unaware / problem-aware / solution-aware / comparing |
| **Intent** | Awareness / consideration / SEO / conversion |
| **Voice** | Tumai or Ariki |
| **Length** | 900–1,400 words (standard) |
| **CTA** | One. Named explicitly |
| **Approval tier** | 1 / 2 / 3 — per [approval rules](../../07-compliance-and-guardrails/approval-rules.md) |

## 2 · Load order

Read in this order before writing:

1. `07-compliance-and-guardrails/guardrails.md`
2. `04-voice-and-messaging/banned-language.md`
3. `04-voice-and-messaging/brand-voice.md`
4. `04-voice-and-messaging/messaging-pillars.md` — the one pillar
5. The cluster file
6. The ICP file
7. `05-proof-and-evidence/claims-register.md`
8. Any linked evidence in `06-research-and-market/`

## 3 · The argument

**One sentence.** What this piece argues. If it takes two, it is two pieces.

> …

**The reframe:** what the reader believes now → what they should believe after.

## 4 · Approved facts for this piece

Only these. **Everything else is out of bounds.**

| Fact | Source file | Tier |
|---|---|---|
| | | verified / inferred |

## 5 · Approved evidence

| Stat or proof | Source + date | Attribution required in copy |
|---|---|---|
| | | |

**If this section is empty, the piece argues from mechanism.** That is legitimate and often stronger.

## 6 · What this piece must NOT claim

Pulled from [what we cannot claim](../../05-proof-and-evidence/what-we-cannot-claim.md):

- No customer results, case studies or client counts
- No timeline or outcome guarantees
- No partner income
- <cluster-specific additions>

## 7 · Structure

| Section | Job | Words |
|---|---|---|
| Opening | Land in the reader's situation. No rhetorical question | 100–150 |
| The problem, specifically | Make the invisible cost visible | 200–300 |
| The reframe | The argument | 200–300 |
| The mechanism | How it actually works | 250–350 |
| The honest limit | What this does not solve. **Do not skip — it is the credibility move** | 100–150 |
| Close + CTA | One ask | 80–120 |

## 8 · Objections to pre-empt

From the cluster's section 5 and [10-faq-and-objections](../../10-faq-and-objections/):

- …

## 9 · Keywords

**Primary:** · **Secondary:** · **Questions to answer:**

> Marked `assumed` — no keyword research exists.

## 10 · Pre-publish checklist

- [ ] Maps to exactly **one** messaging pillar
- [ ] Every fact traces to a file in section 4
- [ ] Every statistic carries its source **and date in the copy itself**
- [ ] No claim outside the [claims register](../../05-proof-and-evidence/claims-register.md)
- [ ] No performance claim about OS A.I
- [ ] **GoHighLevel not named**, and no false provenance implied
- [ ] No banned language — **Tier 1, 2 and 3 checked explicitly**
- [ ] Australian English. No emoji. No exclamation marks
- [ ] No rule-of-three cadence, no "not just X — it's Y"
- [ ] Paragraph lengths vary
- [ ] The honest-limit section is present
- [ ] One CTA
- [ ] Approval tier identified and routed
- [ ] Passes: **would Tumai say this out loud without wincing?**

## 11 · Sources statement

Ends the handoff:

> Sources: `file.md`, `file.md`
> Approval: Tier N — <reason>
```

---

## Why the honest-limit section is mandatory

Section 7 requires a passage naming what the piece's argument does **not** solve. This is not
hedging. For a business with no case studies, **the willingness to name a limit is the primary
credibility mechanism available** — it is the difference between an argument and a pitch, and this
reader has been pitched before.

It is also the fastest way to disqualify bad-fit readers, which makes the sales conversations that
follow better.

## Related

- [Content standards](content-standards.md) · [Worked example](worked-example-brief.md)
- [Blog and article playbook](../08-channels-and-playbooks/blog-and-article.md)
