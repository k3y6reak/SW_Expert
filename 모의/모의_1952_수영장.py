# [아이디어]
# 1일권과 1월권은 기준이 1달이 되므로 둘 중 작은 것을 넣으면 된다.
# 3달이 넘어가는 순간부터 3달 이전의 값(3달을 선택하지 않은 달들)과 3달권을 선택한 현재 달 중 작은 값을 구한다.
# 마지막달에서 1년권과 지금까지의 가격 중 작은 것을 선택한다.


def main():
    for t in range(1, int(input()) + 1):
        price = list(map(int, input().split()))
        plan = list(map(int, input().split()))

        dp = [0]*13
        for i in range(1, 13):
            dp[i] = min(dp[i-1] + plan[i-1] * price[0], dp[i-1] + price[1])
            if i >= 3:
                dp[i] = min(dp[i-3] + price[2], dp[i])

        res = min(dp[12], price[3])

        print("#%d %d"%(t, res))


if __name__ == '__main__':
    main()
