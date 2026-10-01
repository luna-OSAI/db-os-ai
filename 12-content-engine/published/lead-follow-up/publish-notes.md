---
id: publish-lead-follow-up
title: Publish notes — How to Set Up Automated Lead Follow-Up in 5 Steps
type: playbook
status: approved
confidence: verified
source: Vercel prototype (osai-leadfollowup-live.vercel.app) converted for the GoHighLevel blog builder
as_of: 2026-10-01
owner: Luna
tags: [publish, lead-follow-up, ghl, blog]
---

# Publish notes — automated lead follow-up

Paste-ready body: `paste-chunks/01.txt` through `06.txt`, in order.

## How to publish

GHL's Insert custom code field has a length limit and silently drops the
overflow, so the body ships pre-split into six pieces, each under 8,600
characters.

1. Blog builder → click into the canvas → Ctrl+A, Delete
2. Toolbar → `<>` → paste `01.txt` → Insert code
3. Click below the block, `<>` again for `02.txt`, and so on through `06.txt`
4. **Continue** → fill the fields below
5. Preview on desktop and phone

Copy from the `.txt` files. An `.html` file renders in most previews and
copying a rendered view strips every tag.

Chunks 1 to 3 are the stylesheet, 4 and 5 the article, 6 the script. Order
matters, but CSS and JS work wherever they land, so a mis-ordered middle chunk
shows up as scrambled prose rather than lost styling.

## The Continue screen

| Field | Value | Length |
|---|---|---|
| **Title** | How to Set Up Automated Lead Follow-Up in 5 Steps | 49 |
| **URL slug** | `automated-lead-follow-up-setup-guide` | 36 |
| **Description** | Set up automated lead follow-up in 5 steps: map the journey, centralise lead data, automate the first reply, build a sequence and test it before launch. | 152 |
| **Alt text** | Two tradespeople sitting in the back of a work van, one checking a new enquiry on his phone | 91 |
| **Author** | Ariki Meroiti | Per `content-standards.md`: Ariki for delivery reality and practical how-to |
| **Publish date** | 29 September 2026 | |
| **Category** | Match the existing posts | |
| **Status** | Draft until approval tier is signed | |

The slug comes from the prototype's own canonical tag, so the internal links
other articles already point at will resolve.

**Canonical link:** confirm after saving that it reads the full post URL. If it
stays as `www.oscale.ai/post`, clear the field. A canonical pointing at the blog
index tells Google the article duplicates that index.

### Keywords

`automated lead follow-up` · `how to automate lead follow-up` · `lead follow-up system`

Volume unverified: no keyword tool or network access in this session. Chosen
from the copy and the prototype's own title and description.

## What is in the body, and what is not

Left out because the blog template renders them: the `<h1>`, the lede, the
byline and date, the masthead and footer, and the hero photograph (that goes in
the **Featured Image** field).

Kept and working: the audio overview, the six-stage lead journey diagram, the
TL;DR panel, the five step headers with their progress dots, the cell grids, the
sourced statistic, the one-week sequence timeline and table, the interactive
pre-launch checklist with its progress meter, the FAQ accordions, the CTA band
and the suggested-reading links.

## Built differently from the founder bottleneck article

That one used inline styles on every element. This one uses a scoped stylesheet,
because the founder bottleneck build proved a `<style>` block survives the custom
code field. Everything is scoped under `.lf`, which each chunk wrapper carries.
It is a quarter of the size and supports what inline styles cannot: `::before`
bars, `:hover`, `:checked`, media queries and the mobile table stacking.

## The host theme carries !important on its own rules

Every declaration in the stylesheet is forced. That is not belt and braces: a
theme rule on `ol`/`ul` beat the plain `display:grid` on the lead journey, which
collapsed the six stages into a stacked list while their horizontal connectors
kept drawing, running off the side of the panel. A stylesheet `!important` beats
any amount of selector specificity, so forcing every declaration is the only
reliable answer.

Two consequences worth remembering:

**Script-set inline styles now need priority too.** An ordinary
`el.style.transform = ...` loses to a forced stylesheet rule. The checklist
meter bar sets its width with `setProperty(..., 'important')` for that reason.

**Chunks may only break where nothing is open.** Several markup lines together
form one element, so the splitter tracks tag depth and ends a chunk at depth
zero. An earlier version split by line and happened to land on clean boundaries;
when the stylesheet grew, it cut a card in half.

## What was lost

**The theme toggle and the reading progress bar.** Both belong to the prototype's
own page chrome, which the blog template replaces.

**The audio speed control.** It needs a control the native player does not
expose. The narration still plays, and the script still reads the real runtime
into the subtitle.

## Verified, not assumed

| Check | Result |
|---|---|
| Horizontal overflow | None at 320, 360, 390, 414, 640, 768, 1024, 1280, 1440 |
| Lead journey | Six across above 900px, stacked vertically below |
| Cell grids | Two columns, one below 560px |
| Sequence table | Stacks to labelled rows below 640px |
| Checklist | 3 of 7 → 7 of 7 → untick to 6 of 7, meter bar and message track correctly |
| Statistic | Counts up and settles on 42 hours and 23%, the real figures, on first view and on return |
| Contents rail | Measured against the real column, hidden at the top, 0 overlap, correct section highlighted at steps 2, 4 and the FAQ, hidden at the end |
| Text contrast | Every measurable pair passes AA; the CTA gradient samples 5.71 to 7.34 against white |
| Heading order | h2/h3/h4 with no skipped levels |
| Checkboxes | All seven inside labels, with a live region announcing the count |
| Tap targets | Contents 31px, checklist 44px, FAQ 60px, CTA 53px |
| Keyboard | Visible 2px focus ring on first Tab |

Scripted checks, not a live screen reader. VoiceOver or NVDA on the published
post is still worth ten minutes.

## One bug found in the prototype

The hero `srcset` is malformed in both the `<source>` and the `<img>`: a stray
`,,,` closes the attribute after the 640w candidate, so the 960, 1280 and 1920
files are parsed as junk attributes and never served. Every visitor gets the
640px image. It does not affect the GHL post, which uses the Featured Image
field, but it is worth fixing if the prototype stays up.


## Device sweep

Run across seventeen viewports in Chromium, portrait and landscape, with a real
mobile viewport meta: 280x653 (folded phone), 320x568, 360x780, 393x852,
412x915, 430x932, 852x393 and 915x412 (phones on their side), 744x1133,
1024x1366 and 1366x1024 (tablets), 1280x800, 1440x900, 1920x1080, 2560x1080,
1280x500 (short window) and 360x1200 (tall narrow).

**No horizontal page scroll and nothing spilling past the viewport at any of
them.** Tables and the lead journey keep their own scroll containers, so the
page body never moves sideways.

The only elements under the 24px tap minimum are inline text links inside a
sentence, which WCAG 2.5.8 exempts by name. Every control that is not inline
text clears it: contents links 31px, checklist rows 44px, FAQ rows 60px, the
call-to-action button 53px.

An earlier sweep reported a one-pixel scroll on one device. That was the test
harness, not the article: mobile emulation was on without a viewport meta, so
those rows were quietly laying out at 980px rather than the phone width. With
the meta in place the result is clean.

## The audio mark

The prototype for this article uses the OS A.I logo at 36px beside the title, not
a headphone. The ringed headphone was carried over from the founder bottleneck
article, whose prototype does use one.

What ships is a filled brand disc with a white headphone glyph: closer in weight
to the logo mark the prototype intends, and it needs no asset to be uploaded.
To match the prototype exactly, swap the `<span class="lf-mark">` for an `<img>`
of the logo from the GHL media library and drop the `.lf-mark` background.

A selector bug sat underneath this the whole time. `.lf-listen-head span` was
written for the subtitle, but the icon's wrapper is a span in the same block, and
at equal weight the longer selector won. The glyph was rendering in muted grey
rather than brand blue, which is why it read as unfinished even once its size was
correct. The rule is now `.lf-listen-head>div>span`.

The two articles' audio blocks now differ: a filled disc here, a hairline ring on
the founder bottleneck piece. Each matches its own prototype. Worth unifying if
they are meant to look like one series.
