---
id: claims-policy
title: Claims policy — what evidence a claim needs
type: compliance
status: approved
confidence: verified
source: Australian Consumer Law s18, s29 · SCHEMA decision D2 · 05-proof-and-evidence/claims-register.md
as_of: 2026-08-18
owner: Tumai
tags: [compliance, claims, evidence, substantiation]
---

# Claims policy

What evidence a statement needs before it can ship.

## The four claim types

| Type | Example | Evidence required |
|---|---|---|
| **Capability** | "Books appointments inside the conversation" | The feature exists in [platform capabilities](../02-offer-and-pricing/platform-capabilities.md). **Lowest bar — most copy should live here** |
| **Commercial** | "$297 per month" · "7-day trial" | Matches the live site or [subscription plans](../02-offer-and-pricing/subscription-plans.md) |
| **Market** | "SMBs run 8–12 tools on average" | Dated, URL-cited third-party source in [research and market](../06-research-and-market/README.md) |
| **Performance** | "Clients get 5 leads a week" | **A measured OS A.I result. None exist.** Cannot ship |

**The safest strong copy is capability plus customer pain.** You do not need a performance claim to
be persuasive — you need a specific mechanism against a specific frustration.

## The register-first rule

Before writing any claim about OS A.I's results, effects or scale, check the
[claims register](../05-proof-and-evidence/claims-register.md).

- **In the register, approved** → use it, in its registered wording.
- **Not in the register** → it does not ship. Escalate via [approval rules](approval-rules.md).

New claims are added by decision, not by drafting.

## Language that upgrades a claim without evidence

These constructions turn a safe statement into an unsafe one. Watch for them:

| Safe | Becomes unsafe as |
|---|---|
| "Responds to enquiries 24/7" | "Never miss another lead" |
| "Replaces Mailchimp, Calendly and Zapier" | "Cuts your software bill in half" |
| "Built and installed for you" | "Live in 7 days" |
| "Designed to reduce admin time" | "Saves you 20 hours a week" |
| "The platform handles follow-up" | "Doubles your conversion rate" |

The right column all make **performance claims**. None can be substantiated. The pattern is the
same each time: a description of what the system *does* is quietly converted into a promise of what
the customer *gets*.

## The company's own figures

Several numbers recur across internal documents. They are the company's estimates, not measurements:

| Figure | Status | How to use |
|---|---|---|
| Replaces 8–12 tools | `inferred` | As OS A.I's position, phrased as such |
| Cuts software costs 50–70% | `inferred` | Never as a promise to a specific buyer |
| Reclaims 15–20 hours/week | `inferred` | Never as a promise |
| Typical stack costs $500–1,000/mo | `inferred` | Better replaced with a sourced market figure |
| ≤7 day onboarding | Internal target | Intent, never a commitment |
| 90–95% retention | Internal target | **Never publish.** It is a goal, and publishing it reads as achieved |
| HubSpot at $890/month | **Unsourced** | **Do not use** until [competitor-hubspot](../06-research-and-market/competitor-hubspot.md) verifies it |

## The five published site claims

Approved for reuse as published, per D2. Bounded exactly as set out in
[guardrails § the claims exception](guardrails.md). Do not escalate, do not attach to a customer,
do not use where substantiation will be demanded.

## Before publishing anything with a number in it

- [ ] Is it a capability, commercial, market or performance claim?
- [ ] If performance — stop. It does not ship.
- [ ] If market — does it have a URL and a `researched:` date?
- [ ] If commercial — does it match the live site today?
- [ ] Is it in the claims register, in the registered wording?
- [ ] Has a safe capability statement been silently upgraded into a promise?
- [ ] Would OS A.I be able to hand a regulator the evidence tomorrow?

## Related

- [Guardrails](guardrails.md) · [Claims register](../05-proof-and-evidence/claims-register.md)
- [What we cannot claim](../05-proof-and-evidence/what-we-cannot-claim.md)
