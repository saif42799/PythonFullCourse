# Data structure and performance
# dictionary, sets are fast
# lists are slow

# BIG-O Notation


list_of_word = "Word"

def word_count(list_of_word):
    letter_count = 0
    word_list = []

    for i in list_of_word:
        letter_count += 1

    for i in list_of_word:
        if i.islower():
            word_list.append("0")
        elif i.isupper():
            word_list.append("1")
        else:
            pass
    print(word_list)


word_count(list_of_word)












