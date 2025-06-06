def get_book_text (filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

from stats import count_words
from stats import characters
import sys


def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one file path. Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the file path from the command line
    filepath = sys.argv[1]

    try:
        full_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)

    word_count = count_words(full_text)
    character = characters(full_text)

    print(f"Found {word_count} total words")
    print(character)


main()
