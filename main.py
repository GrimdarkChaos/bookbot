#Import functions
from stats import num_of_words, count_characters

#Take the file path and open the file returning the contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#Define main
def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    word_count = num_of_words(file_contents)
    character_count= count_characters(file_contents)
    print(f"Found {word_count} total words")
    print(character_count)

#Calling main
main("./books/frankenstein.txt")