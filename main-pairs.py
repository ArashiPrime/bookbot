# Import Counter function to count words
from collections import Counter
import sys

def read_file(filepath):
    # Read the contents of the file and return it as a string
    with open(filepath, 'r') as file:
        file_contents = file.read()
        return file_contents

def count_characters(text):
    # Count all characters in the text
    return len(text)

def count_words(text):
    # Count all words in the text
    words = text.split()
    return len(words)    

def count_unique_words(text):
    # Split the text into words
    words = text.split()

    # Use Counter to count the frequency of each word
    word_counts = Counter(words)
    return len(word_counts)    

def count_first_two_letters(text):
    # Dictionary to store frequency of starting letter pairs
    letter_pairs_dict = {}

    words = text.split()
    
    for word in words:
        # Normalize to lowercase to combine cases like 'Th' and 'th'
        word = word.lower()
        if len(word) >= 2:
            first_two = word[:2]
            # Only count pairs of letters, not numbers or symbols
            if first_two.isalpha():
                if first_two in letter_pairs_dict:
                    letter_pairs_dict[first_two] += 1
                else:
                    letter_pairs_dict[first_two] = 1
    return letter_pairs_dict

def count_unique_characters(text):
    # Count all unique characters in the text
    character_dict={}
    symbol_dict={}
    number_dict={}
    whitespace_dict={}

    # Convert the string to lowercase to ensure case-insensitivity
    unique_character_string = text.lower()
    
    # Create a dictionary to store the frequency of each character
    for character in unique_character_string:
        if character.isalpha():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
        elif character.isdigit():
            if character in number_dict:
                number_dict[character] += 1
            else:
                number_dict[character] = 1
        elif character.isspace():
            if character in whitespace_dict:
                whitespace_dict[character] += 1
            else:
                whitespace_dict[character] = 1
        else:
            if character in symbol_dict:
                symbol_dict[character] += 1
            else:
                symbol_dict[character] = 1 
    return character_dict, number_dict, whitespace_dict, symbol_dict

def find_most_common_word(text):
    # Split the text into words
    words = text.split()

    # Use Counter to count the frequency of each word
    word_counts = Counter(words)

    # Find the most common word and its frequency
    if word_counts:
        most_common_word, frequency = word_counts.most_common(1)[0]
    else:
        most_common_word, frequency = None, 0
    return most_common_word, frequency

def main(filepath):
    # Read the file contents
    text = read_file(filepath)

    # Count words and characters
    word_count = count_words(text)
    character_count = count_characters(text)
    unique_word_count = count_unique_words(text)
    character_dict, number_dict, whitespace_dict, symbol_dict = count_unique_characters(text)
    most_common_word, frequency = find_most_common_word(text)
    letter_pairs_counts = count_first_two_letters(text)

    # Print the results
    print(f"--- Begin report of {filepath} ---")
    print(f"Word count: {word_count}")
    print(f"Unique word count: {unique_word_count}")
    print(f"Most common word: '{most_common_word}' with a frequency of {frequency}")
    print("")
    print(f"Total character count: {character_count}")
    print(f"Count of each unique character: {character_dict}")

    def sort_by_count(item):
        return item[1]

    for char_count in sorted(character_dict.items(), key=sort_by_count, reverse=True):
        if char_count[0].isalpha():
            print(f"The character '{char_count[0]}' was found {char_count[1]} times")
    

    print("")
    print(f"The following 2-character pairs are the most common to start words with:")
    
    sorted_pairs = sorted(letter_pairs_counts.items(), key=sort_by_count, reverse=True)[:10]
    
    # Get top 10 pairs sorted by frequency
    
    for pair, count in sorted_pairs:
        print(f"The letter pair '{pair}' appears at the start of {count} words")

    print("--- End report ---")
   
if __name__ == "__main__":
    # Execute the main function
    if len(sys.argv) != 2:
        print("Usage: python main-pairs.py <filepath>")
    else:
        main(sys.argv[1])
