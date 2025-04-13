def find_max_sum(filename):
    with open(filename) as f:
        N, K = map(int, f.readline().split())
        values = [int(f.readline()) for _ in range(N)]

    best1 = [0] * N
    best1[0] = values[0]
    for i in range(1, N):
        best1[i] = max(best1[i-1], values[i])

    best2 = [0] * N
    for i in range(K, N):
        best2[i] = max(best2[i-1], values[i] + best1[i-K])

    max_sum = 0
    for i in range(2*K, N):
        max_sum = max(max_sum, values[i] + best2[i-K])

    return max_sum

print(find_max_sum("27-166b.txt"))
