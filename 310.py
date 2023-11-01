def binary_generator(n):
    configuration = [0]*n
    while True:
        yield configuration
        i = n-1
        while configuration[i] == 1:
            configuration[i] == 0
            i -= 1
            if i == -1:
                break
        if i == -1:
            break
        configuration[i] = 1


def binary_generator2(n):
    configuration = [0] * n
    yield configuration
    i = n - 1
    while i >= 0:
        if configuration[i] == 1:
            i -= 1
        if configuration[i] == 0:
            configuration[i] = 1
            for j in range(i+1, n):
                configuration[j] = 0
            yield configuration
            i = n - 1


if __name__ == "__main__":
    number = int(input())

    for i in range(1, number+1):
        generator = binary_generator2(i)
        for val in generator:
            print(val)