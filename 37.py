import random

def random_generator(start, end):
    while True:
        yield random.randint(start, end)


start = int(input())
end = int(input())

generator = random_generator(start, end)

for _ in range(10):
    print(next(generator))
