#!/usr/bin/env python3
"""Create a new OghamLab app microsite from a JSON configuration (stdlib only)."""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def esc(value):
    return html.escape(str(value), quote=True)

def page(title, body, description):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#050507"><meta name="description" content="{esc(description)}"><title>{esc(title)} — OghamLab</title><link rel="stylesheet" href="/css/style.css"><link rel="stylesheet" href="/css/lab.css"><link rel="stylesheet" href="/css/app-template.css"><script defer src="/js/main.js"></script></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="site-header lab-header"><a class="brand" href="/" aria-label="OghamLab home">OGHAM<span>LAB</span></a><nav class="lab-nav" aria-label="Main navigation"><a href="/">Home</a><a href="/apps/">Apps</a><a href="/about/">About</a><a href="/support/">Support</a></nav></header><main id="main">{body}</main><footer class="site-footer lab-footer"><span>© <span data-year>2026</span> OghamLab</span><span><a href="/apps/">Apps</a> · <a href="/support/">Support</a> · <a href="mailto:support@oghamlab.com">Email</a></span></footer></body></html>
'''

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path, help='JSON app configuration')
    parser.add_argument('--publish', action='store_true', help='Add app to public catalog and support directory')
    args = parser.parse_args()
    data = json.loads(args.config.read_text(encoding='utf-8'))
    slug = data['slug']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in {'apps','about','support','frontis','css','js','images'}:
        raise SystemExit('Invalid or reserved slug')
    name, tagline, description = (data[k].strip() for k in ('name','tagline','description'))
    if not all((name,tagline,description)):
        raise SystemExit('name, tagline, description must not be blank')
    features = data.get('features', [])
    if not isinstance(features, list) or not all(isinstance(f, str) for f in features):
        raise SystemExit('features must be a list of strings')
    path = ROOT / slug
    if path.exists():
        raise SystemExit(f'{path} already exists; no files overwritten')
    art = data.get('artwork', '')
    if art and (not art.startswith('/images/') or '..' in art or not (ROOT / art.lstrip('/')).is_file()):
        raise SystemExit('artwork must point to an existing file under /images/')
    art_html = f'<img class="product-art" src="{esc(art)}" alt="{esc(name)} artwork">' if art else '<div class="product-art-placeholder" aria-hidden="true">✦</div>'
    feature_html = ''.join(f'<li>{esc(f)}</li>' for f in features)
    screenshots = data.get('screenshots', [])
    for screenshot in screenshots:
        if not isinstance(screenshot, str) or not screenshot.startswith('/images/') or '..' in screenshot or not (ROOT / screenshot.lstrip('/')).is_file():
            raise SystemExit('Every screenshot must exist under /images/')
    screenshots_html = ''.join(f'<img src="{esc(s)}" alt="{esc(name)} screenshot {i}" loading="lazy">' for i,s in enumerate(screenshots,1))
    links = f'<a href="/{slug}/privacy/">Privacy policy</a> · <a href="/{slug}/support/">Support</a>'
    body = f'''<section class="product-hero"><div><p class="eyebrow">OGHAMLAB APPLICATION</p><h1>{esc(name)}</h1><p class="product-tagline">{esc(tagline)}</p><p class="product-description">{esc(description)}</p><div class="product-links">{links}</div></div>{art_html}</section><section class="product-section"><h2>Features</h2><ul class="product-features">{feature_html or '<li>Features will be announced soon.</li>'}</ul></section>{f'<section class="product-section"><h2>App preview</h2><div class="product-screenshots">{screenshots_html}</div></section>' if screenshots_html else ''}'''
    # Intentionally create a review-required policy draft; no fabricated data-handling promises.
    privacy = f'''<section class="lab-section text-page"><p class="eyebrow">PRIVACY</p><h1>{esc(name)} Privacy Policy</h1><p><strong>Draft — do not publish or submit this policy until reviewed.</strong></p><p>Describe the app's actual permissions, data collection, processing, sharing, third-party SDKs, retention, deletion, and contact information here. Confirm all statements against the shipped app.</p><p>Questions: <a href="mailto:support@oghamlab.com">support@oghamlab.com</a></p><p><a href="/{slug}/">Back to {esc(name)}</a></p></section>'''
    support = f'''<section class="lab-section text-page"><p class="eyebrow">SUPPORT</p><h1>{esc(name)} Support</h1><p>Need assistance with {esc(name)}? Contact <a href="mailto:support@oghamlab.com?subject={esc(name)}%20Support">support@oghamlab.com</a>.</p><p>Include your device model, Android version, app version, and a description of the issue. Do not include passwords or sensitive personal information.</p><p><a href="/{slug}/privacy/">Privacy policy</a> · <a href="/{slug}/">Back to app</a></p></section>'''
    for sub, content, title in [('',body,name),('privacy',privacy,f'{name} Privacy Policy'),('support',support,f'{name} Support')]:
        folder = path / sub
        folder.mkdir(parents=True,exist_ok=True)
        (folder/'index.html').write_text(page(title,content,description),encoding='utf-8')
    print(f'Created /{slug}/, /{slug}/privacy/, /{slug}/support/')
    if args.publish:
        if 'Draft — do not publish' in privacy:
            print('NOT added to catalog: privacy policy is a review-required draft. Complete the policy before publishing.')
    else:
        print('Not listed publicly. Review privacy and app content before linking it from the catalog.')

if __name__ == '__main__':
    main()
