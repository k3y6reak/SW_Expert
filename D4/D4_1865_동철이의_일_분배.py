# [아이디어]
# n명의 사람마다 n개의 확률이 존재한다.
# 10 20 30
# 20 30 40 옆과 같은 확률이 주어진다면 10-20-30, 10-20-40, 10-20-60, 10-30-30 ... 과 같이 전부 탐색을 진행해야한다.
# 40 50 60 
# 전부 탐색을 위해 DFS를 사용한다. cnt 값을 방문할 때마다 1씩 증가시켜 이 값이 n과 같아질 때 확률을 계산하여 big과 비교한다.



big = 0


def dfs(map_, vi, cnt, hap, n):
    global big


    if big >= hap*100:
        return

    if cnt == n:
        tmp = hap * 100
        if tmp > big:
            big = tmp
        return

    for i in range(n): # cnt위치에서 다음 사람의 확률을 모두 탐색.
        if not vi[i]: # 방문하지 않았을때
            vi[i] = True # 방문 표시
            dfs(map_, vi, cnt + 1, hap*map_[cnt][i], n) # 들어간다.
            vi[i] = False # 방문 해제


def main():
    global big

    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        map_ = [[0]*n for _ in range(n)]

        for i in range(n):
            line = list(map(int, input().split()))
            for j in range(n):
                map_[i][j] = line[j] / 100

        vi = [False]*n
        big = 0
        dfs(map_, vi, 0, 1.0, n)

        print("#%d %0.6f" %(t, big))

if __name__ == '__main__':
    main()
