# [아이디어]
# 플루이드-마샬을 사용한다.
# 작은사람 - 큰사람 꼴로 입력이 들어오면 해당 배열에 1을 넣어준다. (나머지는 inf) 처리.
# 플루이드-마샬 알고리즘을 이용해 연결될 수 있으면 키를 정할 수 있는 것이다.
# 마지막에 배열을 모두 탐색하면서 자신보다 큰 사람과 작은 사람을 모두 저장하고, 큰 사람의 수 + 작은 사람 수 = 인원 - 1(자기자신 제외)
# 위와 같이 진행하면 된다.


inf = 99999


def main():
    for t in range(1, int(input())+1):
        n = int(input())
        m = int(input())
        map_ = [[inf]*(n+1) for _ in range(n+1)]

        for i in range(m):
            a, b = map(int, input().split())
            map_[a][b] = 1

        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    tmp = map_[i][k] + map_[k][j]
                    if map_[i][j] > tmp:
                        map_[i][j] = tmp

        cnt = 0
        high = [0]*(n+1)
        low = [0]*(n+1)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue

                if map_[i][j] != inf:
                    high[i] += 1
                    low[j] += 1

        for i in range(1, n+1):
            if high[i] + low[i] == n - 1:
                cnt += 1

        print("#%d %d" %(t, cnt))


if __name__ == '__main__':
    main()
