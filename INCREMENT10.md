# Increment 10 — Automated app catalog

The **single source of truth** for the OghamLab homepage, Apps catalog, and Support directory is `apps.json`. The site remains static and deploys to GitHub Pages without a backend.

## Update the catalog

1. Edit `apps.json`. `status` can be `concept`, `draft`, or `published`. `draft` apps are excluded from all generated lists. `concept` apps display a non-clickable placeholder. `published` apps get linked product, privacy, and support pages.
2. For a new app, run `python3 create_app.py templates/app.example.json` after customizing the JSON and reviewing its contents. The generator creates product, privacy, and support pages but **does not add the app to the catalog**.
3. Complete and manually review the generated privacy page. The draft template is not a valid privacy policy. Before changing an entry to `published`, verify the privacy page, actual data handling, permissions, and contact details; then set `privacy_reviewed` to `true` in `apps.json`. This flag is a manual attestation, not an automatic legal review.
4. Add the app entry to `apps.json` and run `python3 build_catalog.py`. Set `featured: true` if it should also appear on the homepage.
5. Run `python3 build_catalog.py --check` before committing.
6. Test locally with `python3 -m http.server 8000` and visit `/`, `/apps/`, and `/support/`.

**Note:** Any generated HTML pushed to the public GitHub Pages repository can be accessed by its direct URL, even if not linked from the catalog. Do not push unreviewed privacy pages to the public site. Keep unfinished work on a local branch or outside the publishing directory.

## Deploy

Copy the updated website into your existing GitHub Pages repository without deleting `.git` or changing `CNAME`. Commit and push the configured publishing branch. Frontis routes stay unchanged.

## Build rules

The builder validates unique slugs, image paths, published page existence, the `privacy_reviewed` flag, and obvious generated draft warnings. It escapes text to prevent accidental HTML injection. Generated sections are bounded by `AUTO-APPS` markers; avoid hand-editing content between them.
