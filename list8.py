import random

def has_duplicates(t):
    sort = t[:]
    sort.sort()
    for i in range(len(sort)-1):
        if sort[i] == sort[i+1]:
            return True

def birthday_duplicates():
    birthdays = []
    count = 0
    i = 0
    while i < 1000:
        for items in range(23):
            birthdays.append(random.randint(1,365))

        if has_duplicates(birthdays):
                count += 1
        i +=1
    return count/i * 100
