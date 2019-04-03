# [아이디어]
# 먼저 n이 공을 발사할 수 있는 횟수이므로, w 값 (시작 위치)를 중복순열로 구한다.
# 만약 [0, 0, 0] 위치로 발사한다면 0 위치부터 벽돌을 깨기 시작한다.
# 벽돌을 깰 때 BFS를 이용하여 해당 벽돌이 깨지면서 추가적으로 깨질 수 있는 곳을 확인한다.
# 여기서 델타 배열을 이용하는데, 이 델타배열을 2중 for loop으로 구성하여 범위만큼 탐색할 수 있도록 한다.
# 해당 벽돌이 깨질 수 있다면 큐에 넣고, 그 자리를 방문표시 한다.
# 깨질 수 있는 벽돌이 모두 제거된다면, 큐는 비어있게 되고, 모두 True로 표시가 되었을 것이다.
# True로 표시된 벽을 모두 0으로 변환하고, 맵을 탐색하여 밑에서부터 벽돌을 모두 내린다.
# 두번째 발사를 하기위해 vi를 초기화 하고 들어간다.



from itertools import product as pd
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def chk_range(map_, vi, x, y, h, w):
    global dx, dy

    q = deque()
    q.append([x, y])

    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]

        for i in range(4):
            for j in range(1, map_[x][y]):
                nx = x + dx[i] * j
                ny = y + dy[i] * j

                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue

                if map_[nx][ny] != 0 and (not vi[nx][ny]):
                    vi[nx][ny] = True
                    q.append([nx, ny])

def remove_map(map_, vi, h, w):
    for i in range(h):
        for j in range(w):
            if vi[i][j]:
                map_[i][j] = 0


def drop_map(map_, h, w):
    for i in range(h - 1, -1, -1):
        for j in range(w):
            if map_[i][j] == 0:
                for k in range(i - 1, -1, -1):
                    if map_[k][j] != 0:
                        map_[i][j] = map_[k][j]
                        map_[k][j] = 0
                        break

low = 99999


def cnt_map(map_, h, w):
    global low
    cnt = 0
    for i in range(h):
        for j in range(w):
            if map_[i][j] != 0:
                cnt += 1

    if low > cnt:
        low = cnt


def shot(map_, sel, h, w):
    for s in sel:
        s = int(s)
        vi = [[False] * w for _ in range(h)]
        for i in range(h):
            if map_[i][s] != 0:
                vi[i][s] = True
                chk_range(map_, vi, i, s, h, w)
                remove_map(map_, vi, h, w)
                drop_map(map_, h, w)
                cnt_map(map_, h, w)
                break


def set_map(map_, h, w):
    tmp_map = [[0]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            tmp_map[i][j] = map_[i][j]

    return tmp_map


def make_drop_idx(map_, h, w, n):
    sel = pd(range(w), repeat=n)

    for s in sel:
        if low == 0:
            break
        else:
            shot(set_map(map_, h, w), s, h, w)




def main():
    global low

    for t in range(1, int(input()) + 1):
        n, w, h = map(int, input().split())

        map_ = [list(map(int, input().split())) for _ in range(h)]
        low = 99999
        make_drop_idx(map_, h, w, n)
        print("#%d %d" %(t, low))

if __name__ == '__main__':
    main()
