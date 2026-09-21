import glob

files = glob.glob('*.html')
for f in files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        original_content = content
        
        # Clean up corrupted classes
        content = content.replace('dark:text-espresso dark:text-ivory/80', 'dark:text-ivory/80')
        content = content.replace('dark:text-espresso dark:text-ivory/60', 'dark:text-ivory/60')
        content = content.replace('dark:text-espresso dark:text-ivory/50', 'dark:text-ivory/50')
        content = content.replace('dark:text-espresso dark:text-ivory/40', 'dark:text-ivory/40')
        content = content.replace('dark:text-espresso dark:text-ivory', 'dark:text-ivory')
        
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Cleaned up {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
