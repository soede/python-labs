def count_series(filename):
    with open(filename) as f:
        numbers = list(map(int, f.read().split()))

    if not numbers:
        return 0

    count = 1
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            count += 1

    return count
