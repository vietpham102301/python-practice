def generate_permutations(n):
    configuration = [0]*(n+1)
    for i in range(1, n+1):
        configuration[i] = i

    while True:
        for i in range(1, n+1):
            print(configuration[i], end="")
        print(" ", end="")
        j = n - 1
        k = n
        while configuration[j] > configuration[j+1]:
            j -= 1
        if j == 0:
            break
        else:
            while configuration[k] < configuration[j]:
                k -= 1
            configuration[j], configuration[k] = configuration[k], configuration[j]
            l = j+1
            r = n
            while l < r:
                configuration[l], configuration[r] = configuration[r], configuration[l]
                l += 1
                r -= 1


if __name__ == "__main__":
    generate_permutations(5)
