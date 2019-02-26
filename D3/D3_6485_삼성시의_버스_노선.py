def main():
    tc = int(input())

    for t in range(1, tc+1):
        n = int(input())
        n_list = []
        for i in range(n):
            n_list.append(list(map(int, input().split())))

        p = int(input())

        print("#"+str(t)+" ", end='')
        for i in range(1, p+1):
            c = int(input())
            ans = 0
            for j in range(0, n):
                if n_list[j][0] <= c and c <= n_list[j][1]:
                    ans += 1
            print(str(ans) + " ", end='')
        print()


if __name__ == '__main__':
    main()
