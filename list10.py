import time

f = open('words.txt')

def build_list1():
    word_list = []
    for line in f:
        word = line.strip()
        word_list.append(word)
    f.seek(0)
    return word_list

def build_list2():
    word_list = []
    for line in f:
        word = line.strip()
        word_list += [word]
