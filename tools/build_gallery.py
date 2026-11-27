#!/usr/bin/env python3
"""Generate site/index.html, site/apk/index.html and site/web/index.html from gallery/*.json.
Run from the repo root: python3 tools/build_gallery.py"""
import html, json, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
e = lambda s: html.escape(str(s), quote=True)
CSS = """:root{color-scheme:light dark;--bg:#fafaf7;--fg:#1d1d1b;--mu:#605f58;--card:#fff;--ln:#dcdad0;--ac:#0b6b4f}
@media(prefers-color-scheme:dark){:root{--bg:#161614;--fg:#eeede6;--mu:#a5a398;--card:#1f1f1c;--ln:#37362f;--ac:#6fd1ad}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif}
main{max-width:860px;margin:0 auto;padding:20px 16px 48px}h1{font-size:1.6rem;margin:.2em 0}h2{font-size:1.15rem;margin:1.8em 0 .6em}
p.lead{color:var(--mu);margin:.3em 0 1em}a{color:var(--ac)}nav a{margin-right:14px}
.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}
.card{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:6px}
.top{display:flex;gap:12px;align-items:center}.top img,.ph{width:64px;height:64px;border-radius:14px;flex:none}
.ph{background:var(--ln);display:grid;place-items:center;font-weight:700;font-size:1.6rem;color:var(--mu)}
.card h3{margin:0;font-size:1.05rem}.tag{font-size:.78rem;color:var(--mu)}.card p{margin:0;color:var(--mu);font-size:.92rem;overflow-wrap:anywhere}
.btn{display:inline-block;padding:7px 12px;border-radius:8px;border:1px solid var(--ac);text-decoration:none;font-size:.92rem;margin:4px 6px 0 0}
.btn.main{background:var(--ac);color:var(--bg)}code{font-size:.72rem;word-break:break-all;color:var(--mu)}
[hidden]{display:none!important}.app-picker{display:grid;grid-template-columns:repeat(auto-fill,minmax(64px,1fr));gap:8px;margin:12px 0 20px}.app-filter{font:inherit;font-size:.75rem;line-height:1.25;min-height:92px;padding:8px 3px;background:var(--card);color:var(--fg);border:1px solid var(--ln);border-radius:12px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;overflow-wrap:anywhere}.app-filter img,.app-filter .ph{width:44px;height:44px;border-radius:10px}.app-filter[aria-pressed=true],.filter-toolbar .btn[aria-pressed=true]{border:2px solid var(--ac);background:color-mix(in srgb,var(--ac) 9%,var(--card))}.app-filter:focus-visible{outline:3px solid var(--ac);outline-offset:2px}.filter-toolbar{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.filter-toolbar p{margin:0;color:var(--mu);font-size:.85rem}.filter-toolbar .btn{font:inherit;cursor:pointer;background:var(--card);color:var(--ac)}
footer{margin-top:2.4em;color:var(--mu);font-size:.85rem}
ul.index{padding-left:1.2em}ul.index li{margin:5px 0}
h2 .permalink{margin-left:.55rem;padding:0 .4rem;border:1px solid transparent;border-radius:5px;background:none;color:var(--mu);font:inherit;font-size:.9rem;line-height:1.4;cursor:pointer;vertical-align:middle}
h2 .permalink:hover,h2 .permalink:focus-visible{border-color:var(--ac);color:var(--ac)}"""
PERMALINK_JS = """<script>
document.addEventListener("click", async (event) => {
  const button = event.target.closest(".permalink");
  if (!button) return;
  const original = button.textContent;
  const url = location.origin + location.pathname + "#" + button.dataset.section;
  try {
    await navigator.clipboard.writeText(url);
    button.textContent = "Copied";
  } catch {
    button.textContent = "Copy failed";
  }
  window.setTimeout(() => { button.textContent = original; }, 1600);
});
</script>"""
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "section"
def h2p(title_html, sid): return f'<h2 id="{sid}">{title_html}<button class="permalink" type="button" data-section="{sid}" aria-label="Copy link to this section" title="Copy link to this section">#</button></h2>'
def page(title, lead, body, base):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><style>{CSS}</style></head><body><main>
<nav><a href="{base}">kaji</a><a href="{base}apk/">apps</a><a href="{base}web/">web examples</a></nav>
<h1>{e(title)}</h1><p class="lead">{lead}</p>{body}
<footer>Public information only. Pages are maintained by Instinct (an AI assistant) from <a href="https://github.com/irvan-putra/kaji/tree/main/gallery">gallery/*.json</a>; each card states its status.<br>Built with AI assistance (Instinct and others). Not everything has been reviewed by Irvan.</footer>
</main>{PERMALINK_JS}</body></html>"""
def btn(label, url, main=False): return f'<a class="btn{" main" if main else ""}" href="{e(url)}">{e(label)}</a>'
def apps():
    d = json.loads((root/"gallery/apps.json").read_text())
    groups = {"available": "Available now", "pending": "Qualification in progress", "source": "Source only, no APK", "legacy": "Previous builds"}
    unique = {}
    for a in d["apps"]:
        if a["name"] not in unique: unique[a["name"]] = a
    out = '<section aria-label="Filter builds by app">' + h2p("Choose an app", "choose-an-app") + '<div class="filter-toolbar"><button class="btn" type="button" data-filter="" aria-pressed="true">All apps</button><p id="filter-status" role="status" aria-live="polite"></p></div><div class="app-picker">'
    for name, a in unique.items():
        icon = f'<img src="icons/{e(a["icon"])}" alt="" width="44" height="44">' if a.get("icon") else f'<span class="ph" aria-hidden="true">{e(name[0])}</span>'
        out += f'<button class="app-filter" type="button" data-filter="{e(name)}" aria-pressed="false">{icon}<span>{e(a.get("display_name", name))}</span></button>'
    out += '</div><noscript>Filtering needs JavaScript. All builds and download links are listed below.</noscript></section>'
    for g, title in groups.items():
        items = [a for a in d["apps"] if a["state"] == g]
        if not items: continue
        out += f"<section class='build-group'>" + h2p(e(title), slug(title)) + "<div class='grid'>"
        for a in items:
            icon = f'<img src="icons/{e(a["icon"])}" alt="{e(a.get("display_name", a["name"]))} launcher icon" width="64" height="64">' if a.get("icon") else f'<div class="ph" aria-hidden="true">{e(a["name"][0])}</div>'
            ver = f' {e(a["version"])}' if a.get("version") else ""
            b = ""
            if a.get("apk"): b += btn("Download APK", a["apk"], True)
            if a.get("release"): b += btn("Release page", a["release"])
            b += btn("Source", a["repo"])
            sha = f'<code>SHA-256 {e(a["sha256"])}</code>' if a.get("sha256") else ""
            out += f'<div class="card" data-app="{e(a["name"])}"><div class="top">{icon}<div><h3>{e(a.get("display_name", a["name"]))}{ver}</h3><div class="tag">{e(a["tag"])}</div></div></div><p>{e(a["about"])}</p><div>{b}</div>{sha}</div>'
        out += "</div></section>"
    out += """<script>(()=>{const buttons=[...document.querySelectorAll('[data-filter]')],cards=[...document.querySelectorAll('[data-app]')],groups=[...document.querySelectorAll('.build-group')];function filter(name){for(const b of buttons)b.setAttribute('aria-pressed',String(b.dataset.filter===name));for(const c of cards)c.hidden=!!name&&c.dataset.app!==name;for(const g of groups)g.hidden=![...g.querySelectorAll('[data-app]')].some(c=>!c.hidden);const n=cards.filter(c=>!c.hidden).length;document.getElementById('filter-status').textContent=(name?(buttons.find(b=>b.dataset.filter===name)?.textContent||name)+': ':'All apps: ')+n+' build'+(n===1?'':'s');}for(const b of buttons)b.addEventListener('click',()=>filter(b.dataset.filter));filter('');})();</script>"""
    lead = f'Current Android APKs, with versioned downloads and status. Check the SHA-256 after downloading. Status as of {e(d["checked"])}. Previous builds are listed separately below.'
    return page("kaji apps", lead, out, "../")
def web():
    d = json.loads((root/"gallery/web.json").read_text())
    # Every listed example has public source. Fail rather than silently omit a button.
    for sec in d["sections"]:
        for item in sec["items"]:
            if not item.get("source", "").startswith("https://github.com/"):
                raise ValueError("Missing GitHub source for " + item["name"])
    out = ""
    for sec in d["sections"]:
        out += h2p(e(sec["title"]), slug(sec["title"])) + '<div class="grid">'
        for w in sec["items"]:
            b = btn("Open", w["url"], True) + (btn("Source", w["source"]) if w.get("source") else "")
            if w.get("android"): b += btn("Android test release", w["android"])
            out += f'<div class="card"><div class="top"><img src="{e(w["icon"])}" alt="{e(w["icon_note"])}" width="64" height="64"><div><h3>{e(w["name"])}</h3><div class="tag">{e(w["tag"])}</div></div></div><p>{e(w["about"])}</p><div>{b}</div></div>'
        out += "</div>"
    return page("kaji web examples", f'Pages, demos and examples made with Instinct (an AI assistant). Links checked {e(d["checked"])} by Instinct (an AI assistant). Proposals and simulations are labeled as such. Numbered app icons identify the linked Android build, not a web version. Web-only projects use category symbols where no project icon exists.', out, "../")
def notes():
    out = []
    for f in sorted((root/"site").rglob("index.html")):
        rel = f.relative_to(root/"site")
        if len(rel.parts) == 1 or rel.parts[0] in ("apk", "web", "assets"):
            continue
        m = re.search(r"<title>(.*?)</title>", f.read_text(), re.S)
        if not m: continue
        t = re.sub(r"\s*\|\s*[Kk]aji\s*$", "", html.unescape(m.group(1))).strip()
        out.append((t, str(rel.parent) + "/"))
    out.sort(key=lambda x: x[0].lower())
    return "".join(f'<li><a href="{e(u)}">{e(t)}</a></li>' for t, u in out)
def home():
    body = "<div class='grid'><div class='card'><h3>Apps</h3><p>APK downloads, icons and status for every Android app.</p><div>" + btn("Open", "apk/", True) + "</div></div><div class='card'><h3>Web examples</h3><p>Animate, the cook recipe boxes, Indomie, charts and concept pages.</p><div>" + btn("Open", "web/", True) + "</div></div><div class='card'><h3>Research notes</h3><p>Cross-project notes in the repository.</p><div>" + btn("Read", "https://github.com/irvan-putra/kaji#notes") + "</div></div></div>"
    body += h2p("Notes and pages", "notes-and-pages") + '<ul class="index">' + notes() + "</ul>"
    body += (h2p("Examples", "examples") + '<ul class="index">'
             '<li><a href="indomie/">Indomie Mi Goreng: the customizable recipe box</a></li>'
             '<li><a href="cook/">Kaji cook: customizable recipe boxes</a></li>'
             '<li><a href="economics-synthetic/">Cash and time: synthetic break-even charts</a></li>'
             '<li><a href="tumbuh/">Tumbuh&#39;s first page (draft)</a></li></ul>')
    return page("kaji", "Research notes, apps and examples from building personal software. Every note and page is indexed below.", body, "./")
for p, h in (("site/index.html", home()), ("site/apk/index.html", apps()), ("site/web/index.html", web())):
    f = root/p; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(h)
print("ok")
