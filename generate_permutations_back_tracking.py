n = int(input())
visited = [0] * (n + 1)
configuration = [0] * (n + 1)


def generate_permutations_back_tracking(i):
    for j in range(1, n + 1):
        if visited[j] == 0:
            visited[j] = 1
            configuration[i] = j
            if i == n:
                print(configuration[1:])
            else:
                generate_permutations_back_tracking(i + 1)
            visited[j] = 0


if __name__ == "__main__":
    generate_permutations_back_tracking(1)
