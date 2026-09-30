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
not fit, so the body ships pre-split into twelve pieces in `paste-chunks/`. Each is
under 10,000 characters and is valid HTML on its own.

1. Blog builder → click into the canvas → Ctrl+A, Delete, so it starts empty
2. Toolbar → the **`<>`** button → paste `paste-chunks/01.txt` → Insert code
3. Click **below** the block that just appeared, then `<>` again for `02.txt`
4. Repeat through `12.txt`, **in order**
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
| Interactive audit scorer | Rebuilt without JavaScript. Clickable 1-5 chips, a running total, and a working Reset |
| Internal links to the other four posts | Kept |

## What was lost, and why

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

## Title and hero image: why they are not in the body

**The title stays out.** The blog template renders the post title as the page's
`<h1>`, built from the Title field on the Continue screen. That field is what
search engines read. Putting the title in the body as well gives the page two
`<h1>` elements and, more to the point, shows the reader the headline twice.
Google tolerates duplicate H1s; readers notice them. Use the field.

**The hero image depends on the theme.** The Featured Image field does three
jobs: the thumbnail on the A.I Articles card, the `og:image` for social shares,
and, on some themes but not all, the image at the top of the post page.

Set the Featured Image first, then preview the post:

| What the preview shows | What to do |
|---|---|
| Image at the top of the post | Nothing. It is already there, adding it to the body would show it twice |
| Title but no image | Insert [`optional-hero-image.txt`](optional-hero-image.txt) as a code block **above** chunk `01.txt`, and swap `PASTE-YOUR-GHL-IMAGE-URL-HERE` for the media-library URL |

Keep the Featured Image set either way. The card and the social preview read
that field, not the body.

An in-body image carries no SEO penalty and a small benefit, because it sits in
the content flow with surrounding text and carries alt text. The snippet has
the alt text written in. Do not remove it.

## The audit scorer

The prototype's scorer ran on JavaScript, which a blog editor will strip. It has
been rebuilt with none: radio inputs styled as chips, `:checked` for the blue
fill, a **CSS counter** that sums the ten answers into the running total, and a
native `<button type="reset">` for the Reset.

It lives in `paste-chunks/09.txt` on its own, and is also kept standalone in
[`interactive-audit.txt`](interactive-audit.txt).

Verified by driving it in a browser: ten answers summing to 31 read 31, changing
one answer from 5 to 1 dropped it to 27, all fives read 50, and Reset returned it
to 0. Checked at 900px and 390px, where the rows stack and the chips stay at a
44px touch target.

What it still cannot do is name the reader's three highest areas, which needs
real arithmetic rather than a counter. The prose underneath already tells them to
pick their top three, so the instruction survives.

**The upgrade worth considering later:** rebuild it as a GHL survey. Right now the
reader scores themselves and keeps the answer. As a survey you capture the score
and the contact, and you walk into the call knowing which three areas they are
stuck on. That turns the best-engaging thing on the page into a lead magnet.

## The SEO metadata screen, filled

| Field | Value | Length |
|---|---|---|
| **URL slug** | `how-to-stop-being-the-founder-bottleneck` | 40 |
| **Title** | How to stop being the founder bottleneck in your business | 57, under Google's ~60 cutoff |
| **Alt text** | How to stop being the founder bottleneck, over a photo of a tradesperson stopping mid-job to answer his phone | 109 |
| **Post description** | Every decision routes through you. How to spot the founder bottleneck, keep the calls only you should make, and systemise the rest. With a scored audit. | 152, under the ~155 cutoff |
| **Author** | Tumai | Create the author if the dropdown has only Admin |
| **Category** | Whatever the existing five posts use | Wrong category means it misses the feed |
| **Status** | Draft | Approval tier is still unsigned |

Alt text describes the photo **and** repeats the words burned into the image.
Text inside an image is invisible to a screen reader and to Google unless the
alt carries it.

### Canonical link: check this after saving

The field defaults to `www.oscale.ai/post`. That is a base GHL completes with the
slug. **Confirm after saving that it reads the full post URL.** If it stays as
`www.oscale.ai/post`, clear the field completely rather than leave it: a canonical
pointing at `/post` tells Google this article is a duplicate of the blog index,
which is an instruction to drop it from results. An empty canonical is safe. A
wrong one is not.

### Keywords

| Keyword | Why |
|---|---|
| `founder bottleneck` | Exact topic match. Carried by the title, the slug, the H1 and the definition panel |
| `how to stop being the bottleneck in your business` | How people actually phrase it. The title answers the question verbatim, which is what gets pulled into featured snippets and AI answers |
| `business that runs without me` | From the cluster's own keyword map. Lower volume, highest emotional match to the buyer |

Volume is unverified: this session has no keyword tool and no network access to
one. These are chosen from `12-content-engine/keyword-map.md`, the cluster file
and what the copy actually supports, not from live search data. Check them in
Search Console or Ahrefs before building more around them.

This is a low-volume, high-intent cluster. Nobody searches "founder bottleneck"
in large numbers. The people who do are the buyer, exactly.

## The "On this page" rail

Above 1200px viewport width the panel leaves the content flow and parks in the
left gutter as a fixed rail, and a small script highlights the section you are
currently reading. Below 1200px it stays exactly as before: a static panel at the
top of the article. All of it lives in `paste-chunks/01.txt`.

Sticky positioning was not an option. Each chunk is its own code block, so a
sticky element's containing block ends a few hundred pixels down and it would
unstick immediately. Fixed positioning does not care about the parent's height.

The script is guarded on `DOMContentLoaded`, because chunk `01.txt` is parsed
before chunks 2 to 12 exist in the DOM. Without that guard it would find no
sections and silently do nothing.

Verified at 1400px: the rail held at top 110px, left 90px through the whole
scroll, and each of `why`, `step-3`, `step-6`, `audit` and `faq` highlighted its
own link. At 1000px the rail returned to static.

### If it misbehaves on the live site

Two failure modes, both from the page builder rather than this code.

**The rail scrolls away, or sits in the wrong place.** An ancestor has a
`transform`, `filter` or `will-change`, which makes `position:fixed` resolve
against that ancestor instead of the viewport. No CSS fix from inside the block.

**Nothing highlights.** The editor stripped the `<script>`. Everything else still
works, the links still jump, only the highlight is gone.

In both cases the fallback is the same: republish `01.txt` with the `<style>` and
`<script>` blocks removed, and the panel returns to a static list at the top.

## Stat block effects

The six figures count up from zero when they scroll into view, and the cards
fade and rise in with a 90ms stagger. Both are driven from the single
`<style>` + `<script>` block at the end of `paste-chunks/12.txt`, which also
carries the contents-rail scroll-spy.

The markup holds the final value, so a reader whose browser never runs the
script sees `2,241` sitting there. The fade is gated behind an `osai-go` class
that the script puts on `<html>`, so nothing is ever hidden on a page where the
script did not run. `prefers-reduced-motion: reduce` skips both effects.

**Mobile.** The grid is three across on desktop and drops to one full-width card
below 560px. Two columns with three cards left an orphan on the bottom row.

The column rule had to move out of the inline style to make that work. An inline
`!important` outranks a stylesheet `!important`, so while the columns were
declared on the element the breakpoint could never win. Both rules now live in
the stylesheet, where normal cascade order applies.

Verified in a browser: mid-animation the figures read 640, 15hrs and 8% with
card opacities of 0.63, 0.07 and 0 (the stagger), settling to the correct six
values. At 390px the grid computed to a single 348px column with no horizontal
overflow.
