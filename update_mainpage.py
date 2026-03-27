import os
import re

# Path to the folder
folder_path = r"c:\Users\Connor\Documents\BabyGang Files"

# List all HTML files except MainPage.html
html_files = [f for f in os.listdir(folder_path) if f.endswith('.html') and f != 'MainPage.html']

# Function to get display name
def get_display_name(filename):
    # Remove the [id].html part
    return re.sub(r'\s*\[\d+\]\.html$', '', filename)

# Generate dmFiles array
dm_files = []
dm_list_items = []
for f in sorted(html_files):
    display = get_display_name(f)
    dm_files.append(f"{{name: '{f}', display: '{display}'}}")
    dm_list_items.append(f'<li><a href="{f}">{display}</a></li>')

dm_files_str = ',\n            '.join(dm_files)
dm_list_str = '\n        '.join(dm_list_items)

# Read the MainPage.html
with open(os.path.join(folder_path, 'MainPage.html'), 'r', encoding='utf-8') as file:
    content = file.read()

# Replace the dmFiles array
pattern = r'const dmFiles = \[.*?\];'
replacement = f'const dmFiles = [\n            {dm_files_str}\n        ];'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Replace the ul content
pattern_ul = r'<ul id="dm-list">.*?</ul>'
replacement_ul = f'<ul id="dm-list">\n        {dm_list_str}\n    </ul>'
new_content = re.sub(pattern_ul, replacement_ul, new_content, flags=re.DOTALL)

# Write back
with open(os.path.join(folder_path, 'MainPage.html'), 'w', encoding='utf-8') as file:
    file.write(new_content)

print("MainPage.html updated with all HTML files.")