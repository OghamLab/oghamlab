# OghamLab — Frontis Landing Page (Increment 2)

Responsive static website for the Frontis music app, currently in development.

## What is new in Increment 2

- Dark Audiophile visual polish and refined feature cards
- Responsive conceptual music-player mockup, explicitly labeled as an illustration
- Preview section linked from navigation
- Improved mobile menu behavior
- Original Frontis waveform artwork preserved

**Important:** The phone mockup is not an actual app screenshot. Replace it with verified Frontis screenshots when available. Store download links are intentionally omitted until release.

## Run locally

```bash
cd OghamLab
python3 -m http.server 8000
```

Visit `http://localhost:8000/frontis/`. The main brand page is at `/`.

## Deploy

Push the contents of `OghamLab` to the root of the GitHub Pages publishing repository. Configure `oghamlab.com` in GitHub Pages settings and verify the DNS records.

The Contact link uses `hello@oghamlab.com` as a placeholder. Set up the mailbox or replace the link before launch.

## Increment 3 — Frontis Privacy Policy

- New page: `/frontis/privacy/` (`frontis/privacy/index.html`)
- Styles: `css/privacy.css`
- Linked from Frontis footer.
- **DRAFT ONLY:** Replace every `[BRACKETED PLACEHOLDER]` and remove the draft warning before publishing.
- Verify actual Android permissions, data flows, SDKs, ads, recording/transcription providers, retention, deletion, and privacy contact.
- Ensure published policy matches Google Play Data safety form and in-app privacy disclosure.
- No download button has been added.

## Privacy policy draft — October 16, 2026

The Frontis privacy policy has been updated with the developer-confirmed on-device processing and support contact support@oghamlab.com. Before publishing, verify all app permissions, third-party network services, storage/deletion, SDKs, target audience, and consistency with the Google Play Data safety declaration. Replace the draft warning and draft date with an effective date only after this review. Verify that the support mailbox receives messages.


## Increment 4 — Support page

- `/frontis/support/` — FAQ, troubleshooting, and email support.
- Support address: `support@oghamlab.com` (verify email forwarding works before publishing).
- Frontis footer and Privacy Policy navigation link to Support.
- No download button was added.
- The Frontis landing page now reflects that Frontis is listed on Google Play while further development continues.
- The Privacy Policy remains a **draft** requiring a permissions/SDK/retention/audience review before publication.

Run `python3 -m http.server 8000` from this directory and open `http://localhost:8000/frontis/support/`.
