# [아이디어]
# DFS 탐색을 진행한다. 델타배열을 이용하는데 현재 위치에서 꺽을 때를 기준으로 값을 주어야 한다.
# 모든 점에서 시작하여 3번 방향을 바꾸면 사각형이 만들어지는데, 이때 시작점으로 돌아왔을때 완전한 사각형이므로 시작점과 값을 비교한다.
# 방향을 꺽지 않고 들어가는 것도 확인해야 한다.
# 방향을 꺽지 않고 들어갈 때 방문 배열을 원 상태로 돌려줘야 이동이 가능하며 ( 기존의 꺽어 들어가면서 숫자를 방문체크 했기 때문)
# 꺽어 들어가는데 꺽는 횟수가 3번 이상일 경우에는 사각형이 만들어지지 않기 때문에 제외한다.



dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


big = -1


def dfs(map_, vi, x, y, turn, cnt, start_x, start_y, n):
    global big, dx, dy

    if turn > 3:
        return

    nx = x + dx[turn]
    ny = y + dy[turn]

    if turn == 3 and nx == start_x and ny == start_y:
        big = max(big, cnt)
        return

    if 0 <= nx < n and 0 <= ny < n and (not vi[map_[nx][ny]]):
        vi[map_[nx][ny]] = True
        # 방향을 꺽는 것.
        dfs(map_, vi, nx, ny, turn + 1, cnt + 1, start_x, start_y, n)
        # 해당 방향으로 계속 들어가는 것.
        dfs(map_, vi, nx, ny, turn, cnt + 1, start_x, start_y, n)
        vi[map_[nx][ny]] = False
    else:
        return


def main():
    global big

    for t in range(1, int(input()) + 1):
        n = int(input())
        map_ = [list(map(int, input().split())) for _ in range(n)]

        big = -1
        for i in range(n):
            for j in range(n):
                vi = [False]*101
                vi[map_[i][j]] = True
                dfs(map_, vi, i, j, 0, 1, i, j, n)
                vi[map_[i][j]] = False

        print("#%d %d" %(t, big))


if __name__ == '__main__':
    main()
