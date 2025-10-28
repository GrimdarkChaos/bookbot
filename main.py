#Take the file path and open the file returning the contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#Define main
def main(file_path):
    print(get_book_text(file_path))

#Calling main
main("./books/frankenstein.txt")