# Increment 11 — App Showcase Management

## Features
- Edit `apps.json` to maintain each app’s `platforms`, `release`, `highlights`, and `screenshots`.
- `python3 build_catalog.py` updates the homepage, catalog, support directory, and published product-page showcases.
- `python3 build_catalog.py --check` verifies all generated sections are up to date.
- Frontis keeps its original marketing layout and its existing privacy and support URLs.
- No screenshot images are fabricated: the gallery appears only after real images are added.

## Adding real screenshots
1. Export genuine app screenshots (PNG/JPG/WebP) to `images/`, e.g. `images/frontis-player.png`. Do not use private information in screenshots.
2. In `apps.json`, add to the Frontis `screenshots` list:

```json
{"src":"/images/frontis-player.png","alt":"Frontis now-playing screen showing playback controls","caption":"Now playing"}
```

3. Update `platforms`, `release.version`, `release.stage`, and `highlights` to reflect **verified** features.
4. Run `python3 build_catalog.py`, then `python3 build_catalog.py --check`.
5. Preview with `python3 -m http.server 8000`, then commit and push.

**Do not mark unreleased features as shipped.** The example News App remains a concept. The current Frontis `screenshots` array is empty until genuine screenshots are provided.

## Generator notes
Future apps created by `create_app.py` include showcase markers and styling. Only apps with `status: published` are eligible for generated product showcases; privacy review safeguards from Increment 10 remain in place.
