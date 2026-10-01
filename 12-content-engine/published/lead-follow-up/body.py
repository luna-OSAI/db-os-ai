# -*- coding: utf-8 -*-
BOOK = "https://link.teamos.ai/widget/booking/JJUNz06hsFi7yjpvBt13"
AUDIO = "https://assets.cdn.filesafe.space/LCUeYJ3q8BPlvSWsMlb9/media/6abb5ca0df795f5ccc776c13.m4a"

def cells(items, label, lvl=4):
    # lvl follows the nearest preceding heading: cells under a step h2 take h3,
    # cells inside a card (which already has an h3) take h4. Skipping a level
    # breaks heading navigation for screen-reader users.
    out = ['<ul class="lf-cells lf-kids" aria-label="%s">' % label]
    for i, (n, h, p) in enumerate(items):
        body = '<p>%s</p>' % p if p else ''
        out.append('<li class="lf-cell" style="--i:%d"><span class="n">%s</span><h%d>%s</h%d>%s</li>'
                   % (i, n, lvl, h, lvl, body))
    out.append('</ul>')
    return ''.join(out)

def dots(on):
    return '<span class="lf-dots" aria-hidden="true">' + ''.join(
        '<i class="%s"></i>' % ('on' if i < on else '') for i in range(5)) + '</span>'

def step(num, sid, title):
    return ('<div class="lf-step-head lf-rev" id="%s">'
            '<p class="lf-step-mark">Step %d %s <span class="of">of 5</span></p>'
            '<h2>%s</h2></div>') % (sid, num, dots(num), title)

P = lambda t: '<p>%s</p>' % t
TICK = ('<span class="lf-tick"><svg viewBox="0 0 22 22" aria-hidden="true">'
        '<path pathLength="1" d="M5.5 11.5l3.8 3.8 7.2-8"></path></svg></span>')

CHECKS = ["The contact is created correctly.",
          "Messages arrive at the right time.",
          "Personalisation fields display properly.",
          "Qualification logic sends leads down the correct path.",
          "Calendar links work.",
          "Internal notifications reach the right person.",
          "A booked appointment stops unnecessary follow-up messages."]

FAQ = [
 ("What is automated lead follow-up?", "Automated lead follow-up is a set of workflows that respond to new enquiries and keep in touch with them without manual effort. It typically covers an instant first reply, qualification questions, booking links and a timed sequence of follow-up messages."),
 ("How quickly should you follow up with a new lead?", "As quickly as you can, ideally within minutes. Interest is usually highest at the moment someone enquires, so a fast first reply gives you the best chance of starting the conversation. Automation makes that possible after hours and on weekends, when nobody is at a desk."),
 ("How many follow-up messages should you send?", "Most businesses do well with four to five touchpoints over about a week, as in the sequence above. Vary the content each time and stop the moment the lead books or asks you to stop."),
 ("Do you need a CRM to automate lead follow-up?", "You need one place where lead data lives, and a CRM is the usual answer. Without it, automation has no reliable record of who enquired, what they asked and where they are in the journey."),
 ("Will automated follow-up feel impersonal?", "It does not have to. Automate the predictable steps, such as the first reply, common questions and reminders, and hand over to a person for anything complex or sensitive. Writing the messages in your own tone helps as well."),
 ("What should you test before launching lead follow-up automation?", "Submit a test enquiry and check the whole journey: contact creation, message timing, personalisation fields, qualification logic, calendar links, team notifications and whether a booking stops the sequence. Then test what happens when a lead never replies, books straight away or is not qualified."),
]

TOC = [("&#9654;","#listen","Listen instead"),("&mdash;","#tldr","The short version"),
 ("01","#step-1","Map your lead journey"),("02","#step-2","Put lead data in one CRM"),
 ("03","#step-3","Build the first response"),("04","#step-4","Create a follow-up sequence"),
 ("05","#step-5","Test before going live"),("&bull;","#limits","The honest limit"),
 ("?","#faq","Questions"),("&rarr;","#call","Build it once")]

JOURNEY = [("1","New enquiry","Any source"),("2","Instant response","SMS or email"),
 ("3","Qualification","A few questions"),("4","Follow-up","Over about a week"),
 ("5","Booked","Sequence stops"),("6","Sales handoff","A person takes over")]

SEQ = [("Day 0","Immediate acknowledgement and booking link","Confirm you received the enquiry and show the next step"),
 ("Day 1","Quick check-in asking if they have questions","Remove small blockers"),
 ("Day 3","Helpful answer to a common objection or problem","Give them a reason to reply"),
 ("Day 5","Reminder with another chance to book","Make booking low effort"),
 ("Day 7","Final check-in before moving them to longer-term nurture","Close the loop politely")]

b = []
A = b.append

# contents
A('<div id="lf-toc"><p class="lf-rail-title">In this guide</p><ol>')
for n, href, t in TOC:
    A('<li><a href="%s"><span class="n">%s</span><span>%s</span></a></li>' % (href, n, t))
A('</ol></div>')

# audio
A('<div class="lf-listen" id="listen"><div class="lf-listen-bar"></div><div class="lf-listen-in">'
  '<div class="lf-listen-head"><span class="lf-mark"><svg viewBox="0 0 24 24" width="19" height="19" '
  'fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" '
  'style="display:block"><path d="M3 14v-2a9 9 0 0 1 18 0v2"></path>'
  '<path d="M21 15a2 2 0 0 1-2 2h-1v-5h1a2 2 0 0 1 2 2zM3 15a2 2 0 0 0 2 2h1v-5H5a2 2 0 0 0-2 2z"></path>'
  '</svg></span><div><p>Want to listen to this article instead?</p>'
  '<span>Audio overview &middot; <span id="lf-mins">narrated</span></span></div></div>'
  '<audio id="lf-audio" controls preload="metadata" src="%s">Your browser cannot play audio. '
  '<a href="%s">Download the narration</a>.</audio></div></div>' % (AUDIO, AUDIO))

# journey figure
A('<div class="lf-journey-fig"><div class="lf-panel-bar"></div><div class="lf-journey-in">'
  '<div class="lf-journey-title"><span>The lead journey you are about to build</span><b>6 stages</b></div>'
  '<ol class="lf-journey">')
for i,(n,l,s) in enumerate(JOURNEY):
    A('<li style="--i:%d"><span class="node">%s</span><span><span class="lbl">%s</span>'
      '<span class="sub">%s</span></span></li>' % (i,n,l,s))
A('</ol><p class="lf-journey-note">Steps 1 to 5 below build this, in order.</p></div></div>')

# intro
A('<p id="lf-start">Most businesses do the opposite. They switch on a tool first and decide what it should do later, which leaves leads slipping through gaps nobody planned for. This guide gives you the order that works, so the system handles the repetitive work and your team spends its time on the conversations that need a person.</p>')

# TL;DR
A('<div class="lf-brief lf-rev" id="tldr"><div class="lf-panel-bar"></div><div class="lf-panel-in">'
  '<h2>TL;DR</h2><p class="lf-brief-note">The five steps in one glance</p><ul>')
for href, lead, rest in [
 ("#step-1","Step 1:","Map the path from first enquiry to booked appointment before you build anything."),
 ("#step-2","Step 2:","Keep every lead in one CRM with clear ownership and only the pipeline stages you use."),
 ("#step-3","Step 3:","Automate the first response so every enquiry gets a reply straight away, including after hours."),
 ("#step-4","Step 4:","Add a short follow-up sequence over about a week, with a different reason to reply each time."),
 ("#step-5","Step 5:","Test the full journey, including the edge cases, before you go live.")]:
    A('<li><a href="%s"><strong>%s</strong> %s</a></li>' % (href, lead, rest))
A('</ul></div></div>')

# Step 1
A(step(1,'step-1','Map Your Lead Journey'))
A(P('Automation needs a job to do. Without a mapped journey, you end up automating random tasks that do not connect to a booking.'))
A(P('Start with the path from first enquiry to booked appointment, and answer five questions:'))
A(cells([("1","Where does the lead come from?",""),("2","What information do you need to capture?",""),
         ("3","Who needs to respond?",""),("4","What makes a lead qualified?",""),
         ("5","What is the next action you want them to take?","")], "Five journey questions", 3))
A(P('For most service businesses, the journey looks like this:'))
A('<p class="lf-flow lf-rev"><strong>New enquiry &rarr; instant response &rarr; qualification &rarr; follow-up &rarr; appointment booked &rarr; sales handoff</strong></p>')
A(P('Write yours on one page. If a step has no owner or no next action, that is a gap, and it is where leads go missing today.'))

# Step 2
A(step(2,'step-2','Put Your Lead Data in One CRM'))
A(P('Follow-up breaks down when lead information is scattered. Website enquiries sit in one tool, messages in another and appointment details somewhere else. Your team ends up checking platforms, copying details across and trying to remember who needs a reply.'))
A(P('The fix is one central CRM that every lead source feeds into. OS A.I brings CRM, communication, appointment scheduling, funnels and automation into one connected platform, so lead information moves through the customer journey without constant manual handling.'))
A('<div class="lf-card lf-rev"><div class="lf-panel-bar"></div><div class="lf-panel-in">'
  '<p class="lf-kicker">Setup mistakes</p><h3>Three to avoid</h3>' +
  cells([("1","Too many pipeline stages","Start with the stages your team genuinely uses. You can add more later."),
         ("2","Unnecessary information","Ask only for data that helps you qualify or serve the lead."),
         ("3","Unclear lead ownership","Every qualified opportunity needs a named owner or a routing rule.")],
        "Three setup mistakes") + '</div></div>')
A(P('A clean data structure makes the next step much easier to build.'))

# Step 3
A(step(3,'step-3','Build the First-Response Automation'))
A(P('The first-response automation is the workflow that runs the moment someone enquires. Interest is usually highest right when a prospect reaches out, so this is where speed pays off. If you want the case for why timing matters so much, read <a href="https://www.oscale.ai/post/speed-to-lead-why-the-first-five-minutes-decide-who-gets-the-job">Speed to Lead: Why the First Five Minutes Decide Who Gets the Job</a>.'))
A('<div class="lf-stat lf-rev" role="figure" aria-label="Lead response findings from the 2011 Harvard Business Review audit">'
  '<div class="lf-stat-bar"></div><div class="lf-stat-in"><div class="lf-stat-figs">'
  '<p class="lf-stat-fig"><b class="lf-num" data-count="42" data-suffix=" hours">42 hours</b>'
  '<span>Average time to a first response, across 2,241 audited companies</span></p>'
  '<p class="lf-stat-fig"><b class="lf-num" data-count="23" data-suffix="%">23%</b>'
  '<span>Of those companies never responded at all</span></p></div>'
  '<p class="lf-stat-src">Oldroyd, McElheran and Elkington, &ldquo;The Short Life of Online Sales Leads&rdquo;, '
  '<em>Harvard Business Review</em> (2011). The canonical studies in this field are old, 2007 and 2011, '
  'and they are still the ones the industry cites.</p></div></div>')
A(P('A basic first-response workflow does five things:'))
A(cells([("1","Creates or updates the contact","One record per lead, always current."),
         ("2","Sends an immediate reply","SMS or email, straight away."),
         ("3","Asks a few qualifying questions","Only a small number."),
         ("4","Directs qualified prospects to the right calendar",""),
         ("5","Notifies your team","When human attention is required.")], "First-response workflow", 3))
A(P('An <a href="https://www.oscale.ai/chat">AI chat agent</a> can carry this conversation around the clock. It answers common questions, qualifies the enquiry and helps book the appointment, so the conversation starts at once instead of hours later when someone spots a form submission. If your leads also call, an <a href="https://www.oscale.ai/voice">AI voice agent</a> covers the phone in the same way.'))
A(P('Do not automate everything. Automate the predictable steps and set clear handoff points for the conversations your team should handle personally, such as complex quotes or upset customers.'))
A('<div class="lf-next lf-rev"><span class="lf-next-label">If enquiries are not arriving</span>'
  '<a href="https://www.oscale.ai/post/why-your-website-isnt-generating-leads">Why Your Website Isn&rsquo;t Generating Leads (And How AI Can Fix It) &rarr;</a>'
  '<p class="why">If your website gets traffic but few enquiries, the problem may sit before this step.</p></div>')

# Step 4
A(step(4,'step-4','Create a Follow-Up Sequence'))
A(P('One message is rarely a complete follow-up system. Most people who enquire do not book on the first reply, so build a short sequence for the ones who go quiet. Mix helpful reminders, answers to common questions and a clear call to action.'))
track = ('<div class="lf-track lf-rev" aria-hidden="true"><div class="lf-track-line"><div class="lf-track-fill"></div>'
 + ''.join('<i class="lf-dot" style="left:%s;--p:%s"><span>%s</span></i>' % (l,p,s)
   for l,p,s in [("0%","0","Day 0"),("14.29%",".143","1"),("42.86%",".429","3"),("71.43%",".714","5"),("100%","1","7")])
 + '</div></div>')
rows = ''.join('<tr style="--i:%d"><td>%s</td><td data-label="Message">%s</td><td data-label="Purpose">%s</td></tr>'
               % (i,d,m,pp) for i,(d,m,pp) in enumerate(SEQ))
A('<div class="lf-card lf-rev"><div class="lf-panel-bar"></div><div class="lf-panel-in">'
  '<p class="lf-kicker">A sequence over one week</p><h3>Five touchpoints, five reasons to reply</h3>'
  + track + '<div class="lf-tablewrap"><table><thead><tr><th scope="col">Day</th>'
  '<th scope="col">Message</th><th scope="col">Purpose</th></tr></thead>'
  '<tbody class="lf-kids">' + rows + '</tbody></table></div></div></div>')
A(P('Avoid sending the same &ldquo;just following up&rdquo; message five times. Each touchpoint should give the prospect a reason to respond, whether that is an answer, a useful detail or an easier way to book.'))
A('<p class="lf-flow lf-rev"><strong>Build in one rule from the start: when a lead books, the sequence stops.</strong> Nothing puts off a new customer faster than a reminder to book an appointment they have already booked.</p>')
A(P('OS A.I can run these workflows across connected channels, so follow-up stays consistent without anyone having to remember it.'))

# Step 5
A(step(5,'step-5','Test the Entire System Before Going Live'))
A(P('Once the build looks complete, do not switch it on and assume it works. Submit a test enquiry yourself and follow the exact journey a prospect will experience.'))
items = ''.join('<li><label><input type="checkbox">%s<span class="lf-txt">%s</span></label></li>' % (TICK, c) for c in CHECKS)
A('<div class="lf-card lf-rev"><div class="lf-panel-bar"></div><div class="lf-panel-in">'
  '<p class="lf-kicker">Pre-launch checklist</p><h3>Check that</h3>'
  '<p class="lf-sub">Tick each one as you confirm it.</p>'
  '<ul class="lf-check" id="lf-check">' + items + '</ul>'
  '<div class="lf-meter" id="lf-meter" hidden><div class="lf-meter-row"><span>Confirmed</span>'
  '<b id="lf-count">0 of 7</b></div><div class="lf-meter-bar" aria-hidden="true"><i id="lf-fill"></i></div>'
  '<p id="lf-msg">Nothing checked yet.</p><span class="lf-live" aria-live="polite" id="lf-live"></span>'
  '</div></div></div>')
A(P('Then test the edge cases:'))
A(cells([("A","The lead never replies","Does the sequence run to the end and move them to nurture?"),
         ("B","The lead books immediately","Do all follow-up messages stop?"),
         ("C","The lead is not qualified","Do they get a polite, useful response rather than a sales push?")],
        "Edge cases to test", 3))
A(P('A good setup makes all three outcomes predictable.'))

# limits
A('<div class="lf-card lf-rev" id="limits"><div class="lf-panel-bar"></div><div class="lf-panel-in">'
  '<p class="lf-kicker">The honest limit</p><h3>What this does not fix</h3>'
  '<p class="lf-sub">Worth knowing before you build it, so you measure the right thing afterwards.</p>' +
  cells([("1","It does not get you more enquiries","This responds to the leads you already have. If the enquiries are not arriving, follow-up is the wrong thing to build first."),
         ("2","It will not define your process for you","You cannot automate a path you have not decided on. Automating an undefined process makes the mess faster and harder to see."),
         ("3","It does not replace the hard conversations","Complex quotes, unhappy customers and anything sensitive still need a person. Build the handoff, do not automate past it.")],
        "Three limits") + '</div></div>')

# FAQ
A('<h2 id="faq" class="lf-rev">Frequently Asked Questions</h2><div class="lf-faq">')
for q, a in FAQ:
    A('<details><summary>%s</summary><div class="lf-faq-body"><p>%s</p></div></details>' % (q, a))
A('</div>')

# wrap
A('<h2 id="wrap" class="lf-rev">Build the System Once, Then Improve It</h2>')
A(P('The order matters more than the tooling. Define the path before you automate it, because a workflow is a decision you write down once instead of making it again every week.'))
A(P('The goal is not more software. It is a system that helps your business capture more opportunities without creating more admin. That is the thinking behind OS A.I: bring the moving parts together so lead capture, communication, qualification and booking work as one connected process.'))

# CTA
A('<div class="lf-cta lf-rev" id="call"><p class="eyebrow-band">Start here</p>'
  '<h2>Map your current lead journey today</h2>'
  '<p class="band-lede">If your business still relies on manual follow-ups, scattered inboxes and disconnected tools, start by mapping your current lead journey. Once you can see the gaps, you can build the system that closes them.</p>'
  '<a class="lf-btn" href="%s">Book a free strategy call &rarr;</a></div>' % BOOK)

# related
A('<div class="lf-related"><p class="lf-related-label">Suggested reading</p><div class="lf-related-links">'
  '<a href="https://www.oscale.ai/post/speed-to-lead-why-the-first-five-minutes-decide-who-gets-the-job">Speed to Lead: Why the First Five Minutes Decide Who Gets the Job</a>'
  '<a href="https://www.oscale.ai/post/why-your-website-isnt-generating-leads">Why Your Website Isn&rsquo;t Generating Leads (And How AI Can Fix It)</a>'
  '<a href="https://www.oscale.ai/post/ai-reduce-customer-churn-small-business-australia">How AI Helps Australian SMBs Reduce Customer Churn</a>'
  '</div></div>')

open('_body.txt','w').write('\n'.join(b))
print('markup built:', len('\n'.join(b)), 'chars,', len(b), 'top-level blocks')
