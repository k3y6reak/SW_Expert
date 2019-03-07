# [아이디어]
# 각 위치에서 다음으로 이동할때 현재 위치의 값 +1이 다음 위치의 값이어야 한다.
# 현재 위치에서 델타배열을 이용해 상하좌우를 탐색해야한다.
# 상하좌우 범위 내에 들어고 다음의 값이 현재 값 + 1인 경우에 다시 dfs를 진행한다.
# 해당 조건에 맞을 경우 cbt를 증가시킨다.
# cnt가 최대값보다 같거나 큰 경우 (이동거리가 큰 경우)에 cnt를 큰 값으로 변경해야 한다.
# 이때 큰 값과 cnt가 동일하면서 방 번호가 작은 경우에는 작은 방번호로 변경해야한다.



big = 0

dx = [0, 0, -1, 1] # 사방 탐색 델타 배열
dy = [-1, 1, 0, 0]


def dfs(m, x, y, n):
    cnt = 1
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and (m[x][y] + 1 == m[nx][ny]): # 해당 범위 내라면
            cnt += dfs(m, nx, ny, n) # 다음 위치부터 dfs를 시작한다.

    return cnt


def main():
    global big

    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        m = [[0]*n for _ in range(n)]

        for i in range(n):
            line = list(map(int, input().split()))
            for j in range(n):
                m[i][j] = line[j]

        big = 0 # 최대값 설정
        room_no = 999999999 # 작은 방 번호 설정
        for i in range(n):
            for j in range(n):
                cnt = dfs(m, i, j, n) # dfs 시작
                if big <= cnt: # dfs를 통해 나온 cnt 값이 저장된 큰 값 보다 크다면
                    if big == cnt and room_no > m[i][j]: # 같은 경우이면서 방 번호가 작으면
                        room_no = m[i][j] # 방번호를 세팅
                    elif big != cnt:
                        room_no = m[i][j]
                    big = cnt # cnt를 세팅

        print("#%d %d %d" %(t, room_no, big))


if __name__ == '__main__':
    main()

    
#####################################################################
# BFS 방식 해당 방식은 시간초과가 발생한다. (python의 경우)
#####################################################################

import queue

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

all = []


def bfs(m, vi, n, i, j):
    global dx, dy, all
    tmp = []
    room_no = m[i][j]
    cnt = 1
    q = queue.Queue()
    q.put([i, j])
    vi[i][j] = True

    while not q.empty():
        p = q.get()
        x = p[0]
        y = p[1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if (not vi[nx][ny]) and (m[nx][ny] == m[x][y] + 1):
                vi[nx][ny] = True
                q.put([nx, ny])
                cnt += 1

    tmp += [room_no, cnt]
    all.append(tmp)


def main():
    global all

    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        m = [[0]*n for _ in range(n)]
        for i in range(n):
            line = list(map(int, input().split()))
            for j in range(n):
                m[i][j] = line[j]

        all = []
        for i in range(n):
            for j in range(n):
                vi = [[False] * n for _ in range(n)]
                bfs(m, vi, n, i, j)

        all.sort(key=lambda x: (x[1], -x[0]))
        print("#%d %d %d" %(t, all[-1][0], all[-1][1]))


if __name__ == '__main__':
    main()
