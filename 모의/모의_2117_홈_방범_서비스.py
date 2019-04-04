# [아이디어]
# 0, 0부터 n, n까지 모두 돌면서 방범 서비스를 할 수 있는지 판단한다.
# 이때 한 점에서 2*n까지 k를 늘리면 모든 영역을 판단할 수 있게 되는데, 미리 집들의 점을 구하여 k 값 내에 들어올 수 있는지 확인한다.
# 집이 방범 서비스 영역에 들어온다면, 그 집을 카운팅하고, 해당 집의 수와 비용을 방범 서비스 비용과 비교하여 손해를 안보면 big에 큰 값을 넣어준다.

big = 0

def check(homes, N, M, x, y):
    global big

    for k in range(1, 2*N):
        cnt = 0
        for home in homes:
            if k > abs(x - home[0]) + abs(y - home[1]):
                cnt += 1
        if (k**2 + (k-1)**2) <= cnt*M:
            big = max(big, cnt)


def main():
    global big

    for t in range(1, int(input()) + 1):
        N, M = map(int, input().split())
        map_ = [[0]*N for _ in range(N)]
        homes = []

        for i in range(N):
            line = list(map(int, input().split()))
            for j in range(N):
                if line[j] == 1:
                    homes.append([i, j])
                map_[i][j] = line[j]
        big = 0
        for i in range(N):
            for j in range(N):
                check(homes, N, M, i, j)

        print("#%d %d" %(t, big))


if __name__ == '__main__':
    main()
