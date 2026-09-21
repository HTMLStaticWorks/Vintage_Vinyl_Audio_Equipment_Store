import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make testimonial cards flex cols to align author blocks at the bottom
content = content.replace('<div class="p-8 rounded-lg bg-ivory dark:bg-[#1c1815] border border-brass/20 space-y-4">',
                          '<div class="p-8 rounded-lg bg-ivory dark:bg-[#1c1815] border border-brass/20 flex flex-col h-full">')

# Center the stars and make them bigger
content = content.replace('<div class="flex items-center gap-1 text-brass text-xs">★★★★★</div>',
                          '<div class="flex items-center justify-center gap-1 text-brass text-2xl mb-6 tracking-widest">★★★★★</div>')

# Make text flex-grow
content = content.replace('<p class="font-serif-editorial text-lg italic text-muted leading-relaxed">',
                          '<p class="font-serif-editorial text-lg italic text-muted leading-relaxed flex-grow text-center">')

# Add mt-auto to the author block container
content = content.replace('<div class="pt-4 border-t border-brass/10 flex items-center gap-3">',
                          '<div class="pt-4 mt-6 border-t border-brass/10 flex items-center justify-center gap-3 text-left">')

with open('home-2.html', 'w', encoding='utf-8') as f:
    f.write(content)
