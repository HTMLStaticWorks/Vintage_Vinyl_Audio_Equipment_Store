import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Make the card a flex column
content = content.replace('record-card group relative bg-ivory-paper', 'record-card group relative flex flex-col bg-ivory-paper')

# 2. Make the inner padding div flex grow
content = content.replace('<div class="p-6">', '<div class="p-6 flex flex-col flex-grow">')

# 3. Push the bottom border container to the bottom
content = content.replace('<div class="flex items-center justify-between border-t border-brass/10 pt-4">', '<div class="mt-auto flex items-center justify-between border-t border-brass/10 pt-4">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
