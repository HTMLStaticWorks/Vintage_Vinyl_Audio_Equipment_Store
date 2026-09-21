import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Target just the H3 headers in those pillar cards
new_content = re.sub(
    r'(<span class="text-2xl font-serif-display text-brass font-bold">\d{2}</span>\s*<h3 class="font-serif-display text-xl font-bold)',
    r'\1 min-h-[3.5rem] flex items-start',
    content
)

with open('home-2.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
