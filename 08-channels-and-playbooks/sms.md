---
id: sms
title: Playbook — SMS
type: playbook
status: approved
confidence: verified
source: Spam Act 2003 · 02-offer-and-pricing/platform-capabilities.md · 04-voice-and-messaging/*
as_of: 2026-08-18
owner: Tumai
tags: [playbook, sms, spam-act, compliance]
---

# Playbook — SMS

## Purpose

Short, functional, time-sensitive. **SMS is the highest-permission channel and the easiest to
abuse.** Every message should be one the recipient would have been annoyed to miss.

## Load order

1. [`../07-compliance-and-guardrails/guardrails.md`](../07-compliance-and-guardrails/guardrails.md)
2. [`../07-compliance-and-guardrails/acl-and-consumer-law.md`](../07-compliance-and-guardrails/acl-and-consumer-law.md) — **Spam Act obligations**
3. [`../04-voice-and-messaging/banned-language.md`](../04-voice-and-messaging/banned-language.md)
4. [`../04-voice-and-messaging/brand-voice.md`](../04-voice-and-messaging/brand-voice.md)

## The legal floor — Spam Act 2003

Non-negotiable, and it applies to **AI-sent messages exactly as it does to human-sent ones**:

- **Consent.** Express or inferred. No purchased lists
- **Accurate sender identification.** The recipient must know who it is from
- **A functional opt-out in every commercial message**, honoured promptly

## Formats

| Type | Length | Job |
|---|---|---|
| **Missed-call follow-up** | Under 160 chars | The highest-value SMS OS A.I sends |
| **Appointment confirmation** | Under 160 | Functional |
| **Reminder** | Under 160 | Functional |
| **No-show follow-up** | Under 160 | One offer to rebook |
| **Reply in conversation** | Varies | Handled by the agent — see [chat agent spec](../10-faq-and-objections/chat-agent-spec.md) |

## Do

- **One message, one purpose**
- Identify who it is from in the first few words
- Use the recipient's name where known
- Include the opt-out
- Send within business hours unless the message is triggered by the recipient's own action
- Lower case is fine. Natural, not shouty

## Don't

- No emoji
- No exclamation marks
- **No marketing broadcast to a list that opted in for something else**
- No urgency or scarcity
- No links without context — it reads as phishing
- **Never name GoHighLevel**
- No performance claim
- **No partner income implication**

## Pre-send checklist

- [ ] Under 160 characters where possible
- [ ] One purpose
- [ ] Sender identifiable
- [ ] **Consent basis exists and is documented**
- [ ] **Opt-out present and functional**
- [ ] Sending hours appropriate
- [ ] No emoji, no exclamation marks
- [ ] Australian English
- [ ] Banned language Tier 1 checked

## Worked examples

**Missed-call follow-up:**
> Hi Sarah — Ariki from OS A.I, sorry we missed your call. Happy to answer by text if easier, or
> here's my calendar: [link]. Reply STOP to opt out.

**Appointment reminder:**
> Hi Sarah, reminder of your call with Tumai tomorrow at 10am. Reply here if you need to move it.
> Reply STOP to opt out.

**No-show follow-up:**
> Hi Sarah — we had 10am today and I know things come up. Want to grab another time? [link]
> Reply STOP to opt out.

**Why these work:** identified sender, one purpose, opt-out, no pressure, and the no-show message
assumes good faith rather than guilting.

## Related

- [ACL and consumer law](../07-compliance-and-guardrails/acl-and-consumer-law.md) · [Email](email.md)
