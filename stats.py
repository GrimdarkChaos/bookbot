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

# Returns what to sort on
def sort_on(items):
    return items["num"]

# Sorts the dictionary of character_count
def sorted_list(character_count):
    counted_char_list = [{"char": c, "num": n} for c, n in character_count.items()]
    counted_char_list.sort(reverse=True, key=sort_on)
    return counted_char_list