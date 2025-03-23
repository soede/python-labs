def is_global_max(arr, index):
    if index < 0 or index >= len(arr):
        return False

    value_at_index = arr[index]

    for i in range(len(arr)):
        if arr[i] > value_at_index:
            return False

    return True



def main():
    task = input("Введи номер задания: (3, 15) ")

    if task not in {"3", "14"}:
        print("Неправильный номер задания")
        return

    print("Введите элементы массива (пустая строка для завершения ввода): ")
    arr = []
    while True:
        line = input().strip()
        if line == "":
            break
        arr.append(int(line))

    if int(task) == 3:
        index = int(input("Введи индекс: "))
        if is_global_max(arr, index):
            print("Это глобальный максимум")
        else:
            print("Это не глобальный максимум ")

        return


if __name__ == "__main__":
    main()
