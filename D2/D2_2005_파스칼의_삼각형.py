dp = []


def nCr_dp(n, r):
    global dp
    for i in range(1, len(dp)):
        for j in range(0, len(dp[0])):
            if j == 0 or i == j:
                dp[i][j] = 1

            elif dp[i][j] == 0:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][r]


def main():
    global dp
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1

        print("#"+str(t))
        for i in range(n):
            for j in range(i+1):
                print(str(nCr_dp(i, j)) + " ", end='')
            print()


if __name__ == '__main__':
    main()
