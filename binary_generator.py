def binary_generator(n):
    configuration = [0] * (n+1)

    while True:
        yield configuration[1:]
        j = n
        while configuration[j] == 1:
            configuration[j] = 0
            j -= 1
        if j == 0:
            break
        else:
            configuration[j] = 1



n = int(input())
generator = binary_generator(n)

for val in generator:
    print(val)