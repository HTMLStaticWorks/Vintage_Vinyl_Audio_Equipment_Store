import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find the footer block
    footer_match = re.search(r'(<footer\b.*?>.*?</footer>)', content, re.DOTALL)
    
    if footer_match:
        footer = footer_match.group(1)
        original_footer = footer
        
        # Replace colors to be responsive
        footer = footer.replace('bg-[#0e0c0a]', 'bg-ivory dark:bg-[#0e0c0a]')
        
        # text-ivory/80
        footer = re.sub(r'\btext-ivory/80\b', 'text-espresso/80 dark:text-ivory/80', footer)
        # border-ivory/10
        footer = re.sub(r'\bborder-ivory/10\b', 'border-espresso/10 dark:border-ivory/10', footer)
        # bg-ivory/5
        footer = re.sub(r'\bbg-ivory/5\b', 'bg-espresso/5 dark:bg-ivory/5', footer)
        # text-ivory/60
        footer = re.sub(r'\btext-ivory/60\b', 'text-espresso/60 dark:text-ivory/60', footer)
        # text-ivory/50
        footer = re.sub(r'\btext-ivory/50\b', 'text-espresso/50 dark:text-ivory/50', footer)
        # text-ivory/40
        footer = re.sub(r'\btext-ivory/40\b', 'text-espresso/40 dark:text-ivory/40', footer)
        # text-ivory (standalone)
        footer = re.sub(r'\btext-ivory\b', 'text-espresso dark:text-ivory', footer)
        
        if footer != original_footer:
            content = content.replace(original_footer, footer)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated footer in {f}")
        else:
            print(f"Footer already responsive in {f}")
    else:
        print(f"No footer found in {f}")
