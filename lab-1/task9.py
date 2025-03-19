def sort_strings_by_length(s):
    s.sort(key=len)

    for string in s:
        print(string)


n = int(input("Введи количество строк: "))
strings = []
for i in range(n):
    strings.append(input(f"{i+1}. "))
sort_strings_by_length(strings)
