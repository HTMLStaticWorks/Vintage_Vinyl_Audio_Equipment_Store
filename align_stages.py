import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Target just the STAGE headers within that grid
new_content = re.sub(
    r'(<span class="text-xs font-mono text-brass uppercase">STAGE \d+</span>\s*<h4 class="font-serif-display text-xl font-bold text-brass)',
    r'\1 min-h-[3.5rem] flex items-start',
    content
)

with open('home-2.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
