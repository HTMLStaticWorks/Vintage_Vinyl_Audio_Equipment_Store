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
        
        # 1. Update the first column of the footer
        col_regex = re.compile(r'(<div class="lg:col-span-2 space-y-4">.*?)master analog sound\.(.*?</p>)', re.DOTALL)
        
        svgs = '''
          <div class="flex items-center gap-4 pt-2 text-espresso dark:text-ivory">
            <a href="#" class="hover:text-brass transition-colors" aria-label="Instagram">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
            </a>
            <a href="#" class="hover:text-brass transition-colors" aria-label="X (Twitter)">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>
            </a>
            <a href="#" class="hover:text-brass transition-colors" aria-label="Spotify">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.54.659.301 1.02zm1.44-3.3c-.301.42-.84.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15.001 10.62 18.72 12.9c.42.3.6.84.24 1.14zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.6.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.239.54-.959.72-1.56.3z"/></svg>
            </a>
          </div>
          <p class="text-[10px] text-brass font-mono pt-1">
            Members of the International Vinyl Collectors Association (IVCA)
          </p>
'''
        
        if 'since 2012.' not in content:
            content = col_regex.sub(r'\1master analog sound since 2012.\2\n' + svgs, content)
        
        # 2. Update the bottom footer row to remove social icons
        bottom_row_regex = re.compile(r'<div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4.*?</div>\s*</footer>', re.DOTALL)
        
        clean_bottom_row = '''<div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-espresso/50 dark:text-ivory/50">
        <div>&copy; 2026 Vinyl Fine Vinyl & Audiophile Equipment Ltd. All rights reserved.</div>
        <div class="flex gap-6">
          <a href="#" class="hover:text-brass transition-colors">Privacy Policy</a>
          <a href="#" class="hover:text-brass transition-colors">Collector Terms</a>
        </div>
      </div>
    </div>
  </footer>'''
        
        content = bottom_row_regex.sub(clean_bottom_row, content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
