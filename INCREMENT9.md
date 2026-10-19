# Increment 9 — Reusable App Template

OghamLab now includes a standard-library Python generator for adding future apps. **Existing Frontis pages, routes, and styling are unchanged.** The News App remains a concept placeholder; no invented news product pages are published.

## Add a new app

1. Put app artwork/screenshots into `images/` (optional).
2. Copy `templates/app.example.json` to `templates/my-app.json` and edit the `slug`, `name`, `tagline`, `description`, `features`, and optional `/images/...` artwork/screenshot paths.
3. From the OghamLab website root, run:

   ```bash
   python3 create_app.py templates/my-app.json
   ```

4. Three routes are created: `/my-app/`, `/my-app/privacy/`, `/my-app/support/`. No existing directory is overwritten.
5. **Before publication**, replace the privacy draft with a factually accurate, reviewed policy and verify support email delivery. The generator intentionally does not add a new app to the public catalog automatically.
6. Once the app is ready, add a card linking to `/my-app/` in `apps/index.html`, optionally feature it in `index.html`, and add a link in `support/index.html`. Use the existing `.app-card` styles. If you want a future project shown as a concept only, use a non-clickable placeholder card instead.
7. Preview with `python3 -m http.server 8000`, inspect on mobile, check all links, and commit/push to GitHub Pages.

## Notes

- `css/app-template.css` styles generated product pages without affecting Frontis.
- Generated pages escape user-supplied HTML to prevent markup injection.
- `--publish` is reserved as a review reminder; it **does not publish** draft policies or auto-edit the catalog.
- Do not add unverified app features, app-store links, or privacy statements.
- Preserve the root `CNAME` file (`oghamlab.com`) and existing `.git` folder during deployment.
