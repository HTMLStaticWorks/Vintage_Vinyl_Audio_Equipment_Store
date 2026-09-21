import re

with open('journal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove margin-top variations
content = re.sub(r'<div class="group cursor-pointer[^"]*">', '<div class="group cursor-pointer">', content)

# 2. Make all image wrappers have aspect-square
content = re.sub(r'aspect-\[.*?\]|aspect-square', 'aspect-square', content)

with open('journal.html', 'w', encoding='utf-8') as f:
    f.write(content)
