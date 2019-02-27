import time

memo = [[0]*10000 for _ in range(10000)]
dp = []

def nCr_dp(n, r):
    global dp
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if j == 0 or i == j:
                dp[i][j] = 1

            elif dp[i][j] == 0:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][r]


def nCr_memo(n, r):
    if r == 0 or r == n:
        return 1

    if memo[n][r] == 0:
        memo[n][r] = nCr_memo(n - 1, r - 1) + nCr_memo(n - 1, r)

    return memo[n][r]


def nCr(n, r):
    if r == 0 or r == n:
        return 1

    return nCr(n-1, r-1) + nCr(n-1, r)


def main():
    global dp

    n = 997
    r = 2

    start = time.time()
    dp = [[0]*(r+1) for _ in range(n+1)]
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(len(dp[0])):
        dp[0][i] = 1

    print(nCr_dp(n, r))
    end = time.time()
    print("dp: ", end - start)

    start = time.time()
    print(nCr_memo(n, r))
    end = time.time()
    print("memo: ", end - start)

    start = time.time()
    print(nCr(n, r))
    end = time.time()
    print("recur: ", end - start)


if __name__ == '__main__':
    main()
