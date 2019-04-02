# [아이디어]
# 항상 왼쪽에 먼저 올릴 수 있게 한다.
# 왼쪽, 오른쪽에 추를 놓았을 때 오른쪽의 무게가 더 커지면 버린다.
# 추의 개수와 올린 횟수가 같아지면 1을 리턴해 카운트한다.
# 현재 추를 올린 시점에서의 무게를 dp에 저장한다.
# dp에 저장할 idx는 겹치지 않도록 주의해야 한다.

def dfs(n, vi, w, dp, idx, cnt, left, right):
    # 오른쪽이 무게가 더 크면 더 이상 올릴 수 없음.
    if left < right:
        return 0

    # 올린 개수가 추의 개수랑 같아지면 끝.
    if cnt == n:
        return 1

    if dp[idx] != False:
        return dp[idx]

    hap = 0
    for i in range(n):
        # 해당 추를 선택하지 않았다면,
        if not vi[i]:
            vi[i] = True # 해당 추를 선택하고
            # dp 인덱스가 겹치지 않도록 설정해야함.
            hap += dfs(n, vi, w, dp, idx + (3**i), cnt + 1, left + w[i], right) # 왼쪽에 넣기
            hap += dfs(n, vi, w, dp, idx + (3**i)*2, cnt + 1, left, right + w[i]) # 오른쪽에 넣기
            vi[i] = False # 해당 추를 선택해제

    dp[idx] = hap
    return hap


def main():
    for t in range(1, int(input()) + 1):
        n = int(input())
        w = list(map(int, input().split()))
        vi = [False]*n
        dp = [False]*20000
        ans = dfs(n, vi, w, dp, 0, 0, 0, 0)
        print("#%d %d" %(t, ans))

if __name__ == '__main__':
    main()
