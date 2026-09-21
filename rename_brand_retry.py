import glob
import re

files = glob.glob('*.html')
for f in files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        original = content
        
        # Exact replacements
        content = content.replace('NEEDLE & GROOVE', 'VINYL')
        content = content.replace('Needle & Groove', 'Vinyl')
        content = content.replace('NEEDLE &amp; GROOVE', 'VINYL')
        content = content.replace('Needle &amp; Groove', 'Vinyl')
        content = content.replace('Needle and Groove', 'Vinyl')
        content = content.replace('needleandgroove', 'vinyl')
        
        if content != original:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
