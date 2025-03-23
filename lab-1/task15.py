def is_global_max(arr, index):
    if index < 0 or index >= len(arr):
        return False
    value_at_index = arr[index]
    for i in range(len(arr)):
        if arr[i] > value_at_index:
            return False
    return True

def is_local_min(arr, index):
    if index < 0 or index >= len(arr):
        return False
    left = arr[index - 1] if index > 0 else float('inf')
    right = arr[index + 1] if index < len(arr) - 1 else float('inf')
    return arr[index] < left and arr[index] < right

def main():
    task = input("Введи номер задания: (3, 15) ")

    if task not in {"3", "15"}:
        print("Неправильный номер задания")
        return

    print("Введите элементы массива (пустая строка для завершения ввода): ")
    arr = []
    while True:
        line = input().strip()
        if line == "":
            break
        arr.append(int(line))

    index = int(input("Введи индекс: "))

    if int(task) == 3:
        if is_global_max(arr, index):
            print("Это глобальный максимум")
        else:
            print("Это не глобальный максимум")
    elif int(task) == 15:
        if is_local_min(arr, index):
            print("Это локальный минимум")
        else:
            print("Это не локальный минимум")

if __name__ == "__main__":
    main()
