# [아이디어]
# 먼저 입력받은 맵에서 가장 큰 값의 i, j를 저장하고 해당 좌표부터 DFS를 진행한다.
# 다음으로 이동할 위치가 방문하지 않았고, 더 작은 값이어야 진행할 수 있다.
# 만약, 크기가 같거나 큰 경우에는 k 만큼 깍고 진행할 수 있다. 여기서 k가 2라면 2만큼, 1만큼 깍을 수 있다는 것이 중요하다.
# 진행 도중에 이미 깍은 경우이면서, 다음 이동 값이 같거나 큰 경우는 더이상 진행할 수 없다.
# 되돌아오기 위해서 DFS 진행 전 방문체크하고 나와서 해제해야 한다.

# 만약.... 몇개의 값만 1씩 차이가 난다면, 초기화를 잘 해주자...


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

big = 0

def dfs(map_, x, y, now, vi, cnt, chk, k, n):
    global big, dx, dy

    if cnt > big:
        big = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < n and -1 < ny < n:
            if not vi[nx][ny]:
                if map_[nx][ny] < now:
                    vi[nx][ny] = True
                    dfs(map_, nx, ny, map_[nx][ny], vi, cnt + 1, chk, k, n)
                    vi[nx][ny] = False

                else:
                    if not chk:
                        for j in range(1, k+1):
                            if map_[nx][ny] - j < now:
                                vi[nx][ny] = True
                                dfs(map_, nx, ny, map_[nx][ny]-j, vi, cnt + 1, True, k, n)
                                vi[nx][ny] = False


def main():
    global big

    for t in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        map_ = [list(map(int, input().split())) for _ in range(n)]
        vi = [[False]*n for _ in range(n)]

        high = 0
        start_list = []
        for i in range(n):
            for j in range(n):
                if high < map_[i][j]:
                    high = map_[i][j]

        for i in range(n):
            for j in range(n):
                if high == map_[i][j]:
                    start_list.append([i, j])

        for s in start_list:
            vi[s[0]][s[1]] = True
            dfs(map_, s[0], s[1], map_[s[0]][s[1]], vi, 1, False, k, n)
            vi[s[0]][s[1]] = False

        print("#%d %d" %(t, big))
        big = 0


if __name__ == '__main__':
    main()
