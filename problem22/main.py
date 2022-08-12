ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import sys

def read_and_sort_names(file):
    file_handle = open(file, 'r')
    lines = file_handle.readlines()
    stripped_string = lines[0].replace('"', '')
    names = stripped_string.split(",")
    names.sort()
    return names

def get_word_sum(word):
    print(word)
    word_total = 0
    for letter in word:
        letter_index = ALPHABET.index(letter)
        word_total += letter_index + 1
    return word_total

def main():
    sorted_names = read_and_sort_names(sys.argv[1])
    name_score_total = 0
    for i, name in enumerate(sorted_names):
        name_score = (i + 1) * get_word_sum(name)
        name_score_total += name_score
    print(name_score_total)

if (__name__) == '__main__':
    main()
