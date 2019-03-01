def power(a, n):
    k = n
    cnt = 0
    while k != 1:
        k //= 2
        cnt += 1

    pow_map = [0]*(cnt+1)
    pow_map[0] = a
    for i in range(1, len(pow_map)):
        pow_map[i] = pow_map[i - 1] * pow_map[i - 1]

    result = 1
    for i in range(0, cnt+1):
        if n & (1 << i) != 0:
            result *= pow_map[i]
    print(result)

def main():
    for t in range(1, 11):
        n = input()
        line = list(map(int, input().split()))
        print("#"+n+" ", end='')
        power(line[0], line[1])


if __name__ == '__main__':
    main()
