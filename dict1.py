x= open('words.txt')
englishdict = dict()


def create_diction():
    counter = 0
    dictionairy = dict()
    for line in x:
        word = line.strip()
        dictionairy[word] = counter
        counter += 1
    return dictionairy
