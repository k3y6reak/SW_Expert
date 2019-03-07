# [아이디어]
# 파도반 수열은 1, 1, 1, 2, 2, 3, 4, 5, 7, 9 ... 과 같은 수열이다.
# 여기서 규칙을 찾아야 하는데, 0, 1, 2 번 인덱스는 그대로 1을 넣어주고 3번 인덱스 = 1번 인덱스 + 0번 인덱스가 된다.
# i >= 3 일때, [i] = [i-2] + [i-3]이 된다.
# 먼저 n이 100까지 이므로 미리 100일때까지 계한하여 넣어둔다.
# 그리고 n-1의 값을 출력하면 된다.

dp = []


def padoban():
    global dp

    for i in range(3, 101):
        dp[i] = dp[i-2] + dp[i-3]


def main():
    global dp
    dp = [0] * 101
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    padoban()

    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        print("#%d %d"%(t, dp[n-1]))


if __name__ == '__main__':
    main()
