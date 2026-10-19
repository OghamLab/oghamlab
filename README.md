# OghamLab — Increment 8: Multi-App Website

A static, GitHub Pages-compatible multi-app developer website.

## Pages
- `/` — OghamLab homepage
- `/apps/` — app catalog (Frontis plus **concept-only** News App placeholder)
- `/about/` — studio overview
- `/support/` — general support directory
- `/frontis/` — existing Frontis landing page
- `/frontis/privacy/` — existing Frontis privacy policy (review before policy submission)
- `/frontis/support/` — existing Frontis support page

## Deploy

Copy the **contents** of `OghamLab/` into your existing GitHub Pages repository, preserving `.git`, then commit and push to `main`. Do not replace your repository's `.git` directory. `CNAME` remains `oghamlab.com`.

## Local preview

Because new site navigation uses root-relative URLs (`/apps/`, etc.), serve from the website root:

```bash
cd OghamLab
python3 -m http.server 8000
```

Open http://localhost:8000/

## Adding another app

1. Create `/your-app/index.html`, `/your-app/privacy/index.html`, and `/your-app/support/index.html` as appropriate.
2. Add a new `<article class="app-card">` in `/apps/index.html` and optionally the homepage.
3. Add artwork in `/images/`.
4. Update support directory `/support/index.html`.
5. Test all links and publish.

The News App is a **placeholder only**; it has no published product page or invented privacy policy. Frontis pages and URLs have not been changed.

## Increment 9: reusable app template

See `INCREMENT9.md`. Run `python3 create_app.py templates/app.example.json` to generate sample pages locally (not added to public navigation). Review and replace the generated privacy draft before publishing any app.


## How to create  next app

For example, when you're ready to develop a News App, copy:
templates/app.example.json
Rename the copy to news-app.json and edit its contents:
{
  "slug": "news",
  "name": "News App",
  "tagline": "Stay informed, wherever you are.",
  "description": "A future news-reading application.",
  "features": [
    "Browse news stories",
    "Explore news categories",
    "Save favorite articles"
  ],
  "artwork": "",
  "screenshots": []
}


These features are examples for a potential future product, not claims about an existing app.
Run:
python3 create_app.py templates/news-app.json


The generator creates:
news/
├── index.html
├── privacy/
│   └── index.html
└── support/
    └── index.html


## Increment 10

See [INCREMENT10.md](INCREMENT10.md) for automated app catalog instructions.

