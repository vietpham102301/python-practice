def combinations_generator(k, n):
    configuration = [0]*(k+1)
    for i in range(1, k+1):
        configuration[i] = i
    while True:
        yield configuration[1:]
        j = k
        while configuration[j] == n - k + j:
            j -= 1
        if j == 0:
            break
        else:
            configuration[j] += 1
            for vt in range(j+1, k+1):
                configuration[vt] = configuration[vt - 1] + 1


n = int(input())
k = int(input())

generator = combinations_generator(k, n)
for val in generator:
    print(val)

