#!/usr/bin/env python3
"""
Updates published dates from 5 October 2026 / 2026-10-05 to 15 Sep 2023 / 2023-09-15 across blog pages and guides.
"""
import glob

def main():
    target_files = glob.glob('blog/**/*.html', recursive=True) + ['custom-erp-guide/index.html']
    
    total_files = 0
    for file_path in target_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        c1 = content.count('2026-10-05')
        c2 = content.count('5 October 2026')
        
        if c1 > 0 or c2 > 0:
            new_content = content.replace('2026-10-05', '2023-09-15')
            new_content = new_content.replace('5 October 2026', '15 Sep 2023')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            total_files += 1
            print(f"Updated {file_path}: {c1} dates, {c2} text labels")
            
    print(f"\nDone! Updated {total_files} files.")

if __name__ == '__main__':
    main()
