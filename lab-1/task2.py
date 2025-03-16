import random


def shuffle_words(sentence):
    words = sentence.split()
    random.shuffle(words)
    return ' '.join(words)


def count_words(sentence):
    words = sentence.split()
    return sum(1 for word in words if len(word) % 2 == 0)


s = input("write something")
shuffled = shuffle_words(s)
count = count_words(s)
print(shuffled)
print(count)
