import random


def shuffle_words(sentence):
    words = sentence.split()
    random.shuffle(words)
    return ' '.join(words)


def count_words(sentence):
    words = sentence.split()
    return sum(1 for word in words if len(word) % 2 == 0)


def sort_flag(colors):
    counts = {"белый": 0, "синий": 0, "красный": 0}

    for color in colors:
        counts[color] += 1

    return ["белый"] * counts["белый"] + ["синий"] * counts["синий"] + ["красный"] * counts["красный"]


s = input("write something")
shuffled = shuffle_words(s)
count = count_words(s)
print(shuffled)
print(count)
print(sort_flag)
