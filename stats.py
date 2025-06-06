def count_words (full_text):
        text=full_text.split()
        word_count=len(text)
        return word_count

import string

def characters(full_text):
    lower_text = full_text.lower()
    character_counts = {}

    # Initialize all letters a–z and space to 0
    for letter in string.ascii_lowercase:
        character_counts[letter] = 0

    # Count each character
    for char in lower_text:
        if char in character_counts:
            character_counts[char] += 1

    # Sort the dictionary by frequency (value) in descending order
    sorted_counts = dict(sorted(character_counts.items(), key=lambda item: item[1], reverse=True))

    print("--------- Character Count -------")
    for char, count in sorted_counts.items():
        if count > 0:
            display_char = "' '" if char == " " else char
            print(f"{display_char}: {count}")
    print("============= END ===============")

    return sorted_counts

