# [아이디어]
# 미생물들의 x, y 좌표와 수, 방향을 deque에 넣는다.
# 격리시간동안 진행하면서 미생물들을 방향대로 이동한다.
# 이동 후 가장자리에 존재하는 미생물들을 찾아 절반으로 나누고
# 중복되는 좌표가 있는 미생물들 중 가장 큰 수의 방향으로 설정한다.


from collections import deque, Counter

#    X, 상, 하, 좌, 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

class Micro:
    def __init__(self, x, y, cnt, go):
        self.x = x
        self.y = y
        self.cnt = cnt
        self.go = go

def move(map_, micro, time, N, tc):

    # 격리 시간동안 진행한다.
    while time > 0:
        micro_len = len(micro)
        # 미생물을 하나씩 보면서 방향대로 이동한다.
        for i in range(micro_len):
            x, y, cnt, go = map(int, micro[i])
            micro[i][0] = x + dx[go]
            micro[i][1] = y + dy[go]

        for i in range(micro_len):
            x, y, cnt, go = map(int, micro[i])
            if x == 0 or x == N - 1 or y == 0 or y == N - 1:
                if go == 1:
                    go = 2
                elif go == 2:
                    go = 1
                elif go == 3:
                    go = 4
                elif go == 4:
                    go = 3
                micro[i][2] //= 2
                micro[i][3] = go

        # 겹쳐있는지
        dup_list = []
        vi = [False]*micro_len
        for i in range(micro_len):
            tmp = [micro[i]]
            for j in range(i+1, micro_len):
                if not vi[j] and micro[i][0] == micro[j][0] and micro[i][1] == micro[j][1]:
                    vi[j] = True
                    tmp.append(micro[j])
            if len(tmp) != 1:
                dup_list.append(tmp)

        for i in range(len(dup_list)):
            x, y, cnt, go = map(int, dup_list[i][0])
            save = cnt + 0
            go = sorted(dup_list[i], key=lambda x:x[2])[-1][3]
            for j in range(len(dup_list[i])):
                cnt += dup_list[i][j][2]
                micro.remove(dup_list[i][j])
            micro.append([x, y, cnt-save, go])

        time -= 1

    micro_cnt = 0
    for i in range(len(micro)):
        micro_cnt += micro[i][2]

    print("#%d %d" %(tc, micro_cnt))

def main():
    for t in range(1, int(input()) + 1):
        N, M, K = map(int, input().split())
        map_ = [[0]*N for _ in range(N)]
        micro = deque()

        for i in range(K):
            x, y, cnt, go = list(map(int, input().split()))
            map_[x][y] = Micro(x, y, cnt, go)
            micro.append([x, y, cnt, go])

        move(map_, micro, M, N, t)



if __name__ == '__main__':
    main()
