---
id: approval-rules
title: Approval rules — what needs sign-off before publication
type: compliance
status: approved
confidence: verified
source: Derived from guardrails.md, claims-policy.md and partner-and-income-claims.md
as_of: 2026-08-18
owner: Tumai
tags: [compliance, approval, workflow, governance]
---

# Approval rules

## Three tiers

### Tier 1 — publish freely
No sign-off needed. Generate, check against the playbook checklist, ship.

- Capability descriptions drawn from [platform capabilities](../02-offer-and-pricing/platform-capabilities.md)
- Commercial facts matching the live site
- Educational content built from a [topic cluster](../11-topic-clusters/README.md) using registered claims
- Answers paraphrased from the [FAQ](../10-faq-and-objections/faq.md)
- Anything using only claims already in the [claims register](../05-proof-and-evidence/claims-register.md)

### Tier 2 — founder sign-off before publication

- Anything stating or implying a **customer result**
- Any **new claim** not in the register
- Anything naming a **competitor** or quoting a competitor price
- Anything asserting **security, compliance or data-handling** properties
- Pricing that differs from the live site
- Anything about the **7-day trial** mechanics
- Any statement about **refunds or cancellation**
- **Any partner-facing asset** — mandatory while [partner and income claims](partner-and-income-claims.md) is `draft`

### Tier 3 — legal review

- The three-tier partner structure against ACL Part 3-1 Div 3
- The refund policy's blanket "all purchases are final" against the consumer guarantees
- Any contract, terms change or partner agreement
- Any claim likely to attract a substantiation demand

## Who signs

| Domain | Approver |
|---|---|
| Positioning, brand, messaging | Tumai |
| Offer, pricing, sales claims | Tumai and Ariki |
| Delivery and onboarding claims | Ariki or Audrey |
| Partner program | Tumai and Ariki — plus legal, currently |
| Legal and compliance | External |

## When an AI is generating

State the tier in the handoff. A draft returned without flagging that it contains a Tier 2 element
is a failed draft, even if the copy is good.

**Format:**

> Sources: `02/subscription-plans.md`, `11/cluster-software-sprawl.md`, `06/competitor-hubspot.md`
> **Approval: Tier 2** — quotes a competitor price. Needs sign-off before publication.

## Related

- [Guardrails](guardrails.md) · [Claims policy](claims-policy.md)
