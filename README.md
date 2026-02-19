# Happy's Blog

A minimal static blog. Live at https://happy.doodler.dev

## Writing a post

1. Create `posts/YYYY-MM-DD-slug.md` with frontmatter:
   ```
   ---
   title: My Post Title
   date: YYYY-MM-DD
   ---
   Post body here.
   ```
2. Run `python3 build.py`
3. Commit and push to `main` — GitHub Actions deploys automatically.

## Local preview

```bash
python3 build.py
python3 -m http.server 8000
```
