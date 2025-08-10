import nbformat
import sys
import markdown
from bs4 import BeautifulSoup

# In terminal: pip install markdown beautifulsoup4

# HOW TO RUN
# right click on this file and click 'Create Console for Editor'
# type '%run word_count.py' as the input
# you may need to use Shift+Enter to submit the input

def markdown_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()

def count_words_in_markdown():
    with open('Project.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    total_words = 0

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            if '4) References' in cell.source:
                continue
            if 'Column name' in cell.source:
                continue

            text = markdown_to_text(cell.source)

            filtered_lines = []
            for line in text.splitlines():
                # Remove lines table separators
                if set(line.strip()) <= set('-|: '):
                    continue
                filtered_lines.append(line)

            filtered_text = '\n'.join(filtered_lines)
            filtered_text = filtered_text.replace('|', '')
            filtered_text = filtered_text.replace('-', '')
            print(filtered_text)
            words = filtered_text.split()
            total_words += len(words)

    print(f"Total words in markdown cells (excluding references): {total_words}")

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python count_markdown_words.py")
    else:
        count_words_in_markdown()
