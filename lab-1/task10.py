def sort_strings_by_word_count(s):
    strings.sort(key=lambda x: len(x.split()))
    for string in s:
        print(string)


n = int(input("Введите количество строк: "))
strings = []

for i in range(n):
    strings.append(input(f"{i+1}:"))
sort_strings_by_word_count(strings)

