#Take the file path and open the file returning the contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#Take the book contents and return the word count
def num_of_words(file_contents):
    word_count = len(file_contents.split())
    return word_count

#Define main
def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    word_count = num_of_words(file_contents)
    print(f"Found {word_count} total words")

#Calling main
main("./books/frankenstein.txt")