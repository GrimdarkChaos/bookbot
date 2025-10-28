#Import functions
from stats import num_of_words, count_characters, sorted_list

#Define file path
path_to_file = "books/frankenstein.txt"

#Take the file path and open the file returning the contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#Define main
def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    word_count = num_of_words(file_contents)
    character_count = count_characters(file_contents)
    sorted_character_count = sorted_list(character_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_character_count:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

#Calling main
main(path_to_file)