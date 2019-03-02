def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        s = 0
        a = [0]*n
        for i in range(n):
            tmp = int(input())
            s += tmp
            a[i] = tmp
        s //= n

        ans = 0
        for i in a:
            l = s - i
            if l < 1:
                continue
            ans += l

        print("#%d %d" %(t, ans))


if __name__ == '__main__':
    main()
