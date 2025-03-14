def max_prime_divisor(a):
    max_prime = -1
    if a <= 1:
        return max_prime

    for i in range(2, a // 2 + 1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                continue
        max_prime = i
    return max_prime


def five_divisible(a):
    mult = 1
    for i in str(a):
        if int(i) % 5 == 0:
            mult *= int(i)
    return mult


value = input('write some value: \n')

print("Largest prime divisor of a number", max_prime_divisor(int(value)))
print("The product of numbers divisible by 5: ", five_divisible(int(value)))
