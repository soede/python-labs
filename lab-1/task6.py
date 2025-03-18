import re


def count_russian_chars(s):
    return re.findall(r'[а-яА-ЯёЁ]', s)


def find_lowercase_latin_chars(text):
    return  re.findall(r'[a-z]', text)


def find_min_integer(text):
    integers = re.findall(r'-?\d+', text)
    integers = [int(i) for i in integers]
    return min(integers) if integers else None


s = input("Введи что-то: ")
print(f"количество русских символов: {len(count_russian_chars(s))}")
print(f"Все латинские символы из строки символов: {find_lowercase_latin_chars(s)}")
print(f"Минимальное числовое значение из строки: {find_min_integer(s)}")
