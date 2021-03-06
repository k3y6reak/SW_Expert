# [아이디어]
# n명의 사람마다 n개의 확률이 존재한다.
# 10 20 30
# 20 30 40 옆과 같은 확률이 주어진다면 10-20-30, 10-20-40, 10-20-60, 10-30-30 ... 과 같이 전부 탐색을 진행해야한다.
# 40 50 60 
# 전부 탐색을 위해 DFS를 사용한다. cnt 값을 방문할 때마다 1씩 증가시켜 이 값이 n과 같아질 때 확률을 계산하여 big과 비교한다.
# 그 전에 최대값과 현재 계산된 결과를 비교하는데, 현재 계산된 결과가 작으면 더 이상 진행하지 않는다.
# 이유는, 처음 배열에 저장할 시점부터 100으로 나눠 1 이하의 수로 만들었기 때문에 해봐야 현재 값에서 뒤로 가면서 해봐야 같은 값이거나, 
# 작은 값일 수 밖에 없다.


big = 0


def dfs(map_, vi, cnt, hap, n):
    global big
    calc = hap*100

    if big >= calc:
        return

    if cnt == n:
        big = max(big, calc)
        return

    for i in range(n):
        if not vi[i]:
            vi[i] = True
            dfs(map_, vi, cnt + 1, hap*map_[cnt][i], n)
            vi[i] = False


def main():
    global big

    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        map_ = [[t/100 for t in list(map(int, input().split()))] for _ in range(n)]

        vi = [False]*n
        big = 0
        dfs(map_, vi, 0, 1.0, n)

        print("#%d %0.6f" %(t, big))


if __name__ == '__main__':
    main()
