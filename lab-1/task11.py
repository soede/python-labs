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

def squared_frequency_deviation(text):
    most_common_char, freq_in_text = most_frequent_char_info(text)
    freq_in_alphabet = alphabet_frequency(text).get(most_common_char, 0)
    return (freq_in_text - freq_in_alphabet) ** 2

def vowel_consonant_difference(text):
    vc_count = 0
    cv_count = 0
    for i in range(len(text) - 1):
        if is_vowel(text[i]) and not is_vowel(text[i + 1]):
            vc_count += 1
        elif not is_vowel(text[i]) and is_vowel(text[i + 1]):
            cv_count += 1
    return abs(vc_count - cv_count)

def global_squared_frequency_deviation(texts):
    all_frequencies = Counter()
    total_chars = sum(len(text) for text in texts)

    for text in texts:
        all_frequencies.update(text)

    global_frequencies = {char: count / total_chars for char, count in all_frequencies.items()}

    def deviation(text):
        most_common_char, freq_in_text = most_frequent_char_info(text)
        freq_in_global = global_frequencies.get(most_common_char, 0)
        return (freq_in_text - freq_in_global) ** 2

    return deviation

def main():
    print("Выберите способ сортировки:")
    print("1. По разнице частот самого частого символа и его частоты в алфавите.")
    print("2. По квадратичному отклонению частоты самого частого символа.")
    print("3. По разнице количества сочетаний ‘гласная-согласная’ и ‘согласная-гласная’.")
    print("4. По квадратичному отклонению частоты самого частого символа в наборе строк от его частоты в данной строке.")

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
    elif choice == "2":
        sorted_strings = sorted(strings, key=squared_frequency_deviation)
    elif choice == "3":
        sorted_strings = sorted(strings, key=vowel_consonant_difference)
    elif choice == "4":
        sorted_strings = sorted(strings, key=global_squared_frequency_deviation(strings))

    print("\nОтсортированные строки:")
    for line in sorted_strings:
        print(line)

if __name__ == "__main__":
    main()
