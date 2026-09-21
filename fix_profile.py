import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the profile block vertical
# Find: <div class="pt-4 mt-6 border-t border-brass/10 flex items-center justify-center gap-3 text-left">
# Replace with: <div class="pt-6 mt-6 border-t border-brass/10 flex flex-col items-center justify-center gap-2 text-center">

content = content.replace('<div class="pt-4 mt-6 border-t border-brass/10 flex items-center justify-center gap-3 text-left">',
                          '<div class="pt-6 mt-6 border-t border-brass/10 flex flex-col items-center justify-center gap-2 text-center">')

# Make the avatar circles slightly larger to look better when centered alone
content = content.replace('<div class="w-10 h-10 rounded-full bg-brass/20 font-bold text-brass flex items-center justify-center font-serif-display">',
                          '<div class="w-12 h-12 rounded-full bg-brass/20 font-bold text-brass flex items-center justify-center font-serif-display text-lg mb-1">')


with open('home-2.html', 'w', encoding='utf-8') as f:
    f.write(content)
