#!/usr/bin/env python3
# The docenta.ai pages, generated from one copy source.
# Run from the site root: python3 tools/gen.py  (writes index.html and for/*/index.html)
# Copy follows docs/go-to-market/positioning-and-question-library-2026-09-17.md
# in the docenta repo: pain before mechanism, questions as the hero content,
# every answer shown as answer + evidence + conflicts + gaps + evidence path.
import html, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = r"""
  :root{
    --rust:#CE422B; --ember:#F7B26B; --crimson:#B03618; --tan:#DEA584;
    --charcoal:#0F0D0B; --charcoal-mid:#1E1B18; --cream:#F2EDE8; --sand:#9A8D82;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{background:var(--charcoal);color:var(--cream);font-family:Inter,'Segoe UI',system-ui,sans-serif;font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
  a{color:var(--ember);text-decoration:none}
  a:hover{text-decoration:underline}
  a:focus-visible,button:focus-visible{outline:2px solid var(--ember);outline-offset:3px}
  .mono{font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
  .wrap{max-width:1060px;margin:0 auto;padding:0 24px}
  nav{display:flex;align-items:center;justify-content:space-between;padding:26px 0}
  .brand{display:flex;align-items:center;gap:12px;font-weight:800;font-size:22px;letter-spacing:-.5px;color:var(--cream)}
  .brand img{width:38px;height:38px}
  .brand:hover{text-decoration:none}
  .nav-cta{font-family:'JetBrains Mono',monospace;font-size:14px;background:var(--rust);padding:10px 18px;border-radius:8px;font-weight:700;color:var(--cream)}
  .nav-cta:hover{background:var(--crimson);text-decoration:none}
  .placard{font-family:'JetBrains Mono',monospace;font-size:12.5px;letter-spacing:.18em;color:var(--tan);text-transform:uppercase;display:flex;align-items:center;gap:14px;margin-bottom:22px;flex-wrap:wrap}
  .placard::before{content:"";display:inline-block;width:34px;height:1px;background:var(--tan);opacity:.6}
  header{padding:56px 0 30px}
  h1{font-weight:800;font-size:clamp(38px,6.4vw,64px);line-height:1.04;letter-spacing:-.03em;max-width:860px;text-wrap:balance}
  h1 em{font-style:normal;color:var(--ember)}
  .sub{color:var(--sand);font-size:clamp(17px,2vw,21px);max-width:680px;margin:26px 0 10px}
  .sub strong{color:var(--cream);font-weight:600}
  /* the prompt rail: what people actually say */
  .chips{display:flex;flex-wrap:wrap;gap:10px;margin:26px 0 6px}
  .chip{font-family:'JetBrains Mono',monospace;font-size:13.5px;color:var(--cream);background:var(--charcoal-mid);border:1px solid #2c2620;border-radius:999px;padding:8px 14px}
  .chip::before{content:"\275D ";color:var(--ember)}
  .chip:hover{border-color:var(--ember);text-decoration:none}
  /* the answer, shown as it is reconstructed */
  .terminal{margin:44px 0 8px;background:var(--charcoal-mid);border:1px solid #2c2620;border-radius:12px;box-shadow:0 24px 60px rgba(0,0,0,.55);overflow:hidden}
  .term-bar{display:flex;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid #2c2620}
  .dot{width:11px;height:11px;border-radius:50%;background:#3a332c}
  .dot.r{background:var(--crimson)}
  .term-title{margin-left:8px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--sand)}
  .term-body{padding:22px 24px 26px;font-family:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;font-size:14px;line-height:1.7}
  .q{color:var(--cream);margin-bottom:14px}
  .q::before{content:"\276F ";color:var(--ember)}
  .ans{font-family:Inter,'Segoe UI',system-ui,sans-serif;font-size:16px;line-height:1.6;color:var(--cream);margin:0 0 16px;max-width:820px}
  .ans strong{color:var(--ember);font-weight:600}
  .lbl{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--tan);margin:14px 0 6px}
  .ev{display:grid;grid-template-columns:22px 1fr;gap:8px;color:var(--cream);margin:4px 0}
  .ev .n{color:var(--ember)}
  .ev .path{color:var(--ember)}
  .ev .span{color:var(--sand)}
  .box{border-left:3px solid var(--tan);padding:6px 12px;margin:8px 0;color:var(--cream);font-family:Inter,'Segoe UI',system-ui,sans-serif;font-size:15px}
  .box.conflict{border-color:var(--rust)}
  .box.gap{border-color:var(--sand)}
  .box b{color:var(--tan);font-weight:600}
  .route{color:var(--sand);font-size:13px;margin-top:10px}
  .route b{color:var(--cream);font-weight:600}
  .term-note{font-family:'JetBrains Mono',monospace;font-size:12.5px;color:var(--sand);margin:14px 2px 0}
  section{padding:72px 0 8px}
  h2{font-weight:800;font-size:clamp(26px,3.6vw,38px);letter-spacing:-.02em;max-width:760px;text-wrap:balance}
  .lead{color:var(--sand);max-width:680px;margin-top:16px}
  .lead strong{color:var(--cream);font-weight:600}
  .cols{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}
  .cols.two{grid-template-columns:repeat(2,1fr)}
  .card{background:var(--charcoal-mid);border:1px solid #2c2620;border-radius:12px;padding:26px 24px}
  .card h3{font-size:18px;font-weight:700;letter-spacing:-.01em;margin-bottom:10px}
  .card h3 .k{color:var(--ember)}
  a.card{display:block;color:inherit;text-decoration:none;transition:border-color .15s ease,transform .15s ease}
  a.card:hover,a.card:focus-visible{border-color:var(--ember);transform:translateY(-2px);outline:none}
  a.card:focus-visible{box-shadow:0 0 0 2px var(--ember)}
  a.card h3::after{content:"\00a0\2192";color:var(--ember);font-weight:400}
  a.card.wide{grid-column:1 / -1;display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center;border-color:var(--tan)}
  a.card.wide .live{margin:0;white-space:nowrap}
  @media (max-width:820px){a.card.wide{grid-template-columns:1fr}}
  .card p{color:var(--sand);font-size:15.5px}
  .card p code{font-family:'JetBrains Mono',monospace;font-size:13.5px;color:var(--tan)}
  .card .qs{margin-top:12px;color:var(--tan);font-family:'JetBrains Mono',monospace;font-size:12.5px;line-height:1.7}
  /* the prompt wall, grouped by job */
  .wall{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:36px}
  .wall .g h4{font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--tan);margin-bottom:10px}
  .wall .g p{color:var(--cream);font-size:14.5px;line-height:1.5;margin-bottom:10px;padding-left:14px;text-indent:-14px}
  .wall .g p::before{content:"\275D ";color:var(--ember)}
  @media (max-width:980px){.wall{grid-template-columns:repeat(2,1fr)}}
  @media (max-width:560px){.wall{grid-template-columns:1fr}}
  /* jobs, not brands */
  table.jobs{width:100%;border-collapse:collapse;margin-top:34px;font-size:15.5px}
  table.jobs th{text-align:left;font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--tan);padding:0 14px 12px 0;font-weight:600}
  table.jobs td{padding:12px 14px 12px 0;border-top:1px solid #2c2620;vertical-align:top;color:var(--sand)}
  table.jobs td:last-child{color:var(--cream)}
  .tablewrap{overflow-x:auto}
  /* the receipts motif */
  .receipts{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:34px}
  .receipts div{border:1px dashed var(--tan);border-radius:10px;padding:16px 14px;background:linear-gradient(180deg,#171310,#12100d)}
  .receipts b{display:block;font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ember);margin-bottom:8px}
  .receipts span{color:var(--sand);font-size:14px;line-height:1.5}
  @media (max-width:980px){.receipts{grid-template-columns:repeat(2,1fr)}}
  .limits{margin-top:30px;max-width:760px}
  .limits p{padding:10px 0;border-top:1px solid #2c2620;color:var(--sand)}
  .limits p b{color:var(--cream);font-weight:600}
  .plaque{margin-top:44px;border:1px solid var(--tan);border-radius:12px;padding:8px 0;background:linear-gradient(180deg,#171310,#12100d)}
  .plaque-title{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--tan);text-align:center;padding:18px 0 6px}
  .plaque-grid{display:grid;grid-template-columns:repeat(5,1fr);padding:10px 10px 20px}
  .stat{padding:14px 10px;text-align:center;border-left:1px solid #2c2620}
  .stat:first-child{border-left:none}
  .stat b{display:block;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:clamp(18px,2.4vw,26px);color:var(--ember);letter-spacing:-.02em}
  .stat span{font-size:12.5px;color:var(--sand);display:block;margin-top:6px;line-height:1.45}
  .plaque-foot{font-size:12px;color:var(--sand);text-align:center;padding:0 20px 16px}
  .spine{margin-top:40px;font-family:'JetBrains Mono',monospace;font-size:14px;line-height:2.05;background:var(--charcoal-mid);border:1px solid #2c2620;border-radius:12px;padding:26px 28px;color:var(--sand);overflow-x:auto}
  .spine b{color:var(--cream);font-weight:600}
  .spine .a{color:var(--ember)}
  .steps{counter-reset:step;margin-top:34px;display:grid;gap:18px;max-width:760px}
  .step{display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:start}
  .step::before{counter-increment:step;content:counter(step);width:38px;height:38px;border-radius:50%;border:1px solid var(--tan);color:var(--ember);font-family:'JetBrains Mono',monospace;font-weight:700;display:flex;align-items:center;justify-content:center}
  .step h3{font-size:18px;font-weight:700;letter-spacing:-.01em;margin-bottom:6px}
  .step p{color:var(--sand);font-size:15.5px}
  .step p strong{color:var(--cream);font-weight:600}
  pre.cmd{margin-top:12px;background:var(--charcoal-mid);border:1px solid #2c2620;border-radius:10px;padding:14px 16px;font-family:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;font-size:13.5px;color:var(--cream);overflow-x:auto;white-space:pre;line-height:1.6}
  pre.cmd .a{color:var(--ember)}
  .live{display:inline-block;margin-left:10px;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--charcoal);background:var(--ember);padding:3px 8px;border-radius:6px;vertical-align:middle}
  .cta{margin:84px 0 0;padding:56px 40px;text-align:center;background:linear-gradient(180deg,var(--charcoal-mid),#171310);border:1px solid #2c2620;border-radius:16px}
  .cta h2{max-width:none}
  .cta p{color:var(--sand);margin:16px auto 30px;max-width:560px}
  .btn{display:inline-block;background:var(--rust);color:var(--cream);font-weight:700;font-size:17px;padding:15px 34px;border-radius:10px}
  .btn:hover{background:var(--crimson);text-decoration:none}
  .cta .alt{display:block;margin-top:18px;font-size:14px;color:var(--sand)}
  .ea{margin:30px auto 0;max-width:640px;text-align:left}
  .ea-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .ea label{display:block;font-size:13.5px;color:var(--sand);margin-bottom:14px}
  .ea input,.ea select,.ea textarea{display:block;width:100%;margin-top:6px;padding:11px 12px;border-radius:8px;background:var(--charcoal);border:1px solid #2c2620;color:var(--cream);font:inherit;font-size:15.5px}
  .ea input:focus,.ea select:focus,.ea textarea:focus{outline:2px solid var(--ember);outline-offset:1px;border-color:var(--ember)}
  .ea textarea{resize:vertical;min-height:84px}
  .ea-turnstile{margin:6px 0 16px;min-height:0}
  .ea .btn{border:0;cursor:pointer;font-family:inherit}
  .ea .btn[disabled]{opacity:.6;cursor:wait}
  .ea-status{margin-top:14px;font-size:14.5px;color:var(--cream);min-height:1.4em}
  .ea-status a{color:var(--ember)}
  @media (max-width:640px){.ea-grid{grid-template-columns:1fr}}
  footer{margin-top:80px;padding:34px 0 44px;border-top:1px solid #2c2620;color:var(--sand);font-size:13.5px}
  footer .frow{display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}
  footer a{color:var(--tan)}
  @media (max-width:820px){
    .cols,.cols.two{grid-template-columns:1fr}
    .plaque-grid{grid-template-columns:repeat(2,1fr)}
    .stat{border-left:none;border-top:1px solid #2c2620}
    .stat:first-child{border-top:none}
  }
"""

AUDIENCES = [
    ("contractors", "Contractors: the Palo Alto building rules door"),
    ("lawyers", "Lawyers: the matter file"),
    ("insurance", "Insurance: the claim file"),
    ("home", "Home: a life in files"),
    ("email", "Mail: the mailbox"),
    ("developers", "Developers: repos and sessions"),
    ("researchers", "Researchers: the reading pile"),
]

def e(s):
    return html.escape(s, quote=True)

def head(title, desc, canonical, og_title=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon-180.png">
<meta property="og:title" content="{e(og_title or title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="https://docenta.ai/assets/og-card-1200x630.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{e(canonical)}">
<link rel="canonical" href="{e(canonical)}">
<meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <nav>
    <a class="brand" href="/"><img src="/assets/docenta-glyph.svg" alt="" width="38" height="38">docenta</a>
    <a class="nav-cta" href="#access">request early access</a>
  </nav>
"""

FOOT = """
  <footer>
    <div class="frow">
      <div>docenta is a product of SKY, LLC. From the makers of <a href="https://uffs.io">UFFS</a>, the open-source NTFS search engine.</div>
      <div>Built in Rust. Runs on macOS, Windows, Linux.</div>
    </div>
  </footer>
</div>
</body>
</html>
"""

def chips(items):
    return '<div class="chips">' + "".join(f'<a class="chip" href="#answer">{e(q)}</a>' for q in items) + "</div>"

def answer(question, ans_html, evidence, conflict, gap, route, note, title="agent session · docenta over MCP"):
    ev = "".join(
        f'<div class="ev"><span class="n">{i+1}.</span><span><span class="path">{e(p)}</span> <span class="span">· {e(s)}</span></span></div>'
        for i, (p, s) in enumerate(evidence)
    )
    conf = f'<div class="box conflict"><b>Conflict.</b> {conflict}</div>' if conflict else '<div class="box"><b>Conflict.</b> None found in the retrieved evidence.</div>'
    gp = f'<div class="box gap"><b>Gap.</b> {gap}</div>'
    rt = f'<div class="route"><b>Evidence path</b> · {e(route)}</div>'
    return f"""
    <div class="terminal" id="answer" aria-label="An answer, shown as it was reconstructed">
      <div class="term-bar"><span class="dot r"></span><span class="dot"></span><span class="dot"></span><span class="term-title">{e(title)}</span></div>
      <div class="term-body">
        <div class="q">{e(question)}</div>
        <div class="lbl">Answer</div>
        <p class="ans">{ans_html}</p>
        <div class="lbl">Evidence</div>
        {ev}
        {conf}
        {gp}
        {rt}
      </div>
    </div>
    <p class="term-note">{note}</p>
"""

def wall(groups):
    out = ['<div class="wall">']
    for title, qs in groups:
        out.append(f'<div class="g"><h4>{e(title)}</h4>' + "".join(f"<p>{e(q)}</p>" for q in qs) + "</div>")
    out.append("</div>")
    return "".join(out)

def cards(items, two=False):
    cls = "cols two" if two else "cols"
    return f'<div class="{cls}">' + "".join(
        f'<div class="card"><h3><span class="k">{e(k)}</span> {e(rest)}</h3><p>{body}</p></div>' for k, rest, body in items
    ) + "</div>"

def limits(items):
    return '<div class="limits">' + "".join(f"<p><b>{e(b)}</b> {e(t)}</p>" for b, t in items) + "</div>"

def contract():
    return cards([
        ("Exact source.", "", "The file, the page, the message, the span. Not \"sources\": the line you can open and read."),
        ("Order and version.", "", "When it was said, which version it was, what replaced what. A three-event timeline beats another paragraph."),
        ("Conflicts.", "", "Two sources that disagree are shown side by side, never smoothed into one confident sentence."),
    ]) + '<div class="cols two" style="margin-top:22px">' + "".join(
        f'<div class="card"><h3><span class="k">{e(k)}</span></h3><p>{body}</p></div>' for k, body in [
            ("Gaps.", "\"Not established by this collection\" is an answer, printed as one. It is how you know the rest is solid."),
            ("The evidence path.", "What was searched, which lanes answered, what was dropped and why, how many tokens the agent was handed. Inspectable, every time."),
        ]) + "</div>"

def privacy(rolewords):
    return f"""
  <section>
    <div class="placard">Ask the sensitive question</div>
    <h2>Ask the sensitive question without first uploading the sensitive file.</h2>
    <p class="lead">{rolewords} stay on your machine: ingest, index, embeddings and answers all run there. Originals are never copied; only searchable derivatives are stored. Your agent gets a small evidence pack, a few kilobytes with the receipts, not your archive. Zero uploads, zero telemetry, and the token budget is printed on every answer.</p>
    <p class="lead" style="margin-top:14px">Served over MCP, the connector standard Claude, ChatGPT and most coding assistants speak, so the agent you already use asks docenta the way it asks any other tool. Deterministic layers, no learned model in the retrieval loop, bit-stable re-runs.</p>
  </section>
"""

def plug(name, host, mcp_name, word):
    return f"""
  <section id="plug">
    <div class="placard">Try the engine on public material <span class="live">live door</span></div>
    <h2>One address, one key, every question cited.</h2>
    <p class="lead">This collection is served as an MCP server at <strong>https://{host}/mcp</strong>. You add the address once; from then on your assistant asks it the way it asks any other tool.</p>
    <div class="steps">
      <div class="step">
        <h3>Ask for a key</h3>
        <p>Use the form at the bottom of this page and say "{word}". You get back a key, a long line of letters and numbers. Keep it like a password: it is what lets your assistant in.</p>
      </div>
      <div class="step">
        <h3>Claude Code: one command</h3>
        <p>Paste this line with your key in place of the words in angle brackets, then start a new session; the collection shows up as <strong>{mcp_name}</strong>.</p>
        <pre class="cmd">claude mcp add --transport http {mcp_name} <span class="a">https://{host}/mcp</span> \\
  --header "Authorization: Bearer &lt;your key&gt;"</pre>
      </div>
      <div class="step">
        <h3>Claude.ai or ChatGPT: a custom connector</h3>
        <p>In the settings, under connectors, add a remote MCP server with the address <strong>https://{host}/mcp</strong>. Where it asks for a header or a token, enter <strong>Authorization: Bearer &lt;your key&gt;</strong>. Save, then ask in a new chat.</p>
      </div>
      <div class="step">
        <h3>Ask, and read the citation</h3>
        <p>Every answer names the document and the page it came from. The first question after a quiet spell can take half a minute while the collection wakes up; your assistant is told so and asks again by itself.</p>
      </div>
    </div>
    <p class="lead" style="margin-top:26px">The door never sees your files, holds nothing you send beyond the question, and cannot be changed by anyone, us included, without a new seal and a new date on this page.</p>
  </section>
"""

def cta(audience, subject_word):
    opts = "".join(
        f'<option value="{v}"{" selected" if v == audience else ""}>{e(t)}</option>' for v, t in AUDIENCES
    ) + '<option value="other">Something else (say what below)</option>'
    subj = "docenta%20early%20access" + (f"%20({subject_word})" if subject_word else "")
    return f"""
  <section id="access">
    <div class="cta">
      <div class="placard" style="justify-content:center">The velvet rope</div>
      <h2>What is one question your files should be able to answer today?</h2>
      <p>docenta is a commercial product of SKY, LLC, now in private preview. Tell us the question; we will tell you when the door opens, and the questions we hear shape what we build.</p>
<form class="ea" id="early-access" data-audience="{audience}" novalidate>
        <div class="ea-grid">
          <label>Your name<input name="name" required maxlength="120" autocomplete="name"></label>
          <label>Your email<input name="email" type="email" required maxlength="200" autocomplete="email"></label>
        </div>
        <label>Which collection, or which desk<select name="audience">{opts}</select></label>
        <label>The question your files should be able to answer (a sentence is plenty)<textarea name="message" maxlength="2000" rows="3"></textarea></label>
        <div class="ea-turnstile"></div>
        <button class="btn" type="submit">request early access</button>
        <p class="ea-status" role="status" aria-live="polite"></p>
      </form>
      <noscript><a class="btn" href="mailto:docenta@nios.net?subject={subj}">request early access by mail</a></noscript>
      <span class="alt">No account and no newsletter: we write back when the door opens. Prefer mail? <a href="mailto:docenta@nios.net?subject={subj}">docenta@nios.net</a></span>
      <script src="/assets/early-access.js" defer></script>
    </div>
  </section>
"""

ALSO = ('<p class="lead" style="margin-top:14px"><a href="/">Back to the collection</a> · also for '
        '<a href="/for/contractors/">contractors</a>, <a href="/for/lawyers/">lawyers</a>, <a href="/for/insurance/">insurance</a>, '
        '<a href="/for/home/">home</a>, <a href="/for/email/">mail</a>, <a href="/for/developers/">developers</a>, <a href="/for/researchers/">researchers</a></p>')

# ---------------------------------------------------------------- the landing page
def index_page():
    out = [head("docenta - your files remember what you forgot",
                "Private evidence-backed memory for your AI agent. Ask what happened, why, and where the proof is, across files, mail, scans, photos, git and agent sessions. Every answer comes with exact receipts; conflicts are shown; gaps are admitted. It runs on your machine.",
                "https://docenta.ai/")]
    out.append("""
  <header>
    <div class="placard">Exhibit 001 · The Corpus · 1998 to today</div>
    <h1>Your machine holds everything you ever wrote. Now ask it <em>what happened</em>.</h1>
    <p class="sub">Your documents know the terms. Your mail knows the conversation. Your photos know when and where. Your git history knows what changed. Your agent sessions know what it already tried. docenta makes them <strong>one private evidence layer</strong>, and every answer points back to the source. <strong>Nothing leaves your machine.</strong></p>
""")
    out.append(chips([
        "When did we decide this, and why?",
        "Which version did we actually approve?",
        "Where is the message where we agreed?",
        "What did the policy say on that date?",
        "Which source contradicts this?",
        "What proof am I missing?",
    ]))
    out.append(answer(
        "for a detached ADU replacing an existing garage, what side and rear setbacks apply, which code edition governs a permit deemed complete in 2025, and does the tree guidance still affect where it can go?",
        "State law sets the ceiling: <strong>no setback</strong> for a unit built in the same location and to the same dimensions as the existing structure, and <strong>no more than four feet</strong> from the side and rear lot lines for a new detached unit (Gov. Code 66310 to 66342, item 7). The City's ordinance implementing that law says ADUs comply with the underlying zone setbacks, requires none for a converted garage, and caps a unit above a garage at five feet. The City's 2018 summary handout still prints <strong>six feet</strong> for a detached unit. The <strong>2022</strong> edition of Title 24 governs a permit deemed complete before 2026. For an ADU on the state pathway (one detached unit up to 800 sq ft) trees, protected ones included, may be removed without meeting the tree ordinance, but a Tree Disclosure Statement on the T1 sheet is still required; a larger unit removes a protected tree only under PAMC 8.10.050.",
        [("california-statutes/gov-code-66310-66342-accessory-dwelling-units.txt", "\"a setback of no more than four feet from the side and rear lot lines shall be required for an accessory dwelling unit that is not converted from an existing structure\""),
         ("palo-alto-handouts/adu-ordinance-5412.pdf", "18.42.040, Setbacks and Daylight Plane: comply with the underlying zone; no setback for a converted existing garage; no more than five feet above a garage"),
         ("palo-alto-handouts/adu-summary-handout-2018-12-05.pdf", "the summary table: \"6 feet from interior side/rear property line\" for a detached unit"),
         ("title24-2022-APPLIES/EDITION.txt", "\"a permit is governed by the code in effect when its application was deemed complete\"; the 2022 parts, and which parts only the 2025 folder has"),
         ("palo-alto-handouts/trees-and-adus-guidelines.pdf", "state-pathway ADUs: trees may be removed without meeting the ordinance, Tree Disclosure Statement still required; Table 2 units: PAMC 8.10.050")],
        "The City's 2018 handout says six feet; the state statute in the same collection caps a local agency at four. The handout predates the current statute and the ordinance defers to it. Both are shown; neither is silently preferred.",
        "The collection holds no permit records and no site survey. Whether this garage is nonconforming, and whether a tree on the lot is protected, are project facts outside the corpus; the plan checker settles them, not this answer.",
        "lexical and semantic lanes over 5 sources · state, city, utility and code-edition documents kept apart · 20 candidates, 5 kept · answered from a collection sealed 2026-09-12",
        "A real answer from a live public collection, paths shortened, reproducible through the contractors door below. Google answers \"Palo Alto ADU setback\"; this answers the configuration, under the edition that governs the permit, and it caught the City's own handout contradicting the state statute. That is the moment: not a better search, a docent that read all of it and said where the sources disagree.",
    ))
    out.append("""
  </header>

  <section>
    <div class="placard">Exhibit 002 · The questions ordinary search misses</div>
    <h2>Search finds files. You want to know what happened.</h2>
    <p class="lead">Nobody wakes up wanting semantic search. People want to know <strong>where the proof is</strong>, which version stands, what the record says on a date, and what it does not say. Those are memory questions: several artifacts, a chronology, a source that outranks another, and a way to inspect the proof. That is what docenta is built for.</p>
    <div class="tablewrap"><table class="jobs">
      <tr><th>What you type into search</th><th>What you actually want to know</th></tr>
      <tr><td>files containing "streaming"</td><td>When did we decide streaming, why, and what happened next?</td></tr>
      <tr><td>emails from the contractor</td><td>Which quote replaced the old one, and did they confirm it stands?</td></tr>
      <tr><td>PDF search for "mold"</td><td>Which policy text applied on the date of loss, and what in the notes conflicts with the claim?</td></tr>
      <tr><td>git blame</td><td>Why was this line introduced, and which incident, note or session explains it?</td></tr>
      <tr><td>papers containing "low dose"</td><td>Which papers in my own library agree, which disagree, and on which page?</td></tr>
      <tr><td>"Palo Alto ADU setback"</td><td>For this configuration, under the edition that governs this permit, which setback applies, and do the city and the state agree?</td></tr>
    </table></div>
    <p class="lead" style="margin-top:26px">Local evidence, exact receipts, explicit conflicts and gaps, served to the agent you already use. <strong>Built for evidence questions ordinary search misses.</strong> A <em>docent</em> is the museum guide you ask about a collection. Your corpus gets one.</p>
  </section>

  <section>
    <div class="placard">Exhibit 003 · Receipts, every time</div>
    <h2>Answers come with receipts. Five kinds.</h2>
    <div class="receipts">
      <div><b>Answer receipt</b><span>The exact source, the exact span, page or message behind every claim.</span></div>
      <div><b>Timeline receipt</b><span>Every event on the timeline carries the source that dates it.</span></div>
      <div><b>Version receipt</b><span>Old and new side by side: what changed, and which one stands.</span></div>
      <div><b>Conflict receipt</b><span>Both contradicting sources visible. Never smoothed into one confident sentence.</span></div>
      <div><b>Gap receipt</b><span>What was searched and what the collection does not establish. "I don't know" you can trust.</span></div>
    </div>
    <p class="lead" style="margin-top:26px">Gaps disclosed, never papered over. When the corpus cannot answer, docenta says so, shows what it did find, and names the document that would settle it.</p>
  </section>

  <section>
    <div class="placard">Exhibit 004 · Ask the sensitive question</div>
    <h2>Ask the sensitive question without first uploading the sensitive file.</h2>
    <p class="lead">The matter file, the claim, the mail archive, the private source tree, the unpublished paper, the household folder: docenta ingests, indexes and answers on your own hardware. Originals are never copied; only searchable derivatives are stored. Your agent gets a <strong>small evidence pack</strong> with the receipts, not your archive, over MCP, the connector standard it already speaks. Zero uploads, zero telemetry, and the token budget is printed on every answer.</p>
    <div class="plaque">
      <div class="plaque-title">Collection statistics · one real machine</div>
      <div class="plaque-grid">
        <div class="stat"><b>815,405</b><span>content objects from 1.7M file instances</span></div>
        <div class="stat"><b>246,000</b><span>searchable messages out of one 32 GB mailbox</span></div>
        <div class="stat"><b>4-6 ms</b><span>entity and timeline answers</span></div>
        <div class="stat"><b>7.5 min</b><span>full ingest of a 463k-file home directory</span></div>
        <div class="stat"><b>0 bytes</b><span>sent to any cloud, ever</span></div>
      </div>
      <div class="plaque-foot">Measured on the maker's own corpus, Apple M4 Max. Every number traces to a committed field run.</div>
    </div>
  </section>

  <section id="for">
    <div class="placard">Exhibit 005 · Who asks</div>
    <h2>One engine, your kind of collection.</h2>
    <p class="lead">The same docent, pointed at what your desk actually holds. Each page shows one real question and the shape of its answer; two collections are live behind a door today.</p>
    <div class="cols">
      <a class="card wide" href="/for/contractors/"><div><h3><span class="k">Contractors.</span> Ask the rule. Get the exact page.</h3><p>City code, handouts, state law, utility standards and the code edition tied to the permit date, as one dated collection. Which rule applies, where the exception lives, whether the sources agree, and what the corpus cannot establish.</p><p class="qs">"Which code edition applies to this permit date?" · "Do the city handout and the ordinance agree?"</p></div><span class="live">live door</span></a>
      <a class="card wide" href="/for/lawyers/"><div><h3><span class="k">Lawyers.</span> Ask the matter. Cite the exhibit.</h3><p>Pleadings, correspondence, scanned exhibits, contracts and notes become one private evidence layer. Reconstruct the chronology, find the version that changed, surface the contradiction, map each assertion to a page, without uploading the matter anywhere. Try the engine today on the federal code and public contracts.</p><p class="qs">"Where does the other side first acknowledge this?" · "Does the declaration conflict with an earlier email?"</p></div><span class="live">live door</span></a>
      <a class="card" href="/for/insurance/"><h3><span class="k">Insurance.</span> Ask the claim, not the folders.</h3><p>Policy, notes, mail, forms, estimates and photos as one timeline with receipts: what happened, which version applies, where the file conflicts, what proof is missing.</p><p class="qs">"Which policy was in force on the loss date?"</p></a>
      <a class="card" href="/for/home/"><h3><span class="k">Home.</span> Your files remember what you forgot.</h3><p>Twenty years of mail, documents and photos, asked in plain words: the receipt tied to the warranty, the quote that replaced the old quote, the letter you half remember.</p><p class="qs">"Is the dishwasher still under warranty?"</p></a>
      <a class="card" href="/for/email/"><h3><span class="k">Mail.</span> Ask what was said, not what the subject line was.</h3><p>The promise, the latest number, the attachment that went with it and the whole thread in order, even when you remember the meaning and not the sender.</p><p class="qs">"What was the last delivery date they committed to?"</p></a>
      <a class="card" href="/for/developers/"><h3><span class="k">Developers.</span> Ask why the code is this way.</h3><p>Code, git history, design notes and every agent session as one cited memory layer. The decision behind a workaround, the attempts that failed, what the next agent should read first.</p><p class="qs">"When did we decide to split this step, and why?"</p></a>
      <a class="card" href="/for/researchers/"><h3><span class="k">Researchers.</span> Ask your library where it disagrees.</h3><p>PDFs, scans, notes, drafts and co-author mail as one evidence layer: the paper you half remember, the results that conflict, the sentence in your draft that has no support.</p><p class="qs">"Which papers support this, and which contradict it?"</p></a>
    </div>
  </section>

  <section>
    <div class="placard">Exhibit 006 · How the docent works</div>
    <h2>A spine that ingests, three channels that answer, one artifact that proves it.</h2>
    <div class="spine">
<b>ingest</b>   walk → hash → extract → index <span class="a">·</span> containers explode into members <span class="a">·</span> re-scan costs O(changes)<br>
<b>channels</b> exact BM25 <span class="a">·</span> paragraph lexical <span class="a">·</span> dense vectors, fused and re-ranked <span class="a">·</span> entities, timelines, themes on top<br>
<b>answer</b>   <span class="a">evidence_pack</span>: route plan, cited spans, conflicts, disclosed gaps, enforced token budget<br>
<b>live</b>     mail, chat exports, and agent sessions stream in continuously <span class="a">·</span> your corpus feeds itself
    </div>
    <p class="lead" style="margin-top:26px">The same 48 judged questions over the same corpus, asked by the same scripted agent two ways. With the evidence pack it cited the right document on <strong>44 of 48</strong>, in <strong>1 to 2.5 tool calls</strong> per task. Limited to search-and-fetch loops, the way an agent works without the pack, it cited it on <strong>39 of 48</strong>, in more calls. The pack reads about four times the tokens; that trade is printed, never hidden. Deterministic layers, zero learned models in the loop, bit-stable re-runs.</p>
  </section>
""")
    out.append(cta("site", ""))
    out.append(FOOT)
    return "".join(out)

# ---------------------------------------------------------------- the specialty pages
def specialty(slug, title, desc, placard, h1, sub, chip_qs, demo, wall_groups, reads, wont, rolewords, plug_html, subject_word, extra_after_demo=""):
    out = [head(title, desc, f"https://docenta.ai/for/{slug}/")]
    out.append(f"""
  <header>
    <div class="placard">{placard}</div>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
""")
    out.append(chips(chip_qs))
    out.append(demo)
    out.append(extra_after_demo)
    out.append("""
  </header>

  <section>
    <div class="placard">Questions your current search cannot answer cleanly</div>
    <h2>You remember the meaning, the date, the argument. Ask that.</h2>
""")
    out.append(wall(wall_groups))
    out.append("""
  </section>

  <section>
    <div class="placard">What docenta reads</div>
""")
    out.append(cards(reads))
    out.append("""
  </section>

  <section>
    <div class="placard">What the answer shows</div>
    <h2>The same four-part contract, every time.</h2>
""")
    out.append(contract())
    out.append("""
  </section>

  <section>
    <div class="placard">What it will not pretend to know</div>
    <h2>Boundedness is the feature.</h2>
    <p class="lead">Most AI marketing hides uncertainty. docenta prints it. The lines below are not disclaimers; they are what a trustworthy answer looks like.</p>
""")
    out.append(limits(wont))
    out.append(ALSO)
    out.append("""
  </section>
""")
    out.append(privacy(rolewords))
    out.append(plug_html)
    out.append(cta(slug, subject_word))
    out.append(FOOT)
    return "".join(out)

PAGES = {}

# ---- contractors (a real answer from the live door)
PAGES["contractors"] = dict(
    title="docenta for contractors - ask the rule, get the exact page",
    desc="Which rule actually applies to this project? Ask the city code, the handouts, state law, the utility's standards and the code edition tied to the permit date as one dated collection. Exact pages, city versus state versus utility, contradictions flagged, gaps admitted. The Palo Alto collection is live behind a door.",
    placard='Exhibit · docenta for contractors · Palo Alto building rules <span class="live">live door</span>',
    h1="Which rule <em>actually</em> applies to this project?",
    sub="Ask across the city code, the current handouts, state law, the utility's standards and the code edition tied to the permit date. docenta returns the exact pages, separates city from state from utility, flags where they contradict each other, and says when the answer needs facts that are not in the collection. <strong>The Palo Alto collection is sealed and live today.</strong>",
    chip_qs=["Which code edition applies to this permit date?", "Which setback rule applies to this exact configuration?", "Do the city handout and the ordinance agree?", "What tree rule could affect placement?", "What can this corpus not answer about my project?"],
    demo=answer(
        "for a detached ADU replacing an existing garage, what side and rear setbacks apply, which code edition governs a permit deemed complete in 2025, and does the tree guidance still affect where it can go?",
        "State law sets the ceiling: <strong>no setback</strong> for a unit built in the same location and to the same dimensions as the existing structure, and <strong>no more than four feet</strong> from the side and rear lot lines for a new detached unit (Gov. Code 66310 to 66342, item 7). The City's ordinance implementing that law says ADUs comply with the underlying zone setbacks, requires none for a converted garage, and caps a unit above a garage at five feet. The City's 2018 summary handout still prints <strong>six feet</strong> for a detached unit. The <strong>2022</strong> edition of Title 24 governs a permit deemed complete before 2026. For an ADU on the state pathway (one detached unit up to 800 sq ft) trees, protected ones included, may be removed without meeting the tree ordinance, but a Tree Disclosure Statement on the T1 sheet is still required; a larger unit removes a protected tree only under PAMC 8.10.050.",
        [("california-statutes/gov-code-66310-66342-accessory-dwelling-units.txt", "\"a setback of no more than four feet from the side and rear lot lines shall be required for an accessory dwelling unit that is not converted from an existing structure\""),
         ("palo-alto-handouts/adu-ordinance-5412.pdf", "18.42.040, Setbacks and Daylight Plane: comply with the underlying zone; no setback for a converted existing garage; no more than five feet above a garage"),
         ("palo-alto-handouts/adu-summary-handout-2018-12-05.pdf", "the summary table: \"6 feet from interior side/rear property line\" for a detached unit"),
         ("title24-2022-APPLIES/EDITION.txt", "\"a permit is governed by the code in effect when its application was deemed complete\"; the 2022 parts, and which parts only the 2025 folder has"),
         ("palo-alto-handouts/trees-and-adus-guidelines.pdf", "state-pathway ADUs: trees may be removed without meeting the ordinance, Tree Disclosure Statement still required; Table 2 units: PAMC 8.10.050")],
        "The City's 2018 handout says six feet; the state statute in the same collection caps a local agency at four. The handout predates the current statute and the ordinance defers to it. Both are shown; neither is silently preferred.",
        "The collection holds no permit records and no site survey. Whether this garage is nonconforming, and whether a tree on the lot is protected, are project facts outside the corpus; the plan checker settles them, not this answer.",
        "lexical and semantic lanes over 5 sources · state, city, utility and code-edition documents kept apart · 20 candidates, 5 kept · answered from a collection sealed 2026-09-12",
        "A real answer from the live door, paths shortened. The collection was assembled for one permit and sealed on 2026-09-12: nothing is added or changed, so what it says today it says tomorrow. Google answers \"Palo Alto ADU setback\"; this answers your configuration, under your permit's edition, with the contradiction on the table.",
    ),
    wall_groups=[
        ("Which rule", ["Which code edition applies to this permit date, and which provision decides it?", "What local amendment changes the base rule for this scope?", "Which requirements come from the city, which from the state, which from the utility?"]),
        ("This project", ["Which setback rule applies to this exact configuration, and does an exception apply to the existing structure?", "Which utility service upgrade, application step or connection fee is triggered by this scope?", "What tree rule could constrain where this addition goes?"]),
        ("Version and edition", ["What changed between the 2022 and 2025 editions on this point?", "What is the latest effective requirement in this collection, and when was it published?"]),
        ("Contradiction", ["Do the city handout, the municipal code, the ordinance and the state handbook say the same thing?", "Does the simplified handout omit a condition present in the ordinance?"]),
        ("Evidence and gaps", ["What source page should I show the plan checker or the client?", "What does the collection not contain that this permit question needs?", "Give me a checklist of cited source pages for this scope, not a generic one."]),
    ],
    reads=[
        ("The City's rules.", "", "The Palo Alto Municipal Code (Supp. 81, 2026), the Building Division and Green Building handouts, Ordinance 5412 on accessory dwelling units, the Tree Technical Manual and the trees-and-ADUs guideline."),
        ("The utility and the state.", "", "CPAU's electric service requirements, rules 3 and 20, connection fees and the application packet; the California ADU statute (Gov. Code 66310 to 66342) and HCD's ADU handbook of March 2026."),
        ("The building code, both editions.", "", "Title 24 as published for 2022 (the edition that governs permits deemed complete before 2026) and 2025, part by part, so the answer names the edition that applies."),
    ],
    wont=[
        ("No permit records, no site survey.", "Whether a structure is nonconforming or a tree is protected is a project fact; the answer says which part is source retrieval and which part still needs plan-check confirmation."),
        ("No other cities, no case law.", "A question outside the collection is answered \"not in this corpus\", never from elsewhere."),
        ("The handout is not the ordinance.", "When a simplified sheet and the code differ, both are shown with their dates; the newer or higher authority is named, not assumed."),
        ("Verify before relying.", "docenta finds and cites; your assistant reads and you decide. For anything load-bearing, open the official text the citation points to."),
    ],
    rolewords="Your own plan sets, site photos, client mail and estimates",
    plug_html=plug("palo-alto", "door.docenta.ai", "docenta-palo-alto", "contractors"),
    subject_word="contractors",
)

# ---- lawyers (a fictional matter as the hero, the public door as the live proof)
PAGES["lawyers"] = dict(
    title="docenta for lawyers - ask the matter, cite the exhibit",
    desc="Pleadings, correspondence, scanned exhibits, contracts and notes become one private evidence layer. Reconstruct the chronology, find the version that changed, surface contradictions, map factual assertions to exact pages, without uploading the matter to a vendor cloud. Try the engine on the United States Code and public contracts, live.",
    placard='Exhibit · docenta for lawyers · The matter file <span class="live">live door: the federal code</span>',
    h1="Ask the matter. <em>Cite the exhibit.</em>",
    sub="Pleadings, correspondence, scanned exhibits, contracts and notes become one private evidence layer on your own machine. Reconstruct the chronology, find the version that introduced the clause, surface the contradiction between a declaration and the contemporaneous record, and map every factual assertion to an exact page, <strong>without first uploading the matter to anyone's cloud</strong>.",
    chip_qs=["Where does the other side first acknowledge this fact?", "Does this declaration conflict with an earlier email?", "Which version introduced this clause, and who sent it?", "Which exhibit supports each paragraph of the fact section?", "What can the matter file not establish?"],
    demo=answer(
        "when did the other side first know about the delivery delay, and is that consistent with paragraph 18 of their declaration, which says they learned of it on May 18?",
        "The indexed record holds two earlier communications. An <strong>April 29</strong> email to the declarant's address states that the shipment would miss the original date; its attached revised schedule gives May 12 as the new target. A <strong>May 3</strong> reply from that address acknowledges the revised schedule. Paragraph 18's statement that the declarant \"first learned\" of the delay on May 18 therefore conflicts with both records. docenta cannot establish who personally read the April 29 email without further evidence.",
        [("Mail · \"Re: PO 4471 shipment\" · 2024-04-29", "\"the shipment will not make the original date\"; sent to the declarant's address"),
         ("Attachment · revised-schedule-r2.pdf · 2024-04-29", "delivery moved to May 12"),
         ("Mail · \"Re: PO 4471 shipment\" · 2024-05-03", "the reply from that address: \"received the revised schedule\""),
         ("Exhibit 14 · Declaration of R. Lund, para. 18 (scan, OCR)", "\"I first learned of the delay on May 18\"")],
        "The declaration's date of knowledge versus two earlier communications in the same matter.",
        "Receipt at an address is not proof of personal reading; no read receipt and no testimony on that point is in the file. Open the original exhibits before using this in a filing.",
        "matter-file store · entity: the declarant · mail, attachments and scanned exhibits joined on the timeline · 4 sources kept, 9 dropped · 18 KB handed to the agent",
        "An illustration of the shape of an answer over a private matter: the parties and documents are made up; the behavior, the refusal to leap from \"sent\" to \"knew\" included, is docenta's. The live door below runs the same engine over public material you can try now.",
    ),
    extra_after_demo="""
    <div class="terminal" style="margin-top:34px" aria-label="A real answer from the live legal door">
      <div class="term-bar"><span class="dot r"></span><span class="dot"></span><span class="dot"></span><span class="term-title">live door · lawyers.docenta.ai · United States Code and public contracts</span></div>
      <div class="term-body">
        <div class="q">how long does copyright in a work made for hire last, and where does the Code say it?</div>
        <div class="lbl">Answer</div>
        <p class="ans">For a work created on or after January 1, 1978, a work made for hire is protected for <strong>95 years from first publication or 120 years from creation, whichever expires first</strong> (17 U.S.C. 302(c)). A work already under copyright on that date runs a renewal term to 95 years from when copyright was originally secured (17 U.S.C. 304), and the termination right over old transfers does not reach works made for hire (304(c)).</p>
        <div class="lbl">Evidence</div>
        <div class="ev"><span class="n">1.</span><span><span class="path">uscode/title-17/302.md</span> <span class="span">· 302(c): "a term of 95 years from the year of its first publication, or a term of 120 years from the year of its creation, whichever expires first"</span></span></div>
        <div class="ev"><span class="n">2.</span><span><span class="path">uscode/title-17/304.md</span> <span class="span">· 304(b): "a copyright term of 95 years from the date copyright was originally secured"; 304(c): "other than a copyright in a work made for hire"</span></span></div>
        <div class="box"><b>Conflict.</b> None found in the retrieved evidence.</div>
        <div class="box gap"><b>Gap.</b> This collection holds statutes and public contracts only: no case law, no 37 CFR, no Copyright Office circulars. What counts as a work made for hire in a given engagement is a question for the contract and the cases, not for this door.</div>
        <div class="route"><b>Evidence path</b> · lexical lane over the United States Code, 29 sections held every term · two sections of Title 17 kept · the House Office of the Law Revision Counsel's current text, cited to the section</div>
      </div>
    </div>
    <p class="term-note">A real answer from the live door, paths shortened: all 54 titles of the federal code, the recent public laws, and two open contract collections (CUAD and ContractNLI, CC BY 4.0), sealed on 2026-09-13.</p>
""",
    wall_groups=[
        ("Chronology", ["Build the chronology of notice, promise, performance and alleged breach from the matter file, with a source for every event.", "What is the earliest contemporaneous evidence of this fact?", "Which later-created summaries disagree with the contemporaneous record?"]),
        ("Acknowledgement", ["Where does opposing counsel first acknowledge this? Show the exact message and what was attached.", "Is there evidence the required notice, approval or consent was actually given, and when?"]),
        ("Versions", ["Which version of the agreement contains this clause, when was it introduced, and who sent that version?", "What changed between the counterparty's redline and the version we approved?", "Which executed version differs from the last circulated draft?"]),
        ("Contradiction", ["Does this declaration conflict with an earlier email or document?", "Where do our own internal notes conflict with the formal record?"]),
        ("Evidence and gaps", ["Which exhibit supports each paragraph in this fact section?", "Find every factual assertion in this draft that lacks a source in the matter file.", "Which scanned exhibits have uncertain OCR around names, amounts or dates and need visual review?"]),
    ],
    reads=[
        ("The matter.", "", "Pleadings, discovery, transcripts, contracts and their drafts, scanned exhibits with OCR and the scan itself, correspondence with attachments, your notes. All of it on your machine."),
        ("Mail as evidence.", "", "Threads stay threads and attachments stay attached, so \"the message where they agreed\" and \"what was attached to it\" are one answer, in order, with both sides."),
        ("The public material, live.", "", "All 54 titles of the United States Code, the recent public laws, and two open contract collections, sealed and served as a door your assistant can ask today."),
    ],
    wont=[
        ("Retrieval is not legal advice.", "docenta finds, cites and orders the record; the judgment about what it means is yours, and the original authorities are the ones you rely on."),
        ("Sent is not read.", "Receipt at an address is a fact the record can show; personal knowledge is not, unless a document says so. The answer keeps that line."),
        ("OCR is disclosed.", "A scanned exhibit whose text reads in visual order is marked as such: find it, do not quote it; render the page."),
        ("What the matter cannot establish is listed.", "\"Not established by the file as indexed\" is printed as an answer, with the searches that were run, so the missing exhibit has a name."),
    ],
    rolewords="The matter, the privileged notes and the client's mail",
    plug_html=plug("legal", "lawyers.docenta.ai", "docenta-legal", "lawyers"),
    subject_word="lawyers",
)

# ---- insurance
PAGES["insurance"] = dict(
    title="docenta for insurance - ask the claim, not the folders",
    desc="A claim is a story told by documents that rarely sit together. Ask the whole story: policy, first notice, notes, correspondence, estimates, scans and photo metadata become one evidence-backed timeline, with exact receipts, contradictions shown and missing evidence named. The claim file stays on your machine.",
    placard="Exhibit · docenta for insurance · The claim file",
    h1="A claim is a story told by documents that rarely sit together. <em>Ask the whole story.</em>",
    sub="\"What happened, when, according to whom, and what in the file proves it?\" docenta reconstructs the answer across policy, first notice, adjuster notes, correspondence, estimates, scans and the time and place inside the photos, with exact receipts and explicit gaps. <strong>Your claim file stays on your machine.</strong>",
    chip_qs=["Build the loss timeline", "Which policy version applies?", "What changed in the supplement?", "Which photos prove the condition?", "What evidence is missing?"],
    demo=answer(
        "was mold reported before mitigation began, and does the policy's mold sublimit apply to this loss?",
        "The earliest indexed report of visible mold is an email at <strong>9:12 on February 14</strong>, one day after the earliest damage photograph; six photos were attached. The policy in the claim folder carries a <strong>$10,000 fungi sublimit</strong> on page 12. The collection does <strong>not</strong> establish whether the mold resulted from the covered water event: the mitigation report that would support that causal link is not present.",
        [("IMG_2231.jpg · 2026-02-13 18:40", "EXIF timestamp; GPS matches the risk address; the earliest damage photograph"),
         ("Mail · \"Claim 44-1187 - basement water\" · 2026-02-14 09:12", "the first indexed message mentioning mold; six photos attached"),
         ("HO-3_2025.pdf · page 12", "fungi and mold sublimit, $10,000"),
         ("Adjuster note · 2026-02-15", "\"possible long-term seepage\"")],
        "The insured's email describes a sudden discovery; the adjuster's note the next day raises possible long-term seepage. Both are on the timeline, neither is preferred.",
        "No mitigation or industrial-hygiene report is in the file to establish cause or duration. Next human check: confirm the policy form and endorsements are complete and apply to the date of loss.",
        "claim store · photo metadata, mail, policy PDF and notes on one timeline · ordered by capture and send time · 4 sources kept, 12 dropped",
        "An illustration of the shape of an answer. The claim is made up; the behavior, timeline reconstruction from image metadata, policy retrieval, the contradiction and the disciplined non-inference, is docenta's.",
    ),
    wall_groups=[
        ("Timeline", ["Build the claim timeline from first notice through the latest supplement; cite every event.", "When was the first mention of mold, water intrusion or roof damage, and by whom?", "What happened between inspection and the denial, approval or payment?"]),
        ("Which version", ["Which policy version was in force on the date of loss, and what exact sublimit or exclusion language applies?", "Which estimate is the latest, and which earlier numbers does it replace?"]),
        ("Photos as evidence", ["Which photos were actually taken before mitigation began, and what do their timestamps and locations show?", "Which photographs have no usable timestamp or location metadata?"]),
        ("Contradiction", ["What did the insured report first, and do later descriptions conflict with it?", "Are there different loss dates in the FNOL, the mail, the photos, the notes and the invoices?"]),
        ("Evidence and gaps", ["What evidence supports each disputed line item, and what is still missing?", "Which request for documents is still unanswered?", "What facts in the claim summary are not supported by the indexed file?"]),
    ],
    reads=[
        ("The policy and the notice.", "", "The policy and its endorsements, the first notice of loss, the forms; each version kept with its date so \"in force on the date of loss\" is a question the file can answer."),
        ("Notes, mail and estimates.", "", "Adjuster notes, correspondence with attachments in order, the carrier estimate and every supplement, invoices tied to the message that discussed them."),
        ("Photos and scans.", "", "Image metadata (time, location) read and kept on the timeline; scanned pages and PDFs with OCR, and the extraction warned about when the text order is unreliable."),
    ],
    wont=[
        ("A timestamp is not causation.", "A photo proves when and where it was taken. Whether the condition it shows was caused by the covered event is a finding the file must contain, or the answer says it does not."),
        ("First reported is not first occurred.", "The earliest indexed mention is dated and cited as such; the answer never turns it into the date of loss."),
        ("Missing documents are named.", "The mitigation report, the endorsement schedule, the signed authorization: what a reviewer would need and the file lacks is listed, not glossed."),
        ("Nothing decides coverage.", "docenta assembles the record with receipts; the coverage position is yours."),
    ],
    rolewords="The claim file, the policy and the insured's photos",
    plug_html="",
    subject_word="insurance",
)

# ---- home
PAGES["home"] = dict(
    title="docenta for home - your files remember what you forgot",
    desc="You remember the event. Your computer remembers the evidence. Ask twenty years of mail, documents and photos in plain English: the receipt tied to the warranty, the quote that replaced the old quote, the photo from that day, the letter you half remember, with the exact source and an honest not-found. It never leaves your computer.",
    placard="Exhibit · docenta for people · A life in files",
    h1="You remember the event. <em>Your computer remembers the evidence.</em>",
    sub="\"Which contractor gave us the lower roof quote?\" \"Where is the dishwasher warranty?\" \"Find the tax letter from around 2019.\" Ask naturally across mail, documents and photos. docenta answers from your own history, cites the proof, and says \"not in the collection\" when it is not there. <strong>It never leaves your computer.</strong>",
    chip_qs=["Is the dishwasher still under warranty?", "Which quote did the roofer say would stand?", "Find the tax letter from around 2019", "Which insurance policy was current when this happened?", "What proof am I missing for this repair?"],
    demo=answer(
        "is the dishwasher still under warranty, and do I have everything needed to make a claim?",
        "The purchase receipt is dated <strong>October 21, 2024</strong> and names model DW-4820. The warranty PDF states two years of parts and labor from purchase, which puts the end of ordinary coverage at October 21, 2026 if that term applies. A March 2026 service email documents an earlier pump failure. The collection holds the receipt, the warranty and the model number, but <strong>no serial-number photo and no registration confirmation</strong>.",
        [("Mail · \"Your order 7731-A\" · 2024-10-21", "the receipt: model DW-4820, the amount, the store"),
         ("~/Documents/house/dw-4820-warranty.pdf · page 2", "\"two (2) years parts and labor from the date of purchase\""),
         ("Mail · \"Service visit confirmation\" · 2026-03-04", "the pump failure and the visit")],
        None,
        "No serial-number photo and no registration email were found. The dates are shown as the sources state them; the arithmetic is yours to check, not a hidden conclusion.",
        "home store · receipt, warranty and service thread joined on the model number · 3 sources kept, 6 dropped",
        "An illustration of the shape of an answer. The files are made up; the behavior is docenta's, including the part where it tells you what is missing before you call the manufacturer.",
    ),
    wall_groups=[
        ("Find it", ["Find the receipt and the manual for this model even though I do not remember the filename.", "Find the photo from the trip where the car broke down and show the date and place if the photo has them.", "Which documents mention this serial number, account or reference number?"]),
        ("Quotes and promises", ["What did the roofer first quote, what was the revised amount, and which number did they say would stand?", "Which contractor promised to do this, for what price, and by when?", "Did the contractor ever send the final invoice after the revised estimate?"]),
        ("Which version", ["Which version of the home insurance policy is newest, and which was in force when the leak happened?", "Do I have a signed final contract, or only drafts?"]),
        ("Timeline", ["When did we buy, replace and service the HVAC, and what records do we have?", "Put every document about the kitchen remodel in date order."]),
        ("Evidence and gaps", ["What do my files prove about when this item was purchased, installed or repaired?", "Which records would I need for this warranty or tax question that are not in my collection?", "Did we ever get written confirmation of the agreement I remember?"]),
    ],
    reads=[
        ("Plain words work.", "", "Ask the way you would ask a friend who read everything. docenta corrects spelling against your own files and tells you when it dropped a word to find an answer."),
        ("Your mail, past and present.", "", "Bring the mailbox export in once; from then on docenta fetches new mail on its own, every hour, from a key you make in four steps. Your real password is never typed anywhere."),
        ("Photos and documents.", "", "The time and place inside a photo, the text inside a scan, the attachment inside a thread. Twenty years of it, on a normal Mac or PC; the heavy work runs at night or on a rented GPU for an hour with your say-so."),
    ],
    wont=[
        ("Honest when it does not know.", "If the answer is not in your files, docenta says \"not in the collection\" and shows what it did find. No invented facts about your own life."),
        ("Dates are quoted, not computed in secret.", "A warranty end date is shown as the receipt date plus the term the document states; you see both and check the sum."),
        ("Drafts are not the signed copy.", "When the final signed document is not in the collection, the answer says so instead of presenting the last draft as the deal."),
        ("Nothing leaves the house.", "Medical, school and money paperwork is indexed on your computer or not at all; there is no cloud copy to worry about."),
    ],
    rolewords="Your household folders, your mail and your photos",
    plug_html="",
    subject_word="home",
)

# ---- email
PAGES["email"] = dict(
    title="docenta for mail - ask what was said, not what the subject line was",
    desc="You remember the conversation. docenta finds the thread, the attachment and the exact line. Ask a large mailbox by meaning, chronology, sender, date, numbers and what was agreed. Threads stay threads; attachments stay attached; the answer stays inspectable.",
    placard="Exhibit · docenta for mail · The mailbox",
    h1="You remember the conversation. <em>docenta finds the thread, the attachment and the exact line.</em>",
    sub="Ask a large mailbox by meaning, chronology, sender, date, numbers and what was agreed, even when you remember the promise and not the subject line. An export in an evening, the live mailbox from then on. <strong>Threads stay threads; attachments stay attached; the answer stays inspectable.</strong>",
    chip_qs=["Find the thread where they agreed to pay", "What was the last delivery date they committed to?", "Which attachment is actually the final version?", "Which question in this thread never got answered?", "Find the email even though I forgot the sender and subject"],
    demo=answer(
        "what was the final delivery date Acme committed to, and did they ever revise it again?",
        "Acme first proposed <strong>September 8</strong>, moved it to <strong>September 15</strong> in an August 21 email, and confirmed September 15 again in the revised schedule attached on August 22. No later message or attachment in the indexed mailbox changes that date. A September 10 email says the team is \"still on track\" and introduces no new date.",
        [("Mail · \"Delivery plan\" · 2026-08-14 · from Acme", "\"we are targeting September 8\""),
         ("Mail · \"Re: Delivery plan\" · 2026-08-21 · from Acme", "\"we need to move this to September 15\""),
         ("Attachment · schedule-r2.xlsx · 2026-08-22", "row 14: delivery, 15 Sep"),
         ("Mail · \"Re: Delivery plan\" · 2026-09-10 · from Acme", "\"still on track\"; no date")],
        None,
        "No acknowledgement from our side of the September 15 date is in the mailbox; if that matters, it is missing, not implied.",
        "mail store · thread reconstructed from both sides · attachments read, not just named · four messages kept in order, 21 dropped",
        "An illustration of the shape of an answer. The thread is made up; the behavior, both sides in order, the attachment read as evidence, the quiet message that changes nothing, is docenta's.",
    ),
    wall_groups=[
        ("Find it", ["Find the email I remember by meaning even though I forgot the sender and the subject.", "Find the attachment sent around the time we discussed this.", "Which messages mention the same reference number even when it is written differently?"]),
        ("Agreement", ["Find the thread where the landlord agreed to cover the repair and the invoice attached later.", "Show the exact message where they approved this.", "Was the final number in the attachment ever acknowledged in the thread?"]),
        ("Versions and dates", ["Who first proposed this price, date or term, and when was it changed?", "Which attachment is the latest version, and which message sent it?", "Did someone retract or qualify an earlier promise?"]),
        ("In order", ["Build the timeline of this thread, both sides and attachments included.", "What was the last message on this topic before the project went quiet?", "What did this person say about this across several threads over two years?"]),
        ("Evidence and gaps", ["Which open questions in this thread never received an answer?", "What did the message say versus what the attached PDF said?", "What cannot be established because part of the thread or the attachments is missing?"]),
    ],
    reads=[
        ("The export, then the live mailbox.", "", "A Takeout or mbox in an evening, then a live IMAP tail every hour from an app password kept in the OS store. Trash and spam included, so nothing is invisible."),
        ("Fields that answer.", "", "From, to, subject, date, labels, thread: query fields that narrow like a database, and a \"latest first\" that never relaxes the question to fit an answer."),
        ("Attachments as members.", "", "A PDF inside a message is a document of its own, still tied to the message that carried it, so the invoice and the promise are one chain."),
    ],
    wont=[
        ("Meaning search is disclosed.", "When a term is not in your mailbox, docenta says which word it dropped or respelled to find the page; a relaxed answer is labelled as one."),
        ("Received is not read.", "A message at an address is a fact; that a person read it is not, unless a reply says so."),
        ("The quiet message is not a change.", "\"Still on track\" carries no date and is cited as carrying none."),
        ("Missing halves are named.", "A thread whose other side or attachment is not in the mailbox is reported as incomplete, with what is there."),
    ],
    rolewords="Your mailbox, its attachments and its history",
    plug_html="",
    subject_word="mail",
)

# ---- developers
PAGES["developers"] = dict(
    title="docenta for developers - ask why the code is this way",
    desc="Your codebase has history. Your agent should be able to remember it. Ask why is this here, what did we already try, when did we make this decision, across code, commits, docs and previous agent sessions. docenta returns the small set of evidence the next agent needs, with exact citations and a disclosed token budget, over MCP.",
    placard="Exhibit · docenta for developers · Repos and sessions",
    h1="Your codebase has history. <em>Your agent should be able to remember it.</em>",
    sub="Ask \"why is this here?\", \"what did we already try?\" or \"when did we decide this?\" across code, commits, design notes and every previous agent session. docenta hands the next agent the <strong>small set of evidence it needs</strong>, with exact citations and a disclosed token budget, over MCP, instead of the whole repository.",
    chip_qs=["Why does this guard exist?", "What did we try before this, and why did it fail?", "Which agent session introduced this pattern?", "Where do the README, the code and git history disagree?", "What should the next agent read before touching this module?"],
    demo=answer(
        "when did we decide to split the sparse encode from the index step, and why?",
        "On <strong>17 September 2026</strong>, in the design record, on the numbers from the winbox rebuild: of the 13,176 seconds the serial index apply spent, about 13,150 were 13,154 calls into the sparse encoder, so the lexical index of 7.5 million representations was hostage to one model lane. That reversed the decision of <strong>4 September</strong> (commit b4f63231), which had put a measured gate on the encode inside the index step after one 2,675-unit batch took 86 minutes on an Intel laptop. The split landed the same day as commit ebffa66b: the index step never encodes, and a new sparse step back-fills.",
        [("docs/architecture/sparse-split-2026-09-17.md", "\"The measurement that decided it\": 13,176 s of apply, about 13,150 s in 13,154 encoder calls"),
         ("git · b4f63231 · 2026-09-04", "\"the index step measures its sparse encode and stops at the line\": \"one 2,675-unit batch took 86 minutes\""),
         ("git · ebffa66b · 2026-09-17", "\"the index step indexes bare units and counts them, the encoder and the gate leave the index write path\""),
         ("agent session · 2026-09-17", "the winbox log and the ledger rows that produced the numbers")],
        "None: the 4 September record is superseded, not contradicted; the 17 September record names it.",
        "The pack ranks the sources and dates them; it does not yet flag a reversed decision as a version change on its own. The dates do.",
        "lexical, semantic and git lanes · design record, two commits, the session and the changelog · 16 sources kept of 28 · 1,082 tokens handed to the agent",
        "Real, from the maker's own corpus, answered today: the design record, the git history and the agent session that made the decision are one collection over MCP, and the docent answers from all of it. This is how the maker's own coding agents work; the grep comparison below is the measurement.",
    ),
    wall_groups=[
        ("Why", ["Why does this guard or workaround exist? Show the bug, incident, commit or session that introduced it.", "Why was this dependency chosen over the other one?", "Which incident or benchmark caused this retry, cache or timeout behavior?"]),
        ("What we tried", ["What did we try before this design, and why did we reject it?", "Find previous attempts to fix this bug and say why each failed, with citations.", "What did the previous agent already investigate about this failing test?"]),
        ("When", ["When did we decide to switch the importer to streaming, and why?", "Which commit changed this schema or API, and what discussion explains it?", "What is the last known-good commit before this regression, and what changed right after?"]),
        ("Contradiction", ["Where do the docs, the code, git history and agent sessions disagree about intended behavior?", "Which TODO or comment is stale against later code and decisions?"]),
        ("Evidence and gaps", ["What context should a fresh coding agent read before modifying this subsystem?", "Which design note states the invariant this function is supposed to preserve?", "What can the current corpus not explain about this code path?"]),
    ],
    reads=[
        ("Code and git.", "", "Every repository with its history: the commit that introduced the line, the files that change together, the message that explained it. Code-aware lanes, identifiers as terms."),
        ("Notes and docs.", "", "Design notes, incident write-ups, READMEs and architecture records, cited to the line, so the invariant a function protects has a source."),
        ("Every agent session.", "", "Claude Code, Codex and ChatGPT sessions rendered and indexed as they happen, so what the last agent learned is one search away for the next, and a compaction loses nothing."),
    ],
    wont=[
        ("A session explains; it can be stale.", "An agent's reasoning from February is cited with its date; a later commit that changed the code outranks it, and the answer says which is newer."),
        ("grep is not replaced, it is measured.", "On the maker's judged sets docenta's top-10 found 114 of 227 targets to ripgrep's 44, reading about 20 KB to the truth instead of 2.8 MB. The numbers are printed, the arm is committed."),
        ("Absent rationale is reported absent.", "\"No design record in the corpus explains this\" is an answer, and a useful one before the next rewrite."),
        ("The budget is on every answer.", "How many tokens the agent was handed, and what was dropped to stay inside them."),
    ],
    rolewords="Private source trees, incident notes and agent transcripts",
    plug_html="",
    subject_word="developers",
)

# ---- researchers
PAGES["researchers"] = dict(
    title="docenta for researchers - ask your library where it disagrees",
    desc="You do not need another paper search. You need your own library to answer back. Ask across PDFs, notes, drafts and co-author mail: where did I read this, which studies disagree, does this draft sentence have support. docenta returns the exact evidence and the conflicts without sending your library away.",
    placard="Exhibit · docenta for researchers · The reading pile",
    h1="You do not need another paper search. <em>You need your own library to answer back.</em>",
    sub="Ask across PDFs, scans, notes, drafts and co-author mail: \"Where did I read this?\", \"Which studies disagree?\", \"Does this sentence in my draft have support?\" docenta returns the exact page and the conflicts, in the language you ask or the one the paper was written in, <strong>without sending your library anywhere</strong>.",
    chip_qs=["Where did I read that claim?", "Which papers in my library support it, and which contradict it?", "Which source supports this sentence in my draft?", "What did my own notes say after the replication?", "What question remains unanswered by the papers I have?"],
    demo=answer(
        "which papers in my library support a low-dose effect, which fail to replicate it, and does my draft overstate the evidence?",
        "Two indexed papers report a low-dose effect; one later replication reports <strong>no effect below a higher threshold</strong>. Your current draft sentence says the effect is \"consistently observed\", which the three papers retrieved do not support. Your journal-club note of May 2024 already flags the dose-response as unresolved.",
        [("library/Okafor-2021.pdf · page 7, table 3", "effect at the low dose, n = 42"),
         ("library/Brandt-2022.pdf · page 4", "effect at the low dose, different assay"),
         ("library/Lindqvist-2024-replication.pdf · page 9", "\"no effect below 12 mg/kg\""),
         ("notes/journal-club-2024-05.md · line 31", "\"dose-response still unresolved; L. replication pending\""),
         ("drafts/review-v3.docx · para 12", "\"the low-dose effect is consistently observed\"")],
        "Two papers versus one replication on the threshold; the draft sentence versus the retrieved evidence.",
        "Retrieval alone performs no meta-analysis or pooling; the three studies are shown, not weighed. One PDF in the library is flagged: its text reads in visual order and is cited by page, not quoted.",
        "dense and lexical lanes, cross-language · papers, notes and the draft on one timeline · 5 sources kept, 23 dropped",
        "An illustration of the shape of an answer. The papers are made up; the behavior is docenta's: it does not pretend to know the science, it proves what your chosen corpus says.",
    ),
    wall_groups=[
        ("Find it", ["I know I read that this works at low dose; where did I read it, and what did the paper actually say?", "Which paper used this dataset, method, instrument or sample size?", "Find the German or French paper that discusses this even though I asked in English."]),
        ("Support", ["Which sources in my library support this sentence in my draft? Give exact pages.", "Which citations in this draft do not appear to support the sentence they are attached to?", "What claim in my draft currently has no source in the library?"]),
        ("Disagreement", ["Which sources contradict my current conclusion?", "Where do papers use the same term differently?", "Which papers share a result but disagree about mechanism?"]),
        ("Over time", ["What is the earliest paper in my collection making this claim, and which later replications failed?", "Did my interpretation change after the later replication or the co-author's email? Show my notes in order."]),
        ("Evidence and gaps", ["Which papers cite the same underlying experiment rather than providing independent evidence?", "What evidence would I need to distinguish these two explanations, and do I have it?", "What question remains unresolved across the papers I have?"]),
    ],
    reads=[
        ("The pile.", "", "Thousands of PDFs and scans, with OCR where needed and a warning where the text order is unreliable; every claim cited to the page."),
        ("Your notes and drafts.", "", "Reading notes, journal-club notes and the manuscript in progress, so \"what did I think at the time\" and \"is this sentence supported\" are questions the library answers."),
        ("Co-author mail.", "", "The thread where the replication was discussed, the attachment with the figure, in order, tied to the papers it talks about."),
    ],
    wont=[
        ("It does not know the science.", "docenta proves what your saved sources say; it does not establish truth outside them and it performs no statistics on retrieval alone."),
        ("A citation is checked, not trusted.", "Whether the cited page says what the sentence claims is a question the answer takes literally."),
        ("Unreliable extraction is flagged.", "A PDF whose text reads in visual order is marked: find it, cite the page, do not quote it."),
        ("The unanswered question is listed.", "What the collection does not settle is printed with the searches that were run, so the next paper to read has a name."),
    ],
    rolewords="The unpublished draft, the annotated PDFs and the co-author threads",
    plug_html="",
    subject_word="researchers",
)

def main():
    written = []
    path = os.path.join(ROOT, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(index_page())
    written.append(path)
    for slug, spec in PAGES.items():
        d = os.path.join(ROOT, "for", slug)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(specialty(slug, **spec))
        written.append(path)
    for p in written:
        print("wrote", os.path.relpath(p, ROOT))

if __name__ == "__main__":
    main()
