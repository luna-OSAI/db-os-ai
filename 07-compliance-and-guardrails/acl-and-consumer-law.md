---
id: acl-and-consumer-law
title: Australian Consumer Law — the obligations that bind this business
type: compliance
status: approved
confidence: verified
source: Competition and Consumer Act 2010 (Cth) Sch 2 · Spam Act 2003 · Do Not Call Register Act 2006 · OS Refund Policy · www.oscale.ai
as_of: 2026-08-18
owner: Tumai
tags: [compliance, acl, accc, consumer-law, australia]
---

# Australian Consumer Law

> **Not legal advice.** This file translates the obligations that plainly apply to how OS A.I
> markets and sells, so content does not walk into them. Anything genuinely contentious goes to a
> lawyer, not to this file.

OS A.I is an Australian business (ABN 75 527 278 804) selling to Australian consumers and small
businesses. The ACL applies to everything it publishes.

## The four that matter most

### 1 · Misleading or deceptive conduct — ACL s18

The broadest provision in the Act. Conduct that is **likely to mislead** breaches it — intent is
irrelevant, and so is whether anyone was actually misled. Overall impression governs, including what
the fine print does not fix.

**Where OS A.I is exposed:** performance claims with no substantiation; implying a track record that
does not exist; an impression that the trial is cost-free; implying tier differences that are not
documented.

### 2 · False or misleading representations — ACL s29

Specific prohibitions, each attracting penalties. The relevant ones:

- **s29(1)(g)** — false representation about performance characteristics, uses or benefits
- **s29(1)(i)** — false representation about price
- **s29(1)(m)** — false representation about a **guarantee, warranty or right to a remedy**

**s29(1)(m) is the one to watch.** A blanket "no refunds under any circumstances" can itself be a
misrepresentation of the consumer's statutory rights.

### 3 · Consumer guarantees — ACL Part 3-2 Div 1

Automatic, statutory, and **cannot be excluded, restricted or modified by contract.** Services must
be supplied with due care and skill, be fit for the disclosed purpose, and be delivered in a
reasonable time. Where a service fails, the consumer has remedies regardless of what the terms say.

**These guarantees apply to businesses buying too**, where goods or services are under $100,000 or
of a kind ordinarily acquired for personal or domestic use — which captures a large share of the
SMB market OS A.I sells to.

**The practical consequence for the refund policy:** the policy's blanket "all purchases are final"
is enforceable only to the extent it does not cut across the guarantees. So:

- ✅ Copy may state the policy — "setup fees are non-refundable."
- ❌ Copy may **never** state or imply the customer **has no rights**, no recourse, or that the policy overrides the law.
- ✅ Best practice is a line noting that nothing in the policy limits rights under the Australian Consumer Law.

**This is worth raising with the founders as a live site issue**, not just a copy rule. It is logged
in the [enrichment roadmap](../00-start-here/ENRICHMENT-ROADMAP.md).

### 4 · Pyramid schemes and referral selling — ACL Part 3-1 Div 3, s49

Covered in [partner and income claims](partner-and-income-claims.md).

## Subscription and trial obligations

The 7-day trial auto-converts to a paid subscription. Where a trial converts to payment, the
consumer must be **clearly informed before signing up** — what will be charged, when, and how to
cancel. Burying it in terms is not sufficient; the ACCC has pursued businesses over exactly this
pattern.

**Every promotion of the trial must state, visibly:** it converts to a paid subscription at day 7
unless cancelled, at what price, and how to cancel.

## Channel legislation

| Law | Applies to | Requirement |
|---|---|---|
| **Spam Act 2003** | Email, SMS | Consent · accurate sender identification · functional unsubscribe in every message |
| **Do Not Call Register Act 2006** | Outbound voice | DNC check before calling. The platform supports this; using it is mandatory |
| **Privacy Act 1988 / APPs** | All customer data | Collection notice, purpose limitation, secure handling. A privacy policy exists |
| **Spam Act, applied to AI agents** | Automated messages | An AI-sent message is still a commercial electronic message. All obligations apply |

## AI-specific exposure

No settled Australian AI-marketing statute exists as at 2026-08-18, but two things already follow
from existing law:

1. **An AI agent's statements are the company's statements.** If Oliver or Olivia makes an unsubstantiated performance claim to a prospect, that is OS A.I's s18 exposure. The agent's knowledge base is a compliance surface. See [chat agent spec](../10-faq-and-objections/chat-agent-spec.md).
2. **Impersonating a human is a misleading-conduct risk.** Agents must never claim to be human, and should identify as AI when asked.

## Related

- [Guardrails](guardrails.md) · [Claims policy](claims-policy.md)
- [Partner and income claims](partner-and-income-claims.md)
