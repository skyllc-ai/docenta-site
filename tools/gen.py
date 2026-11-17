#!/usr/bin/env python3
# The docenta.ai pages, generated from one copy source.
# Run from the site root: python3 tools/gen.py  (writes index.html, for/*/index.html, privacy/ and terms/)
# Copy follows docs/go-to-market/positioning-and-question-library-2026-09-17.md
# in the docenta repo: pain before mechanism, questions as the hero content,
# every answer shown as answer + evidence + conflicts + gaps + evidence path.
import html, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGE = os.path.join(ROOT, "tools", "page")
_SRC = os.path.join(os.path.dirname(ROOT), "docenta", "crates", "docenta-page", "src")
def _sync_page():
    """tools/page/ holds COPIES of the shared layer from the docenta repo
    (crates/docenta-page/src). With the sibling checkout present they are
    refreshed on every run, so the site cannot drift from the product."""
    os.makedirs(PAGE, exist_ok=True)
    for name in ("tokens.css", "theme.js", "glyph.svg"):
        src = os.path.join(_SRC, name)
        if os.path.isfile(src):
            with open(src) as f: text = f.read()
            with open(os.path.join(PAGE, name), "w") as f: f.write(text)
_sync_page()
def _page(name):
    with open(os.path.join(PAGE, name)) as f: return f.read()
TOKENS, THEME_JS, GLYPH = _page("tokens.css"), _page("theme.js"), _page("glyph.svg").strip()
THEME_BUTTON = '<button id="theme" class="btn icon" type="button" title="Theme"><svg class="sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="moon" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="auto" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg></button>'

CSS = r"""
  /* docenta.ai takes the shared tokens-and-chrome layer (tools/page/tokens.css,
     synced from the docenta repo) and keeps its own editorial layout below,
     written in the shared token names so both themes work. */
  .bar-in{max-width:1060px}

  body{font-size:17px;line-height:1.6}
  .mono{font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
  .wrap{max-width:1060px;margin:0 auto;padding:0 24px}
  .nav-cta{font-family:'JetBrains Mono',monospace;font-size:14px;background:var(--accent-2);padding:10px 18px;border-radius:8px;font-weight:700;color:#fff}
  .nav-cta:hover{background:var(--accent-3);color:#fff;text-decoration:none}
  /* Plain prose pages (privacy, terms): the same chrome, running text. */
  .prose{max-width:720px}
  .prose h2{font-size:clamp(22px,2.8vw,28px);margin-top:48px}
  .prose h3{font-size:18px;font-weight:700;margin-top:28px;margin-bottom:6px}
  .prose p{margin-top:14px;color:var(--text)}
  .prose ul{margin:12px 0 0 22px}
  .prose li{margin-top:8px}
  .prose code{font-family:var(--mono);font-size:14px;background:var(--code);padding:1px 6px;border-radius:5px}
  .prose .eff{color:var(--text-2);font-size:14px;margin-top:10px}
  .placard{font-family:'JetBrains Mono',monospace;font-size:12.5px;letter-spacing:.18em;color:var(--label);text-transform:uppercase;display:flex;align-items:center;gap:14px;margin-bottom:22px;flex-wrap:wrap}
  .placard::before{content:"";display:inline-block;width:34px;height:1px;background:var(--label);opacity:.6}
  header{padding:56px 0 30px}
  h1{font-weight:800;font-size:clamp(38px,6.4vw,64px);line-height:1.04;letter-spacing:-.03em;max-width:860px;text-wrap:balance}
  h1 em{font-style:normal;color:var(--accent)}
  .sub{color:var(--text-2);font-size:clamp(17px,2vw,21px);max-width:680px;margin:26px 0 10px}
  .sub strong{color:var(--text);font-weight:600}
  /* the prompt rail: what people actually say */
  .chips{display:flex;flex-wrap:wrap;gap:10px;margin:26px 0 6px}
  .chip{font-family:'JetBrains Mono',monospace;font-size:13.5px;color:var(--text);background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:8px 14px}
  .chip::before{content:"\275D ";color:var(--accent)}
  .chip:hover{border-color:var(--accent);text-decoration:none}
  /* the answer, shown as it is reconstructed */
  .terminal{--bg:#0F0D0B;--surface:#1E1B18;--text:#F2EDE8;--text-2:#9A8D82;--line:#2C2620;--line-2:#3A332C;--accent:#F7B26B;--accent-2:#CE422B;--label:#DEA584;color:var(--text);margin:44px 0 8px;background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:0 24px 60px rgba(0,0,0,.55);overflow:hidden}
  .term-bar{display:flex;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid var(--line)}
  .dot{width:11px;height:11px;border-radius:50%;background:var(--line-2)}
  .dot.r{background:var(--accent-3)}
  .term-title{margin-left:8px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--text-2)}
  .term-body{padding:22px 24px 26px;font-family:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;font-size:14px;line-height:1.7}
  .q{color:var(--text);margin-bottom:14px}
  .q::before{content:"\276F ";color:var(--accent)}
  .ans{font-family:Inter,'Segoe UI',system-ui,sans-serif;font-size:16px;line-height:1.6;color:var(--text);margin:0 0 16px;max-width:820px}
  .ans strong{color:var(--accent);font-weight:600}
  .lbl{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--label);margin:14px 0 6px}
  .ev{display:grid;grid-template-columns:22px 1fr;gap:8px;color:var(--text);margin:4px 0}
  .ev .n{color:var(--accent)}
  .ev .path{color:var(--accent)}
  .ev .span{color:var(--text-2)}
  .box{border-left:3px solid var(--label);padding:6px 12px;margin:8px 0;color:var(--text);font-family:Inter,'Segoe UI',system-ui,sans-serif;font-size:15px}
  .box.conflict{border-color:var(--accent-2)}
  .box.gap{border-color:var(--text-2)}
  .box b{color:var(--label);font-weight:600}
  .route{color:var(--text-2);font-size:13px;margin-top:10px}
  .route b{color:var(--text);font-weight:600}
  .term-note{font-family:'JetBrains Mono',monospace;font-size:12.5px;color:var(--text-2);margin:14px 2px 0}
  section{padding:72px 0 8px}
  h2{font-weight:800;font-size:clamp(26px,3.6vw,38px);letter-spacing:-.02em;max-width:760px;text-wrap:balance}
  .lead{color:var(--text-2);max-width:680px;margin-top:16px}
  .lead strong{color:var(--text);font-weight:600}
  .cols{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}
  .cols.two{grid-template-columns:repeat(2,1fr)}
  .card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:26px 24px}
  .card h3{font-size:18px;font-weight:700;letter-spacing:-.01em;margin-bottom:10px}
  .card h3 .k{color:var(--accent)}
  a.card{display:block;color:inherit;text-decoration:none;transition:border-color .15s ease,transform .15s ease}
  a.card:hover,a.card:focus-visible{border-color:var(--accent);transform:translateY(-2px);outline:none}
  a.card:focus-visible{box-shadow:0 0 0 2px var(--accent)}
  a.card h3::after{content:"\00a0\2192";color:var(--accent);font-weight:400}
  a.card.wide{grid-column:1 / -1;display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center;border-color:var(--label)}
  a.card.wide .live{margin:0;white-space:nowrap}
  @media (max-width:820px){a.card.wide{grid-template-columns:1fr}}
  .card p{color:var(--text-2);font-size:15.5px}
  .card p code{font-family:'JetBrains Mono',monospace;font-size:13.5px;color:var(--label)}
  .card .qs{margin-top:12px;color:var(--label);font-family:'JetBrains Mono',monospace;font-size:12.5px;line-height:1.7}
  /* the prompt wall, grouped by job */
  .wall{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:36px}
  .wall .g h4{font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--label);margin-bottom:10px}
  .wall .g p{color:var(--text);font-size:14.5px;line-height:1.5;margin-bottom:10px;padding-left:14px;text-indent:-14px}
  .wall .g p::before{content:"\275D ";color:var(--accent)}
  @media (max-width:980px){.wall{grid-template-columns:repeat(2,1fr)}}
  @media (max-width:560px){.wall{grid-template-columns:1fr}}
  /* jobs, not brands */
  table.jobs{width:100%;border-collapse:collapse;margin-top:34px;font-size:15.5px}
  table.jobs th{text-align:left;font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--label);padding:0 14px 12px 0;font-weight:600}
  table.jobs td{padding:12px 14px 12px 0;border-top:1px solid var(--line);vertical-align:top;color:var(--text-2)}
  table.jobs td:last-child{color:var(--text)}
  .tablewrap{overflow-x:auto}
  /* the receipts motif */
  .receipts{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:34px}
  .receipts div{border:1px dashed var(--label);border-radius:10px;padding:16px 14px;background:linear-gradient(180deg,var(--surface),var(--bg))}
  .receipts b{display:block;font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:8px}
  .receipts span{color:var(--text-2);font-size:14px;line-height:1.5}
  @media (max-width:980px){.receipts{grid-template-columns:repeat(2,1fr)}}
  .limits{margin-top:30px;max-width:760px}
  .limits p{padding:10px 0;border-top:1px solid var(--line);color:var(--text-2)}
  .limits p b{color:var(--text);font-weight:600}
  .plaque{margin-top:44px;border:1px solid var(--label);border-radius:12px;padding:8px 0;background:linear-gradient(180deg,var(--surface),var(--bg))}
  .plaque-title{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--label);text-align:center;padding:18px 0 6px}
  .plaque-grid{display:grid;grid-template-columns:repeat(5,1fr);padding:10px 10px 20px}
  .stat{padding:14px 10px;text-align:center;border-left:1px solid var(--line)}
  .stat:first-child{border-left:none}
  .stat b{display:block;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:clamp(18px,2.4vw,26px);color:var(--accent);letter-spacing:-.02em}
  .stat span{font-size:12.5px;color:var(--text-2);display:block;margin-top:6px;line-height:1.45}
  .plaque-foot{font-size:12px;color:var(--text-2);text-align:center;padding:0 20px 16px}
  .spine{margin-top:40px;font-family:'JetBrains Mono',monospace;font-size:14px;line-height:2.05;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:26px 28px;color:var(--text-2);overflow-x:auto}
  .spine b{color:var(--text);font-weight:600}
  .spine .a{color:var(--accent)}
  .steps{counter-reset:step;margin-top:34px;display:grid;gap:18px;max-width:760px}
  .step{display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:start}
  .step::before{counter-increment:step;content:counter(step);width:38px;height:38px;border-radius:50%;border:1px solid var(--label);color:var(--accent);font-family:'JetBrains Mono',monospace;font-weight:700;display:flex;align-items:center;justify-content:center}
  .step h3{font-size:18px;font-weight:700;letter-spacing:-.01em;margin-bottom:6px}
  .step p{color:var(--text-2);font-size:15.5px}
  .step p strong{color:var(--text);font-weight:600}
  pre.cmd{margin-top:12px;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-family:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;font-size:13.5px;color:var(--text);overflow-x:auto;white-space:pre;line-height:1.6}
  pre.cmd .a{color:var(--accent)}
  .soon{display:inline-block;margin-left:10px;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--label);border:1px solid var(--label);padding:2px 8px;border-radius:6px;vertical-align:middle;white-space:nowrap}
  .status{margin-top:26px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;max-width:760px}
  .status div{border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:14px;color:var(--text-2)}
  .status div b{display:block;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--label);margin-bottom:6px}
  .status div.done{border-color:var(--label);color:var(--text)}
  @media (max-width:640px){.status{grid-template-columns:repeat(2,1fr)}}
  .key{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:.92em;color:var(--bg);background:var(--accent);padding:1px 7px;border-radius:5px;white-space:nowrap}
  .live{display:inline-block;margin-left:10px;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--bg);background:var(--accent);padding:3px 8px;border-radius:6px;vertical-align:middle}
  a.live:hover,a.live:focus-visible{background:var(--text);text-decoration:none}
  .cta{margin:84px 0 0;padding:56px 40px;text-align:center;background:linear-gradient(180deg,var(--surface),var(--bg));border:1px solid var(--line);border-radius:16px}
  .cta h2{max-width:none}
  .cta p{color:var(--text-2);margin:16px auto 30px;max-width:560px}
  .cta-btn{display:inline-block;background:var(--accent-2);color:#fff;font-weight:700;font-size:17px;padding:15px 34px;border-radius:10px}
  .cta-btn:hover{background:var(--accent-3);color:#fff;text-decoration:none}
  .cta .alt{display:block;margin-top:18px;font-size:14px;color:var(--text-2)}
  .ea{margin:30px auto 0;max-width:640px;text-align:left}
  .ea-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .ea label{display:block;font-size:13.5px;color:var(--text-2);margin-bottom:14px}
  .ea input,.ea select,.ea textarea{display:block;width:100%;margin-top:6px;padding:11px 12px;border-radius:8px;background:var(--bg);border:1px solid var(--line);color:var(--text);font:inherit;font-size:15.5px}
  .ea input:focus,.ea select:focus,.ea textarea:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
  .ea textarea{resize:vertical;min-height:84px}
  .ea-turnstile{margin:6px 0 16px;min-height:0}
  .ea .cta-btn{border:0;cursor:pointer;font-family:inherit}
  .ea .cta-btn[disabled]{opacity:.6;cursor:wait}
  .ea-status{margin-top:14px;font-size:14.5px;color:var(--text);min-height:1.4em}
  .ea-status a{color:var(--accent)}
  .ea-hp{position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden}
  .ea-done{margin:18px auto 0;max-width:560px;padding:22px 26px;border:1px solid var(--accent);border-radius:10px;text-align:left}
  .ea-done h3{margin:0 0 8px;font-size:20px}
  .ea-done p{margin:0;font-size:15px;line-height:1.55;color:var(--text)}
  @media (max-width:640px){.ea-grid{grid-template-columns:1fr}}
  footer{margin-top:80px;padding:34px 0 44px;border-top:1px solid var(--line);color:var(--text-2);font-size:13.5px}
  footer .frow{display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}
  footer a{color:var(--label)}
  @media (max-width:820px){
    .cols,.cols.two{grid-template-columns:1fr}
    .plaque-grid{grid-template-columns:repeat(2,1fr)}
    .stat{border-left:none;border-top:1px solid var(--line)}
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
    ("judaism", "Judaism: Tanakh, Mishnah, Talmud and commentary (live door)"),
    ("christianity", "Christianity: scripture and classical commentary (live door)"),
    ("islam", "Islam: the Koran in six translations and Arabic, and the hadith (live door)"),
    ("faith", "Faith: the three traditions together (live door)"),
    ("sleep", "Sleep research: the open corpus (live door)"),
    ("diabetes", "Diabetes research: the open corpus (in collection)"),
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
<style>{TOKENS}{CSS}</style>
<script>{THEME_JS}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="bar"><div class="bar-in"><a class="brand" href="/">{GLYPH}docenta</a><span class="grow"></span><a class="nav-cta" href="#access">request early access</a>{THEME_BUTTON}</div></div>
<div class="wrap" id="main">
"""

FOOT = """
  <footer>
    <div class="frow">
      <div>docenta is a product of SKY, LLC. From the makers of <a href="https://uffs.io">UFFS</a>, the open-source NTFS search engine.</div>
      <div>docenta 0.3.4, November 2026. Built in Rust. Runs on macOS, Windows, Linux. &middot; <a href="/handbook/">Handbook</a> &middot; <a href="/privacy/">Privacy</a> &middot; <a href="/terms/">Terms</a></div>
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
    <p class="lead" style="margin-top:14px">It gets it over MCP, the connector standard Claude, ChatGPT and most coding assistants speak, from a server that <strong>runs on your own machine</strong>: the agent talks to a local process, not to a URL in someone's cloud. The only remote MCP addresses on this site are the public doors, sealed collections hosted on purpose; your own collection never has one. Deterministic layers, no learned model in the retrieval loop, bit-stable re-runs.</p>
  </section>
"""

def plug(name, host, mcp_name, word, placard="Plug the collection into your assistant", h2="One address, one sign-in, every question cited.", lead=None):
    # No key anywhere: the door is an OAuth protected resource (docenta repo,
    # docs/architecture/door-authorization-plan-2026-09.md). A person adds
    # the address; the assistant opens our sign-in page by itself.
    import base64, json, urllib.parse
    url = f"https://{host}/mcp"
    cursor = "cursor://anysphere.cursor-deeplink/mcp/install?name=" + urllib.parse.quote(mcp_name) + "&config=" + base64.b64encode(json.dumps({"url": url}, separators=(",", ":")).encode()).decode()
    vscode = "vscode:mcp/install?" + urllib.parse.quote(json.dumps({"name": mcp_name, "type": "http", "url": url}, separators=(",", ":")))
    lead = lead or f"The collection is served as an MCP server at <strong>{url}</strong>: the one kind of remote address on this site, a sealed public collection we host on purpose. You add it once; from then on your assistant asks it the way it asks any other tool."
    return f"""
  <section id="plug">
    <div class="placard">{placard} <span class="live">live door</span></div>
    <h2>{h2}</h2>
    <p class="lead">{lead}</p>
    <div class="steps">
      <div class="step"><div>
        <h3><a href="#access">Register once</a></h3>
        <p>Use <a href="#access">the form at the bottom of this page</a> and say "{word}". You confirm your address with one click, and that registration is what opens the collection for you. There is <strong>no key to copy</strong>, ever: the address below is not a secret, and signing in is what makes it yours.</p>
      </div></div>
      <div class="step"><div>
        <h3>Add the address to your assistant</h3>
        <pre class="cmd"><span class="a">{url}</span></pre>
        <p><strong>Claude Code</strong>: one line, then type <strong>/mcp</strong> and press Enter on <strong>{mcp_name}</strong>.</p>
        <pre class="cmd">claude mcp add --transport http {mcp_name} <span class="a">{url}</span></pre>
        <p><strong>Claude</strong> (web and desktop): Settings, Connectors, Add custom connector, paste the address, Connect. <strong>ChatGPT</strong>: Settings, Connectors, Create, paste the address, choose OAuth.</p>
        <p style="margin-top:14px"><a class="chip" href="{e(cursor)}">Add to Cursor</a> <a class="chip" href="{e(vscode)}">Add to VS Code</a></p>
      </div></div>
      <div class="step"><div>
        <h3>Allow it, once</h3>
        <p>Your assistant opens a docenta page by itself. It asks who you are (your address and six digits from your mail; nothing at all if you come from your start page) and shows one sentence: which assistant, which collection. Press <strong>Allow</strong>. You can disconnect any assistant later on your start page.</p>
      </div></div>
      <div class="step"><div>
        <h3>Ask, and read the citation</h3>
        <p>Every answer names the document and the page it came from. The first question after a quiet spell can take half a minute while the collection wakes up; your assistant is told so and asks again by itself.</p>
      </div></div>
    </div>
    <p class="lead" style="margin-top:26px">The door never sees your files, and cannot be changed by anyone, us included, without a new seal and a new date on this page. It knows that a registered person asked, so each person gets a fair share of it. <strong>It keeps nothing you ask unless you choose to</strong>, with two boxes that start unticked when you connect: "tell me when a question can be answered later", which keeps only the questions the collection could not answer, and "keep my questions, without my name", which keeps the words for 180 days with no name, address or time of day beside them. You can change both on your start page.</p>
  </section>
"""

def cta(audience, subject_word):
    opts = "".join(
        f'<option value="{v}"{" selected" if v == audience else ""}>{e(t)}</option>' for v, t in AUDIENCES
    ) + '<option value="other">Something else (say what below)</option>'
    subj = "docenta%20early%20access" + (f"%20({subject_word})" if subject_word else "")
    # The mail fallback goes where the form would have gone: the topic's
    # own address on docenta.ai (the domain's catch-all delivers every one).
    mail = f"{audience if audience and audience != 'site' else 'docenta'}@docenta.ai"
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
        <label class="ea-hp" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label>
        <div class="ea-turnstile"></div>
        <button class="cta-btn" type="submit">request early access</button>
        <p class="ea-status" role="status" aria-live="polite"></p>
      </form>
      <noscript><a class="cta-btn" href="mailto:{mail}?subject={subj}">request early access by mail</a></noscript>
      <span class="alt">No account and no newsletter: you confirm your address by mail, then we write back when the door opens. Prefer mail? <a href="mailto:{mail}?subject={subj}">{mail}</a></span>
      <script src="/assets/early-access.js" defer></script>
    </div>
  </section>
"""

ALSO = ('<p class="lead" style="margin-top:14px"><a href="/#for">Back to the collections</a> · also for '
        '<a href="/for/contractors/">contractors</a>, <a href="/for/lawyers/">lawyers</a>, <a href="/for/insurance/">insurance</a>, '
        '<a href="/for/home/">home</a>, <a href="/for/email/">mail</a>, <a href="/for/developers/">developers</a>, <a href="/for/researchers/">researchers</a> '
        '· <a href="/#doors">public collections, live</a>: <a href="/for/judaism/">Judaism</a>, <a href="/for/christianity/">Christianity</a>, '
        '<a href="/for/islam/">Islam</a>, <a href="/for/faith/">faith</a>, <a href="/for/sleep/">sleep</a> · in preparation: <a href="/for/diabetes/">diabetes</a> '
        '· <a href="/handbook/">the handbook</a></p>')

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
        "which price did we actually approve for the roof, and how long was it valid?",
        "The revised quote of <strong>July 29</strong> is the one that stands: <strong>$2,400 below</strong> the original and the latest price in the collection. An August 1 email from the contractor says the revised number \"stands through September\". No later quote or retraction appears in the indexed material.",
        [("Mail · \"Roof - estimate\" · July 27", "the original quote, PDF attached"),
         ("roof_estimate_v2.pdf · July 29", "the revised amount, $2,400 lower"),
         ("Mail · \"Re: Roof - estimate\" · August 1", "\"the revised number stands through September\"")],
        None,
        "No signed work order is in the collection. If you need one, that is the document to find.",
        "the contractor as an entity, plus roof, estimate and quote as concepts · thread and attachments grouped · ordered by date · the later formal artifact preferred · checked for a later contradicting amount · 3 sources kept, 11 dropped · 12 KB handed to the agent",
        "An illustration of the shape of every docenta answer: the files are made up, the behavior is real. The real ones are on the desk pages below and behind the eight live doors, where any visitor can ask.",
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
    <p class="lead" style="margin-top:14px">The one question that sums it up, and the one a retrieval box bolted onto a chatbot cannot answer: <strong>what do my own records actually prove about this, and what do they not prove?</strong> It needs the sources ranked, dated and compared, the contradiction kept visible, and an honest "not established" at the end. That is the whole product.</p>
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
    <p class="lead">The matter file, the claim, the mail archive, the private source tree, the unpublished paper, the household folder: docenta ingests, indexes and answers on your own hardware. Originals are never copied; only searchable derivatives are stored. Your agent gets a <strong>small evidence pack</strong> with the receipts, not your archive. It gets it over MCP, the connector standard it already speaks, from a server that <strong>runs on your own machine</strong>: your agent talks to a local process, not to a URL in someone's cloud. The only remote MCP addresses on this site are the public doors, sealed collections we host on purpose; your own collection never has one. Zero uploads, zero telemetry, and the token budget is printed on every answer.</p>
    <div class="plaque">
      <div class="plaque-title">Collection statistics · one real machine</div>
      <div class="plaque-grid">
        <div class="stat"><b>832,265</b><span>content objects from 3.0M file instances</span></div>
        <div class="stat"><b>315,351</b><span>searchable messages out of one mailbox</span></div>
        <div class="stat"><b>2,766</b><span>AI conversations and 13,368 commits, rendered and searchable</span></div>
        <div class="stat"><b>4-6 ms</b><span>entity and timeline answers</span></div>
        <div class="stat"><b>0</b><span>readable bytes leave your machine</span></div>
      </div>
      <div class="plaque-foot">Measured on the maker's own corpus, Apple M4 Max, 12 October 2026. Every number traces to a committed field run; the turbo lane ships only text sealed to a key this machine holds.</div>
    </div>
  </section>

  <section id="for">
    <div class="placard">Exhibit 005 · Who asks</div>
    <h2>One engine, your kind of collection.</h2>
    <p class="lead">The same docent, pointed at what your desk actually holds. Each page shows one real question and the shape of its answer; eight public collections are live behind doors today, and every door answer below was asked through the same engine.</p>
    <div class="cols">
      <a class="card wide" href="/for/contractors/"><div><h3><span class="k">Contractors.</span> Ask the rule. Get the exact page.</h3><p>City code, handouts, state law, utility standards and the code edition tied to the permit date, as one dated collection. Which rule applies, where the exception lives, whether the sources agree, and what the corpus cannot establish.</p><p class="qs">"Which code edition applies to this permit date?" · "Do the city handout and the ordinance agree?"</p></div><span class="live">live door</span></a>
      <a class="card wide" href="/for/lawyers/"><div><h3><span class="k">Lawyers.</span> Ask the matter. Cite the exhibit.</h3><p>Pleadings, correspondence, scanned exhibits, contracts and notes become one private evidence layer. Reconstruct the chronology, find the version that changed, surface the contradiction, map each assertion to a page, without uploading the matter anywhere. Try the engine today on the federal code and public contracts.</p><p class="qs">"Where does the other side first acknowledge this?" · "Does the declaration conflict with an earlier email?"</p></div><span class="live">live door</span></a>
      <a class="card" href="/for/insurance/"><h3><span class="k">Insurance.</span> Ask the claim, not the folders.</h3><p>Policy, notes, mail, forms, estimates and photos as one timeline with receipts: what happened, which version applies, where the file conflicts, what proof is missing.</p><p class="qs">"Which policy was in force on the loss date?"</p></a>
      <a class="card" href="/for/home/"><h3><span class="k">Home.</span> Your files remember what you forgot.</h3><p>Twenty years of mail, documents and photos, asked in plain words: the receipt tied to the warranty, the quote that replaced the old quote, the letter you half remember.</p><p class="qs">"Is the dishwasher still under warranty?"</p></a>
      <a class="card" href="/for/email/"><h3><span class="k">Mail.</span> Ask what was said, not what the subject line was.</h3><p>The promise, the latest number, the attachment that went with it and the whole thread in order, even when you remember the meaning and not the sender.</p><p class="qs">"What was the last delivery date they committed to?"</p></a>
      <a class="card wide" href="/for/developers/"><div><h3><span class="k">Developers.</span> Ask why the code is this way.</h3><p>Code, git history, design notes and every agent session as one cited memory layer. Test it on a project you know: the Git project, every commit since 2005 and the whole mailing list, sealed as a public collection behind its own door.</p><p class="qs">"Why is it called --force-with-lease, and what was wrong with the other names?"</p></div><span class="live">live door</span></a>
      <a class="card" href="/for/researchers/"><h3><span class="k">Researchers.</span> Ask your library where it disagrees.</h3><p>PDFs, scans, notes, drafts and co-author mail as one evidence layer: the paper you half remember, the results that conflict, the sentence in your draft that has no support.</p><p class="qs">"Which papers support this, and which contradict it?"</p></a>
    </div>
  </section>

  <section id="doors">
    <div class="placard">Exhibit 006 · Public collections, live behind doors</div>
    <h2>Eight sealed collections you can ask today. Each with its own card.</h2>
    <p class="lead">Public material only, one collection per subject, never mixed. Every door carries a card sealed with the collection and shown to your assistant on every connection: exactly what is inside, what is not, and the date nothing changed after. Register once on any page and the doors are open to you; each page below has a real answer asked through its door.</p>
    <div class="cols">
      <a class="card wide" href="/for/judaism/"><div><h3><span class="k">Judaism.</span> Tanakh, Mishnah, Talmud and commentary</h3><p>The Hebrew Bible in the Westminster Leningrad Codex with Open Scriptures morphology, and the openly licensed versions of the Sefaria library: Tanakh, Mishnah, Talmud, Midrash and commentary in Hebrew, Aramaic and English, 183,584 documents, one record per chapter or daf, each cited to its version and license.</p><p class="qs">"Why does the Torah begin with creation and not with the first commandment, and where does Rashi get that from?"</p></div><span class="live">live door</span></a>
      <a class="card wide" href="/for/christianity/"><div><h3><span class="k">Christianity.</span> Scripture and classical commentary</h3><p>The Berean Standard and World English Bibles chapter by chapter, Matthew Henry complete and concise, sixty-three volumes of Spurgeon, the SBL Greek New Testament, the Patristic Text Archive and the First Thousand Years of Greek: 51,876 documents, English first, Greek where the source is Greek.</p><p class="qs">"What does Matthew Henry make of Psalm 23:4, and did Spurgeon preach on that verse?"</p></div><span class="live">live door</span></a>
      <a class="card wide" href="/for/islam/"><div><h3><span class="k">Islam.</span> The Koran in six translations and Arabic, and the hadith</h3><p>Pickthall, Yusuf Ali, Shakir, Sale, Rodwell and Palmer sura by sura, the Arabic text with and without diacritics, and the ten hadith collections in English and Arabic, every hadith under its number with its gradings. No tafsir; the rights in the hadith texts are stated as unresolved on every record.</p><p class="qs">"How do the six translations render Surah 112:1, and which hadith say what the surah is worth?"</p></div><span class="live">live door</span></a>
      <a class="card wide" href="/for/faith/"><div><h3><span class="k">Faith.</span> The three traditions together</h3><p>The union of the three collections, 237,496 documents, nothing re-weighted: every answer says how its matches divide among Judaism, Christianity and Islam, and a question can be put to one of them alone.</p><p class="qs">"Where do the three scriptures tell of Joseph sold by his brothers, and do the commentators agree who sold him?"</p></div><span class="live">live door</span></a>
      <a class="card wide" href="/for/sleep/"><div><h3><span class="k">Sleep.</span> The open research corpus</h3><p>77,899 openly licensed texts: PubMed Central full texts under CC0, CC BY and CC BY-SA, ClinicalTrials.gov registrations, one AHRQ evidence report. Research literature, not medical advice; no subscription literature and no abstracts of closed articles.</p><p class="qs">"Which trials tested melatonin for insomnia in older adults, what did they measure, and does the meta-analysis agree?"</p></div><span class="live">live door</span></a>
      <a class="card" href="/for/diabetes/"><h3><span class="k">Diabetes.</span> The open research corpus</h3><p>The same shape as sleep, for human diabetes research. Being gathered; the card is written when the collection is sealed.</p><p class="qs"><span class="soon">door in preparation</span></p></a>
    </div>
  </section>

  <section>
    <div class="placard">Exhibit 007 · How the docent works</div>
    <h2>A spine that ingests, three channels that answer, one artifact that proves it.</h2>
    <div class="spine">
<b>ingest</b>   walk → hash → extract → index <span class="a">·</span> containers explode into members <span class="a">·</span> re-scan costs O(changes)<br>
<b>channels</b> exact BM25 <span class="a">·</span> paragraph lexical <span class="a">·</span> dense vectors, fused and re-ranked <span class="a">·</span> entities, timelines, themes on top<br>
<b>answer</b>   <span class="a">evidence_pack</span>: route plan, cited spans, conflicts, disclosed gaps, enforced token budget<br>
<b>live</b>     mail, chat exports, git and agent sessions stream in every hour <span class="a">·</span> your corpus feeds itself<br>
<b>tools</b>    <span class="a">search</span> <span class="a">search_meaning</span> <span class="a">evidence</span> <span class="a">read</span> <span class="a">thread</span> <span class="a">related</span> <span class="a">who_is</span> <span class="a">timeline</span> <span class="a">verify_quote</span> <span class="a">status</span> and ten more, over MCP <span class="a">·</span> every page says what was searched, what was dropped and why, and how many documents held every term
    </div>
    <p class="lead" style="margin-top:26px">The same 48 judged questions over the same corpus, asked by the same scripted agent two ways. With the evidence pack it cited the right document on <strong>44 of 48</strong>, in <strong>1 to 2.5 tool calls</strong> per task. Limited to search-and-fetch loops, the way an agent works without the pack, it cited it on <strong>39 of 48</strong>, in more calls. The difference is what the agent is handed: not a hit to go and read, but the evidence itself, the cited spans, the dates, the conflict and the gap, assembled and ranked, so the first answer is the deep one. What each pack used is printed on it. The lexical, entity and timeline layers are deterministic: a re-run gives the same bytes.</p>
  </section>
""")
    out.append(READS_TODAY)
    out.append(cta("site", ""))
    out.append(FOOT)
    return "".join(out)

READS_TODAY = r"""
  <section id="reads">
    <div class="placard">Exhibit 008 · What docenta reads today · 0.3.1</div>
    <h2>Everything on the machine, by what it is.</h2>
    <p class="lead">One engine, every lane. Originals stay where they are; docenta keeps searchable derivatives and a map back to the path. The list below is what the current build reads, as the handbook states it.</p>
    <div class="cols">
      <div class="card"><h3><span class="k">Files.</span></h3><p>Text, Markdown, PDF, Office, ODF, RTF, property lists, XML, JSON record by record, archives down to their members. The author, the dates and the sensitivity label of a document; the time and place inside a photo; ten copies of one file cost one index entry.</p></div>
      <div class="card"><h3><span class="k">Mail.</span></h3><p>A Takeout or mbox export in an evening, then the live account every hour: <strong>Sign in with Google</strong> for Gmail and Workspace, an app password elsewhere, Apple Mail and Outlook messages read as mail. Every folder the server lists, attachments as members, labels kept.</p></div>
      <div class="card"><h3><span class="k">Chats and agent sessions.</span></h3><p>Claude Code, Codex, ChatGPT and claude.ai exports, WhatsApp drops: every session rendered as it happens, so what the last agent learned is one search away for the next, and a compaction loses nothing.</p></div>
      <div class="card"><h3><span class="k">Git.</span></h3><p>Every repository on the machine, end to end: each commit rendered as correspondence with the files it changed, so a hash finds its commit and a line finds the message that introduced it.</p></div>
      <div class="card"><h3><span class="k">Scans and photos.</span></h3><p>OCR over scanned PDFs, images, HEIC and camera RAW previews, the pictures inside documents and animated images, on the machine's own GPU where it has one; a warning where a page's text order is unreliable.</p></div>
      <div class="card"><h3><span class="k">Code.</span></h3><p>C, C++, Go, Java, JavaScript, Kotlin, Python, Rust and TypeScript parsed by structure: functions, forms and identifiers as terms, with the commit and the thread that explain a line.</p></div>
    </div>
    <p class="lead" style="margin-top:26px">Runs on macOS (Apple silicon and Intel), Windows and Linux, identically. Speaks MCP to Claude Code, Claude, ChatGPT, Codex, Cursor and VS Code. People, places and dates become entities with timelines; meaning search works across languages; a rented GPU takes the heavy arithmetic for an hour on your say-so, sealed. <a href="/handbook/">The handbook</a> is the full account.</p>
  </section>
"""

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
    placard='Exhibit · docenta for contractors · Palo Alto building rules <a class="live" href="#plug">live door</a>',
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
    plug_html=plug("palo-alto", "door.docenta.ai", "docenta-palo-alto", "contractors",
                   placard="The Palo Alto collection, plugged into your assistant",
                   h2="One address, one sign-in, every question cited to the page.",
                   lead="The sealed collection above is served as an MCP server at <strong>https://door.docenta.ai/mcp</strong>: the one kind of remote address on this site, a public collection we host on purpose so your assistant can ask it today. You add it once; from then on it asks the collection the way it asks any other tool, and every answer names the document and the page."),
    subject_word="contractors",
)

# ---- lawyers (a fictional matter as the hero, the public door as the live proof)
PAGES["lawyers"] = dict(
    title="docenta for lawyers - ask the matter, cite the exhibit",
    desc="Pleadings, correspondence, scanned exhibits, contracts and notes become one private evidence layer. Reconstruct the chronology, find the version that changed, surface contradictions, map factual assertions to exact pages, without uploading the matter to a vendor cloud. Try the engine on the United States Code and public contracts, live.",
    placard='Exhibit · docenta for lawyers · The matter file <a class="live" href="#plug">live door: the federal code</a>',
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
    plug_html=plug("legal", "lawyers.docenta.ai", "docenta-legal", "lawyers",
                   placard="Try the engine on public material",
                   h2="The federal code and public contracts: one address, one sign-in, every question cited to the section.",
                   lead="The public collection shown above is served as an MCP server at <strong>https://lawyers.docenta.ai/mcp</strong>: the one kind of remote address on this site, a sealed public collection we host on purpose. Your matter file never has one; this door is where you try the engine before it runs on your own machine."),
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
        ("Your mail, past and present.", "", "Bring the mailbox export in once; from then on docenta fetches new mail on its own, every hour. A Google account signs in with one click on Allow; any other provider takes an app password you make in four steps. Your real password is never typed anywhere."),
        ("Photos and documents.", "", "The time and place inside a photo, the words on the receipt you photographed, the text inside a scan, the attachment inside a thread. Twenty years of it, HEIC and camera RAW included, on a normal Mac or PC; the heavy work runs at night or on a rented GPU for an hour with your say-so."),
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
        ("The export, then the live mailbox.", "", "A Takeout or mbox in an evening, then the live account every hour: Sign in with Google for a Google account, one click on Allow; an app password elsewhere, kept in the OS credential store. Every folder the server lists, trash and spam included, so nothing is invisible."),
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
        ("On the Git project, public", ["Why is it called --force-with-lease, and what was wrong with the other names?", "Why does git rerere exist, and who asked for it?", "Which thread settled the SHA-256 transition plan?", "When did git switch and git restore appear, and what did they refuse that checkout allowed?"]),
    ],
    reads=[
        ("Code and git.", "", "Every repository on the machine with its whole history: the commit that introduced the line, the files that change together, the message that explained it. C, C++, Go, Java, JavaScript, Kotlin, Python, Rust and TypeScript parsed by structure, identifiers as terms."),
        ("Notes and docs.", "", "Design notes, incident write-ups, READMEs and architecture records, cited to the line, so the invariant a function protects has a source."),
        ("Every agent session.", "", "Claude Code, Codex and ChatGPT sessions rendered and indexed as they happen, so what the last agent learned is one search away for the next, and a compaction loses nothing."),
    ],
    wont=[
        ("A session explains; it can be stale.", "An agent's reasoning from February is cited with its date; a later commit that changed the code outranks it, and the answer says which is newer."),
        ("grep is not replaced, it is measured.", "On the maker's judged sets docenta's top-10 found 114 of 227 targets to ripgrep's 44, reading about 20 KB to the truth instead of 2.8 MB. The numbers are printed, the arm is committed."),
        ("Absent rationale is reported absent.", "\"No design record in the corpus explains this\" is an answer, and a useful one before the next rewrite."),
        ("The budget is on every answer.", "How many tokens the agent was handed, and what was dropped to stay inside them."),
    ],
    extra_after_demo="""
  <section id="git">
    <div class="placard">Exhibit · the same docent on a project you know · The Git project</div>
    <h2>Try the questions on git itself.</h2>
    <p class="lead">Your repositories are private, so the exhibit above is the maker's own. To let you test the claim on code you know, we sealed a public collection of the Git project: git/git at the sealed commit, all 82,305 commits since 2005 rendered as correspondence, and the git mailing list from lore.kernel.org, 552,249 messages. Below, four questions asked of it on 18 September 2026, answered the way the door answers over MCP. The door at git.docenta.ai opens shortly; its card, when it opens, is the one your assistant reads.</p>
""" + answer(
        "Why is it called --force-with-lease, and what was wrong with the other names?",
        "Because nobody liked the first two. On <strong>22 July 2013</strong> Junio C Hamano sent the third round of the series that had introduced the option as <strong>--cas</strong> and then <strong>--lockref</strong>, renamed: \"Nobody liked 'cas' as it was too technical, many disliked 'lockref' because 'lock' sounded as if push by others were excluded by it while in fact this is to fail us.\" The name chosen says it is a kind of --force, and \"with-lease\" says the forcing holds only while the lease you took on the ref, the state you observed before you rebased, is unbroken. The same letter warns that the default lease, the remote-tracking branch, had been shown fragile in the discussion and is documented as experimental.",
        [("git list · Junio C Hamano · 2013-07-22", "[PATCH v3 0/6] \"git push --cas/--lockref\" renamed to \"--force-with-lease\": the paragraph quoted above"),
         ("git list · 2013-07-08", "remote.c: add command line option parser for \"--force-with-lease\", the patch the letter carries"),
         ("git list · 2017-07-05", "[PATCH] push: add config option to --force-with-lease by default, and the replies"),
         ("git list · 2018-08-27", "Would a config var for --force-with-lease be useful?")],
        "",
        "The pack ranks twenty messages and dates them; it does not say who first proposed the winning name. The thread holds that one hop away.",
        "lexical and semantic lanes over 552,249 list messages and 82,305 commits · 20 messages cited, 19 shown · 1,324 of 1,400 tokens",
        "Real, from the sealed git collection, asked through the same engine the door serves. Three more, asked the same day:",
        title="docenta over MCP · the Git project",
    ) + """
    <div class="limits">
      <p><b>Why does git rerere exist?</b> Since 29 January 2006: Junio C Hamano's commit 8389b52b, "reuse recorded resolve", for a workflow of long-lived topic branches where the same conflict is resolved over and over; the list saw it the same day as [PATCH/RFC]. In July 2006 Shawn Pearce proposed a second tool so that git merge could reuse resolutions on its own, and in July 2007 a patch to enable rerere by default drew a thread of nine replies.</p>
      <p><b>Which thread settled the SHA-256 transition?</b> The plan was argued as "RFC: Another proposed hash function transition plan" through 2017, v3 in September; the function was settled in July 2018, when the cover letter "document that NewHash is now SHA-256" quoted Linus Torvalds on the libgit2 argument that the system's crypto libraries already carry it: "I think this is probably the single strongest argument for sha256. It's just there." The base SHA-256 implementation landed in November 2018.</p>
      <p><b>When did git switch and git restore appear, and what did they refuse?</b> Duy Nguyen's RFC v3 of 29 November 2018 introduced switch-branch and restore-files after two rounds of renames, listing what they refuse that checkout allowed: no invocation that does nothing, no implicit detach, no pathspec on switch. The branch nd/switch-and-restore cooked from April 2019 and merged on 9 July 2019; in May 2021 the list was still asking whether the two are experimental.</p>
    </div>
    <p class="term-note">Each answer names the message or the commit it came from; the door returns the same citations to your assistant, and a question the collection cannot answer is answered "not in this corpus".</p>
  </section>
""",
    rolewords="Private source trees, incident notes and agent transcripts",
    plug_html=plug("git", "git.docenta.ai", "docenta-git", "developers",
                   placard="The Git project, plugged into your assistant",
                   h2="One address, one sign-in, every answer cited to the commit or the message.",
                   lead="The sealed Git collection above is served as an MCP server at <strong>https://git.docenta.ai/mcp</strong>: 653,394 documents, the git/git tree at the seal, every commit since 2005 and the whole mailing list. Your own repositories never have an address like it; this door is where you test the claim on code you know."),
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

# ---------------------------------------------------------------- the door pages (2026-10-12)
# Five public collections are live behind doors. Each page shows the
# sealed card verbatim and one REAL answer asked through the door the day
# the page was written, in the shape a retrieval box cannot produce: the
# versions compared, the scope counted, the commentators in conflict, the
# gap named.
def door_page(slug, title, desc, placard, h1, sub, chip_qs, demo, card, sealed_line, reads, wall_groups, wont, host, mcp_name, word, plug_lead):
    out = [head(title, desc, f"https://docenta.ai/for/{slug}/")]
    out.append(f"""
  <header>
    <div class="placard">{placard} <a class="live" href="#plug">live door</a></div>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
""")
    out.append(chips(chip_qs))
    out.append(demo)
    out.append(f"""
  </header>

  <section>
    <div class="placard">The card, as the door says it</div>
    <h2>What is in the collection, and what is not.</h2>
    <p class="lead">Every door carries a card, sealed with the collection and shown to your assistant on every connection. This one reads:</p>
    <div class="terminal" style="margin-top:26px"><div class="term-body"><p class="ans" style="margin:0">{e(card)}</p></div></div>
    <p class="term-note">{e(sealed_line)}</p>
""")
    out.append(cards(reads))
    out.append("""
  </section>

  <section>
    <div class="placard">Questions a plain search cannot answer cleanly</div>
    <h2>Ask across editions, across volumes, across the shelf.</h2>
""")
    out.append(wall(wall_groups))
    out.append("""
  </section>
""")
    out.append(plug(slug, host, mcp_name, word,
                    placard="The collection, plugged into your assistant",
                    h2="One address, one sign-in, every answer cited to the passage.",
                    lead=plug_lead))
    out.append("""
  <section>
    <div class="placard">What it will not pretend to know</div>
    <h2>Boundedness is the feature.</h2>
""")
    out.append(limits(wont))
    out.append(ALSO)
    out.append("""
  </section>
""")
    out.append(cta(slug, word))
    out.append(FOOT)
    return "".join(out)

DOORS = {}

DOORS["judaism"] = dict(
    title="docenta for Judaism - Tanakh, Mishnah, Talmud and commentary, live",
    desc="A sealed, live collection of Judaism's scripture and commentary in the public domain or under open licenses: the Westminster Leningrad Codex with morphology and the openly licensed Sefaria library. Ask it through your assistant; every answer names the passage, the version and the license.",
    placard="Exhibit · docenta for Judaism · Tanakh, Mishnah, Talmud and commentary",
    h1="Ask the library. <em>Get the passage, the version and the license.</em>",
    sub="The Hebrew Bible in the Westminster Leningrad Codex with Open Scriptures morphology, and the openly licensed versions and translations of the Sefaria library: Tanakh, Mishnah, Talmud, Midrash and commentary in Hebrew, Aramaic and English, 183,584 documents, one record per chapter or daf. Every answer cites the passage and the edition it comes from, with its license; <strong>versions under other licenses are not in this collection</strong>, and it gives no halachic ruling.",
    chip_qs=["Why does the Torah begin with creation and not with the first commandment?", "Which editions of Rashi does the library hold, and do they word this comment differently?", "Which tractate discusses this ruling, and what does the Mishnah say first?", "Where does this phrase first appear, and where is it cited later?", "What does the collection not contain?"],
    demo=answer(
        "why does the Torah begin with creation and not with the first commandment, and where does Rashi get that from?",
        "Rashi opens his commentary on Genesis 1:1 with Rabbi Isaac's question: the Torah, as Israel's book of law, should have begun with Exodus 12:2, \"This month shall be unto you the first of the months\", the first commandment given to Israel. His answer rests on <strong>Psalm 111:6</strong>, \"He declared to His people the strength of His works, in order that He might give them the heritage of the nations\": the account of creation is there so that when the nations call Israel robbers for taking the land of the seven nations, Israel can answer that the whole earth belongs to the Holy One, who created it and gives it to whom He pleases. Rashi's editors trace the thought to <strong>Yalkut Shimoni on Torah 187</strong>. The library holds the comment in two editions, a 1929 translation in the public domain and a 2009 translation under CC BY, worded differently and saying the same thing.",
        [("Rashi on Genesis 1, verse 1 · Rosenbaum and Silbermann, 1929-1934 · public domain", "\"Rabbi Isaac said: The Torah which is the Law book of Israel should have commenced with the verse (Exodus 12:2)...\""),
         ("Rashi on Genesis 1, verse 1 · Rashi Chumash, Metsudah Publications, 2009 · CC BY", "\"R. Yitzchok said: The Torah should have begun with [the verse] 'This month shall be [your first month]', it being the first precept...\""),
         ("the proof text · Psalms 111:6", "\"He declared to His people the strength of His works, in order that He might give them the heritage of the nations\""),
         ("the source the editors name · Yalkut Shimoni on Torah 187", "cited inside the 1929 edition's note")],
        "None between the editions: a version receipt, not a conflict. The 1929 text says \"robbers\"; the 2009 text says \"the first precept that the Israelites were commanded\"; both carry the Psalm.",
        "Whether the collection holds the Yalkut Shimoni passage itself as a text was not checked by this answer; it is cited here as Rashi's editors cite it. The Hebrew of Rashi's comment is one hop away in the same library.",
        "lexical lane over origin:judaism · 3 hits, 2 editions of Rashi kept, 1 unrelated homily dropped · every hit holds all of the question's terms",
        "Real, from the sealed Judaism collection, asked through the same engine the door serves, on 12 October 2026. Two editions, one Psalm, one named source: a search box returns the passage; the docent returns the chain.",
        title="docenta over MCP · the Judaism collection",
    ),
    card="The Hebrew Bible in the Westminster Leningrad Codex (Open Scriptures Hebrew Bible), and the openly licensed versions of the Sefaria library: public domain, CC0, CC BY and CC BY-SA texts and translations of Tanakh, Mishnah, Talmud, Midrash and commentary, one record per chapter or daf, each cited to its version. Versions under other licenses are not in this collection; it gives no halachic ruling; cite the passage and the version it returns.",
    sealed_line="Sealed 2026-09-21; 183,584 documents; nothing is added, changed or removed, and a question outside the collection is answered \"not in this corpus\".",
    reads=[("Scripture.", "", "The Westminster Leningrad Codex (public domain) with Open Scriptures morphology (CC BY): every word tagged, so a form finds its root."),
           ("The Sefaria library.", "", "Every version whose license is public domain or CC BY: Tanakh, Mishnah, Talmud, Midrash and commentary, in Hebrew, Aramaic and English, each cited with its version and license."),
           ("What stays out.", "", "Versions under other licenses, and anything the registry files as research-only. The card names the cut; the door serves nothing else.")],
    wall_groups=[
        ("Trace a comment", ["Where does Rashi comment on this verse, and which other commentator disagrees?", "Which Mishnah does this Gemara discuss, and where is the ruling first stated?", "Which later source cites this passage, and does it quote it exactly?"]),
        ("Editions and versions", ["Which editions of this commentary does the library hold, under which license, and where do their wordings differ?", "Does the English follow the Hebrew here, or does the translator add a gloss?"]),
        ("Across the shelf", ["Where does this phrase first appear in Tanakh, and where does the Talmud take it up?", "What do the Midrash and the Rishonim make of the same verse, side by side?", "What does the collection not contain on this question?"]),
    ],
    wont=[("It gives no ruling.", "Halacha is not retrieval. The door cites the passage, the version and the license and stops there."),
          ("Rights are on every record.", "A text under a license the collection cannot carry is simply not inside, and the card says so."),
          ("\"Not in this corpus\" is an answer.", "A question the collection cannot settle is answered with that sentence and the searches that were run."),
          ("The seal is the date.", "Nothing is added, changed or removed after the seal; a new seal means a new date on this page.")],
    host="judaism.docenta.ai", mcp_name="docenta-judaism", word="judaism",
    plug_lead="The sealed collection above is served as an MCP server at <strong>https://judaism.docenta.ai/mcp</strong>: a public collection we host on purpose so your assistant can ask it today. You add it once; from then on it asks the collection the way it asked the question above, and reads the passage back with its version.",
)

DOORS["christianity"] = dict(
    title="docenta for Christianity - scripture and classical commentary, live",
    desc="A sealed, live collection of Christian scripture and classical commentary in the public domain or under open licenses: the Berean and World English Bibles, Matthew Henry, sixty-three volumes of Spurgeon, the SBL Greek New Testament, the Patristic Text Archive and the First Thousand Years of Greek. Every answer names the passage, the translation and the volume.",
    placard="Exhibit · docenta for Christianity · Scripture and classical commentary",
    h1="Ask the shelf. <em>Get the verse, the commentary and the sermon.</em>",
    sub="The Berean Standard Bible and the World English Bible chapter by chapter, Matthew Henry's complete and concise commentaries, sixty-three volumes of Spurgeon's sermons, the SBL Greek New Testament, the Patristic Text Archive and the First Thousand Years of Greek in their original languages: 51,876 documents, English first, Greek where the source is Greek. <strong>Nothing from the Christian Classics Ethereal Library and no denominational statements</strong>; it gives no pastoral advice.",
    chip_qs=["What does Matthew Henry make of Psalm 23:4, and did Spurgeon preach on that verse?", "Which translations render this verse differently, and how?", "Which church father first uses this term, and where?", "What does the Greek say here?", "What does the collection not contain?"],
    demo=answer(
        "what does Matthew Henry make of Psalm 23:4, and did Spurgeon ever preach on that verse?",
        "Henry reads the psalm as <strong>three comfortable premises and three comfortable conclusions</strong>: from God's being his shepherd David infers that he shall want no good (verse 1), that he need <strong>fear no evil</strong> (verse 4), and that God will never leave him (verse 6), with an eye not only to providence but to grace received by a lively faith. Spurgeon did preach on the verse: <strong>Sermon 1595, \"The Valley of the Shadow of Death\"</strong>, in volume 27, opens with the confession that he had laid the text by for his own last hours and found he needed to eat this heavenly loaf at once, a tempest having howled around him some days before. The concise Henry says the same in a paragraph.",
        [("Psalm 23 · Matthew Henry's Complete Commentary, volume 3 · CC0", "\"From three very comfortable premises David, in this psalm, draws three very comfortable conclusions\"; \"he needed to fear no evil (Ps 23:4)\""),
         ("Psalm 23 · Matthew Henry's Concise Commentary · CC0", "the same reading in short"),
         ("Sermon 1595, The Valley Of The Shadow Of Death · Spurgeon, volume 27 · CC0", "on Psalm 23:4: \"Do you know I had laid this text by? ... The other day I found that I needed to eat this heavenly loaf at once\""),
         ("Sermon 2448, Herein Is Love · Spurgeon, volume 42 · CC0", "passes through verses 3 and 4 of the psalm in an exposition")],
        None,
        "The sermon's preaching date is not in the text as sealed; the volume number is. A first pass surfaced Sermon 2260, which quotes the connection of a verse to its neighbour, and reading it showed the verse is Psalm 147:3, not 23:4; it was dropped. The answer names what was read, not only what was found.",
        "evidence over 20 passages, then two searches and three reads · Henry complete, Henry concise and two sermons kept · one false lead read and dropped",
        "Real, from the sealed Christianity collection, asked through the same engine the door serves, on 12 October 2026. The commentary, the sermon and the verse are one shelf; the false lead was read and named, not hidden.",
        title="docenta over MCP · the Christianity collection",
    ),
    card="Christian scripture and classical commentary in the public domain or under open licenses: the Berean Standard Bible and the World English Bible chapter by chapter, Matthew Henry's complete and concise commentaries, sixty-three volumes of Spurgeon's sermons, the SBL Greek New Testament, the Patristic Text Archive and the First Thousand Years of Greek in their original languages. English first, Greek where the source is Greek. It holds nothing from the Christian Classics Ethereal Library and no denominational statements, and gives no pastoral advice; cite the passage or the volume it returns.",
    sealed_line="Sealed 2026-09-21; 51,876 documents; nothing is added, changed or removed, and a question outside the collection is answered \"not in this corpus\".",
    reads=[("Scripture, two ways.", "", "The Berean Standard Bible (public domain, 2023 release) and the World English Bible (public domain), chapter by chapter, so a verse is cited to its translation."),
           ("Commentary and sermons.", "", "Matthew Henry complete and concise (CC0), Spurgeon's sermons in sixty-three volumes (CC0): the exposition and the pulpit on the same verse, found together."),
           ("The Greek shelf.", "", "The SBL Greek New Testament, the Patristic Text Archive (CC BY-SA) and the First Thousand Years of Greek (CC BY-SA), in the original languages, English where the source is English.")],
    wall_groups=[
        ("Verse to shelf", ["What does Matthew Henry say on this chapter, and what does Spurgeon preach on it?", "Which sermons take this verse as their text, and in which volumes?", "Which church father first uses this term, and where?"]),
        ("Translations", ["How do the Berean and the World English render this verse, and where do they differ?", "What does the Greek say here, and which English word carries it?"]),
        ("Across time", ["How does a patristic reading of this passage compare with Henry's?", "Where does the same figure appear across Philo, the fathers and the sermons?", "What does the collection not contain on this question?"]),
    ],
    wont=[("It gives no pastoral advice.", "The door cites the passage, the commentary and the volume; counsel is not retrieval."),
          ("Nothing from the Christian Classics Ethereal Library.", "Its terms keep it out; the card says so, and the door serves nothing else."),
          ("A false lead is named, not hidden.", "What was read and dropped is part of the answer, so the next question starts where this one stopped."),
          ("The seal is the date.", "Nothing is added, changed or removed after the seal; a new seal means a new date on this page.")],
    host="christianity.docenta.ai", mcp_name="docenta-christianity", word="christianity",
    plug_lead="The sealed collection above is served as an MCP server at <strong>https://christianity.docenta.ai/mcp</strong>: a public collection we host on purpose so your assistant can ask it today. You add it once; from then on it asks the collection the way it asked the question above, and reads the passage back with its translation and volume.",
)

DOORS["islam"] = dict(
    title="docenta for Islam - the Koran in six translations and Arabic, and the hadith, live",
    desc="A sealed, live collection: the Koran in six English translations and in Arabic, sura by sura, and the ten hadith collections in English and Arabic, every hadith under its number with its gradings. No tafsir; every answer names the sura and verse, or the collection, book and number.",
    placard="Exhibit · docenta for Islam · The Koran in six translations and Arabic, and the hadith",
    h1="Ask the text. <em>Get the sura, the verse, the translator, and the hadith by its number.</em>",
    sub="The Koran in six English translations, Pickthall, Yusuf Ali and Shakir, George Sale (1734), J. M. Rodwell (1861) and E. H. Palmer (1880), and in Arabic with and without diacritics, one record per sura per edition; and the ten hadith collections in English and Arabic, Bukhari, Muslim, Abu Dawud, Tirmidhi, Nasai, Ibn Majah, Malik's Muwatta and the three Forty Hadith, every hadith under its number with its gradings. <strong>No tafsir</strong>, no religious ruling; the rights in the hadith texts are stated as unresolved on every record.",
    chip_qs=["How do the six translations render Surah 112:1, and what is the Arabic?", "Which hadith say what Al-Ikhlas is worth, and do the graders agree?", "Where does the Koran treat this theme, sura by sura?", "Which translator uses this word, and where?", "What does the collection not contain?"],
    demo=answer(
        "how do the six English translations render the first verse of Surah 112, what is the Arabic, and which hadith say what the surah is worth?",
        "Six renderings of four Arabic words, <strong>قُلْ هُوَ اللَّهُ أَحَدٌ</strong>: Pickthall \"Say: He is Allah, the One!\", Yusuf Ali \"Say: He is Allah, the One and Only\", Shakir \"Say: He, Allah, is One\", Sale (1734) \"Say, God is one God\", Rodwell (1861) \"SAY: He is God alone\", Palmer (1880) \"Say, He is God alone\". The hadith on the surah's worth: Bukhari, Book 66 (Virtues of the Qur'an), narrated Abu Said al-Khudri, a man heard another recite it repeatedly and the Prophet said it is <strong>equal to one third of the Qur'an</strong>; Muslim, Book 6, Hadith 1889, Abu Huraira, the same measure. Ibn Majah, Book 5, has it recited with Al-Kafirun in the two rak'ah of Fajr, graded Sahih by Al-Albani; Tirmidhi, Book 9, in the two rak'ah of Tawaf; Nasai, Book 20, in the night prayer, and there <strong>the graders disagree</strong>: Daif isnad per Abu Ghuddah and Al-Albani, Hasan per Zubair Ali Zai.",
        [("Koran, Sura 112 · six editions: Pickthall, Yusuf Ali, Shakir (Gutenberg 16955), Sale, Rodwell, Palmer · public domain", "verse 1 in each, one record per sura per edition"),
         ("Koran, Sura 112 · the Arabic text, with and without diacritics · Arabic Wikisource, CC BY-SA", "قُلْ هُوَ اللَّهُ أَحَدٌ"),
         ("Sahih al-Bukhari, Book 66 · Virtues of the Qur'an · rights unresolved", "\"equal to one third of the Qur'an\", narrated Abu Said Al-Khudri"),
         ("Sahih Muslim, Book 6 · Hadith 1889 · rights unresolved", "Abu Huraira: \"I am going to recite before you one-third of the Qur'an\""),
         ("Sunan Ibn Majah, Book 5 · rights unresolved", "the two rak'ah of Fajr; grading Sahih (Al-Albani)"),
         ("Sunan an-Nasai, Book 20 · rights unresolved", "the night prayer; gradings Daif isnad (Abu Ghuddah, Al-Albani), Hasan (Zubair Ali Zai)")],
        "The graders disagree on the Nasai narration: Daif isnad for two of them, Hasan for the third. Both verdicts are on the record and both are shown; the door does not pick one.",
        "No tafsir is in the collection, so what the surah means is not a question it answers; what each translator wrote and what each collection narrates is. The rights in the hadith texts are unresolved and every such record says so.",
        "lexical lane over origin:islam · 6 translations, 2 Arabic texts and 9 hadith records · every hadith cited with its collection, book and gradings",
        "Real, from the sealed Islam collection, asked through the same engine the door serves, on 12 October 2026. Six translators, the Arabic, five collections and a disagreement among the graders, on one answer with the number of every hadith.",
        title="docenta over MCP · the Islam collection",
    ),
    card="The Koran in six English translations (Pickthall, Yusuf Ali and Shakir from Project Gutenberg eBook 16955; George Sale 1734, J. M. Rodwell 1861 and E. H. Palmer 1880) and in Arabic (the text of Arabic Wikisource, with and without diacritics), one record per sura per edition; and the ten hadith collections of the hadith-api project in English and Arabic (Bukhari, Muslim, Abu Dawud, Tirmidhi, Nasai, Ibn Majah, Malik's Muwatta and the three Forty Hadith), one record per book with every hadith under its number. The rights in the hadith texts are not stated by their source and every such record says so. No tafsir is in this collection; it gives no religious ruling; cite the sura and the verse, or the collection, the book and the hadith number it returns.",
    sealed_line="Sealed 2026-09-21; 2,036 documents; nothing is added, changed or removed, and a question outside the collection is answered \"not in this corpus\".",
    reads=[("Six translations and the Arabic.", "", "Pickthall, Yusuf Ali, Shakir, Sale, Rodwell and Palmer, one record per sura per edition, and the Arabic text with and without diacritics, as people type it."),
           ("Ten hadith collections.", "", "Bukhari, Muslim, Abu Dawud, Tirmidhi, Nasai, Ibn Majah, Malik's Muwatta and the three Forty Hadith, in English and Arabic, every hadith under its number with its gradings."),
           ("What the card promises.", "", "The translator named on every verse, the collection and number on every hadith, the rights stated as unresolved where they are, and \"not in this corpus\" for everything else.")],
    wall_groups=[
        ("Across editions", ["How do the six translations render this verse, and where do they part?", "Which translator uses this word, and where else?", "What is the Arabic, and does the diacritic text differ from the typed one?"]),
        ("The hadith", ["Which collections carry this narration, under which numbers, and do the graders agree?", "Which hadith mention this sura, and in which prayers?", "Where does a Forty Hadith collection quote a longer one?"]),
        ("Limits", ["What does this collection not contain?", "Which records carry rights the source did not state?"]),
    ],
    wont=[("It gives no ruling and holds no tafsir.", "What a verse means is not a question this collection answers; what each translator wrote and what each collection narrates is."),
          ("Gradings disagree, and both are shown.", "A narration graded Daif by one scholar and Hasan by another is cited with both; the door does not pick."),
          ("Rights are stated as they are.", "The hadith texts' source states no rights; every such record says so, and the card says so."),
          ("The seal is the date.", "Nothing is added, changed or removed after the seal; a new seal means a new date on this page.")],
    host="islam.docenta.ai", mcp_name="docenta-islam", word="islam",
    plug_lead="The sealed collection above is served as an MCP server at <strong>https://islam.docenta.ai/mcp</strong>: a public collection we host on purpose so your assistant can ask it today. You add it once; from then on it asks the collection the way it asked the question above, and reads the verse back with its translator, or the hadith with its number.",
)

DOORS["faith"] = dict(
    title="docenta for faith - the three traditions together, live",
    desc="The union of the Judaism, Christianity and Islam collections, 237,496 documents, nothing re-weighted: one question, three scriptures, each answer cited to its own tradition and counted by origin. Live behind a door.",
    placard="Exhibit · docenta for faith · The three traditions together",
    h1="One question, three scriptures, <em>each in its own words, and counted</em>.",
    sub="The union of the Judaism, Christianity and Islam collections, each described on its own card: 237,496 documents, Judaism 77.3 percent, Christianity 21.8 percent, Islam 0.9 percent, as uneven as the open sources are and nothing re-weighted. Every answer says how its matches divide among the three, and a question can be put to one of them alone. <strong>Nothing is blended into a single voice.</strong>",
    chip_qs=["Where do the three scriptures tell of Joseph sold by his brothers?", "Do the commentators agree who sold him?", "How do the traditions' commentators read this shared figure?", "Which tradition's text is this phrase from, and where else does it appear?", "What does each collection not contain?"],
    demo=answer(
        "where do the three scriptures tell of Joseph sold by his brothers, in their own words, and do the commentators agree who sold him?",
        "The search counts itself before it answers: <strong>20 matches from Judaism, 18 from Christianity, 2 from Islam</strong>. Genesis 37:28 in three Jewish editions (the Sefaria Community Translation, the Modernized JPS 1917, the Rashi Chumash) and two Christian ones (Berean, World English): Midianite merchants pass, the brothers pull Joseph from the pit, he is sold to the Ishmaelites for twenty pieces of silver and brought to Egypt. In Islam the story is Sura 12, Yusuf Ali: the dream of the sun, the moon and eleven stars, and the father's warning not to tell the brothers. On <strong>who sold him</strong> the commentators do not agree, and the answer shows both: Rashi reads the brothers as the sellers, to the Ishmaelites who sold him on to the Midianites; Da'at Zekenim reads two separate groups and the Midianites hauling him from the pit. Philo's treatise On Joseph and Spurgeon's Sermon 1610, A Miniature Portrait of Joseph, stand beside them on the Christian shelf.",
        [("Genesis 37 · Sefaria Community Translation · CC0 · origin:judaism", "verse 28: \"They sold Joseph for twenty pieces of silver to the Ishmaelites, who brought Joseph to Egypt\""),
         ("Genesis 37 · Berean Standard Bible · public domain · origin:christianity", "\"Joseph Sold into Egypt\", verses 12 to 28"),
         ("Koran, Sura 12 · Abdullah Yusuf Ali · public domain · origin:islam", "verses 4 and 5: the dream, and \"relate not thy vision to thy brothers\""),
         ("Da'at Zekenim on Genesis 37 · tr. Eliyahu Munk · CC BY · origin:judaism", "\"According to Rashi, the subject here are the brothers ... There were two separate groups of people\""),
         ("On Joseph · Philo Judaeus · First Thousand Years of Greek · CC BY-SA · origin:christianity", "\"the eleven brethren drew Joseph up out of the pit and sold him to them\""),
         ("Sermon 1610, A Miniature Portrait Of Joseph · Spurgeon, volume 27 · CC0 · origin:christianity", "\"the Patriarchs, moved with envy, sold Joseph into Egypt\"")],
        "Rashi against Da'at Zekenim on the subject of \"they sold\": brothers, or Midianites. Both readings are on the page, cited to their edition; the door does not decide between them.",
        "Islam's share of this answer is the sura alone: the hadith collections mention Yusuf only in passing (Bukhari, Book 78). The Arabic of Sura 12 is one hop away; this answer read the English.",
        "lexical lane over the union · 39 matches counted by origin · 6 kept across three traditions · the commentary conflict surfaced by the second question",
        "Real, from the sealed faith collection, asked through the same engine the door serves, on 12 October 2026. The count by origin, the three scriptures in their own editions and a commentary disagreement held open: a retrieval box returns a passage; the docent returns the shelf.",
        title="docenta over MCP · the faith collection",
    ),
    card="Scripture, classical commentary and interpretive tradition of Judaism, Christianity and Islam, in the public domain or under open licenses: the union of the judaism, christianity and islam collections, each described on its own card. What it is made of, by documents: Judaism 183,589 documents (77.3 percent), Christianity 51,876 documents (21.8 percent), Islam 2,036 documents (0.9 percent). The shares are as uneven as the open sources are and nothing is re-weighted: every result page's scope_counts say how a question's matches divide among origin:judaism, origin:christianity and origin:islam, and a question can be put to one of them (scopes: origin:islam). It gives no religious ruling; cite the passage, the version or the volume it returns.",
    sealed_line="Sealed 2026-09-21 from the three sealed collections; 237,496 documents; nothing is added, changed or removed.",
    reads=[("Three collections, one door.", "", "Everything the Judaism, Christianity and Islam doors hold, served together, with the tradition named on every answer and the count by origin on every page."),
           ("Kept apart inside.", "", "Each source stays cited to its own tradition, version and license; a question that spans them returns three answers, not one blend, and scopes: origin:islam asks one alone."),
           ("The same limits.", "", "No religious ruling, nothing under a restrictive license, and \"not in this corpus\" when a tradition's cut lacks the text.")],
    wall_groups=[
        ("The shared story", ["Where do the three scriptures tell this story, in their own words?", "Which tradition's text is this phrase from, and where else does it appear?", "How does each tradition's commentary read the same figure?"]),
        ("Counted, not blended", ["How do the matches for this question divide among the three, and why?", "Put the question to one tradition alone: what changes?"]),
        ("Disagreement and gaps", ["Where do two commentators in one tradition read the same verse differently?", "What does each collection not contain on this question?"]),
    ],
    wont=[("It gives no ruling in any tradition.", "The door cites the passage, the version or the volume and stops there."),
          ("The shares are uneven and said so.", "Judaism holds 77 percent of the documents; the count on every page keeps that visible instead of hiding it in a ranking."),
          ("A disagreement stays open.", "Two readings of one verse are shown side by side, cited to their editions; the docent does not decide between them."),
          ("The seal is the date.", "Made from the three sealed collections; a new seal of any of them means a new seal here, and a new date on this page.")],
    host="faith.docenta.ai", mcp_name="docenta-faith", word="faith",
    plug_lead="The sealed union above is served as an MCP server at <strong>https://faith.docenta.ai/mcp</strong>: a public collection we host on purpose so your assistant can ask it today. You add it once; from then on it asks all three traditions at once, reads the count by origin, and can ask one of them alone.",
)

DOORS["sleep"] = dict(
    title="docenta for sleep research - the open corpus, live",
    desc="A sealed, live collection of open-access sleep research: PubMed Central full texts under open licenses, ClinicalTrials.gov registrations and one AHRQ evidence report, 77,899 texts. Ask which trials tested what, and where the papers and the review disagree; every answer cites the paper or the registration.",
    placard="Exhibit · docenta for sleep research · The open corpus",
    h1="Ask the literature. <em>Get the trial, the paper and the page.</em>",
    sub="Human sleep research from the public biomedical infrastructure: the open-access full texts of PubMed Central articles under CC0, CC BY and CC BY-SA, ClinicalTrials.gov registrations, and one AHRQ evidence report from the NCBI Bookshelf, 77,899 texts, every one carrying its license and source. <strong>Research literature, not medical advice</strong>; no subscription literature, no abstracts of closed articles, no clinical practice guidelines.",
    chip_qs=["Which trials tested melatonin for insomnia in older adults, and what did they measure?", "Does the meta-analysis agree with the trials it pooled?", "Which registration belongs to this paper?", "What is the earliest paper here making this claim, and did a replication fail?", "What does the collection not contain?"],
    demo=answer(
        "which trials tested melatonin for insomnia in older adults, what did they measure, and does the meta-analysis agree?",
        "The registry and the papers answer together. <strong>NCT00230737</strong>, Melatonin Randomized Trial for Insomnia in the Elderly: phase 2, completed, 27 enrolled, 0.4 mg against 4.0 mg, for sleep initiation and maintenance disorders. <strong>NCT07695246</strong>: cognitive behavioural therapy for insomnia with and without adjunct melatonin in older adults, randomised, double-blind, placebo-controlled, measuring sleep, circadian outcomes and daytime functioning. The largest paper, <strong>Wade and colleagues</strong>, nightly prolonged-release melatonin for six months: 791 randomized, 722 analysed, patients 55 and older, sleep latency shortened by 15.6 minutes in the 65 to 80 group (95 percent CI minus 25.3 to minus 6.0). The <strong>systematic review and meta-analysis</strong> of melatonin and ramelteon in older adults with chronic insomnia searched 1990 to June 2021, the year the Beers Criteria chose, and pools these designs. One hit was dropped on reading: the tasimelteon phase III trial tests a receptor agonist, not melatonin.",
        [("NCT00230737 · ClinicalTrials.gov registration · COMPLETED, PHASE2, enrollment 27", "Melatonin Randomized Trial for Insomnia in the Elderly: melatonin 0.4 mg, 4.0 mg"),
         ("NCT07695246 · ClinicalTrials.gov registration", "CBT-I with adjuvant melatonin in older adults with chronic insomnia, randomised, double-blind, placebo-controlled"),
         ("Wade et al. · PMC open access · nightly prolonged release melatonin for 6 months", "\"the observed effect on sleep latency for patients aged 65-80 years (-15.6 min; 95% CI -25.3 to -6.0)\""),
         ("Use of Melatonin and/or Ramelteon for the Treatment of Insomnia in Older Adults · systematic review and meta-analysis · PMC open access", "\"searches were conducted from 1 January 1990 to 20 June 2021\"; Beers Criteria as the start"),
         ("Synnott et al. · tasimelteon phase III · PMC open access", "read and dropped: a melatonin receptor agonist, not melatonin")],
        None,
        "The primary outcome measure of NCT00230737 is on the registration, which this answer cited by title and arms; the endpoint line was not read. Whether the meta-analysis pooled Wade's trial is a question for its tables, one read away.",
        "lexical lane over origin:sleep · 497 documents held every term · 2 registrations, 3 papers kept, 1 read and dropped",
        "Real, from the sealed sleep collection, asked through the same engine the door serves, on 12 October 2026. Registrations and full texts on one answer, with the arms, the numbers and the one that did not belong.",
        title="docenta over MCP · the sleep collection",
    ),
    card="Human sleep research from the public biomedical infrastructure: the open-access full texts of PubMed Central articles under CC0, CC BY and CC BY-SA, ClinicalTrials.gov registrations, and one AHRQ evidence report from the NCBI Bookshelf (a US Government work). Every text is openly licensed or in the public domain and carries its licence and source. It holds no subscription literature, no abstracts of closed articles and no clinical practice guidelines; it is research literature, not medical advice.",
    sealed_line="Sealed 2026-09-22; 77,899 texts; nothing is added, changed or removed, and a question outside the collection is answered \"not in this corpus\".",
    reads=[("Full texts, openly licensed.", "", "PubMed Central articles under CC0, CC BY and CC BY-SA, normalized with their license flags, cited to the passage."),
           ("Trial registrations.", "", "ClinicalTrials.gov records with status, phase, enrollment, conditions and arms, so \"which trial tested what\" is answered from the registry and tied to the papers that report it."),
           ("What stays out.", "", "Abstract-only records, author manuscripts and publisher open access under other licenses, the clinical practice guidelines, and the literature indexes that need the reader's own subscription.")],
    wall_groups=[
        ("Trials and papers", ["Which trials registered this intervention, with which arms, and which papers report them?", "Which studies report this effect at this dose, and where do they disagree?", "Which registration belongs to this paper?"]),
        ("Over time", ["What is the earliest paper here making this claim, and did a replication fail?", "Which review pooled these trials, and what window did it search?"]),
        ("Evidence and gaps", ["Which papers cite the same underlying experiment rather than providing independent evidence?", "What does the collection not contain on this question?"]),
    ],
    wont=[("It is research literature, not medical advice.", "The door cites the paper, the page and the registration; what to do about it is not retrieval."),
          ("A near miss is read and dropped.", "A receptor agonist trial surfaced for a melatonin question; reading it put it out, and the answer says so."),
          ("The window is stated.", "A review's search dates are part of its citation, because a 2021 window cannot pool a 2026 trial."),
          ("The seal is the date.", "Nothing is added, changed or removed after the seal; a new seal means a new date on this page.")],
    host="sleep.docenta.ai", mcp_name="docenta-sleep", word="sleep",
    plug_lead="The sealed collection above is served as an MCP server at <strong>https://sleep.docenta.ai/mcp</strong>: a public collection we host on purpose so your assistant can ask it today. You add it once; from then on it asks the collection the way it asked the question above, and reads the paper or the registration back with its license.",
)

PLACEHOLDERS = {
    "diabetes": dict(
        title="docenta for diabetes research - the open corpus",
        desc="A sealed collection of open-access human diabetes research in the same shape as the sleep collection. In preparation; the collection is being gathered.",
        placard="Exhibit · docenta for diabetes research · The open corpus",
        h1="Ask the literature. <em>Get the paper, the page and the trial.</em>",
        sub="Human diabetes research from the public biomedical infrastructure, in the same shape as the sleep collection: open-access full texts, trial registrations, open Bookshelf titles and guidelines, across biology, types, the life course, therapy, technology, complications and the study families. <strong>Under collection; the card is written when the cut is known.</strong>",
        chip_qs=["Which trials tested this intervention, and what did they measure?", "Which papers report this outcome in this population, and where do they disagree?", "Which guideline recommends this, and on which studies?", "What does the collection not contain?"],
        card="The card is written when the collection is sealed: it will name the licenses inside, the registries tied to the papers, and everything left out, in the sleep collection's shape.",
        reads=[("The same infrastructure.", "", "PubMed, Europe PMC, PMC open access, OpenAlex, ClinicalTrials.gov, NCBI Bookshelf and curated guidelines, with the diabetes query library."),
               ("The same rights discipline.", "", "Every record carries its license; only the openly licensed full texts, trials and guidelines reach the public door."),
               ("Not yet.", "", "Collection started on 2026-09-17; normalization and the seal follow.")],
        status=[("collected", False), ("rights sorted", False), ("sealed", False), ("door", False)],
        note="Being gathered now; the door opens after the sleep collection and the three traditions.",
    ),
}

def placeholder(slug, title, desc, placard, h1, sub, chip_qs, card, reads, status, note):
    out = [head(title, desc, f"https://docenta.ai/for/{slug}/")]
    out.append(f"""
  <header>
    <div class="placard">{placard} <span class="soon">door in preparation</span></div>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
""")
    out.append(chips(chip_qs))
    st = "".join(f'<div class="{"done" if done else ""}"><b>{e(name)}</b>{"done" if done else "next"}</div>' for name, done in status)
    out.append(f"""
    <div class="status">{st}</div>
    <p class="term-note">{e(note)}</p>
  </header>

  <section>
    <div class="placard">The card, as the door will say it</div>
    <h2>What is in the collection, and what is not.</h2>
    <p class="lead">Every door carries a card, sealed with the collection and shown to your assistant on every connection. This one will read:</p>
    <div class="terminal" style="margin-top:26px"><div class="term-body"><p class="ans" style="margin:0">{e(card)}</p></div></div>
""")
    out.append(cards(reads))
    out.append(ALSO)
    out.append("""
  </section>
""")
    out.append(cta(slug, slug))
    out.append(FOOT)
    return "".join(out)

# ---------------------------------------------------------------- the plain pages
# Privacy and terms: the same chrome, running text. The privacy page is
# what the Google OAuth consent screen links to (Branding, 2026-10-12),
# so its Google user data section states the Limited Use compliance.
def plain(path, title, desc, placard, body):
    out = [head(title, desc, f"https://docenta.ai{path}").replace('href="#access"', 'href="/#access"')]
    out.append(f"""
  <header>
    <div class="placard">{placard}</div>
    {body}
  </header>
""")
    out.append(FOOT)
    return "".join(out)

PLAIN = {}
PLAIN["privacy"] = dict(
    title="docenta privacy policy - your files, mail and history stay on your machine",
    desc="What docenta sends to SKY, LLC and what it never does: your content stays on your computer; Google user data is read over IMAP on your machine only, under the Limited Use requirements.",
    placard="Exhibit · docenta · Privacy",
    body=r"""<h1>Privacy policy. <em>Your files, mail and history stay on your machine.</em></h1>
    <p class="eff">SKY, LLC &middot; docenta &middot; effective 2026-10-12</p>
<div class="prose">
<h2>What docenta is</h2>
<p>docenta is software you install on your own computer. It reads the files, mail archives, mail accounts, repositories and AI session transcripts you point it at, builds a searchable index of them on that computer, and answers questions from it. Originals are never copied anywhere, and the index, the extracted text and the models that run over them live on your machine. SKY, LLC operates no service that holds your content.</p>

<h2>What the software sends to SKY, LLC</h2>
<p>docenta talks to our servers for four things and nothing else.</p>
<ul>
<li><strong>Downloads.</strong> Binaries, models and updates come from dl.docenta.ai. Like any web server, it logs the address a request came from and the time.</li>
<li><strong>Licensing.</strong> Your installation generates a key pair on your machine. The public half identifies the machine to our license service at license.docenta.ai, which issues and renews a lease. The service learns that key, the time of each renewal and the address the request came from. It does not learn what you indexed or asked.</li>
<li><strong>Turbo, only on your word.</strong> When you consent to the turbo lane, docenta packs the extracted text of your pending documents, seals it with encryption to a key that exists only on your machine, and sends the sealed pack through our relay to a GPU rented for that one job. The relay sees ciphertext only. The rented machine computes search vectors, returns them sealed, and is destroyed afterwards. Nothing ships without an explicit consent naming the hours, and <code>docenta cloud consent 0</code> withdraws it.</li>
<li><strong>Early access requests.</strong> If you fill in the form on this site, we keep the name, address and question you typed, after you confirm the address by mail, to write back when the door opens. Nothing else is collected and there is no newsletter.</li>
</ul>
<p>docenta sends no telemetry, no usage statistics and no crash reports.</p>

<h2>Google user data</h2>
<p>When you connect a Google account with "Sign in with Google", docenta asks Google for the mail scope (<code>https://mail.google.com/</code>) so it can read your mailbox over IMAP, the same way a desktop mail program does. This section describes how that data is handled.</p>
<ul>
<li><strong>Where the permission lives.</strong> The token Google hands back is stored in your operating system's credential store on your computer (Keychain on macOS, Credential Manager on Windows, the secret service on Linux). It is never written to a file and never sent to SKY, LLC.</li>
<li><strong>What docenta does with your mail.</strong> It fetches messages and attachments to your computer, extracts their text, and indexes them there so you can search and ask questions about them. That is the only use.</li>
<li><strong>What docenta does not do.</strong> Your mail is not transferred to SKY, LLC servers, not sold, not used for advertising, not used to build models or profiles, and not read by any person at SKY, LLC. The one transfer that can occur is the turbo lane described above: extracted text sealed to your own key, sent only on your explicit consent, processed on a machine rented for your job alone, for the sole purpose of building your own search index, and destroyed afterwards.</li>
<li><strong>Limited use.</strong> docenta's use and transfer of information received from Google APIs adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy#additional_requirements_for_specific_api_scopes">Google API Services User Data Policy</a>, including the Limited Use requirements.</li>
<li><strong>Taking it back.</strong> Remove docenta at <a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a> and it stops fetching mail and says so. <code>docenta uninstall mail</code> revokes the grant, deletes the token from the credential store and removes the fetched mail from your machine. <code>docenta uninstall --everything</code> removes everything docenta kept.</li>
</ul>

<h2>Other mail providers</h2>
<p>An account at another provider is connected with an app password you make on the provider's own page. docenta stores it in the same operating system credential store, uses it only to fetch your mail to your computer, and never sends it anywhere.</p>

<h2>Retention and deletion</h2>
<p>Everything docenta builds is on your computer, under your control, and the remove command above takes it away part by part or all at once. License records are kept while your installation holds a lease. An early access request is kept until we have written back or you ask us to drop it. Write to <a href="mailto:docenta@docenta.ai">docenta@docenta.ai</a> and we delete what we hold about you.</p>

<h2>Children</h2>
<p>docenta is not directed to children under 13 and we do not knowingly collect information from them.</p>

<h2>Changes and contact</h2>
<p>When this policy changes, the date at the top changes with it and the current text is always at docenta.ai/privacy. Questions go to <a href="mailto:docenta@docenta.ai">docenta@docenta.ai</a>. SKY, LLC, California, United States.</p>
</div>""")
PLAIN["terms"] = dict(
    title="docenta terms of service - a private preview, on your own machine",
    desc="The terms under which SKY, LLC licenses docenta: a proprietary private preview, your content stays yours, no warranty, California law.",
    placard="Exhibit · docenta · Terms",
    body=r"""<h1>Terms of service. <em>A private preview, on your own machine, on these terms.</em></h1>
    <p class="eff">SKY, LLC &middot; docenta &middot; effective 2026-10-12</p>
<div class="prose">
<h2>The agreement</h2>
<p>These terms are between you and SKY, LLC ("SKY", "we") and govern docenta, the software, its updates, the docenta.ai site and the services the software talks to. By installing or using docenta you accept them. If you use docenta for an organization, you accept them on its behalf.</p>

<h2>The license</h2>
<p>docenta is proprietary software. SKY grants you a personal, non-exclusive, non-transferable license to install and run it on machines you control, for the term of your lease, under the license text that ships with it. You may not sell, sublicense, reverse engineer or redistribute it, or use it to build a competing product. docenta is in private preview: features, prices and terms may change, and access may end, with notice where we can give it.</p>

<h2>Your content</h2>
<p>Everything docenta indexes stays yours. We claim no rights to your files, mail, repositories or transcripts, and the <a href="/privacy/">privacy policy</a> says exactly what the software sends us, which is not your content. You are responsible for having the right to index what you point docenta at, including mail accounts and shared drives.</p>

<h2>Connected accounts</h2>
<p>When you connect a mail account, you authorize docenta to fetch that account's mail to your computer. A Google account connected with "Sign in with Google" is subject to Google's terms as well as these, and our handling of Google user data is described in the privacy policy. You can disconnect an account at any time from the provider's permissions page or with <code>docenta uninstall mail</code>.</p>

<h2>The turbo lane</h2>
<p>The turbo lane rents a GPU on your explicit consent, which names a number of hours. The consent is the authorization to spend that amount on your behalf; the rate card shown before you consent is the price. Sealed packs are processed on a machine rented for your job alone and destroyed afterwards.</p>

<h2>Acceptable use</h2>
<p>Do not use docenta to index content you have no right to hold, to break the law, or to attack, probe or overload our services. Do not share license leases between people.</p>

<h2>No warranty</h2>
<p>docenta is provided as is and as available. To the fullest extent the law allows, SKY disclaims all warranties, express or implied, including merchantability, fitness for a particular purpose and non-infringement. Answers are reconstructed from your own material and cite it; verify them before you act on them.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent the law allows, SKY is not liable for indirect, incidental, special, consequential or punitive damages, or for lost data, profits or revenue, arising from docenta or these terms, and SKY's total liability for any claim is limited to the amount you paid SKY for docenta in the twelve months before the claim.</p>

<h2>Termination</h2>
<p>You may stop using docenta at any time; <code>docenta uninstall --everything</code> removes what it kept. We may end your access if you break these terms. Sections on your content, no warranty, limitation of liability and governing law survive.</p>

<h2>Governing law and contact</h2>
<p>These terms are governed by the laws of the State of California, United States, without regard to its conflict of law rules. When these terms change, the date at the top changes with them and the current text is always at docenta.ai/terms. Questions go to <a href="mailto:docenta@docenta.ai">docenta@docenta.ai</a>.</p>
</div>""")

PLAIN["results"] = dict(
    title="docenta results - where docenta stands on public benchmarks",
    desc="docenta's retrieval on LongMemEval-S and LoCoMo beside the published numbers of other retrievers and memory systems, against grep and Spotlight on a real machine, with every source and caveat.",
    placard="Exhibit · docenta · Results",
    body=r"""<h1>Results. <em>Where docenta stands on public benchmarks, beside the numbers others have published.</em></h1>
    <p class="eff">SKY, LLC &middot; docenta 0.3.2 &middot; measured 2026-10-30 and 2026-10-31 on one MacBook Pro (M4 Max)</p>
<div class="prose">
<h2>Where docenta stands, in four lines</h2>
<ul>
<li><strong>LongMemEval-S retrieval:</strong> in the top band of the published retrievers measured the same way: 0.956 of questions find an evidence session in the top five, against 0.966 for the best raw retriever we found published (MemPalace, MiniLM embeddings) and 0.862 for a stemmed BM25. Grep over the same files finds 0.75.</li>
<li><strong>LoCoMo retrieval:</strong> ahead of the paper's own retrieval baseline at five and ten sessions (80.0 and 91.2 against 72.1 and 84.7, the paper's metric), slightly behind it at two (63.0 against 65.9).</li>
<li><strong>On a real machine:</strong> the evidence for 114 of 227 questions in the top ten, against 42 to 47 for Spotlight, ripgrep and ripgrep-all, and an agent reads 20 KB to reach it instead of 2.2 to 2.7 MB.</li>
<li><strong>Answer accuracy</strong> (what memory products usually quote) is a different measure: it scores an answering model and a judge as well as the retrieval. Those numbers are listed below for orientation, in their own tables, never in the same column as ours.</li>
</ul>
<p>What is measured here is retrieval: did the evidence land on the page an agent reads. Every store was built on the machine by the shipped binaries; no model wrote, rewrote or summarized anything that was indexed.</p>

<h2>LongMemEval-S: 500 questions, about 50 chat sessions each</h2>
<p>LongMemEval (Wu et al., ICLR 2025), the S split, cleaned. Each question gets its own store holding only its haystack. Session level: a hit is an evidence session in the top k.</p>
<p><strong>Beside published retrievers measured the same way</strong> (same split, same unit, recall_any: any evidence session in the top k, all 500 questions):</p>
<div class="tablewrap"><table class="jobs">
<thead><tr><th>retriever</th><th>recall@5</th><th>recall@10</th><th>source</th></tr></thead>
<tbody>
<tr><td>MemPalace, raw (ChromaDB, all-MiniLM-L6-v2, no LLM)</td><td>0.966</td><td>about 0.98</td><td>project benchmark page, self-reported</td></tr>
<tr><td><strong>docenta lexical channel (BM25)</strong></td><td><strong>0.956</strong></td><td><strong>0.976</strong></td><td>this page</td></tr>
<tr><td>agentmemory, BM25 + MiniLM vectors</td><td>0.952</td><td>0.986</td><td>project repo, self-reported, older pipeline</td></tr>
<tr><td><strong>docenta hybrid (lexical, sparse and dense fused)</strong></td><td><strong>0.948</strong></td><td><strong>0.976</strong></td><td>this page</td></tr>
<tr><td><strong>docenta dense channel (arctic-embed-m-v2.0)</strong></td><td><strong>0.940</strong></td><td><strong>0.966</strong></td><td>this page</td></tr>
<tr><td>agentmemory, BM25 with stemming and synonyms</td><td>0.862</td><td>0.946</td><td>project repo, self-reported</td></tr>
<tr><td>docenta keyword tool (every word of the question)</td><td>0.89</td><td>0.90</td><td>this page</td></tr>
<tr><td>grep (ripgrep, ranked by distinct terms matched)</td><td>0.75</td><td>0.86</td><td>this page</td></tr>
</tbody></table></div>
<p><strong>The benchmark's own strict metric.</strong> The official scorer also reports recall_all (EVERY evidence session in the top k) over the 470 questions that have an answer. docenta: lexical 0.832 at five and 0.900 at ten, hybrid 0.843 and 0.917, dense 0.813 and 0.904. The paper's own retriever table (BM25 0.634, Contriever 0.723, Stella 0.720 at five) was measured on the M split, ten times the haystack per question, so it is not a like-for-like row and is not set beside ours. One later paper reports the strict metric on the S split (Associa, ACL Findings 2025): BM25 0.51, Contriever 0.67, Stella 0.70, BGE-m3 0.75, Associa 0.87 at five, with keys built from the user's turns only; read it as orientation, the units are not fully stated.</p>
<p>Where the words differ from the evidence, fusion pays: on preference questions ("what would I like ...") lexical finds 0.73 at five, dense and hybrid 0.93. Where the question quotes the user, lexical wins (0.99 against hybrid's 0.93). The keyword tool is the weak rung by design: it asks for every word, which is right for exact terms and wrong for a question phrased unlike its evidence, and the tool descriptions send questions to the meaning tool for that reason.</p>
<p><strong>Answer accuracy on LongMemEval-S, for orientation only</strong> (an answering model reads what was retrieved and a judge model grades it; not comparable with the recall above):</p>
<div class="tablewrap"><table class="jobs">
<thead><tr><th>system</th><th>answering model</th><th>accuracy</th><th>source</th></tr></thead>
<tbody>
<tr><td>Full context (the whole haystack in the prompt)</td><td>GPT-4o</td><td>60.6%</td><td>LongMemEval paper</td></tr>
<tr><td>Zep</td><td>GPT-4o</td><td>71.2%</td><td>Zep paper (arXiv 2501.13956)</td></tr>
<tr><td>Mastra, RAG top 20</td><td>GPT-4o</td><td>80.05%</td><td>Mastra research page, self-reported</td></tr>
<tr><td>Mastra, observational memory</td><td>GPT-4o</td><td>84.23%</td><td>same</td></tr>
<tr><td>Emergence, internal system</td><td>GPT-4o</td><td>86.0%</td><td>Emergence blog, self-reported</td></tr>
</tbody></table></div>

<h2>LoCoMo: 1,982 questions over ten long conversations</h2>
<p>LoCoMo (Maharana et al., ACL 2024, CC BY-NC 4.0), every session one Add and every question one Search, through the same Add/Search adapter docenta entered the Agent Memory Leaderboard with. Conversations hold 19 to 32 sessions, so ten sessions are about a third of a conversation: a generous k, and said so.</p>
<p><strong>Beside the paper's retrieval baseline</strong> (the paper's metric: the share of a question's evidence sessions in the top k, averaged; DRAGON retriever; their unit is an LLM-written summary of each session, ours the session itself):</p>
<div class="tablewrap"><table class="jobs">
<thead><tr><th>sessions retrieved</th><th>paper: DRAGON over session summaries</th><th>docenta over the raw sessions</th></tr></thead>
<tbody>
<tr><td>2</td><td>65.9</td><td>63.0</td></tr>
<tr><td>5</td><td>72.1</td><td><strong>80.0</strong></td></tr>
<tr><td>10</td><td>84.7</td><td><strong>91.2</strong></td></tr>
</tbody></table></div>
<p>In the plainer metric (any evidence session in the top k): 0.53 at one, 0.85 at five, 0.94 at ten; every cited session at ten 0.87; search p50 0.41 s. Rank 1 is the weak spot: two people talk about the same few subjects for months, so the session that answers competes with near-copies of itself. The paper's turn-level rows (56.7 at five turns) measure a finer unit and are not set beside these.</p>
<p><strong>Answer accuracy on LoCoMo, for orientation only</strong> (judge GPT-4o-mini, adversarial questions excluded; not comparable with the recall above):</p>
<div class="tablewrap"><table class="jobs">
<thead><tr><th>system</th><th>judged accuracy</th><th>source</th></tr></thead>
<tbody>
<tr><td>Best plain RAG (2 chunks of 256 tokens)</td><td>60.97</td><td>Mem0 paper (arXiv 2504.19413)</td></tr>
<tr><td>Mem0 / Mem0 with graph</td><td>66.88 / 68.44</td><td>same</td></tr>
<tr><td>Full context</td><td>72.90</td><td>same</td></tr>
<tr><td>Letta, filesystem agent</td><td>74.0</td><td>Letta blog</td></tr>
<tr><td>Zep, as corrected by Zep</td><td>75.14</td><td>Zep blog</td></tr>
</tbody></table></div>

<h2>On a real machine: against grep and Spotlight</h2>
<p>227 questions about one person's own machine (repositories, mail, agent sessions), every tool run by the same deterministic policy and judged by the same truth. These questions are ours and self-judged; the public sets above exist to answer that.</p>
<div class="tablewrap"><table class="jobs">
<thead><tr><th>tool</th><th>truth in top 10</th><th>what the agent reads to reach it (median)</th></tr></thead>
<tbody>
<tr><td><strong>docenta meaning tool</strong></td><td><strong>114 of 227</strong></td><td><strong>20 KB</strong></td></tr>
<tr><td>docenta keyword tool</td><td>63</td><td>19 KB</td></tr>
<tr><td>ripgrep-all (reads PDFs and Office files)</td><td>47</td><td>2.2 MB</td></tr>
<tr><td>ripgrep</td><td>44</td><td>2.7 MB</td></tr>
<tr><td>Spotlight (mdfind)</td><td>42</td><td>19 KB</td></tr>
</tbody></table></div>
<p>Spotlight is the real competitor on one shape, filename-like code questions, and answers in about 100 ms; it cannot see hidden folders, where mail and sessions live. 100 of the 227 questions no tool answered in the top ten.</p>

<h2>The Agent Memory Leaderboard</h2>
<p>agentmemoryleaderboard.ai scores memory systems end to end: the system serves Add and Search, the leaderboard fixes the answering model, the prompts and the judge, and reports judged accuracy over a mix of public sets (PersonaMem, LoCoMo-Refined, LongMemEval and others). For orientation, its first cycle (published 2026-08-12, textual track): industry entries from 58.02 (MemoraX) down, Mem0 41.40, MemPalace 39.48; in the academic table a SQLite full-text baseline scored 41.79 and a plain BM25 38.47. docenta entered the second cycle on 2026-10-31 as 0.3.2; its score will stand here when it is published, wherever it lands.</p>

<h2>Invented tool calls</h2>
<p>A probe in the classes of the Hallucinated-Tools Benchmark (arXiv 2609.19425), whose suite is not published, so this is not an HTB score: 32 invented calls against docenta's MCP surface, 10 honest ones. Every invented tool name is refused and named, no honest call is refused.</p>

<h2>The harness</h2>
<p>Every number of ours comes from a script in the docenta repository that builds the stores, runs the queries and writes one audit row per question: <code>scripts/eval/longmemeval.py</code> and <code>scripts/eval/lme-official.py</code> (the official metrics), <code>scripts/eval/aml.py locomo</code>, <code>scripts/eval/head-to-head.py</code>, <code>scripts/eval/tool-calls.py</code>. Published numbers are quoted with their source and labelled where the source reports on itself. The repository is in private preview; write to <a href="mailto:docenta@docenta.ai">docenta@docenta.ai</a> for the harness and the audit files.</p>
</div>""")

def main():
    written = []
    path = os.path.join(ROOT, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(index_page())
    written.append(path)
    for slug, spec in PLACEHOLDERS.items():
        d = os.path.join(ROOT, "for", slug)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(placeholder(slug, **spec))
        written.append(path)
    for slug, spec in DOORS.items():
        d = os.path.join(ROOT, "for", slug)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(door_page(slug, **spec))
        written.append(path)
    for slug, spec in PAGES.items():
        d = os.path.join(ROOT, "for", slug)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(specialty(slug, **spec))
        written.append(path)
    for slug, spec in PLAIN.items():
        d = os.path.join(ROOT, slug)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(plain(f"/{slug}/", **spec))
        written.append(path)
    written.extend(sitemap_and_robots(written))
    for p in written:
        print("wrote", os.path.relpath(p, ROOT))


def sitemap_and_robots(pages):
    """sitemap.xml and robots.txt beside the pages: every generated page
    that does not say noindex, with the day its file last changed in git
    (today for a file git does not know yet). Search Console 2026-11-09:
    the site had neither, and Google found the doors' /mcp addresses
    before some of the pages."""
    import subprocess, datetime
    # Pages the generator does not write but the site serves (the handbook,
    # rendered by handbook-html in the docenta repo) join the list; a path
    # held back in .assetsignore is not served and stays out.
    held = set()
    try:
        with open(os.path.join(ROOT, ".assetsignore"), encoding="utf-8") as f:
            held = {line.strip().strip("/") for line in f if line.strip() and not line.startswith("#")}
    except OSError:
        pass
    pages = list(pages)
    handbook = os.path.join(ROOT, "handbook", "index.html")
    if os.path.isfile(handbook) and handbook not in pages:
        pages.append(handbook)
    urls = []
    for path in pages:
        rel_dir = os.path.relpath(os.path.dirname(path), ROOT)
        if rel_dir.split(os.sep)[0] in held:
            continue
        with open(path, encoding="utf-8") as f:
            if 'name="robots"' in f.read(4096):
                continue
        rel = os.path.relpath(path, ROOT)
        loc = "https://docenta.ai/" + ("" if rel == "index.html" else rel[: -len("index.html")])
        day = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        urls.append((loc, day or datetime.date.today().isoformat()))
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, day in urls:
        out.append(f"  <url><loc>{html.escape(loc)}</loc><lastmod>{day}</lastmod></url>")
    out.append("</urlset>")
    sitemap = os.path.join(ROOT, "sitemap.xml")
    with open(sitemap, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    robots = os.path.join(ROOT, "robots.txt")
    with open(robots, "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: https://docenta.ai/sitemap.xml\n")
    return [sitemap, robots]

if __name__ == "__main__":
    main()
