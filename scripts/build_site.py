#!/usr/bin/env python3
"""Build the static site published at GitHub Pages.

Why this exists: notebook bodies live inside .ipynb JSON, which search engines
and LLM crawlers index poorly, and GitHub refuses to preview large notebooks at
all. Rendering everything to plain HTML at a stable URL gives the course content
a crawlable home.

Outputs into ./site:
  index.html          landing page, carrying schema.org Course JSON-LD
  <path>.html         every notebook, rendered by nbconvert
  curriculum.html     and the other top-level docs
  sitemap.xml         every page, for crawlers
  robots.txt          explicitly allowing them
  llms.txt            copied to the site root, where the convention expects it

Run locally with:  python scripts/build_site.py
"""
from __future__ import annotations

import html
import json
import shutil
import subprocess
import sys
import urllib.parse
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
BASE = "https://diogoalvesderesende.github.io/time-series-forecasting-python"
GITHUB = "https://github.com/diogoalvesderesende/time-series-forecasting-python"
COURSE = "https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A"

COURSE_TITLE = "Master Time Series Analysis and Forecasting with Python"
RATING, RATING_COUNT, STUDENTS = "4.3", 1545, 13693

PARTS = [
    ("Time Series Analysis", "Part 1 — Time Series Analysis",
     "Datetime indexing, decomposition, ACF and PACF, stationarity, exponential "
     "smoothing, Holt-Winters, ARIMA, SARIMA and SARIMAX."),
    ("Modern Time Series Forecasting Techniques", "Part 2 — Modern Techniques",
     "Prophet with holidays and tuning, intermittent demand, LinkedIn Silverkite."),
    ("Deep Learning for Time Series Forecasting", "Part 3 — Deep Learning",
     "LSTM on one series and on many, Temporal Fusion Transformer, N-BEATS, all on Darts."),
    ("Advanced Content for Time Series", "Part 4 — Advanced",
     "Amazon Chronos and Chronos 2, AutoGluon, Google TSMixer, InceptionTime, "
     "and the automated forecasting pipeline."),
]

CSS = """
:root { --fg:#1a1a1a; --muted:#5c5c5c; --bg:#fff; --card:#f6f7f9; --line:#e3e5e8; --accent:#0b5fff; }
@media (prefers-color-scheme: dark) {
  :root { --fg:#e8e8e8; --muted:#a0a0a0; --bg:#14161a; --card:#1c1f25; --line:#2c3037; --accent:#6ea8ff; }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg);
       font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
.wrap { max-width: 900px; margin: 0 auto; padding: 0 16px 72px; }
header.site { border-bottom:1px solid var(--line); margin-bottom:32px; }
header.site .wrap { padding-top:20px; padding-bottom:20px; display:flex; gap:20px;
                    flex-wrap:wrap; align-items:baseline; }
header.site a { color:var(--fg); text-decoration:none; font-weight:600; }
header.site nav a { color:var(--muted); font-weight:400; margin-right:16px; }
header.site nav a:hover { color:var(--accent); }
h1 { font-size:2rem; line-height:1.25; margin:0 0 12px; }
h2 { margin-top:2.2em; border-bottom:1px solid var(--line); padding-bottom:6px; }
a { color:var(--accent); }
.lede { font-size:1.12rem; color:var(--muted); margin:0 0 24px; }
.stats { display:flex; flex-wrap:wrap; gap:10px; margin:0 0 28px; padding:0; list-style:none; }
.stats li { background:var(--card); border:1px solid var(--line); border-radius:8px;
            padding:8px 14px; font-size:.92rem; }
.stats b { font-size:1.05rem; }
.cta { display:inline-block; background:var(--accent); color:#fff; text-decoration:none;
       padding:12px 22px; border-radius:8px; font-weight:600; }
.card { background:var(--card); border:1px solid var(--line); border-radius:10px;
        padding:18px 20px; margin:16px 0; }
.reviews { display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr));
           gap:14px; margin:20px 0; }
.review { background:var(--card); border:1px solid var(--line); border-radius:10px;
          padding:16px 18px; }
.review blockquote { margin:0 0 12px; font-size:.97rem; }
.review .who { color:var(--muted); font-size:.85rem; }
.review .who b { color:var(--fg); font-weight:600; }
.stars { color:#f6b100; letter-spacing:1px; font-size:.9rem; display:block; margin-bottom:8px; }
.card h3 { margin:0 0 6px; font-size:1.12rem; }
.card p { margin:0 0 12px; color:var(--muted); }
.card ul { margin:0; padding-left:20px; column-gap:28px; }
.card li { margin:3px 0; }
table { border-collapse:collapse; width:100%; margin:18px 0; font-size:.95rem; }
th,td { border:1px solid var(--line); padding:8px 10px; text-align:left; }
th { background:var(--card); }
code { background:var(--card); padding:2px 5px; border-radius:4px; font-size:.9em; }
pre { background:var(--card); border:1px solid var(--line); border-radius:8px;
      padding:14px; overflow:auto; }
pre code { background:none; padding:0; }
footer.site { border-top:1px solid var(--line); margin-top:56px; padding-top:20px;
              color:var(--muted); font-size:.9rem; }
img { max-width:100%; }
"""

NAV = f"""<header class="site"><div class="wrap">
<a href="{{root}}/">Time Series Forecasting with Python</a>
<nav>
  <a href="{{root}}/curriculum.html">Curriculum</a>
  <a href="{{root}}/setup.html">Setup</a>
  <a href="{{root}}/changelog.html">Updates</a>
  <a href="{GITHUB}">GitHub</a>
  <a href="{COURSE}">Take the course</a>
</nav></div></header>"""

FOOT = f"""<footer class="site"><div class="wrap">
Companion code for <a href="{COURSE}">{COURSE_TITLE}</a> by Diogo Alves de Resende ·
<a href="{GITHUB}">Source on GitHub</a> · MIT licensed
</div></footer>"""


def page(title: str, body: str, depth: int = 0, description: str = "", extra_head: str = "") -> str:
    root = "/".join([".."] * depth) if depth else "."
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{BASE}/social-preview.png">
<meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style>
{extra_head}
</head><body>
{NAV.format(root=root)}
<main class="wrap">
{body}
</main>
{FOOT}
</body></html>
"""


def notebooks() -> list[Path]:
    return sorted(p for p in REPO.rglob("*.ipynb")
                  if ".ipynb_checkpoints" not in p.parts and "site" not in p.parts)


def convert_notebooks() -> list[tuple[Path, str]]:
    """Render each notebook to HTML, wrapped in the site chrome."""
    from nbconvert import HTMLExporter

    exporter = HTMLExporter(template_name="basic")
    built = []
    for nb_path in notebooks():
        rel = nb_path.relative_to(REPO)
        out = SITE / rel.with_suffix(".html")
        out.parent.mkdir(parents=True, exist_ok=True)
        body, _ = exporter.from_filename(str(nb_path))
        depth = len(rel.parts) - 1
        title = f"{rel.stem} — {COURSE_TITLE}"
        desc = f"{rel.stem}, a notebook from the course {COURSE_TITLE}."
        colab = ("https://colab.research.google.com/github/diogoalvesderesende/"
                 "time-series-forecasting-python/blob/main/"
                 + urllib.parse.quote(rel.as_posix()))
        header = (f'<p class="lede">Notebook from <a href="{COURSE}">{COURSE_TITLE}</a>. '
                  f'<a href="{colab}">Run it in Colab</a> · '
                  f'<a href="{GITHUB}/blob/main/{urllib.parse.quote(rel.as_posix())}">View source</a></p>')
        out.write_text(page(title, header + body, depth, desc), encoding="utf-8")
        built.append((rel, rel.with_suffix(".html").as_posix()))
    return built


def convert_docs() -> list[str]:
    import markdown

    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"])
    pages = []
    for name, out_name in [("README.md", "readme.html"), ("CURRICULUM.md", "curriculum.html"),
                           ("SETUP.md", "setup.html"), ("CHANGELOG.md", "changelog.html"),
                           ("NOTICE.md", "notice.html"), ("CONTRIBUTING.md", "contributing.html")]:
        src = REPO / name
        if not src.is_file():
            continue
        md.reset()
        body = md.convert(src.read_text(encoding="utf-8"))
        title = f"{src.stem.title()} — {COURSE_TITLE}"
        (SITE / out_name).write_text(page(title, body, 0, f"{src.stem} for {COURSE_TITLE}."),
                                     encoding="utf-8")
        pages.append(out_name)
    return pages


def course_jsonld() -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Course",
        "name": COURSE_TITLE,
        "description": ("A Python course covering time series forecasting from exponential "
                        "smoothing and ARIMA through Prophet, LSTM, Temporal Fusion "
                        "Transformers and N-BEATS to foundation models such as Amazon "
                        "Chronos, Amazon AutoGluon and Google TSMixer."),
        "url": COURSE,
        "inLanguage": "en",
        "educationalLevel": "Beginner",
        "teaches": ["Time series forecasting", "Exponential smoothing", "Holt-Winters",
                    "ARIMA", "SARIMAX", "Prophet", "Intermittent demand forecasting",
                    "LSTM", "Temporal Fusion Transformer", "N-BEATS", "Amazon Chronos",
                    "Amazon AutoGluon", "Google TSMixer", "Time series classification"],
        "provider": {"@type": "Organization", "name": "The Data Hero",
                     "url": "https://thedatahero.com/"},
        "author": {"@type": "Person", "name": "Diogo Alves de Resende",
                   "url": "https://www.udemy.com/user/diogo-resende-2/"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": RATING,
                            "ratingCount": RATING_COUNT, "reviewCount": RATING_COUNT,
                            "bestRating": "5", "worstRating": "1"},
        "hasCourseInstance": {
            "@type": "CourseInstance", "courseMode": "online",
            "courseWorkload": "PT38H14M",
            "instructor": {"@type": "Person", "name": "Diogo Alves de Resende"},
        },
        "isAccessibleForFree": False,
        "offers": {"@type": "Offer", "category": "Paid", "url": COURSE},
    }
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False, indent=2) + "</script>")


def reviews_section(limit: int = 8) -> str:
    """Render real student reviews from data/reviews.json.

    Deliberately not emitted as schema.org Review markup: Google's review-snippet
    guidelines expect reviews collected by the site itself, not republished from a
    third party. They are shown to readers and credited to Udemy instead.
    """
    src = REPO / "data" / "reviews.json"
    if not src.is_file():
        return ""
    data = json.loads(src.read_text(encoding="utf-8"))
    items = data.get("reviews", [])[:limit]
    if not items:
        return ""
    cards = "".join(
        f'<div class="review"><span class="stars">★★★★★</span>'
        f"<blockquote>{html.escape(r['quote'])}</blockquote>"
        f'<div class="who"><b>{html.escape(r["name"])}</b> · {html.escape(r["date"][:7])}</div></div>'
        for r in items)
    total = data.get("totals", {})
    return f"""
<h2 id="what-students-say">What students say</h2>
<p>Real reviews from Udemy, where the course holds <b>{total.get('rating', '')} out of 5</b>
from {total.get('rating_count', 0):,} ratings.
<a href="{COURSE}">Read them all on the course page</a>.</p>
<div class="reviews">{cards}</div>
"""


def build_index(built: list[tuple[Path, str]]) -> None:
    by_part = {folder: [] for folder, _, _ in PARTS}
    root_nbs = []
    for rel, href in built:
        top = rel.parts[0]
        (by_part[top] if top in by_part else root_nbs).append((rel, href))

    cards = []
    for folder, heading, blurb in PARTS:
        items = "".join(
            f'<li><a href="{urllib.parse.quote(href)}">{html.escape(rel.stem)}</a></li>'
            for rel, href in sorted(by_part[folder]))
        cards.append(f'<div class="card"><h3>{html.escape(heading)}</h3>'
                     f"<p>{html.escape(blurb)}</p><ul>{items}</ul></div>")
    if root_nbs:
        items = "".join(f'<li><a href="{urllib.parse.quote(href)}">{html.escape(rel.stem)}</a></li>'
                        for rel, href in sorted(root_nbs))
        cards.append(f'<div class="card"><h3>Reference</h3>'
                     f"<p>Snippets to reuse in any project.</p><ul>{items}</ul></div>")

    body = f"""
<h1>{html.escape(COURSE_TITLE)}</h1>
<p class="lede">Every notebook, dataset and capstone from the Udemy course, rendered as
readable web pages. {len(built)} notebooks covering classical statistical forecasting
through deep learning and time series foundation models in Python.</p>

<ul class="stats">
  <li><b>{RATING} ★</b> rating</li>
  <li><b>{RATING_COUNT:,}</b> reviews</li>
  <li><b>{STUDENTS:,}</b> students</li>
  <li><b>397</b> lectures</li>
  <li><b>38h 14m</b> of video</li>
  <li>Updated <b>September 2026</b></li>
</ul>

<p><a class="cta" href="{COURSE}">Take the full course on Udemy →</a></p>
{reviews_section()}
<h2>Browse the notebooks</h2>
<p>Every notebook runs one click from Google Colab. The code is
<a href="{GITHUB}">on GitHub</a> under the MIT licence.</p>
{''.join(cards)}

<h2>What the course covers</h2>
<table>
<tr><th>Model</th><th>What it is good at</th></tr>
<tr><td>Exponential Smoothing and Holt-Winters</td><td>Trend and seasonality, fast and explainable</td></tr>
<tr><td>ARIMA, SARIMA, SARIMAX</td><td>Classical forecasting with external regressors</td></tr>
<tr><td>Prophet</td><td>Strong baselines with holidays and little data prep</td></tr>
<tr><td>Intermittent demand methods</td><td>Sparse, spiky series with many zeros</td></tr>
<tr><td>LinkedIn Silverkite</td><td>Regression-based forecasting at scale</td></tr>
<tr><td>LSTM</td><td>Long-term dependencies, one series or many</td></tr>
<tr><td>Temporal Fusion Transformer</td><td>Many series, covariates, interpretable attention</td></tr>
<tr><td>N-BEATS</td><td>Deep learning with no feature engineering</td></tr>
<tr><td>Amazon Chronos and Chronos 2</td><td>Foundation models, zero-shot forecasting</td></tr>
<tr><td>Amazon AutoGluon</td><td>AutoML that trains and ensembles for you</td></tr>
<tr><td>Google TSMixer</td><td>All-MLP, univariate and multivariate</td></tr>
<tr><td>InceptionTime</td><td>Time series classification</td></tr>
</table>

<h2>Documentation</h2>
<ul>
  <li><a href="readme.html">Overview</a> — what the repository contains</li>
  <li><a href="curriculum.html">Curriculum</a> — all 39 course sections mapped to notebooks</li>
  <li><a href="setup.html">Setup</a> — Colab and local installation</li>
  <li><a href="changelog.html">Updates</a> — the nine documented course updates</li>
  <li><a href="notice.html">Licence and dataset credits</a></li>
</ul>
"""
    desc = (f"Companion notebooks for {COURSE_TITLE}. Rated {RATING} from "
            f"{RATING_COUNT:,} reviews. ARIMA, Prophet, LSTM, TFT, N-BEATS, Amazon Chronos, "
            f"AutoGluon and Google TSMixer, all in Python.")
    (SITE / "index.html").write_text(page(COURSE_TITLE, body, 0, desc, course_jsonld()),
                                     encoding="utf-8")


def build_sitemap(paths: list[str]) -> None:
    today = date.today().isoformat()
    urls = "".join(
        f"<url><loc>{BASE}/{urllib.parse.quote(p)}</loc><lastmod>{today}</lastmod></url>\n"
        for p in paths)
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}</urlset>\n", encoding="utf-8")
    (SITE / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {BASE}/sitemap.xml\n", encoding="utf-8")


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    built = convert_notebooks()
    docs = convert_docs()
    build_index(built)

    for extra in ("llms.txt",):
        src = REPO / extra
        if src.is_file():
            shutil.copy2(src, SITE / extra)

    social = REPO / "assets" / "social-preview.png"
    if social.is_file():
        shutil.copy2(social, SITE / "social-preview.png")

    (SITE / ".nojekyll").touch()          # serve folders with spaces verbatim
    build_sitemap(["index.html"] + docs + [href for _, href in built])

    total = sum(f.stat().st_size for f in SITE.rglob("*") if f.is_file())
    print(f"site/: {len(built)} notebooks + {len(docs)} doc pages + index, "
          f"{total / 1048576:.1f} MB")


if __name__ == "__main__":
    sys.exit(main())
