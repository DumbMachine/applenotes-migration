# applenotes-migration

https://news.ycombinator.com/item?id=35316679 was a reminder to remove my notes from :apple: notes to obsidian. So here's a simple script

<mark>Note this won't work for rich media stored in your notes, like pdfs. :(</mark>

1. Run the JXA script to extract all notes to seperate html files

   ```bash
   $ osascript -l JavaScript index.js
   ```

2. Run the python script to convert `html` files to `md` and save em into your obsidian vault. If you just need to export the notes to markdown and don't care for obsidian, just punch in any folder of your choice.
   ```bash
   $ python main.py <folder_name>
   ```

##### Finding your Obsidian Vault
Checkout these images