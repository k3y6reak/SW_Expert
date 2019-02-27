def main():
    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        n = line[0]
        k = line[1]

        items = []
        dp = [[0]*(k+1) for _ in range(n+1)]

        for i in range(n):
            items.append(list(map(int, input().split())))

        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if j >= items[i - 1][0]:
                    dp[i][j] = max(dp[i - 1][j - items[i - 1][0]] + items[i - 1][1], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        print("#"+str(t), dp[-1][-1])


if __name__ == '__main__':
    main()
