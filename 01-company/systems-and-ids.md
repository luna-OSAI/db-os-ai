---
id: systems-and-ids
title: Systems and IDs
type: system
status: approved
confidence: verified
source: 13_Onboarding_SOP.md · www.oscale.ai fetched 2026-08-18 · legal policy documents
as_of: 2026-08-18
owner: Tumai
tags: [systems, ids, infrastructure, tooling]
---

# Systems and IDs

What OS A.I runs on. **Incomplete — see the gaps at the bottom.**

## Known systems

| System | Purpose | Detail |
|---|---|---|
| **GoHighLevel (white-label)** | The platform itself | Clients are provisioned as sub-accounts. **Never named client-facing** |
| **Website** | www.oscale.ai | Nav: Chat Agent · Voice Agent · Free Blueprints · A.I News · Login |
| **Slack** | Internal comms | Ops notifications during onboarding |
| **Asana** | Project management | Referenced in the master KB ops section |
| **Termly** | Legal policy hosting | Policy UUIDs embedded in the T&C |
| **Skool** | Community | Free and paid onboarding workflows exist |

## Public surfaces

| Surface | Value |
|---|---|
| Site | https://www.oscale.ai |
| General contact | hello@oscale.ai |
| Support / escalation | success@teamos.ai |
| Phone | (+61) 467 733 801 |
| Named AI agents | **Oliver** and **Olivia** — the site's chat/voice personas |

## Site structure, as published

- **Chat Agent** — the chat product
- **Voice Agent** — the voice product
- **Free Blueprints** — the lead magnet surface
- **A.I News** — the content surface. **This is where article output lands.** See [the content engine](../12-content-engine/idea-bank.md)
- **Login** — customer portal
- Pricing section: Pro · Partner · Platinum

## Not recorded — needed before any live integration

These are genuine gaps, not oversights (G9 in the [gap list](../00-start-here/GAP-LIST.md)):

- GoHighLevel **location ID** for the OS A.I account
- **Calendar IDs** for the discovery and demo calendars
- **Pipeline names and stage IDs**
- **Form and survey IDs** for the audit and opt-in flows
- Website **repository** — whether the site is in GHL, a repo, or both
- Analytics property IDs

Anything that must read from or write to live systems is blocked until these exist.

## Related

- [How we work](how-we-work.md) · [White-label disclosure](../07-compliance-and-guardrails/white-label-disclosure.md)
