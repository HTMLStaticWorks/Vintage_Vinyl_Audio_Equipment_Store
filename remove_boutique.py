import glob

files = glob.glob('*.html')
target = '<span class="text-[10px] tracking-[0.2em] uppercase text-brass font-medium">Boutique & Listening Lounge</span>'

for f in files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        if target in content:
            # We'll also remove the trailing newline/spaces if possible, or just the string itself.
            new_content = content.replace(target, '')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Removed from {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
