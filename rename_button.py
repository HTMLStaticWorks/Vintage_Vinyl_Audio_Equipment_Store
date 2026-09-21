import glob

files = glob.glob('*.html')
for f in files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # Replace the desktop button text
        content = content.replace('>Join Lounge</a>', '>Signup</a>')
        # Replace the mobile button text which might be "Create Account" or "Join Lounge"
        content = content.replace('>Create Account</a>', '>Signup</a>')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
