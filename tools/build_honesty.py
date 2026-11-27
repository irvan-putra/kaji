#!/usr/bin/env python3
"""Build site/honesty/index.html from gallery/honesty.json (AI-written by Instinct)."""
import json, html, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((root/"gallery/honesty.json").read_text())
e = lambda s: html.escape(str(s), quote=True)
CSS = open(root/"site/reuse/index.html").read().split("<style>")[1].split("</style>")[0]
if ".permalink" not in CSS:
    CSS += ("\nh2 .permalink{margin-left:.55rem;padding:0 .4rem;border:1px solid transparent;border-radius:5px;"
            "background:none;color:#7d877f;font:inherit;font-size:.9rem;line-height:1.4;cursor:pointer;vertical-align:middle}"
            "\nh2 .permalink:hover,h2 .permalink:focus-visible{border-color:#156c60;color:#156c60}\n")
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
def h2p(title, sid): return (f'<h2 id="{sid}">{e(title)}<button class="permalink" type="button" data-section="{sid}" '
                             f'aria-label="Copy link to this section" title="Copy link to this section">#</button></h2>')
def links(cs): return " ".join(f'<a href="{e(c["url"])}">{e(c["sha"])}</a>' for c in cs)
rows = "".join(
 f'<tr><td data-label="Repo">{e(r["repo"])}</td><td data-label="Where">{e(r["what"])}</td>'
 f'<td data-label="Before">{e(r["before"])}</td><td data-label="After">{e(r["after"])}</td>'
 f'<td data-label="Commits">{links(r["commits"])}</td><td data-label="Live"><a href="{e(r["live"])}">open</a></td>'
 f'<td data-label="Status">{e(r["status"])}{("<br>"+e(r["note"])) if r.get("note") else ""}</td></tr>' for r in d["changes"])
disc = "".join(
 f'<tr><td data-label="Repo">{e(r["repo"])}</td><td data-label="Commit"><a href="{e(r["url"])}">{e(r["sha"])}</a></td>'
 f'<td data-label="Live"><a href="{e(r["live"])}">open</a></td></tr>' for r in d["disclosure"])
plan = "".join(f"<li>{e(x)}</li>" for x in d.get("planned", []))
skip = "".join(f"<li>{e(x)}</li>" for x in d["skipped"])
left = "".join(f'<section><h3>{e(x["title"])}</h3><p><strong>Where:</strong> {e(x["where"])}. '+" · ".join(f'<a href="{e(a["url"])}">{e(a["label"])}</a>' for a in x["links"])+f'</p><p><strong>What:</strong> {e(x["what"])}</p><p><strong>Why:</strong> {e(x["why"])}</p><p><strong>Choice:</strong> {e(x["choice"])}</p><p><strong>Status:</strong> {e(x["status"])}</p></section>' for x in d.get("left_on_purpose", []))
sub = d.get("subpages", {})
subrows = "".join(f'<li>{e(x["repo"])}: <a href="{e(x["url"])}">{e(x["sha"][:8])}</a></li>' for x in sub.get("commits", []))
out = f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Honest wording: every change</title><style>{CSS}</style><main><nav><a href="../">Kaji</a> / Wording changes · updated {e(d["updated"])}</nav><h1>Honest wording: every change so far</h1>
<p><em>Irvan asked on 24 Nov 2026 that nothing in his repos, pages or apps imply a person did, wrote or checked work that Instinct (an AI assistant) or automation did. This page lists each wording change, with commit and live links. Edits were made by Instinct under his GitHub identity.</em></p>
{h2p('Wording changes', 'wording-changes')}
<table><thead><tr><th>Repo</th><th>Where</th><th>Before</th><th>After</th><th>Commits</th><th>Live</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table>
{h2p('AI-assistance line (option b)', 'ai-assistance-line-option-b')}
<p>Added to the README of each repo and to the main page footer where a page exists. The subpage pass below extends that disclosure across the published site. English: <strong>{e(d["disclosure_line"])}</strong> Indonesian pages (jasa): <strong>{e(d["disclosure_line_id"])}</strong></p>
<table><thead><tr><th>Repo</th><th>Commit</th><th>Live</th></tr></thead><tbody>{disc}</tbody></table>
{h2p('Still planned or open', 'still-planned-or-open')}<ul>{plan}</ul>
{h2p('Subpage disclosure pass', 'subpage-disclosure-pass')}<p>{e(sub.get("status", ""))}</p><p>{e(sub.get("note", ""))}</p><ul>{subrows}</ul>
{h2p('Wording left as is on purpose, and one correction', 'wording-left-as-is-on-purpose')}{left}
{h2p('Not changed', 'not-changed')}<ul>{skip}</ul>
<footer>Maintained by Instinct (an AI assistant). Built with AI assistance (Instinct and others). Not everything has been reviewed by Irvan.</footer></main>{PERMALINK_JS}</html>"""
(root/"site/honesty").mkdir(exist_ok=True)
(root/"site/honesty/index.html").write_text(out)
