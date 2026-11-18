#!/usr/bin/env python3
"""Generate site/index.html, site/apk/index.html and site/web/index.html from gallery/*.json.
Run from the repo root: python3 tools/build_gallery.py"""
import html, json, pathlib
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
footer{margin-top:2.4em;color:var(--mu);font-size:.85rem}"""
def page(title, lead, body, base):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><style>{CSS}</style></head><body><main>
<nav><a href="{base}">kaji</a><a href="{base}apk/">apps</a><a href="{base}web/">web examples</a></nav>
<h1>{e(title)}</h1><p class="lead">{lead}</p>{body}
<footer>Public information only. Pages are hand-maintained from <a href="https://github.com/irvan-putra/kaji/tree/main/gallery">gallery/*.json</a>; each card states its status.</footer>
</main></body></html>"""
def btn(label, url, main=False): return f'<a class="btn{" main" if main else ""}" href="{e(url)}">{e(label)}</a>'
def apps():
    d = json.loads((root/"gallery/apps.json").read_text())
    groups = {"available": "Available now", "pending": "Corrected build in progress", "source": "Source only, no APK", "legacy": "Previous builds"}
    out = ""
    for g, title in groups.items():
        items = [a for a in d["apps"] if a["state"] == g]
        if not items: continue
        out += f"<h2>{e(title)}</h2><div class='grid'>"
        for a in items:
            icon = f'<img src="icons/{e(a["icon"])}" alt="{e(a["name"])} launcher icon" width="64" height="64">' if a.get("icon") else f'<div class="ph" aria-hidden="true">{e(a["name"][0])}</div>'
            ver = f' {e(a["version"])}' if a.get("version") else ""
            b = ""
            if a.get("apk"): b += btn("Download APK", a["apk"], True)
            if a.get("release"): b += btn("Release page", a["release"])
            b += btn("Source", a["repo"])
            sha = f'<code>SHA-256 {e(a["sha256"])}</code>' if a.get("sha256") else ""
            out += f'<div class="card"><div class="top">{icon}<div><h3>{e(a["name"])}{ver}</h3><div class="tag">{e(a["tag"])}</div></div></div><p>{e(a["about"])}</p><div>{b}</div>{sha}</div>'
        out += "</div>"
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
        out += f'<h2>{e(sec["title"])}</h2><div class="grid">'
        for w in sec["items"]:
            b = btn("Open", w["url"], True) + (btn("Source", w["source"]) if w.get("source") else "")
            out += f'<div class="card"><h3>{e(w["name"])}</h3><div class="tag">{e(w["tag"])}</div><p>{e(w["about"])}</p><div>{b}</div></div>'
        out += "</div>"
    return page("kaji web examples", f'Pages, demos and examples we made. Links checked {e(d["checked"])}. Proposals and simulations are labeled as such.', out, "../")
def home():
    body = "<div class='grid'><div class='card'><h3>Apps</h3><p>APK downloads, icons and status for every Android app.</p><div>" + btn("Open", "apk/", True) + "</div></div><div class='card'><h3>Web examples</h3><p>Animate, the cook recipe boxes, Indomie, charts and concept pages.</p><div>" + btn("Open", "web/", True) + "</div></div><div class='card'><h3>Research notes</h3><p>Cross-project notes in the repository.</p><div>" + btn("Read", "https://github.com/irvan-putra/kaji#notes") + "</div></div></div>"
    return page("kaji", "Research notes, apps and examples from building personal software.", body, "./")
for p, h in (("site/index.html", home()), ("site/apk/index.html", apps()), ("site/web/index.html", web())):
    f = root/p; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(h)
print("ok")
