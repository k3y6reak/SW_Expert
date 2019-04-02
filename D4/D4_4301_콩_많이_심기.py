# [아이디어]
# 입력받은 n, m으로 배열을 그려본다.
# (0,0)에서 콩을 심는다면 오른쪽으로 2칸에 있는 곳은 심지 못하고, 아래로 2칸에 있는 곳도 심지 못한다.
# 심지 못하는 곳을 x로 표시하고 map_이 False인 곳만 탐색하여 심을 수 있으면 True로 변경하고.
# True의 개수를 세어주면 된다.

def main():
    for t in range(1, int(input())+1):
        n, m = map(int, input().split())
        map_ = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not map_[i][j]:
                    map_[i][j] = True
                    if j + 2 < n:
                        map_[i][j+2] = 'x'
                    if i + 2 < m:
                        map_[i+2][j] = 'x'

        cnt = 0
        for i in range(m):
            for j in range(n):
                if map_[i][j] == True:
                    cnt += 1

        print("#%d %d" %(t, cnt))


if __name__ == '__main__':
    main()
