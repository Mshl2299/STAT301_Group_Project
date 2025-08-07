import nbformat
import sys

# HOW TO RUN
# right click on this file and click 'Create Console for Editor'
# type '%run word_count.py' as the input
# you may need to use Shift+Enter to submit the input

def count_words_in_markdown():
    with open('Project.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    total_words = 0

    # Counter for markdown cells
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            
            # Skip the 'References' cell
            if '4) References' in cell.source:
                continue

            # Count #words in cell
            words = cell.source.split()
            total_words += len(words)

    print(f"Total words in markdown cells (excluding references): {total_words}")

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python count_markdown_words.py")
    else:
        count_words_in_markdown()
