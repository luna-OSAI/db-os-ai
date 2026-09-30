---
id: publish-founder-bottleneck
title: Publish notes — How to stop being the founder bottleneck
type: playbook
status: approved
confidence: verified
source: Vercel prototype source (osai-founderbottleneck-live.vercel.app) converted for the GoHighLevel blog builder
as_of: 2026-09-30
owner: Luna
tags: [publish, founder-bottleneck, ghl, blog]
---

# Publish notes — founder bottleneck article

Paste-ready body: [`body.html`](body.html)

## How to publish

GHL's Insert custom code field has a length limit and silently drops what does
not fit, so the body ships pre-split into ten pieces in `paste-chunks/`. Each is
under 9,100 characters and is valid HTML on its own.

1. Blog builder → click into the canvas → Ctrl+A, Delete, so it starts empty
2. Toolbar → the **`<>`** button → paste `paste-chunks/01.txt` → Insert code
3. Click **below** the block that just appeared, then `<>` again for `02.txt`
4. Repeat through `10.txt`, **in order**
5. **Continue** → fill the fields below
6. Preview on desktop and phone before publishing

Copy from the `.txt` files, never from `body.html`. An `.html` file renders in
most previews, and copying a rendered view strips every tag.

`body.html` is the single-file master, kept for reference and for regenerating
the chunks if the copy changes.

## The Continue screen

| Field | Value |
|---|---|
| **Title** | How to stop being the founder bottleneck in your business |
| **URL slug** | `how-to-stop-being-the-founder-bottleneck` |
| **Description** | Every decision still routes through you. How to spot the founder bottleneck, keep the calls only you should make, and systemise all the rest. |
| **Author** | Tumai |
| **Category** | Match the existing A.I Articles feed |
| **Publish date** | 29 September 2026 |
| **Featured image** | `founder-bottleneck-hero-1600.jpg`, uploaded to GHL media |
| **Image alt** | Founder bottleneck in practice: a mechanic pauses the job to answer a message on his phone |

**Tags** — matches the density of the existing cards:

`Founder Bottleneck` · `Business That Runs Without Me` · `Systemise My Business` · `AI Automation For Business` · `Small Business Australia` · `Delegation For Founders` · `AI For Small Business`

## What the body does NOT include, on purpose

The GHL blog template already renders these, so they are not in `body.html`:

- The `<h1>` title
- The byline and publish date
- The hero image (set it as the featured image instead)
- The site masthead and footer

The lede paragraph became the **Description** field rather than body copy, so the post opens on "A quote request lands at 7:40 on a Tuesday night", which is the intended opening per `12-content-engine/content-standards.md`.

## Optional: get the real typeface

The prototype uses **Barlow Condensed**. The body HTML falls back to Oswald, Roboto Condensed and Arial Narrow if it is not loaded. To get the actual font, add this once in GHL under Sites → your site → Settings → Tracking Code → **Head**:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

Check first whether the site already loads it. The A.I Articles card titles look like a condensed face already.

## Optional: FAQ rich results

The prototype carries FAQPage structured data for the eight questions. Rich text editors usually strip `<script>` on save. Try pasting the block below at the very end of the code view, save, then reload the editor. If it is gone, the schema did not survive and there is no clean per-post workaround in the GHL blog. The FAQ section still reads fine without it, you just lose the chance of an expanded search result.

```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is a founder bottleneck?","acceptedAnswer":{"@type":"Answer","text":"A founder bottleneck occurs when business operations, decisions or growth depend too heavily on the founder's personal time, knowledge or approval. It is a structural condition rather than a personal failing, and it usually accumulates one reasonable decision at a time."}},
{"@type":"Question","name":"How do I know if I am the bottleneck?","acceptedAnswer":{"@type":"Answer","text":"Look for recurring patterns where work stops when you are unavailable, team members regularly ask for approval, or you are personally handling repeatable tasks that could follow a defined process."}},
{"@type":"Question","name":"At what size does the founder bottleneck become a problem?","acceptedAnswer":{"@type":"Answer","text":"Earlier than most advice assumes. A business with three or four staff hits the same ceiling as a larger one, because it has no management layer to absorb decisions. At that size the available owner for routine work is a system rather than a new manager."}},
{"@type":"Question","name":"Is being the founder bottleneck the same as micromanaging?","acceptedAnswer":{"@type":"Answer","text":"No. Micromanaging is a behaviour, which means staying involved in work someone else owns. A founder bottleneck is a structure, where the business routes decisions through one person because it has no other way to resolve them. A founder can stop micromanaging entirely and still be the bottleneck."}},
{"@type":"Question","name":"Does hiring more staff fix the founder bottleneck?","acceptedAnswer":{"@type":"Answer","text":"Not on its own. If new team members still need the founder for routine decisions, extra staff can increase the number of requests coming back to you. The underlying process has to change first."}},
{"@type":"Question","name":"Can AI remove the founder bottleneck?","acceptedAnswer":{"@type":"Answer","text":"AI can reduce founder involvement in repeatable workflows. It does not replace founder-level judgement. The best starting point is to identify a clear process, define the rules, then automate the predictable parts of it."}},
{"@type":"Question","name":"What should a founder automate first?","acceptedAnswer":{"@type":"Answer","text":"Start with repetitive, high-volume workflows that follow clear rules. Lead follow-up, missed-call handling, appointment booking, CRM updates, onboarding communication and routine reporting are the usual candidates."}},
{"@type":"Question","name":"How do I delegate without losing control?","acceptedAnswer":{"@type":"Answer","text":"Use approval mode for anything you want to see before it goes out. Replies and actions are drafted and held for your sign-off rather than sent automatically. Then define the outcome, the decision boundaries, the owner and the escalation rules, and move individual workflows to autopilot as you get comfortable with them."}}]}
</script>
```

## What survived the transfer

| Element | Status |
|---|---|
| Typography scale and hierarchy | Kept, `clamp()` works inline so headings still scale with the viewport |
| Blue rule above every H2 | Kept |
| Pull quotes with the blue left bar | Kept |
| Definition and rule panels, with gradient top bar | Kept, gradient bar rebuilt as a real div since `::before` cannot inline |
| Stat blocks | Kept, `auto-fit` grid so they reflow without media queries |
| Flow diagrams with blue arrows | Kept |
| All four data tables | Kept, wrapper scrolls horizontally on narrow screens |
| Blue list markers | Kept, via a colour trick on the `li` |
| FAQ accordions | Kept, native `<details>`, works without JavaScript |
| Gradient CTA band and button | Kept |
| Audio overview player | Kept, and the file is already on GHL's CDN so it will play |
| In-page table of contents | Kept as a static panel at the top, anchors work |
| Internal links to the other four posts | Kept |

## What was lost, and why

**The interactive audit scorer.** It was built entirely by JavaScript, which the blog editor strips. Without it the form renders as an empty box. Replaced with a static ten-row scoring table. The surrounding prose still works because it already tells the reader to add their own scores.

> Worth considering: rebuild the scorer as a **GHL survey** and embed it. It becomes a lead magnet rather than a toy, because you capture the score and the contact instead of the reader keeping both. That is a bigger change than a paste, so it is a separate job.

**Scroll-reveal animation, the reading progress bar, the table-of-contents scroll-spy, the theme toggle, the counting stat numbers, and the audio speed control.** All JavaScript. The stat numbers still display their final values, which was already the no-JS fallback in the prototype.

**Hover states on the CTA button and links.** Inline styles cannot express `:hover`.

**Dark mode.** Converted to the prototype's own light-theme token values, because the blog template renders on a white page and the dark palette would have put white text on white.

**The sticky sidebar layout.** GHL's blog body is one narrow column.

## Two bugs in the prototype

Neither affects the GHL post, but fix them if the Vercel build stays up.

**The responsive image srcset is malformed.** Both the `<source>` and the `<img>` have a stray `,,"` that closes the attribute after the 800w candidate, so the 1200w and 1600w files are parsed as junk attributes and never served. Every visitor gets the 800px image.

**The footer of the live news listing reads "Copyrights 20234".** Separate from this article, but it is on every page.

## Already handled

The prototype carries `<meta name="robots" content="noindex, nofollow, noarchive, noimageindex">`, so it will not compete with the oscale.ai post for the "founder bottleneck" keyword. Nothing to do there.

## Pre-publish checklist

Run against [`08-channels-and-playbooks/blog-and-article.md`](../../../08-channels-and-playbooks/blog-and-article.md):

- [x] Exactly one messaging pillar — Pillar 3, the founder bottleneck
- [x] Every stat attributed in the copy with publisher and year — HBR 2011, ABS 2024-25
- [x] No OS A.I performance claim
- [x] GoHighLevel not named anywhere in the body
- [x] Honest-limit section present — "What this does not solve"
- [x] One CTA — book a walkthrough
- [x] Byline assigned — Tumai
- [x] Australian English, no emoji, no exclamation marks
- [x] Paragraph lengths vary
- [x] Sources stated in the copy
- [ ] Approval tier identified — outstanding, needs Tumai's sign-off before it goes live
