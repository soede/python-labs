import sys

from collections import Counter


def max_anagram_subarray_length(n, a, m, b):
    for L in range(min(n, m), 0, -1):
        seen_hashes = set()

        counter_a = Counter(a[:L])
        seen_hashes.add(frozenset(counter_a.items()))

        for i in range(L, n):
            counter_a[a[i]] += 1
            counter_a[a[i - L]] -= 1

            if counter_a[a[i - L]] == 0:
                del counter_a[a[i - L]]

            seen_hashes.add(frozenset(counter_a.items()))

        counter_b = Counter(b[:L])

        if frozenset(counter_b.items()) in seen_hashes:
            return L

        for i in range(L, m):
            counter_b[b[i]] += 1
            counter_b[b[i - L]] -= 1

            if counter_b[b[i - L]] == 0:
                del counter_b[b[i - L]]

            if frozenset(counter_b.items()) in seen_hashes:
                return L

    return 0


input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))
m = int(input().strip())
b = list(map(int, input().split()))

print(max_anagram_subarray_length(n, a, m, b))
