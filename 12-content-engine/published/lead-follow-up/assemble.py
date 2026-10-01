# -*- coding: utf-8 -*-
import os, glob, re
from html.parser import HTMLParser

CSS = open('_css.txt').read()
BODY = open('_body.txt').read()

JS = """(function(){function init(){
var go=document.documentElement;go.classList.add("lf-go");
var R=matchMedia("(prefers-reduced-motion:reduce)").matches;
var IO="IntersectionObserver" in window;

/* reveals */
var els=[].slice.call(document.querySelectorAll(".lf-rev,.lf-kids,.lf-track"));
function showAll(){els.forEach(function(e){e.classList.add("in");});}
if(!IO||R){showAll();}else{
document.querySelectorAll(".lf-kids").forEach(function(g){
[].slice.call(g.children).forEach(function(k,i){k.style.setProperty("--i",Math.min(i,8));});});
var io=new IntersectionObserver(function(en){en.forEach(function(e){
if(!e.isIntersecting)return;e.target.classList.add("in");io.unobserve(e.target);});},
{rootMargin:"0px 0px -12% 0px",threshold:0});
els.forEach(function(e){if(e.getBoundingClientRect().top<innerHeight*0.85)e.classList.add("in");else io.observe(e);});}

/* statistic count-up */
if(IO&&!R){[].slice.call(document.querySelectorAll(".lf-num")).forEach(function(el){
var tg=parseInt(el.getAttribute("data-count"),10),sf=el.getAttribute("data-suffix")||"";
var o=new IntersectionObserver(function(en){if(!en[0].isIntersecting)return;o.disconnect();
var t0=null,d=800;el.textContent="0"+sf;
requestAnimationFrame(function s(ts){if(t0===null)t0=ts;var p=Math.min(1,(ts-t0)/d),e=1-Math.pow(1-p,3);
el.textContent=Math.round(tg*e)+sf;if(p<1)requestAnimationFrame(s);else el.textContent=tg+sf;});
/* these are sourced figures: never leave a partial count on screen if the
   frame loop is interrupted mid-animation */
setTimeout(function(){el.textContent=tg+sf;},d+600);},
{threshold:.6});o.observe(el);});}

/* pre-launch checklist */
var list=document.getElementById("lf-check"),meter=document.getElementById("lf-meter");
if(list&&meter){var boxes=[].slice.call(list.querySelectorAll("input"));
var cnt=document.getElementById("lf-count"),fill=document.getElementById("lf-fill"),
msg=document.getElementById("lf-msg"),live=document.getElementById("lf-live");
meter.hidden=false;
function sync(){var n=boxes.filter(function(b){return b.checked;}).length;
cnt.textContent=n+" of "+boxes.length;fill.style.transform="scaleX("+(n/boxes.length)+")";
msg.textContent=n===0?"Nothing checked yet.":n<boxes.length?
(boxes.length-n)+" still to confirm before you go live.":
"Everything confirmed. Now run the three edge cases below.";
if(live)live.textContent=n+" of "+boxes.length+" confirmed. "+msg.textContent;}
boxes.forEach(function(b){b.addEventListener("change",sync);});sync();}

/* audio runtime */
var au=document.getElementById("lf-audio"),mins=document.getElementById("lf-mins");
if(au&&mins){var set=function(){var d=au.duration;if(!isFinite(d)||d<=0)return;
var t=Math.round(d),m=Math.floor(t/60),s=t%60;
mins.textContent=t<60?t+" sec":t<600?(s?m+" min "+s+" sec":m+" min"):Math.round(d/60)+" min";};
au.addEventListener("loadedmetadata",set);au.addEventListener("durationchange",set);set();}

/* contents rail: measured against the real column, never assumed */
var t=document.getElementById("lf-toc");if(!t)return;
var col=t.parentElement,bs=document.getElementById("lf-start"),
en=document.getElementById("call"),TOP=110,W=230,GAP=44;
function place(){if(!col||!bs||!en)return;
t.classList.remove("rail");t.style.left="";t.style.width="";
var r=col.getBoundingClientRect();
if(innerWidth<1100||r.left<W+GAP+16)return;
t.style.left=Math.max(16,Math.round(r.left-W-GAP))+"px";t.style.width=W+"px";
t.classList.add("rail");}
function show(){if(!t.classList.contains("rail"))return;
var started=bs.getBoundingClientRect().top<=TOP+16,
ended=en.parentElement.getBoundingClientRect().bottom<=TOP+t.offsetHeight;
t.classList.toggle("show",started&&!ended);}

/* current section marker, computed from geometry so a deep link cannot lie */
var links=[].slice.call(t.querySelectorAll('a[href^="#"]')),map={},secs=[];
links.forEach(function(a){var e=document.getElementById(a.getAttribute("href").slice(1));
if(e){map[e.id]=a;secs.push(e);}});
secs.sort(function(a,b){return a.compareDocumentPosition(b)&Node.DOCUMENT_POSITION_FOLLOWING?-1:1;});
var cur=null;
function spy(){if(!secs.length)return;var line=innerHeight*.28,best=secs[0],i;
for(i=0;i<secs.length;i++)if(secs[i].getBoundingClientRect().top-line<=0)best=secs[i];
if(innerHeight+scrollY>=document.body.scrollHeight-4)best=secs[secs.length-1];
var a=map[best.id];if(a===cur)return;if(cur)cur.classList.remove("on");
cur=a;if(!cur)return;cur.classList.add("on");
if(t.scrollHeight>t.clientHeight){var o=cur.offsetTop;
if(o<t.scrollTop||o>t.scrollTop+t.clientHeight-30)t.scrollTop=o-t.clientHeight/2;}}

var tick=false;
function onScroll(){if(tick)return;tick=true;
requestAnimationFrame(function(){show();spy();tick=false;});}
function relayout(){place();show();spy();}
relayout();
addEventListener("scroll",onScroll,{passive:true});
addEventListener("resize",relayout,{passive:true});
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(relayout);
setTimeout(relayout,600);
}
if(document.readyState!=="loading")init();else addEventListener("DOMContentLoaded",init);})();"""
JS = re.sub(r'\n\s*', '', re.sub(r'/\*.*?\*/', '', JS, flags=re.S))

# One document: stylesheet, markup, script. Split into blocks GHL will accept.
blocks = ['<style>%s</style>' % CSS] + BODY.split('\n') + ['<script>%s</script>' % JS]

# A <style> larger than the field limit is cut across several <style> elements;
# CSS from separate elements merges, so the split is invisible.
LIMIT = 8600
out = []
for blk in blocks:
    if len(blk) <= LIMIT:
        out.append(blk); continue
    if blk.startswith('<style>'):
        css = blk[7:-8]
        parts, buf = [], ''
        for rule in re.findall(r'[^{}]+\{[^{}]*\}|@media[^{]+\{(?:[^{}]*\{[^{}]*\})*\}', css):
            if len(buf) + len(rule) > LIMIT - 200:
                parts.append(buf); buf = ''
            buf += rule
        if buf: parts.append(buf)
        out += ['<style>%s</style>' % p for p in parts]
    else:
        out.append(blk)

chunks, cur, size = [], [], 0
for blk in out:
    if cur and size + len(blk) > LIMIT:
        chunks.append(cur); cur, size = [], 0
    cur.append(blk); size += len(blk)
if cur: chunks.append(cur)

os.makedirs('paste-chunks', exist_ok=True)
for f in glob.glob('paste-chunks/*.txt'): os.remove(f)
for i, c in enumerate(chunks, 1):
    open('paste-chunks/%02d.txt' % i, 'w').write('<div class="lf">\n' + '\n'.join(c) + '\n</div>')

full = '\n'.join('<div class="lf">\n' + '\n'.join(c) + '\n</div>' for c in chunks)
open('body.html','w').write(full)

VOID={'br','img','hr','input','meta','link','source','area','base','col','embed','param','track','wbr'}
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False); self.st=[]; self.err=[]
    def handle_starttag(self,t,a):
        if t not in VOID: self.st.append(t)
    def handle_endtag(self,t):
        if t in VOID: return
        if not self.st or self.st.pop()!=t: self.err.append(t)
ok=True
for f in sorted(glob.glob('paste-chunks/*.txt')):
    c=open(f).read(); p=P(); p.feed(c)
    tag = ' <- stylesheet' if '<style>' in c else (' <- script' if '<script>' in c else '')
    print('%s %6d%s' % (os.path.basename(f), len(c), tag))
    if p.st or p.err: ok=False; print('   BROKEN', p.st, p.err)
print('chunks:', len(chunks), '| all well-formed:', ok)
