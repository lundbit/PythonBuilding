def break_words(stuff):
    """This function will break up words for us."""
    # split() breaks up and puts a ' ' in between
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ Sorts the words """
    # return sorted is a function
    return sorted(words)

def print_first_word(words):
    """ prints the first words after popping it off."""
    # .pop(n) returns n position after popping  --- 0 is first position
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ prints the last word after popping it off."""
    # -1 is the last pop position, or in this case, word printed
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """ Takes in a full sentence and returns the sorted words. """
    # uses function defined above which split them
    words = break_words(sentence)
    # uses function above which sorts them
    return sort_words(words)

def print_first_and_last(sentece):
    """ Prints the first and last word of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentnece(sentence)
    print_first_word(words)
    print_last_word(words)
