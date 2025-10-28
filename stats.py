#Take the book contents and return the word count
def num_of_words(file_contents):
    word_count = len(file_contents.split())
    return word_count

#Take the book contents and return a count of each character
def count_characters(file_contents):
    lower_case = file_contents.lower()
    character_count = {}
    for c in lower_case:
        if c in character_count:
            character_count[c] +=1
        else:
            character_count[c] = 1
    return character_count