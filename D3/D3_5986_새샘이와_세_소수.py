prime_map = []


def main():
    global prime_map
    n = 999
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            prime_map.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    tc = int(input())
    for t in range(1, tc+1):
        num = int(input())
        num_prime_map = []

        for p in prime_map:
            if p > num:
                break
            else:
                num_prime_map.append(p)
        ans = 0
        for i in range(0, len(num_prime_map)):
            for j in range(i, len(num_prime_map)):
                for k in range(j, len(num_prime_map)):
                    if num == num_prime_map[i] + num_prime_map[j] + num_prime_map[k]:
                        ans += 1

        print("#"+str(t), ans)


if __name__ == '__main__':
    main()
