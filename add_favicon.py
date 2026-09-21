import os
import glob

favicon_link = """  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23c5a059' stroke-width='1.5' stroke-linecap='round'%3E%3Ccircle cx='12' cy='12' r='9' /%3E%3Ccircle cx='12' cy='12' r='3' fill='%23c5a059' /%3E%3Cpath d='M12 3v3M21 12h-3M12 21v-3M3 12h3' /%3E%3C/svg%3E">
"""

def add_favicon_to_html_files():
    html_files = glob.glob('*.html')
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'rel="icon"' in content or 'rel="shortcut icon"' in content:
            print(f"Favicon already exists in {file_path}")
            continue
            
        if '</head>' in content:
            new_content = content.replace('</head>', f'{favicon_link}</head>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added favicon to {file_path}")
        else:
            print(f"Could not find </head> in {file_path}")

if __name__ == "__main__":
    add_favicon_to_html_files()
