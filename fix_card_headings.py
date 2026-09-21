import os
import glob
import re

def fix_cards():
    html_files = glob.glob('*.html')
    
    # Pattern to match the card header
    pattern = re.compile(
        r'<div class="flex items-center justify-between mb-2">\s*'
        r'<h3 class="font-serif-display text-2xl font-bold">(.*?)</h3>\s*'
        r'<span class="text-xs font-semibold px-2\.5 py-0\.5 rounded bg-brass/10 text-brass">(.*?)</span>\s*'
        r'</div>',
        re.DOTALL
    )
    
    replacement = (
        r'<div class="flex items-start justify-between mb-2 min-h-[4rem]">\n'
        r'                <h3 class="font-serif-display text-2xl font-bold pr-2">\1</h3>\n'
        r'                <span class="text-xs font-semibold px-2.5 py-0.5 rounded bg-brass/10 text-brass shrink-0 mt-1">\2</span>\n'
        r'              </div>'
    )
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = pattern.sub(replacement, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed cards in {file_path}")

if __name__ == "__main__":
    fix_cards()
