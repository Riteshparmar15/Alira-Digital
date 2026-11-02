#!/usr/bin/env python3
"""
Prepares the site/ folder for GitHub Pages deployment:
- Ensures .nojekyll is present.
- If deployed to a subpath (e.g. /my-repo), adjusts absolute paths in HTML and sitemap.
- Leaves local files intact when base_path is empty or '/'.
"""
import sys
import os
import glob
import re

def main():
    base_path = sys.argv[1].strip() if len(sys.argv) > 1 else ""
    # Normalize base_path: strip trailing slash, keep leading slash if non-empty
    if base_path in ["", "/", "."]:
        print("[GitHub Pages] Deploying to root domain / custom domain. No path prefixing needed.")
        return

    if not base_path.startswith('/'):
        base_path = '/' + base_path
    base_path = base_path.rstrip('/')

    print(f"[GitHub Pages] Adapting site for subpath: {base_path}")

    site_dir = "site"
    html_files = glob.glob(f"{site_dir}/**/*.html", recursive=True)

    # Patterns to prefix: href="/...", src="/..."
    # Excluding external links (http, https, //)
    attr_pattern = re.compile(r'((?:href|src|content|url)=")(/(?!/|assets|build|about|services|projects|areas|custom|online|mobile|website|industries|faq|contact|privacy|blog|favicon|apple)[^"]*|/(?:assets|build|about-us|services|projects|areas-we-serve|custom-erp-system|online-platform-development|mobile-app-development|website-design|custom-erp-guide|industries|faq|contact|privacy-policy|blog|favicon\.ico|apple-touch-icon\.png)[^"]*)(")')

    updated_count = 0
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        def replacer(match):
            prefix = match.group(1)
            val = match.group(2)
            suffix = match.group(3)
            if val.startswith(base_path):
                return match.group(0)
            return f"{prefix}{base_path}{val}{suffix}"

        new_content = attr_pattern.sub(replacer, content)
        
        # Also adjust canonical and schema urls
        new_content = new_content.replace('window.location.replace(\'/\'', f'window.location.replace(\'{base_path}/\'')
        new_content = new_content.replace('href="/"', f'href="{base_path}/"')

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1

    print(f"[GitHub Pages] Successfully adapted {updated_count} HTML files with base_path: {base_path}")

if __name__ == '__main__':
    main()

