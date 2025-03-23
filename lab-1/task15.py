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

def cyclic_shift_left(arr):
    if len(arr) > 1:
        first_element = arr.pop(0)
        arr.append(first_element)

def main():
    task = input("Введи номер задания: (3, 15, 27) ")

    if task not in {"3", "15", "27"}:
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

    elif int(task) == 27:
        cyclic_shift_left(arr)
        print("Массив после циклического сдвига влево: ", arr)

if __name__ == "__main__":
    main()
