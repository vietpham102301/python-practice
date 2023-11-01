def fib_generator(start, end):
    first = 0
    second = 1
    for i in range(end+1):
        if start <= first <= end:
            yield first
        third = first + second
        first = second
        second = third


start = int(input())
end = int(input())

for val in fib_generator(start, end):
    print(val)
