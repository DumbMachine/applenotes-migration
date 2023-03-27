import os
import sys

from glob import glob
from markdownify import markdownify as md


# Example: /Users/dumbmachine/Library/Mobile Documents/com~apple~CloudDocs/obisidian-data/
try:
    OBSIDIAN_VAULT_LOC = sys.argv[1]
except IndexError:
    print("Please provide the path to your Obsidian vault")
    os._exit(1)

# OBSIDIAN_VAULT_LOC = "/tmp/obisidian-data/"
html_files = glob(os.path.join("", "*-apnotes.html"))
files_not_updated = []
for file in html_files:
    markdown = None
    with open(file, "r") as html:
        raw_html = html.read()
        markdown = md(raw_html)
    if markdown:
        try:
            md_file = file.replace("-apnotes.html", ".md")
            with open(os.path.join(OBSIDIAN_VAULT_LOC, md_file), "w") as md_file:
                bytes_written = md_file.write(markdown)
            os.remove(file)
        except Exception as reason:
            files_not_updated.append((file, reason))
