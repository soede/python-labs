import random


def shuffle_words(sentence: str) -> str:
    words = sentence.split()
    random.shuffle(words)
    return ' '.join(words)


s = input("write text for shuffle")
shuffled = shuffle_words(s)
print(shuffled)
