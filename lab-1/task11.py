from collections import Counter
import math

VOWELS_LATIN = "AEIOUYaeiouy"
VOWELS_CYRILLIC = "АЕЁИОУЫЭЮЯаеёиоуыэюя"

def is_vowel(char):
    return char in VOWELS_LATIN or char in VOWELS_CYRILLIC

def char_frequency(text):
    counter = Counter(text)
    total_chars = len(text) if text else 1
    return {char: count / total_chars for char, count in counter.items()}

def most_frequent_char_info(text):
    frequencies = char_frequency(text)
    if not frequencies:
        return None, 0
    most_common_char = max(frequencies, key=frequencies.get)
    return most_common_char, frequencies[most_common_char]

def alphabet_frequency(text):
    unique_chars = set(text)
    return {char: 1 / len(unique_chars) for char in unique_chars} if unique_chars else {}

def frequency_difference(text):
    most_common_char, freq_in_text = most_frequent_char_info(text)
    freq_in_alphabet = alphabet_frequency(text).get(most_common_char, 0)
    return abs(freq_in_text - freq_in_alphabet)



def main():
    print("Выберите способ сортировки:")
    print("1. По разнице частот самого частого символа и его частоты в алфавите.")

    choice = input("Введите номер (1-4): ").strip()

    if choice not in {"1", "2", "3", "4"}:
        print("Неверный выбор, попробуйте снова.")
        return

    print("Введите строки (пустая строка для завершения ввода):")
    strings = []
    while True:
        line = input().strip()
        if line == "":
            break
        strings.append(line)

    if not strings:
        print("Нет строк для обработки.")
        return

    if choice == "1":
        sorted_strings = sorted(strings, key=frequency_difference)

    print("\nОтсортированные строки:")
    for line in sorted_strings:
        print(line)


if __name__ == "__main__":
    main()
