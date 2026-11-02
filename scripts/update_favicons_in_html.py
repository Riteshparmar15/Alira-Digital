#!/usr/bin/env python3
"""
Updates favicon links across all HTML files to include vector SVG favicon and cache-busting v=2.
"""
import glob, re

def main():
    html_files = [f for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.')]
    
    # Pattern to match the existing icon links
    pattern = re.compile(
        r'<link rel="icon" href="/favicon\.ico"[^>]*>\s*'
        r'<link rel="icon" href="/assets/img/favicon-32x32\.png"[^>]*>\s*'
        r'<link rel="icon" href="/assets/img/favicon-192\.png"[^>]*>\s*'
        r'<link rel="apple-touch-icon" href="/apple-touch-icon\.png">'
    )
    
    replacement = (
        '<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg?v=2">\n'
        '  <link rel="icon" href="/favicon.ico?v=2" sizes="48x48">\n'
        '  <link rel="icon" href="/assets/img/favicon-32x32.png?v=2" type="image/png" sizes="32x32">\n'
        '  <link rel="icon" href="/assets/img/favicon-192.png?v=2" type="image/png" sizes="192x192">\n'
        '  <link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">'
    )
    
    count = 0
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated favicons in: {file_path}")
        else:
            # Check if brand-preview or other
            if "favicon" not in content and file_path == "brand-preview.html":
                # Add into head
                new_content = content.replace("</head>", f"  {replacement}\n</head>")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Added favicons to: {file_path}")
            else:
                print(f"Notice: Pattern didn't match in {file_path}")
    
    print(f"\nTotal files updated: {count}/{len(html_files)}")

if __name__ == '__main__':
    main()

