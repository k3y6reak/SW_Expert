prime_map = []
n = 999
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            prime_map.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
