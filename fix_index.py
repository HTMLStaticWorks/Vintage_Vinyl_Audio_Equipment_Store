import re

with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()
    
# Extract the social block
social_pattern = r'(\s*<div class="flex items-center gap-4 ">.*?</a>\s*</div>)'
match = re.search(social_pattern, content, re.DOTALL)

if match:
    social_block = match.group(1)
    
    # Remove from old location
    content = content.replace(social_block, '')
    
    # Add a top margin for spacing when moving it under the text
    modified_social_block = social_block.replace('<div class="flex items-center gap-4 ">', '<div class="flex items-center gap-4 mt-6">')
    
    # Find the text under the logo
    logo_text_pattern = r'(Luxury vinyl boutique and audiophile listening room based in London and Paris\. Curating rare original pressings and master analog sound since 2012\.\s*</p>)'
    
    if re.search(logo_text_pattern, content):
        content = re.sub(logo_text_pattern, r'\1' + modified_social_block, content)
        
        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(content)
        print("Updated index.html")
    else:
        print("Logo text not found in index.html")
else:
    print("Social block not found in index.html")
