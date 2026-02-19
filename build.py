#!/usr/bin/env python3
"""Build script: reads posts/*.md, outputs posts.json"""
import json
from pathlib import Path


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


posts = []
posts_dir = Path(__file__).parent / "posts"
for md_file in sorted(posts_dir.glob("*.md"), reverse=True):
    text = md_file.read_text(encoding="utf-8")
    meta, content = parse_frontmatter(text)
    slug = md_file.stem
    title = meta.get("title", slug)
    date = meta.get("date", "")
    time = meta.get("time", "")
    posts.append({"slug": slug, "title": title, "date": date, "time": time, "content": content})

out = Path(__file__).parent / "posts.json"
out.write_text(json.dumps(posts, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Built {len(posts)} post(s) -> posts.json")
