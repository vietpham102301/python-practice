import math


def is_primes(a_number):
    for i in range(2, math.floor(math.sqrt(a_number)) + 1):
        if a_number % i == 0:
            return False

    return True


def primes_generator(start, end):
    for i in range(start, end + 1):
        if is_primes(i):
            yield i


start = int(input())
end = int(input())

for val in primes_generator(start, end):
    print(val)
