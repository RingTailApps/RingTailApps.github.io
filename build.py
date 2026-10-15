#!/usr/bin/env python3
"""Generates the static pages. Run: python3 build.py"""
import re, pathlib
R = pathlib.Path(__file__).parent
SRC = pathlib.Path('/workspace/weeknight-app/invite-web')
APPLE = '<svg viewBox="0 0 24 24"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8-1.41-.14-2.76.83-3.47.83-.72 0-1.82-.81-3-.79-1.54.02-2.96.9-3.76 2.28-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.35 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.78.74 2.99.72 1.24-.02 2.02-1.12 2.78-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.39-.92-2.41-3.69zM14.1 5.86c.63-.77 1.06-1.83.94-2.89-.91.04-2.02.61-2.67 1.37-.58.67-1.1 1.76-.96 2.8 1.02.08 2.06-.52 2.69-1.28z"/></svg>'
STORE = f'<span class="store soon" aria-label="App Store, coming soon">{APPLE}<span><small>Coming soon to the</small><b>App Store</b></span></span>'
def page(path, title, desc, body, depth):
    p = '../' * depth
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://ringtailapps.com/assets/ringtail-logo.png"><meta name="theme-color" content="#FBF6EE">
<link rel="icon" href="/assets/favicon.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="stylesheet" href="/assets/site.css"></head><body>
<header class="nav"><div class="wrap"><a class="brand" href="/"><img src="/assets/ringtail-logo.png" alt="">RingTailApps</a>
<nav class="links"><a href="/chowhall/">Chow Hall</a><a href="/support/">Support</a><a class="hide-sm" href="/privacy/">Privacy</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><span>© 2026 RingTailApps. Made by a small team (okay, one raccoon).</span><nav><a href="/chowhall/">Chow Hall</a><a href="/support/">Support</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></nav></div></footer>
</body></html>'''
    out = R / path; out.parent.mkdir(parents=True, exist_ok=True); out.write_text(html)
def phone(n, cls='', alt=''): return f'<div class="phone {cls}"><img src="/assets/shots/{n}.jpg" alt="{alt}" loading="lazy"></div>'
def card(ic, h, p, cls=''): return f'<div class="card {cls}"><div class="ic">{ic}</div><h3>{h}</h3><p>{p}</p></div>'

page('index.html', 'RingTailApps · Small apps, made with care', 'RingTailApps is a small indie studio making thoughtful iPhone apps, starting with Chow Hall, the friendly dinner planner.', f'''
<section class="hero"><div class="wrap"><img class="logo" src="/assets/ringtail-logo.png" alt="RingTailApps raccoon">
<div class="eyebrow">An independent app studio</div><h1>Small apps that make everyday life easier.</h1>
<p class="lead">RingTailApps builds simple, beautiful iPhone apps for real households. No clutter, no ads, no tracking. Just tools that do their job well.</p>
<div class="btns"><a class="btn" href="/chowhall/">Meet Chow Hall</a><a class="btn ghost" href="/support/">Get in touch</a></div></div></section>
<section style="padding-top:20px"><div class="wrap"><div class="feature">
<div class="copy"><div class="appid"><img src="/assets/chowhall-icon.png" alt="Chow Hall icon"><div><div class="eyebrow">Our first app</div><b>Chow Hall</b></div></div>
<h2>Dinner, sorted for the whole week.</h2><p class="lead" style="font-size:17.5px">Chow Hall plans your family's meals, builds the grocery list for you and keeps everyone in the house on the same page, with a little help from a raccoon chef.</p>
<ul class="ticks"><li>Plan your whole week in one tap</li><li>Chow Haul: a grocery list sorted by aisle</li><li>Shared lists and a potluck planner</li><li>Levels and badges as you cook</li></ul>
<div class="btns" style="justify-content:flex-start;margin-top:0">{STORE}<a class="btn ghost" href="/chowhall/">Learn more</a></div></div>
<div class="art">{phone('list','sm','Grocery list')}{phone('week','','Chow Hall week plan')}</div></div></div></section>
<section class="alt"><div class="wrap"><div class="head"><div class="eyebrow">How we build</div><h2>Made with care, not clutter.</h2></div>
<div class="grid c3">{card('🦝','Thoughtfully simple','Every screen earns its place. If a feature makes things harder, it doesn’t ship.')}{card('🔒','Private by default','No ads, no tracking and no selling data. Your stuff stays yours, mostly on your own phone.')}{card('🧡','Built for families','Real tools for busy households, designed to be easy for everyone at the table.')}</div></div></section>
<section><div class="wrap"><div class="head"><div class="eyebrow">Our apps</div><h2>The den is just getting started.</h2></div>
<div class="grid c3"><a class="card" href="/chowhall/" style="color:inherit;text-decoration:none"><img src="/assets/chowhall-icon.png" alt="" style="width:52px;border-radius:12px"><h3>Chow Hall</h3><p>The friendly dinner planner for families. Coming soon to iPhone.</p></a>
{card('✦','Next app','Something new is in the works. Check back soon.','future')}{card('✦','Your idea here','Have an app you wish existed? We’d love to hear it.','future')}</div></div></section>
<section class="alt"><div class="wrap about"><img src="/assets/ringtail-logo.png" alt="">
<div><div class="eyebrow">About the studio</div><h2>Why a raccoon?</h2><p class="lead" style="font-size:17.5px">Raccoons are clever, curious and very good at finding food. That felt about right for a studio whose first app helps you figure out what’s for dinner. RingTailApps is independently owned and run, and every app is designed, built and supported in-house.</p>
<p style="margin-top:18px">Questions or ideas? <a href="mailto:ringtailapps@gmail.com">ringtailapps@gmail.com</a></p></div></div></section>''', 0)

feat = [('week','Plan my week','Tell Chow Hall who you’re feeding and what you like, and it fills the week with simple family dinners in one tap. Swap anything you don’t feel like.'),
('list','Chow Haul grocery list','Every ingredient lands on one list, combined and sorted by aisle, so the store trip is quick. Seasonings you already have stay off it.'),
('potluck','Potluck planner','Host a potluck, share one link, and let guests claim a dish. No more five bags of chips and no dessert.'),
('badges','Levels and badges','Earn chef points every time you cook, level up and collect badges. Your raccoon chef cheers you on.')]
rows = ''.join(f'<div class="row{" flip" if i%2 else ""}"><div class="txt"><div class="eyebrow">0{i+1}</div><h2>{h}</h2><p class="lead" style="font-size:18px">{p}</p></div>{phone(n,"",h)}</div>' for i,(n,h,p) in enumerate(feat))
page('chowhall/index.html', 'Chow Hall · The friendly dinner planner', 'Plan the week, build the grocery list and share it with the whole house. Chow Hall is coming soon to iPhone.', f'''
<section class="apphero"><div class="wrap"><img class="icon" src="/assets/chowhall-icon.png" alt="Chow Hall icon"><div class="eyebrow">For iPhone · by RingTailApps</div>
<h1>What’s for dinner? Sorted.</h1><p class="lead">Chow Hall plans the week, writes the grocery list and keeps the whole house in sync, with simple everyday dinners your family will actually eat.</p>
<div class="btns">{STORE}</div>
<div class="phones">{phone('potluck','side','Potluck')}{phone('detail','','Recipe')}{phone('badges','side','Badges')}</div></div></section>
<section><div class="wrap">{rows}
<div class="row"><div class="txt"><div class="eyebrow">05</div><h2>Can’t decide?</h2><p class="lead" style="font-size:18px">Spin the wheel and let Chow Hall pick, whether it’s dinner at home or a night out.</p></div>{phone('eatout','','Eat out wheel')}</div>
<div class="mascot"><img src="/assets/raccoon-chef.png" alt="Raccoon chef"><div><h3 style="font-size:22px">Meet your chef.</h3><p style="margin:6px 0 0;color:var(--mute)">A friendly raccoon chef guides you through the app, celebrates your wins, and even dresses up for the holidays.</p></div></div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="grid c3">{card('🍳','Real family food','Simple everyday American dinners, plus breakfasts and lunches, with step-by-step cooking mode.')}{card('👨‍👩‍👧','Shared lists','Invite your household with a code. Checks sync to everyone’s phone instantly.')}{card('⭐','Chow Hall Pro','Optional Pro unlocks extras like budget mode. The core planner is free.')}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="cta"><h2>Coming soon to the App Store.</h2><p>Want to know when it launches? Email us and we’ll let you know.</p><div class="btns"><a class="btn" href="mailto:ringtailapps@gmail.com?subject=Chow%20Hall%20launch">Notify me</a><a class="btn ghost" href="/support/">Support</a></div></div></div></section>''', 1)

faq = [('Is Chow Hall free?','Yes. Planning your week, recipes, the grocery list, shared lists and potlucks are free. Chow Hall Pro is an optional subscription that adds extras like budget mode.'),
('Do I need an account?','No. Chow Hall works without one, and your plan stays on your phone. An account lets you back up your data and share lists and potlucks.'),
('How do I share my grocery list?','Open your list, tap Share and send the invite to your household. They can join with the link or by typing the code in Chow Hall.'),
('I forgot my password.','On the sign-in screen, tap “Forgot password?” and we’ll email you a link to set a new one. Check your spam folder if it doesn’t arrive within a few minutes.'),
('How do I cancel Pro?','Subscriptions are managed by Apple. On your iPhone, open Settings, tap your name, then Subscriptions, and choose Chow Hall. Deleting the app doesn’t cancel it.'),
('How do I restore a purchase?','In Chow Hall, open the Chow Hall Pro screen and tap Restore purchases while signed in to the same Apple ID you used to subscribe.'),
('How do I delete my account?','In Chow Hall, go to Settings → Delete account. This permanently removes your account and cloud data. You can also email us and we’ll do it for you.'),
('Can I suggest a recipe or feature?','Please do! Email us. Many of our favorite ideas came from families using the app.')]
qs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
page('support/index.html','Support · RingTailApps','Get help with Chow Hall and other RingTailApps apps.',f'''<div class="doc"><div class="eyebrow">Support</div><h1>How can we help?</h1><p class="meta">Answers for Chow Hall and every RingTailApps app.</p>
<div class="contact"><img src="/assets/raccoon-chef.png" alt=""><h2 style="margin:0;font-size:24px">Email us anytime</h2><p style="margin:0;color:var(--mute)">A real person reads every message. We usually reply within 1–2 business days.</p><a class="btn" href="mailto:ringtailapps@gmail.com">ringtailapps@gmail.com</a></div>
<h2>Frequently asked questions</h2>{qs}
<p style="margin-top:30px;color:var(--mute)">See also our <a href="/privacy/">Privacy Policy</a> and <a href="/terms/">Terms of Use</a>.</p></div>''',1)

def legal(name, title):
    t = (SRC/f'{name}.html').read_text()
    body = t.split('</nav>',1)[1].split('</main>')[0]
    body = body.replace('class="card"','class="box"').replace('href="/support"','href="/support/"').replace('href="/privacy"','href="/privacy/"').replace('href="/terms"','href="/terms/"')
    body = re.sub(r'<h1>', '<div class="eyebrow">Legal</div><h1>', body, count=1)
    if name=='privacy':
        body = body.replace('hosts this website and invite pages.', 'hosts the app’s invite and account pages.')
        body = body.replace('<h2>How we use data</h2>', '<h2>This website</h2><p>ringtailapps.com uses no cookies, analytics or tracking, and our fonts are served from our own site. Our web host may keep standard server logs, such as IP address and time, briefly for security.</p><h2>How we use data</h2>')
    assert 'eeknight' not in body
    page(f'{name}/index.html', f'{title} · RingTailApps', f'{title} for Chow Hall by RingTailApps.', f'<div class="doc">{body}</div>', 1)
legal('privacy','Privacy Policy'); legal('terms','Terms of Use')
