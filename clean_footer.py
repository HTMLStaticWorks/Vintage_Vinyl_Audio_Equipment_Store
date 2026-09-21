# -*- coding: utf-8 -*-
import glob
import re

files = glob.glob('*.html')
skip_files = ['login.html', 'signup.html']

for f in files:
    if f in skip_files:
        continue
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # We need to remove the block:
        # <div class="flex items-center gap-4 mt-6">
        #   ...
        # </div>
        # But only if it's inside the footer or just globally if it's social icons.
        # Actually, let's target the exact block with mt-6 and aria-label="Instagram".
        
        duplicate_icons_regex = re.compile(r'<div class="flex items-center gap-4 mt-6">\s*<a href="#" class="hover:text-brass transition-colors" aria-label="Instagram">.*?</a>\s*</div>', re.DOTALL)
        
        content = duplicate_icons_regex.sub('', content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Cleaned {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
