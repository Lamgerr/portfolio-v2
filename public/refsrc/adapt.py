import json, re, pathlib

base = pathlib.Path('/data/data/com.termux/files/home/portfolio-v2/public/refsrc')
html = (base/'index.original.html').read_text()
js = (base/'app.original.js').read_text()

# --- JS replacements ---
# contact/socials
js = js.replace('var MAIL="ayushraj.design@gmail.com";', 'var MAIL="adi.workspace76865@gmail.com";')
js = js.replace('var CAL_URL="";', 'var CAL_URL="";')  # keep mailto fallback behavior, user has no cal
js = js.replace('var CALL=CAL_URL||"mailto:ayushraj.design@gmail.com";', 'var CALL=CAL_URL||"mailto:adi.workspace76865@gmail.com";')
js = js.replace('if(CAL_URL){[].forEach.call(document.querySelectorAll(".nav .cta,.hcta"),function(a){a.href=CAL_URL;a.target="_blank";a.rel="noopener"})}', 
                'if(CAL_URL){[].forEach.call(document.querySelectorAll(".nav .cta,.hcta"),function(a){a.href=CAL_URL;a.target="_blank";a.rel="noopener"})}')
old_soc = r'''var SOC=[["Instagram","@ayxsh.dll","https://www.instagram.com/ayxsh.dll/","#FFD44E"],
         ["GitHub","ayushraj-dev","https://github.com/ayushraj-dev","#B4F6B8"],
         ["Email","ayushraj.design@gmail.com","mailto:ayushraj.design@gmail.com","#A9DEFF"]];'''
new_soc = r'''var SOC=[["GitHub","adityakumar027","https://github.com/adityakumar027","#B4F6B8"],
         ["LinkedIn","adicrzz","https://www.linkedin.com/in/adicrzz/","#A9DEFF"],
         ["Email","adi.workspace76865@gmail.com","mailto:adi.workspace76865@gmail.com","#FFD44E"],
         ["Résumé","PDF","/Aditya_Kumar_Resume.pdf","#E7BBFF"]];'''
if old_soc not in js:
    raise SystemExit('SOC block not found')
js = js.replace(old_soc, new_soc)

# work string in home story maybe
js = js.replace('NexaHQ (SaaS), MediCore (Clinic Management), and StayOps (Hotel Management). Built with Next.js, Node.js, Python, PostgreSQL, and AWS.',
                'Automated Job Application System, Graph Node Classification, and PyOS. Built with React, Node.js, Python, TensorFlow, and more.')

# Replace projects P (final overridden set) - easier to replace the whole IIFE block that sets real project list
old_p_block = r'''/* =================== ROUND 12: the real project list =================== */
(function(){
  function get(id){for(var i=0;i<P.length;i++)if(P[i].id===id)return P[i]}
  var alter=get("alter"),track=get("track-it"),hb=get("focus"),wa=get("laundry");
  hb.id="hourbit";hb.n="Hourbit";hb.t="Focus timer · Android";
  hb.g="A visual focus tracker that turns deep work into falling sand, a daily heatmap and long-term momentum. Built around a 25-minute hourglass that flips and keeps going.";
  hb.k=["Android","Kotlin + Compose","Widget","In daily use"];
  hb.st=[["The problem","Focus timers ask you to care about <b>this one session</b>. What keeps me going is the streak."],["How I got there","A contribution grid already makes people come back every day. <b>So the grid became the timer.</b>"],["The key decision","The grid lives <b>on the home screen</b>, not inside the app. Darker squares mean more time."],["What I'd fix","A missed day looks like failure. I want it to read as <b>pick it back up</b>."]];
  wa.id="washio";wa.n="Washio";wa.t="Laundry app · UX/UI case study";
  wa.g="Pick a garment care, fill a bag, choose a pickup slot, and see which stage your clothes are in. Borrowed from delivery apps, rebuilt for a round trip that takes days.";
  wa.k=["UX + UI","Design system","Figma prototype"];
  wa.st=[["The problem","In smaller cities there is no one place to find a laundry. You ask around, or <b>you don't find one at all</b>."],["How I got there","Research first, then personas, then <b>a full clickable prototype in Figma</b>."],["The key decision","Treat laundries like restaurants: <b>browse, compare, book</b>, all in one list."],["Being honest","This one is a design case study. It hasn't been built or run with real laundries yet."]];
  var parchi={id:"parchi",n:"Parchi",t:"Voice billing · Android",s:"#E7BBFF",tint:"#F5E3FF",
    g:"The shopkeeper says the order out loud, in Hindi, Hinglish or English, and Parchi turns it into a receipt: item, quantity, price, total. Then print it, or share it straight to WhatsApp.",
    k:["Android","Kotlin + Compose","Voice billing"],
    shots:["Home","Listening","Receipt","Edit","Daily sales","Onboarding"],
    a:'<rect x="28" y="16" width="44" height="68" rx="6" fill="#1F0038" opacity=".92"/><rect x="36" y="28" width="28" height="3.5" rx="1.7" fill="#A500FF"/><rect x="36" y="38" width="20" height="3" rx="1.5" fill="#FAFAF8" opacity=".6"/><rect x="36" y="46" width="24" height="3" rx="1.5" fill="#FAFAF8" opacity=".6"/><rect x="36" y="54" width="16" height="3" rx="1.5" fill="#FAFAF8" opacity=".6"/><rect x="36" y="66" width="28" height="4" rx="2" fill="#A500FF"/>',
    st:[["The problem","At a kirana counter the queue doesn't wait. <b>Writing a bill by hand, or tapping through a menu, is the slow part.</b>"],["How I got there","I designed the flow and directed Google AI Studio to build it in Kotlin and Jetpack Compose, reshaping it across five versions."],["The key decision","<b>You talk, the bill writes itself.</b> Gemini reads the sentence when there's network, and a local phonetic parser takes over when there isn't."],["Being honest","It's in daily testing, not yet run by a shopkeeper who isn't me. Direct thermal printing over Bluetooth isn't built; printing goes through Android's own print dialog."]]};
  P.length=0;[alter,wa,track,parchi,hb].forEach(function(p){P.push(p)});
})();'''

new_p_block = r'''/* =================== Aditya: project list (content swapped) =================== */
(function(){
  var job={id:"job-automation",n:"Automated Job Application System",t:"Full-stack browser automation",s:"#A9DEFF",tint:"#E0F3FF",
    g:"A full-stack Chrome extension that turns unstructured résumé PDFs into editable profiles and completes applications across job portals.",
    k:["React","Node.js","Express","MongoDB","JWT","Chrome Extension"],
    shots:["PDF\nimport","Profile\nreview","Autofill","APIs","Schema","Portal flow"],
    a:'<rect x="18" y="22" width="64" height="56" rx="8" fill="#131316" opacity=".88"/><rect x="28" y="34" width="28" height="4" rx="2" fill="#A9DEFF"/><rect x="28" y="44" width="40" height="3" rx="1.5" fill="#FAFAF8" opacity=".55"/><rect x="28" y="52" width="34" height="3" rx="1.5" fill="#FAFAF8" opacity=".35"/><path d="M30 66h40" stroke="#FFD44E" stroke-width="4" stroke-linecap="round"/>',
    st:[["The problem","Job applications repeat the same data entry across portals. <b>Résumés are unstructured, but forms demand structure.</b>"],["How I got there","I built an extension + app stack to parse PDFs, let users review extracted fields, and drive autofill through secured APIs."],["The key decision","Keep profile data <b>editable and modular</b> (JWT-secured, scalable schema) so parsing errors never become permanent."],["What I'd ship next","Broader portal adapters and stronger field-mapping confidence signals for messy résumés."]]};
  var gnn={id:"node-classifier",n:"Graph Node Classification",t:"Graph machine learning",s:"#B4F6B8",tint:"#E0FBE1",
    g:"A GCN-based node classifier with two-hop neighborhood aggregation and weighted loss for the imbalanced CORA citation dataset.",
    k:["Python","TensorFlow","Keras","GCN","CORA"],
    shots:["Graph\ninput","2-hop\nagg","GCN","Weighted\nloss","Eval","Results"],
    a:'<circle cx="32" cy="38" r="8" fill="#131316" opacity=".88"/><circle cx="68" cy="34" r="8" fill="#131316" opacity=".88"/><circle cx="50" cy="66" r="8" fill="#131316" opacity=".88"/><path d="M38 42l8 18M62 38l-8 22M40 38h20" stroke="#131316" stroke-width="3" opacity=".5"/><circle cx="32" cy="38" r="3" fill="#B4F6B8"/><circle cx="68" cy="34" r="3" fill="#B4F6B8"/><circle cx="50" cy="66" r="3" fill="#FFD44E"/>',
    st:[["The problem","Dense baselines underused citation structure, and class imbalance hurt convergence on CORA."],["How I got there","Implemented a GCN with <b>two-hop neighborhood aggregation</b> to capture richer graph context."],["The key decision","Pair representation learning with a <b>weighted loss</b> and balancing so minority classes learn reliably."],["Result","+15% accuracy over dense-network baselines on the classification task."]]};
  var pyos={id:"pyos",n:"PyOS",t:"Systems simulation",s:"#FFD44E",tint:"#FFF3C4",
    g:"A modular terminal operating-system simulation with authentication, concurrent command execution, process scheduling, and an extensible shell.",
    k:["Python","CLI","Multithreading","OOP"],
    shots:["Auth","Shell","Scheduler","Processes","Modules","Commands"],
    a:'<rect x="16" y="24" width="68" height="52" rx="6" fill="#131316" opacity=".9"/><rect x="22" y="32" width="10" height="3" rx="1.5" fill="#FFD44E"/><rect x="22" y="40" width="42" height="3" rx="1.5" fill="#FAFAF8" opacity=".5"/><rect x="22" y="48" width="30" height="3" rx="1.5" fill="#FAFAF8" opacity=".35"/><rect x="22" y="58" width="6" height="6" rx="1" fill="#B4F6B8"/>',
    st:[["The problem","I wanted a concrete way to practice OS-shaped concerns: auth, scheduling, concurrency, and clean module boundaries."],["How I got there","Built a custom CLI with secure auth and multithreading, structured around object-oriented modules."],["The key decision","Make the shell <b>extensible</b> — new commands ship in fewer than 10 lines without touching core logic."],["What I'd explore next","Richer process primitives and persistence to push it closer to a teaching-grade simulation."]]};
  P.length=0;P.push(job,gnn,pyos);
})();'''

if old_p_block not in js:
    # try to locate by markers
    raise SystemExit('P override block not found')
js = js.replace(old_p_block, new_p_block)

# OFFER - adapt to engineering services/capabilities
old_offer = r'''var OFFER=[
 {id:"uiux",h:"UI/UX &amp; Product design",p:"An app or a web product taken from a rough idea to screens a developer can build without guessing.",
  inc:["User flows","Wireframes","UI + system","Prototype","Handoff"],pc:"#A9DEFF",tool:0,lbl:"UI/UX"},
 {id:"systems",h:"Design systems",p:"Tokens, components and the rules behind them, so a product keeps looking like itself as it grows and new people start building on it.",
  inc:["Tokens","Component library","Documentation","Figma + code"],pc:"#E7BBFF",tool:3,lbl:"Design systems"},
 {id:"graphic",h:"Graphic design",p:"Posts, banners, campaign statics and print. The pieces people see before they ever open the product, made as a set so they look like they came from the same place.",
  inc:["Social + campaign","Banners","Print + packaging","Presentations"],pc:"#FFD44E",tool:1,lbl:"Graphic design"},
 {id:"brand",h:"Brand identity",p:"A mark, a palette, type, and the rules that keep it holding together once other people start using it.",
  inc:["Logo system","Palette + type","Guidelines","Collateral"],pc:"#B4F6B8",tool:1,lbl:"Brand identity"},
 {id:"motion",h:"Micro-interactions &amp; motion",p:"The layer most products skip. Scroll behaviour, transitions, state changes. Designed, then built as real code components.",
  inc:["Motion spec","Code components","Scroll systems","Handoff"],pc:"#A9DEFF",tool:2,lbl:"Motion"}
];'''

new_offer = r'''var OFFER=[
 {id:"backend",h:"Backend &amp; API engineering",p:"Production APIs and services designed for reliability, observability, and scale — from schema to deploy.",
  inc:["REST APIs","Auth &amp; data models","Service design","Monitoring","Docs"],pc:"#A9DEFF",tool:0,lbl:"Backend"},
 {id:"ai",h:"AI automation &amp; agents",p:"Agentic workflows, RCA, and human-in-the-loop automation that reduce toil and resolve failures in production.",
  inc:["Agent workflows","RCA &amp; feedback loops","Integrations","Guardrails","Cost/latency"],pc:"#E7BBFF",tool:3,lbl:"AI systems"},
 {id:"platform",h:"Platform &amp; reliability",p:"Pipelines and operational glue across queues, observability, and CI/CD so systems stay healthy under load.",
  inc:["Observability","AWS SQS &amp; pipelines","Incident response","Dashboards","Runbooks"],pc:"#FFD44E",tool:1,lbl:"Reliability"},
 {id:"fullstack",h:"Full-stack products",p:"End-to-end features and tools — from React UIs to Node/Express services and databases — shipped with care.",
  inc:["React/TypeScript","Node.js/Express","MongoDB/MySQL","Auth","Delivery"],pc:"#B4F6B8",tool:1,lbl:"Full-stack"},
 {id:"ml",h:"Data &amp; ML experimentation",p:"Applied ML and quantitative research: models, backtesting, and learning systems grounded in real evaluation.",
  inc:["Modeling","TensorFlow/Keras","Backtesting","Analysis","Iteration"],pc:"#A9DEFF",tool:2,lbl:"ML &amp; data"}
];'''
if old_offer not in js:
    raise SystemExit('OFFER block not found')
js = js.replace(old_offer, new_offer)

# footer/home contact copy context
js = js.replace('home:["Your turn","Good ideas deserve a thoughtful start.","Tell me what you want to create and who it\'s for. We\'ll find a clear direction for the design and the build."]',
                'home:["Get in touch","Have a system to build or scale?","I\'m open to software engineering roles. Tell me about the problem, the stack, and what reliability looks like for you."]')

(base/'app.adapted.js').write_text(js)

# --- HTML replacements ---
# title/meta
html = re.sub(r'<title>.*?</title>', '<title>Aditya Kumar · AI &amp; Backend Software Engineer</title>', html, count=1)
html = html.replace('content="Ayush builds full-stack products, backend systems, and cloud infrastructure — from rough idea to production-ready code."',
                    'content="Aditya Kumar builds production AI, backend infrastructure, and reliable automation — systems engineered to scale, recover, and stay dependable."')
html = html.replace('content="Ayush · Full-Stack Developer &amp; System Architect"', 'content="Aditya Kumar · AI &amp; Backend Software Engineer"')
html = html.replace('content="I build full-stack products, backend systems, and cloud infrastructure — rough idea to production-ready code."',
                    'content="Production AI and backend infrastructure engineered to scale, recover, and stay reliable."')
html = html.replace('<meta property="og:site_name" content="Ayush">', '<meta property="og:site_name" content="Aditya Kumar">')
html = html.replace('content="Ayush’s portfolio hero, with real app and website previews"', 'content="Aditya Kumar — portfolio"')
# json-ld
old_ld = r'{"@context": "https://schema.org", "@type": "Person", "name": "Ayush", "alternateName": "System Architect", "jobTitle": "Full-Stack Developer & System Architect", "url": "", "email": "mailto:ayushraj.design@gmail.com", "address": {"@type": "PostalAddress", "addressLocality": "Remote / Worldwide", "addressCountry": ""}, "knowsAbout": ["Full-stack development", "System design", "DevOps & cloud", "Backend architecture", "Design systems", "API development"], "sameAs": ["https://www.instagram.com/ayxsh.dll/", "https://github.com/ayushraj-dev"]}'
new_ld = r'{"@context": "https://schema.org", "@type": "Person", "name": "Aditya Kumar", "jobTitle": "AI & Backend Software Engineer", "url": "", "email": "mailto:adi.workspace76865@gmail.com", "address": {"@type": "PostalAddress", "addressLocality": "Gwalior", "addressCountry": "IN"}, "knowsAbout": ["Backend engineering", "AI automation", "APIs", "Distributed systems", "Observability", "Machine learning"], "sameAs": ["https://github.com/adityakumar027", "https://www.linkedin.com/in/adicrzz/"]}'
html = html.replace(old_ld, new_ld)
html = html.replace('aria-label="Ayush · Full-Stack Developer &amp; System Architect"', 'aria-label="Aditya Kumar · AI &amp; Backend Software Engineer"')
html = html.replace('aria-label="Ayush, home"', 'aria-label="Aditya Kumar, home"')
html = html.replace('<span class="name-face">Ayush</span><span class="visually-hidden"> · Full-Stack Developer &amp; System Architect</span>',
                    '<span class="name-face">Aditya</span><span class="visually-hidden"> Kumar · AI &amp; Backend Software Engineer</span>')
html = html.replace('<span class="negname" id="negName">Ayush</span>', '<span class="negname" id="negName">Aditya</span>')
html = html.replace('<p class="hero-role rise" style="animation-delay:.26s">Full-Stack Developer &amp; System Architect</p>',
                    '<p class="hero-role rise" style="animation-delay:.26s">AI &amp; Backend Software Engineer</p>')
html = html.replace('<span class="hm-line">I build full-stack products, backend systems <button class="hero-stack" type="button" data-group="websites" aria-label="Expand project previews" aria-expanded="false"></button> and cloud infrastructure,</span> <span class="hm-line">and ship them to production <span class="hero-build"></span><span class="visually-hidden">.</span></span> <span class="hero-credit-clause">Production-grade work built with modern web &amp; cloud stacks.<span class="visually-hidden">.</span></span>',
                    '<span class="hm-line">I build production AI, backend infrastructure <button class="hero-stack" type="button" data-group="websites" aria-label="Expand project previews" aria-expanded="false"></button> and reliable automation,</span> <span class="hm-line">engineered to scale and recover <span class="hero-build"></span><span class="visually-hidden">.</span></span> <span class="hero-credit-clause">IIIT Gwalior · open to software engineering roles.<span class="visually-hidden">.</span></span>')
html = html.replace('Available for projects &amp; freelance', 'Open to software engineering roles')
html = html.replace('<p class="kick">AYUSH � FULL-STACK DEVELOPER &amp; SYSTEM ARCHITECT</p>',
                    '<p class="kick">ADITYA KUMAR · AI &amp; BACKEND SOFTWARE ENGINEER</p>')

# about page headline/copy (rough adaptation)
html = html.replace('<h1 class="big">I came out of a CS degree and started shipping products.</h1>',
                    '<h1 class="big">I build systems that scale, recover, and stay reliable.</h1>')
html = html.replace('<p class="lede" style="margin-top:20px;text-align:center">The short answer is that I kept building things until someone paid me to do it. The longer answer is below.</p>',
                    '<p class="lede" style="margin-top:20px;text-align:center">Integrated B.Tech IT + MBA at IIIT Gwalior, working at the intersection of backend engineering, intelligent automation, and production operations.</p>')

# jobs/experience section in about (static in HTML)
old_jobs = r'''        <h2 class="jobs-h">Where I've worked.</h2>
        <div class="jobs">
          <div class="job"><span class="yr">2024</span><div><h3>Freelance · Full-Stack Development</h3><p>Working directly with founders and product teams. StayOps (US hospitality), MediCore (clinic management), and NexaHQ (SaaS) all shipped during this period. Remote / Worldwide.</p></div></div>
          <div class="job"><span class="yr">2023</span><div><h3>Freelance · Backend &amp; API Development</h3><p>RESTful APIs, database design, and cloud deployments for early-stage startups. The first time people paid for systems thinking, not just code.</p></div></div>
          <div class="job"><span class="yr">2022</span><div><h3>Open Source &amp; Personal Projects</h3><p>Building in public. Where the stack choices were mine to make and the production incidents were mine to fix. Where I learned what "it works on my machine" really costs.</p></div></div>
        </div>
        <p class="edu"><b>Education:</b> B.Tech / Bachelor's in Computer Science, 2021–2025. The systems thinking and architectural instincts are self-sharpened — which is either a red flag or the most interesting thing about me, depending on who's reading.</p>'''
new_jobs = r'''        <h2 class="jobs-h">Where I've worked.</h2>
        <div class="jobs">
          <div class="job"><span class="yr">2026</span><div><h3>Curefit · House of Cult — Software Engineering Intern</h3><p>May 2026 — Present. Production AI automation across campaign, segmentation, notification, and internal ops. Built RCA agent with self-learning feedback (60%+ failures auto-resolved), integrated Coralogix/AWS SQS/Sentry/Metabase (70% faster incident response), evolved leave approval Copilot→Autopilot (85% less manual review), and maintained 20+ REST APIs.</p></div></div>
          <div class="job"><span class="yr">2025</span><div><h3>WorldQuant BRAIN — Quantitative Research Consultant (Expert)</h3><p>May 2025 — Apr 2026. Researched and backtested quantitative alpha models; 300+ alphas submitted, 12+ passing all quality checks (Sharpe &gt; 2.25, turnover &lt; 30%), improving strategy performance by 20%.</p></div></div>
        </div>
        <p class="edu"><b>Education:</b> IIIT Gwalior · Integrated B.Tech IT + MBA · Nov 2022 — Jun 2027 · CGPA 7.97.</p>'''
if old_jobs in html:
    html = html.replace(old_jobs, new_jobs)

# work page intro
html = html.replace('<h1 class="big">Products I built, and mostly shipped.</h1>',
                    '<h1 class="big">Systems and projects I\'ve built.</h1>')
html = html.replace('<p class="lede" style="margin-top:20px;text-align:center">Full-stack products built from scratch — SaaS, clinic ops, hotel management. Each case study covers the problem, the architecture, the call that mattered, and what I\'d fix.</p>',
                    '<p class="lede" style="margin-top:20px;text-align:center">Selected work across full-stack automation, graph ML, and systems simulation — with real code, tradeoffs, and outcomes.</p>')

# tools section on work page (static wtools) - replace with Aditya projects links
old_wtools = r'''    <section style="padding-block:0 60px"><div class="wrap"><h2 class="wsec">Websites &amp; OSS tools</h2><div class="wtools">
      <a class="wtool lead" href="https://github.com/ayushraj-dev" target="_blank" rel="noopener" style="--c:#E7BBFF"><b>NexaHQ</b><span>AI-powered team collaboration platform. Next.js, Node.js, PostgreSQL, Redis, deployed on AWS with Docker + Kubernetes.</span><i>GitHub ↗</i></a>
      <a class="wtool" href="https://github.com/ayushraj-dev" target="_blank" rel="noopener" style="--c:#B4F6B8"><b>MediCore</b><span>Full clinic management: patient records, appointments, billing, reporting. React, Django, PostgreSQL, Docker.</span><i>GitHub ↗</i></a>
      <a class="wtool" href="https://github.com/ayushraj-dev" target="_blank" rel="noopener" style="--c:#FFD44E"><b>StayOps</b><span>Hotel operations platform for a US hospitality group. Reservations, housekeeping, billing, analytics. Next.js, Node.js, MongoDB, Redis, AWS.</span><i>GitHub ↗</i></a>
    </div></div></section>'''
new_wtools = r'''    <section style="padding-block:0 60px"><div class="wrap"><h2 class="wsec">Links</h2><div class="wtools">
      <a class="wtool lead" href="https://github.com/adityakumar027/Automated-Job-Application-System" target="_blank" rel="noopener" style="--c:#A9DEFF"><b>Automated Job Application System</b><span>Chrome extension + app: résumé PDF → editable profile → autofill. React, Node.js, Express, MongoDB, JWT.</span><i>GitHub ↗</i></a>
      <a class="wtool" href="https://github.com/adityakumar027/node-classifier" target="_blank" rel="noopener" style="--c:#B4F6B8"><b>Graph Node Classification</b><span>GCN on CORA with two-hop aggregation and weighted loss. +15% accuracy over dense baselines.</span><i>GitHub ↗</i></a>
      <a class="wtool" href="https://github.com/adityakumar027/PyOS" target="_blank" rel="noopener" style="--c:#FFD44E"><b>PyOS</b><span>Modular terminal OS simulation: auth, scheduling, multithreading, extensible shell (&lt;10 lines/command).</span><i>GitHub ↗</i></a>
    </div></div></section>'''
if old_wtools in html:
    html = html.replace(old_wtools, new_wtools)

# footer/copyright/testimonial refs to Ayush
html = html.replace('<span>© 2026 Ayush</span>', '<span>© 2026 Aditya Kumar</span>')
html = html.replace('A few words for Ayush', 'A few words for Aditya')
html = html.replace("Write it the way you'd say it to a friend. Ayush reads it first, and it only goes on his site once he's checked it with you in mind.",
                    "Write it the way you'd say it to a friend. I'll read it first, and it only goes up once I've reviewed it.")
html = html.replace("How your card will look on Ayush's site", "How your card will look on my site")
html = html.replace('Send it to Ayush <', 'Send it <')
html = html.replace("It's with Ayush now. He'll review it and let you know before it goes up.", "It's with me now. I'll review it before it goes up.")
html = html.replace("testimonials (Oct 23, Ayush's design):", "testimonials:")

# swap script reference to our adapted bundle
html = html.replace('<script src="/assets/bundles/app.ayush.js"></script>', '<script src="/assets/bundles/app.adapted.js"></script>')

(base/'index.adapted.html').write_text(html)

print('ok')
