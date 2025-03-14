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


def sum_of_numbers(a):
    s = 0
    for i in str(a):
        s += int(i)
    return s


def find_coprime_divisors(n):
    s = sum_of_numbers(n)
    divisors = [i for i in range(1, n+1) if n % i == 0]

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    coprime_divisors = [divisor for divisor in divisors if gcd(divisor, s) == 1]
    return coprime_divisors


value = input('write some value: \n')

print("Largest prime divisor of a number", max_prime_divisor(int(value)))
print("The product of numbers divisible by 5: ", five_divisible(int(value)))
print("Largest prime divisor of sum of the number: ", find_coprime_divisors(int(value)))
