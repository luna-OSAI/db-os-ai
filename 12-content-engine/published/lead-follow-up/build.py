# -*- coding: utf-8 -*-
"""Builds the GHL-ready body for the lead follow-up article.

The prototype's styling is hand-written CSS with semantic class names. A
<style> block survives GoHighLevel's custom-code field (proven on the founder
bottleneck article), so the design ports as a scoped stylesheet rather than as
thousands of inline declarations. Every chunk wrapper carries .lf, which scopes
the rules and lets the stylesheet live in the first chunk alone.
"""
F = "'Barlow Condensed','Oswald','Roboto Condensed',sans-serif"

# Light-theme tokens, taken from the prototype's own [data-theme="light"] block.
# The page renders on white, so the dark palette would be white-on-white.
CSS = """
.lf{font-family:__FONT__;max-width:68ch;margin:0 auto}
.lf *{box-sizing:border-box}
.lf p,.lf li,.lf td,.lf th,.lf h2,.lf h3,.lf h4,.lf summary,.lf span,.lf b,.lf a{font-family:__FONT__!important}
.lf p{margin:0 0 24px!important;font-size:18px!important;line-height:1.62!important;color:#2D2D2D!important}
.lf h2{font-weight:700!important;font-size:clamp(30px,4vw,44px)!important;line-height:1.06!important;letter-spacing:-.003em!important;color:#002147!important;margin:80px 0 24px!important;padding-top:24px!important;border-top:1px solid #DDE5EE!important;scroll-margin-top:90px}
.lf h3{font-weight:700!important;font-size:clamp(24px,3vw,33px)!important;line-height:1.1!important;color:#002147!important;margin:0 0 16px!important}
.lf h4,.lf-cell h3{font-weight:700!important;font-size:20px!important;line-height:1.2!important;color:#002147!important;margin:0 0 6px!important}
.lf strong,.lf b{font-weight:700!important;color:#002147!important}
.lf a{color:#0F52BA!important;text-decoration:underline;text-underline-offset:3px}
.lf a:hover{color:#002147!important}
.lf a:focus-visible,.lf summary:focus-visible,.lf input:focus-visible+.lf-tick{outline:2px solid #007FFF!important;outline-offset:3px;border-radius:2px}

/* contents rail */
#lf-toc{border:1px solid #DDE5EE!important;border-radius:4px!important;background:#F4F7FA!important;padding:20px 22px 22px!important;margin:0 0 40px!important}
#lf-toc .lf-rail-title{margin:0 0 14px!important;padding:0 0 12px!important;border-bottom:1px solid #DDE5EE!important;font-size:14px!important;font-weight:600!important;letter-spacing:.16em!important;text-transform:uppercase!important;color:#5A6675!important}
#lf-toc ol{list-style:none!important;margin:0!important;padding:0!important}
#lf-toc li{margin:0!important}
#lf-toc a{display:flex!important;gap:9px!important;align-items:baseline!important;font-size:16px!important;line-height:1.3!important;color:#48525F!important;text-decoration:none!important;border-left:2px solid transparent!important;padding:7px 0 7px 12px!important;transition:color .15s,border-color .15s}
#lf-toc a:hover{color:#002147!important}
#lf-toc a.on{color:#002147!important;font-weight:700!important;border-left-color:#007FFF!important}
#lf-toc .n{flex:0 0 auto;font-size:13px!important;font-weight:700!important;letter-spacing:.08em!important;color:#0F52BA!important;font-variant-numeric:tabular-nums}
#lf-toc.rail{box-sizing:border-box!important;position:fixed!important;top:110px!important;max-height:calc(100vh - 140px)!important;overflow-y:auto!important;margin:0!important;z-index:5!important;padding:16px 18px 18px!important;opacity:0;visibility:hidden;transition:opacity .25s ease}
#lf-toc.rail.show{opacity:1;visibility:visible}
#lf-toc.rail a{font-size:14.5px!important;padding:6px 0 6px 10px!important}

/* audio */
.lf-listen{border:1px solid #C4DCF7!important;border-radius:4px!important;background:#F4F7FA!important;overflow:hidden;margin:0 0 40px!important}
.lf-listen-bar{height:3px;background:linear-gradient(100deg,#6F42C1 0%,#007FFF 100%)}
.lf-listen-in{padding:20px 22px 22px}
.lf-listen-head{display:flex;align-items:center;gap:13px;margin:0 0 14px}
.lf-mark{flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:999px;border:1px solid #C4DCF7;color:#0F52BA}
.lf-listen-head p{margin:0!important;font-size:19px!important;font-weight:600!important;line-height:1.25!important;color:#002147!important}
.lf-listen-head span{display:block;margin-top:3px;font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:#5A6675}
.lf-listen audio{display:block;width:100%;height:40px}

/* lead journey */
.lf-journey-fig{border:1px solid #C4DCF7!important;border-radius:4px!important;background:#F4F7FA!important;overflow:hidden;margin:0 0 40px!important}
.lf-journey-in{padding:26px 24px 28px}
.lf-journey-title{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;margin:0 0 24px;font-size:14px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#5A6675}
.lf-journey-title b{color:#0F52BA!important;font-weight:700!important}
.lf-journey{list-style:none!important;margin:0!important;padding:0!important;display:grid;grid-template-columns:repeat(6,minmax(0,1fr))}
.lf-journey li{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 3px;margin:0!important}
.lf-journey .node{position:relative;z-index:1;width:40px;height:40px;display:grid;place-items:center;border-radius:4px;background:#E7EDF4;border:1px solid #C4DCF7;color:#0F52BA;font-size:17px;font-weight:700;font-variant-numeric:tabular-nums}
.lf-journey li:last-child .node{background:linear-gradient(100deg,#007FFF 0%,#2A52BE 100%);border-color:transparent;color:#fff}
.lf-journey li::after{content:"";position:absolute;top:19px;left:calc(50% + 26px);width:calc(100% - 52px);height:2px;background:linear-gradient(100deg,#007FFF 0%,#2A52BE 100%)}
.lf-journey li:last-child::after{content:none}
.lf-journey .lbl{display:block;margin-top:12px;font-size:15px;font-weight:700;line-height:1.15;color:#002147}
.lf-journey .sub{display:block;margin-top:4px;font-size:12.5px;letter-spacing:.05em;color:#48525F;line-height:1.3}
.lf-journey-note{margin:24px 0 0!important;padding-top:14px!important;border-top:1px solid #DDE5EE!important;font-size:15px!important;letter-spacing:.06em!important;text-transform:uppercase!important;color:#5A6675!important}
@media(max-width:900px){.lf-journey-in{padding:22px 18px 24px}.lf-journey{grid-template-columns:minmax(0,1fr)}.lf-journey li{flex-direction:row;align-items:flex-start;text-align:left;gap:16px;padding:0 0 22px}.lf-journey li:last-child{padding-bottom:0}.lf-journey li::after{top:46px;left:19px;width:2px;height:calc(100% - 46px)}.lf-journey .lbl{margin-top:0}}

/* step headings */
.lf-step-head{margin:80px 0 24px!important;padding-top:24px!important;border-top:1px solid #DDE5EE!important;scroll-margin-top:90px}
.lf-step-mark{display:flex!important;align-items:center!important;gap:12px!important;margin:0 0 16px!important;font-size:14px!important;font-weight:700!important;letter-spacing:.18em!important;text-transform:uppercase!important;color:#0F52BA!important;font-variant-numeric:tabular-nums}
.lf-step-mark .of{color:#5A6675!important;font-weight:600!important;letter-spacing:.14em!important}
.lf-dots{display:inline-flex;gap:5px}
.lf-dots i{display:block;width:6px;height:6px;border-radius:50%;background:#C4DCF7}
.lf-dots i.on{background:#007FFF}
.lf-step-head h2{margin:0!important;padding:0!important;border:0!important}

/* pull / flow line */
.lf-flow{font-size:clamp(20px,2.4vw,25px)!important;line-height:1.35!important;color:#002147!important;padding:16px 20px!important;border-left:3px solid #007FFF!important;background:linear-gradient(90deg,rgba(0,127,255,.09),rgba(0,127,255,0) 82%)!important;border-radius:0 4px 4px 0!important;margin:0 0 24px!important}

/* panels */
.lf-brief,.lf-card{border:1px solid #DDE5EE!important;border-radius:4px!important;overflow:hidden;margin:56px 0!important}
.lf-brief{background:#F4F7FA!important}
.lf-card{background:#E4EFFC!important}
.lf-panel-bar{height:3px;background:linear-gradient(100deg,#007FFF 0%,#2A52BE 100%)}
.lf-panel-in{padding:30px 30px 32px}
.lf-brief h2{margin:0 0 2px!important;padding:0!important;border:0!important;font-size:clamp(26px,3.2vw,34px)!important}
.lf-brief-note{font-size:15px!important;font-weight:500!important;letter-spacing:.12em!important;text-transform:uppercase!important;color:#5A6675!important;margin:0 0 18px!important}
.lf-brief ul{margin:0!important;padding:0!important;list-style:none!important}
.lf-brief li{position:relative;padding-left:24px!important;margin:0 0 16px!important;color:#2D2D2D!important;font-size:18px!important;line-height:1.55!important}
.lf-brief li:last-child{margin-bottom:0!important}
.lf-brief li::before{content:"";position:absolute;left:0;top:.66em;width:12px;height:2px;background:linear-gradient(100deg,#007FFF 0%,#2A52BE 100%)}
.lf-brief li a{color:inherit!important;text-decoration:none!important}
.lf-brief li a:hover strong{color:#0F52BA!important}
.lf-kicker{font-size:14px!important;font-weight:700!important;letter-spacing:.16em!important;text-transform:uppercase!important;color:#0F52BA!important;margin:0 0 10px!important}
.lf-sub{font-size:16.5px!important;color:#48525F!important;margin:-4px 0 24px!important}
.lf-card p{font-size:18px!important}
.lf-card p:last-child{margin-bottom:0!important}

/* cells */
.lf-cells{display:grid!important;gap:14px!important;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))!important;margin:24px 0!important;padding:0!important;list-style:none!important}
.lf-cell{background:#F4F7FA!important;border:1px solid #DDE5EE!important;border-radius:4px!important;padding:20px!important;margin:0!important;transition:border-color .2s,transform .2s cubic-bezier(.2,.7,.2,1)}
.lf-cell:hover{border-color:#C4DCF7!important;transform:translateY(-2px)}
.lf-cell .n{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;margin-bottom:14px;border-radius:3px;background:linear-gradient(100deg,#007FFF 0%,#2A52BE 100%);color:#fff;font-size:16px;font-weight:700;font-variant-numeric:tabular-nums}
.lf-cell p{margin:0!important;font-size:16.5px!important;line-height:1.5!important;color:#48525F!important}
@media(max-width:560px){.lf-cells{grid-template-columns:1fr!important}}

/* sequence timeline */
.lf-track{margin:24px 0 16px;padding:0 6px}
.lf-track-line{position:relative;height:4px;background:#DDE5EE;border-radius:2px;margin:18px 0 62px}
.lf-track-fill{position:absolute;inset:0;background:linear-gradient(100deg,#007FFF 0%,#2A52BE 100%);border-radius:2px;transform-origin:0 50%}
.lf-dot{position:absolute;top:50%;width:16px;height:16px;margin:-8px 0 0 -8px;border-radius:50%;background:#E4EFFC;border:3px solid #007FFF}
.lf-dot span{position:absolute;top:24px;left:50%;transform:translateX(-50%);font-size:14px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#48525F;white-space:nowrap;font-variant-numeric:tabular-nums}
.lf-dot:first-of-type span{transform:translateX(-30%)}
.lf-dot:last-of-type span{transform:translateX(-70%)}
@media(max-width:640px){.lf-dot span{font-size:12.5px;letter-spacing:.06em}}

/* tables */
.lf-tablewrap{margin:16px 0 0;overflow-x:auto}
.lf table{width:100%!important;border-collapse:collapse!important;font-size:17px!important;line-height:1.4!important}
.lf th,.lf td{text-align:left!important;vertical-align:top!important;padding:12px!important;border-bottom:1px solid #DDE5EE!important}
.lf th{font-size:13.5px!important;font-weight:700!important;letter-spacing:.12em!important;text-transform:uppercase!important;color:#5A6675!important;padding-top:0!important}
.lf td{color:#2D2D2D!important}
.lf td:first-child{font-weight:700!important;color:#002147!important;white-space:nowrap!important;width:6em!important}
.lf tr:last-child td{border-bottom:0!important}
@media(max-width:640px){
.lf table,.lf thead,.lf tbody,.lf tr,.lf th,.lf td{display:block!important}
.lf thead{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important}
.lf tr{padding:12px 0!important;border-bottom:1px solid #DDE5EE!important}
.lf tr:last-child{border-bottom:0!important}
.lf td{padding:3px 0!important;border:0!important}
.lf td:first-child{white-space:normal!important;padding-bottom:4px!important;width:auto!important}
.lf td[data-label]:not(:first-child)::before{content:attr(data-label);display:block;font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#5A6675;margin:6px 0 1px}
}

/* checklist */
.lf-check{list-style:none!important;margin:24px 0 0!important;padding:0!important}
.lf-check li{margin:0 0 4px!important}
.lf-check label{display:flex!important;align-items:flex-start!important;gap:14px!important;min-height:44px!important;padding:8px 10px!important;margin:0 -10px!important;border-radius:4px!important;cursor:pointer;font-size:18px!important;line-height:1.45!important;color:#2D2D2D!important;transition:background-color .15s}
.lf-check label:hover{background:rgba(0,127,255,.07)!important}
.lf-check input{position:absolute;opacity:0;width:1px;height:1px}
.lf-tick{position:relative;flex:0 0 auto;width:22px;height:22px;margin-top:2px;border:2px solid #007FFF;border-radius:4px;transition:background-color .18s,transform .18s cubic-bezier(.2,.7,.2,1)}
.lf-tick svg{position:absolute;inset:0;width:100%;height:100%}
.lf-tick path{fill:none;stroke:#fff;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset .22s cubic-bezier(.2,.7,.2,1) .05s}
.lf-check input:checked+.lf-tick{background:#007FFF;transform:scale(1.06)}
.lf-check input:checked+.lf-tick path{stroke-dashoffset:0}
.lf-check input:checked~.lf-txt{color:#002147!important;font-weight:600}
.lf-meter{margin-top:24px;padding:14px 18px;background:#F4F7FA;border-left:3px solid #007FFF;border-radius:0 4px 4px 0}
.lf-meter-row{display:flex;justify-content:space-between;align-items:baseline;gap:12px;font-size:15px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#48525F;font-variant-numeric:tabular-nums}
.lf-meter-row b{color:#002147!important}
.lf-meter-bar{height:4px;margin-top:10px;background:#DDE5EE;border-radius:2px;overflow:hidden}
.lf-meter-bar i{display:block;height:100%;background:linear-gradient(100deg,#007FFF 0%,#2A52BE 100%);transform-origin:0 50%;transform:scaleX(0);transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.lf-meter p{margin:10px 0 0!important;font-size:16.5px!important;color:#48525F!important}

/* sourced statistic */
.lf-stat{border:1px solid #C4DCF7!important;border-radius:4px!important;background:#F4F7FA!important;overflow:hidden;margin:24px 0!important}
.lf-stat-bar{height:3px;background:linear-gradient(100deg,#6F42C1 0%,#007FFF 100%)}
.lf-stat-in{padding:22px 24px 24px}
.lf-stat-figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px 56px}
.lf-stat-fig b{display:block;font-size:clamp(38px,6vw,56px)!important;font-weight:700!important;line-height:1!important;color:#002147!important;font-variant-numeric:tabular-nums;letter-spacing:-.01em!important}
.lf-stat-fig span{display:block;margin-top:6px;font-size:16.5px;line-height:1.35;color:#48525F;max-width:26ch}
.lf-stat-src{margin:18px 0 0!important;padding-top:14px!important;border-top:1px solid #DDE5EE!important;font-size:15.5px!important;line-height:1.5!important;color:#5A6675!important}

/* read next */
.lf-next{margin:32px 0!important;padding:15px 20px 17px!important;border-left:2px solid #007FFF!important;border-radius:0 4px 4px 0!important;background:linear-gradient(90deg,rgba(0,127,255,.09) 0%,rgba(0,127,255,0) 82%)!important}
.lf-next-label{display:block;font-size:14px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#5A6675;margin-bottom:5px}
.lf-next a{display:inline-block!important;padding:3px 0!important;font-size:18.5px!important;font-weight:700!important;line-height:1.3!important;color:#002147!important;text-decoration:none!important}
.lf-next a:hover{color:#0F52BA!important;text-decoration:underline!important}
.lf-next .why{margin:4px 0 0!important;font-size:16.5px!important;line-height:1.5!important;color:#48525F!important}

/* FAQ */
.lf-faq{margin:24px 0}
.lf-faq details{border:1px solid #DDE5EE!important;border-radius:8px!important;background:#F4F7FA!important;overflow:hidden;margin:0 0 10px!important;transition:border-color .2s}
.lf-faq details[open]{background:#E4EFFC!important;border-color:#C4DCF7!important}
.lf-faq summary{cursor:pointer;padding:17px 22px!important;font-weight:600!important;font-size:20px!important;line-height:1.3!important;color:#002147!important;min-height:44px!important}
.lf-faq-body{padding:0 22px 20px}
.lf-faq-body p{margin:0!important;font-size:17.5px!important;line-height:1.55!important;color:#2D2D2D!important}

/* CTA */
.lf-cta{margin:80px 0 32px!important;background:linear-gradient(rgba(0,33,71,.28),rgba(0,33,71,.28)),linear-gradient(100deg,#007FFF 0%,#2A52BE 100%)!important;border-radius:6px!important;padding:36px 30px 34px!important}
.lf-cta .eyebrow-band{margin:0 0 8px!important;font-size:14px!important;font-weight:700!important;letter-spacing:.16em!important;text-transform:uppercase!important;color:#fff!important}
.lf-cta h2{margin:0 0 10px!important;padding:0!important;border:0!important;font-size:clamp(28px,4.2vw,42px)!important;line-height:1.04!important;color:#fff!important}
.lf-cta .band-lede{margin:0 0 24px!important;font-size:18.5px!important;line-height:1.55!important;color:#fff!important;max-width:54ch}
.lf-btn{display:inline-block!important;min-height:48px;background:#fff!important;color:#002147!important;text-decoration:none!important;font-size:18px!important;font-weight:700!important;letter-spacing:.05em!important;text-transform:uppercase!important;padding:14px 30px!important;border:2px solid #fff!important;border-radius:4px!important}
.lf-btn:hover{background:transparent!important;color:#fff!important}

/* related */
.lf-related{margin:56px 0 0!important;padding-top:24px!important;border-top:1px solid #DDE5EE!important}
.lf-related-label{font-size:14px!important;font-weight:600!important;letter-spacing:.16em!important;text-transform:uppercase!important;color:#5A6675!important;margin:0 0 16px!important}
.lf-related-links{display:flex;flex-direction:column;gap:10px;align-items:flex-start}
.lf-related-links a{font-size:17px!important;font-weight:500!important;line-height:1.3!important;color:#2D2D2D!important;text-decoration:none!important;border:1px solid #C4DCF7!important;border-radius:999px!important;padding:10px 18px!important;transition:border-color .15s,color .15s}
.lf-related-links a:hover{border-color:#0F52BA!important;color:#0F52BA!important}

/* motion, gated so nothing is ever hidden without the script to reveal it */
.lf-go .lf-rev{opacity:0;transform:translateY(18px);transition:opacity .55s cubic-bezier(.2,.7,.2,1),transform .55s cubic-bezier(.2,.7,.2,1)}
.lf-go .lf-rev.in{opacity:1;transform:none}
.lf-go .lf-kids>*{opacity:0;transform:translateY(12px);transition:opacity .45s cubic-bezier(.2,.7,.2,1),transform .45s cubic-bezier(.2,.7,.2,1);transition-delay:calc(90ms + var(--i,0) * 70ms)}
.lf-go .lf-kids.in>*{opacity:1;transform:none}
.lf-go .lf-track-fill{transform:scaleX(0);transition:transform 1.1s cubic-bezier(.2,.7,.2,1) .15s}
.lf-go .lf-track.in .lf-track-fill{transform:none}
.lf-go .lf-dot{transform:scale(0);transition:transform .35s cubic-bezier(.34,1.56,.64,1);transition-delay:calc(.15s + var(--p) * 1.1s)}
.lf-go .lf-track.in .lf-dot{transform:none}
@media(prefers-reduced-motion:reduce){.lf-go .lf-rev,.lf-go .lf-kids>*,.lf-go .lf-dot{opacity:1!important;transform:none!important;transition:none!important}.lf-go .lf-track-fill{transform:none!important}}
.lf-live{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;clip:rect(0 0 0 0)!important;white-space:nowrap!important}
"""
import re
CSS = re.sub(r'/\*.*?\*/', '', CSS, flags=re.S)      # strip comments
CSS = re.sub(r'\s*\n\s*', '', CSS)                   # collapse to one line
CSS = CSS.replace('__FONT__', F)                      # unique token, cannot collide with a colour

# The host theme carries !important on its own element rules, which outrank a
# plain declaration however specific the selector. A theme rule on ol/ul was
# enough to drop display:grid and collapse the lead-journey diagram into a
# stacked list with its horizontal connectors still drawn. Force every
# declaration rather than guess which ones the theme will contest.
def _force(m):
    decls = [d.strip() for d in m.group(1).split(';') if d.strip()]
    return '{' + ';'.join(d if d.endswith('!important') else d + '!important' for d in decls) + '}'
CSS = re.sub(r'\{([^{}]*)\}', _force, CSS)
open('_css.txt', 'w').write(CSS)
print('stylesheet built:', len(CSS), 'chars')
