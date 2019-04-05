# [아이디어]
# 각 통로별 갈 수 있는 델타 리스트를 선언한다.
# 해당 좌표부터 BFS를 진행한다. 이때 각 통로에서 방향별로 이동할 수 있는 통로인지 아닌지 검사한다.
# 이동할 수 있으면 현재 시간 + 1을 큐에 넣는다
# BFS를 진행 후에 0보다 큰 값을 체크하고 나 자신을 +1 해준다.


from collections import deque

#       상, 하, 좌, 우
dx_1 = [-1, 1, 0, 0]
dy_1 = [0, 0, -1, 1]

dx_2 = [-1, 1, 0, 0]
dy_2 = [0, 0, 0, 0]

dx_3 = [0, 0, 0, 0]
dy_3 = [0, 0, -1, 1]

dx_4 = [-1, 0, 0, 0]
dy_4 = [0, 0, 0, 1]

dx_5 = [0, 1, 0, 0]
dy_5 = [0, 0, 0, 1]

dx_6 = [0, 1, 0, 0]
dy_6 = [0, 0, -1, 0]

dx_7 = [-1, 0, 0, 0]
dy_7 = [0, 0, -1, 0]


def bfs(map_, vi, X, Y, N, M):
    global dx_1, dy_1, dx_2, dy_2, dx_3, dy_3, dx_4, dy_4, dx_5, dy_5, dx_6, dy_6, dx_7, dy_7
    q = deque()
    vi[X][Y] = 1
    q.append([X, Y, 1])

    while q:
        p = q.popleft()
        # 해당 파이프 모양에 따라 이동이 가능함.
        x = p[0]
        y = p[1]
        time = p[2]

        tmp = map_[x][y]

        for i in range(4):
            if tmp == 1:
                nx = x + dx_1[i]
                ny = y + dy_1[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                # 위로 이동하는데, 갈 수 없는 모양이면 버림.
                if i == 0 and (map_[nx][ny] == 3 or map_[nx][ny] == 4 or map_[nx][ny] == 7):
                    continue
                # 아래로 이동하는데, 갈 수 없는 모양이면 버림.
                elif i == 1 and (map_[nx][ny] == 3 or map_[nx][ny] == 5 or map_[nx][ny] == 6):
                    continue

                elif i == 2 and (map_[nx][ny] == 2 or map_[nx][ny] == 6 or map_[nx][ny] == 7):
                    continue

                elif i == 3 and (map_[nx][ny] == 2 or map_[nx][ny] == 4 or map_[nx][ny] == 5):
                    continue

                if vi[nx][ny] == 0:
                    vi[nx][ny] = time + 1
                    q.append([nx, ny, time+1])

            elif tmp == 2:
                nx = x + dx_2[i]
                ny = y + dy_2[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if i == 0 and (map_[nx][ny] == 3 or map_[nx][ny] == 4 or map_[nx][ny] == 7):
                    continue

                elif i == 1 and(map_[nx][ny] == 3 or map_[nx][ny] == 5 or map_[nx][ny] == 6):
                    continue

                if vi[nx][ny] == 0:
                    vi[nx][ny] = time + 1
                    q.append([nx, ny, time + 1])

            elif tmp == 3:
                nx = x + dx_3[i]
                ny = y + dy_3[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if i == 2 and (map_[nx][ny] == 2 or map_[nx][ny] == 6 or map_[nx][ny] == 7):
                    continue

                elif i == 3 and (map_[nx][ny] == 2 or map_[nx][ny] == 4 or map_[nx][ny] == 5):
                    continue

                if vi[nx][ny] == 0:
                    vi[nx][ny] = time + 1
                    q.append([nx, ny, time + 1])

            elif tmp == 4:
                nx = x + dx_4[i]
                ny = y + dy_4[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if i == 0 and (map_[nx][ny] == 3 or map_[nx][ny] == 4 or map_[nx][ny] == 7):
                    continue

                elif i == 3 and (map_[nx][ny] == 2 or map_[nx][ny] == 4 or map_[nx][ny] == 5):
                    continue

                if vi[nx][ny] == 0:
                    vi[nx][ny] = time + 1
                    q.append([nx, ny, time + 1])

            elif tmp == 5:
                nx = x + dx_5[i]
                ny = y + dy_5[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if i == 1 and (map_[nx][ny] == 3 or map_[nx][ny] == 5 or map_[nx][ny] == 6):
                    continue

                elif i == 3 and (map_[nx][ny] == 2 or map_[nx][ny] == 4 or map_[nx][ny] == 5):
                    continue

                if vi[nx][ny] == 0:
                    vi[nx][ny] = time + 1
                    q.append([nx, ny, time + 1])

            elif tmp == 6:
                nx = x + dx_6[i]
                ny = y + dy_6[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if i == 1 and (map_[nx][ny] == 3 or map_[nx][ny] == 5 or map_[nx][ny] == 6):
                    continue

                elif i == 2 and (map_[nx][ny] == 2 or map_[nx][ny] == 6 or map_[nx][ny] == 7):
                    continue

                if vi[nx][ny] == 0:
                    vi[nx][ny] = time + 1
                    q.append([nx, ny, time + 1])

            elif tmp == 7:
                nx = x + dx_7[i]
                ny = y + dy_7[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if i == 0 and (map_[nx][ny] == 3 or map_[nx][ny] == 4 or map_[nx][ny] == 7):
                    continue

                elif i == 2 and (map_[nx][ny] == 2 or map_[nx][ny] == 6 or map_[nx][ny] == 7):
                    continue

                if vi[nx][ny] == 0:
                    vi[nx][ny] = time + 1
                    q.append([nx, ny, time + 1])


def main():
    for t in range(1, int(input()) + 1):
        N, M, X, Y, L = map(int, input().split())
        vi = [[0]*M for _ in range(N)]
        map_ = [[0]*M for _ in range(N)]

        # 지도에 0인 부분은 갈 수 없으므로 vi를 미리 True로 변경
        for i in range(N):
            line = list(map(int, input().split()))
            for j in range(M):
                tmp = line[j]
                if tmp == 0:
                    vi[i][j] = True
                map_[i][j] = tmp

        bfs(map_, vi, X, Y, N, M)

        for i in range(N):
            for j in range(M):
                if vi[i][j] == True:
                    vi[i][j] = "T"

        cnt = 0
        for i in range(N):
            for j in range(M):
                if vi[i][j] != "T" and 0 < vi[i][j] <= L:
                    cnt += 1

        print("#%d %d" %(t, cnt+1))

if __name__ == '__main__':
    main()
