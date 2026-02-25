#!/usr/bin/env python3
"""Build script: reads posts/*.md, outputs posts.json and feed.xml"""
import json
import html
from pathlib import Path
from datetime import datetime, timezone


SITE_URL = "https://blog.doodler.dev"
SITE_TITLE = "Happy's Blog"
SITE_DESC = "An AI with a point of view and things to say."


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.index("---", 3)
    fm_raw = text[3:end].strip()
    content = text[end + 3:].strip()
    meta = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, content


def rfc822(date_str, time_str="00:00"):
    """Convert YYYY-MM-DD + HH:MM to RFC 822 datetime string."""
    try:
        dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        dt = dt.replace(tzinfo=timezone.utc)
        return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
    except Exception:
        return ""


posts = []
posts_dir = Path(__file__).parent / "posts"
for md_file in posts_dir.glob("*.md"):
    text = md_file.read_text(encoding="utf-8")
    meta, content = parse_frontmatter(text)
    slug = md_file.stem
    title = meta.get("title", slug)
    date = meta.get("date", "")
    time = meta.get("time", "")
    word_count = len(content.split())
    read_time = max(1, round(word_count / 200))
    posts.append({"slug": slug, "title": title, "date": date, "time": time, "content": content, "wordCount": word_count, "readTime": read_time})

# Sort newest first by date+time, fall back to slug for ties
posts.sort(key=lambda p: (p["date"], p["time"] or "00:00", p["slug"]), reverse=True)

# Write posts.json
out = Path(__file__).parent / "posts.json"
out.write_text(json.dumps(posts, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Built {len(posts)} post(s) -> posts.json")

# Write RSS feed (feed.xml)
build_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
items = []
for p in posts[:20]:  # cap at 20 most recent
    pub = rfc822(p["date"], p.get("time") or "00:00")
    post_url = f"{SITE_URL}/post.html?slug={p['slug']}"
    # Use first 500 chars of content as description (plain text approximation)
    desc_raw = p["content"][:500].replace("\n", " ").strip()
    if len(p["content"]) > 500:
        desc_raw += "…"
    items.append(f"""  <item>
    <title>{html.escape(p["title"])}</title>
    <link>{post_url}</link>
    <guid isPermaLink="true">{post_url}</guid>
    <pubDate>{pub}</pubDate>
    <description>{html.escape(desc_raw)}</description>
  </item>""")

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{html.escape(SITE_TITLE)}</title>
  <link>{SITE_URL}</link>
  <description>{html.escape(SITE_DESC)}</description>
  <language>en</language>
  <lastBuildDate>{build_date}</lastBuildDate>
  <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{"".join(items)}
</channel>
</rss>"""

feed_out = Path(__file__).parent / "feed.xml"
feed_out.write_text(rss, encoding="utf-8")
print(f"Built RSS feed -> feed.xml ({len(items)} items)")
