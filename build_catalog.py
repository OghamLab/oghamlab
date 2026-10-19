#!/usr/bin/env python3
"""Build OghamLab app cards and support directory from apps.json (stdlib only)."""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = '<!-- AUTO-APPS:START -->'
END = '<!-- AUTO-APPS:END -->'
VALID_STATUSES = {'published', 'concept', 'draft'}

def escape(value):
    return html.escape(str(value), quote=True)

def validate_image(image):
    if not isinstance(image, str):
        raise ValueError('artwork must be a string')
    if not image:
        return
    if not image.startswith('/images/') or '..' in image or '\\' in image or not (ROOT / image.lstrip('/')).is_file():
        raise ValueError(f'Invalid or missing artwork: {image}')

def load_registry():
    data = json.loads((ROOT / 'apps.json').read_text(encoding='utf-8'))
    apps = data.get('apps')
    if not isinstance(apps, list):
        raise ValueError('apps.json must contain an apps array')
    seen = set()
    for app in apps:
        if not isinstance(app, dict):
            raise ValueError('Each app must be an object')
        slug = app.get('slug')
        if not isinstance(slug, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in seen:
            raise ValueError(f'Invalid or duplicate slug: {slug}')
        seen.add(slug)
        if app.get('status') not in VALID_STATUSES:
            raise ValueError(f'Invalid status for {slug}')
        for field in ('name','category','description'):
            if not isinstance(app.get(field), str) or not app[field].strip():
                raise ValueError(f'{slug} requires {field}')
        validate_image(app.get('artwork',''))
        if app['status'] == 'published':
            for field in ('support','privacy'):
                expected = f'/{slug}/{field}/'
                if app.get(field) != expected or not (ROOT / slug / field / 'index.html').is_file():
                    raise ValueError(f'{slug}: {field} must be {expected} and page must exist')
            if not (ROOT / slug / 'index.html').is_file():
                raise ValueError(f'{slug}: product page missing')
            if app.get('privacy_reviewed') is not True:
                raise ValueError(f'{slug}: privacy_reviewed must be true after human review')
            policy = (ROOT / slug / 'privacy' / 'index.html').read_text(encoding='utf-8')
            if 'Draft — do not publish' in policy or 'Draft &mdash; do not publish' in policy:
                raise ValueError(f'{slug}: privacy page is still a template draft')
    return apps

def card(app):
    slug, name, status = app['slug'], escape(app['name']), app['status']
    category, description = escape(app['category']), escape(app['description'])
    if status == 'published':
        art = (f'<div class="app-art"><img src="{escape(app["artwork"])}" alt="{name} artwork" loading="lazy"></div>'
               if app.get('artwork') else '<div class="future-art" aria-hidden="true"><span class="newspaper-icon">✦</span></div>')
        return (f'<article class="app-card featured">{art}<div class="app-content"><div class="app-top">'
                f'<span class="tag">{category}</span><span class="status">Available app</span></div>'
                f'<h3>{name}</h3><p>{description}</p><a class="card-link" href="/{slug}/">Explore {name} <span aria-hidden="true">↗</span></a></div></article>')
    return (f'<article class="app-card future"><div class="future-art" aria-hidden="true"><span class="newspaper-icon">▤</span>'
            f'<span class="future-lines"></span></div><div class="app-content"><div class="app-top">'
            f'<span class="tag">{category}</span><span class="muted-tag">Future project</span></div>'
            f'<h3>{name}</h3><p>{description}</p><span class="soon">Concept placeholder</span></div></article>')

def support_entries(apps):
    entries=[]
    for app in apps:
        if app['status'] != 'published':
            continue
        name = escape(app['name'])
        entries.append(f'<a href="{escape(app["support"])}"><strong>{name} support</strong><span>{escape(app.get("support_description", "Help and troubleshooting"))} ↗</span></a>')
        entries.append(f'<a href="{escape(app["privacy"])}"><strong>{name} privacy policy</strong><span>Privacy information ↗</span></a>')
    entries.append('<a href="mailto:support@oghamlab.com?subject=OghamLab%20Support"><strong>Email OghamLab</strong><span>support@oghamlab.com ↗</span></a>')
    return '\n'.join(entries)

def replace_section(path, rendered, check):
    content=path.read_text(encoding='utf-8')
    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError(f'Missing/duplicate generation markers in {path}')
    before, rest = content.split(START,1)
    _, after = rest.split(END,1)
    result=before+START+'\n'+rendered+'\n'+END+after
    if check:
        if result != content:
            raise ValueError(f'{path.relative_to(ROOT)} is out of date; run python3 build_catalog.py')
    else:
        path.write_text(result,encoding='utf-8')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Fail if generated HTML is out of date')
    args=parser.parse_args()
    apps=load_registry()
    public=[app for app in apps if app['status'] in ('published','concept')]
    featured=[app for app in public if app.get('featured',False)]
    replace_section(ROOT/'index.html', '\n'.join(map(card,featured)), args.check)
    replace_section(ROOT/'apps'/'index.html','\n'.join(map(card,public)),args.check)
    replace_section(ROOT/'support'/'index.html',support_entries(apps),args.check)
    print('Catalog is current.' if args.check else 'Updated homepage, Apps catalog, and Support directory.')

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        raise SystemExit(f'Catalog build failed: {error}')
