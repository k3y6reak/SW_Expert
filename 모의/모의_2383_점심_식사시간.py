# [아이디어]
# 사람들의 큐에 [i, j, 1번 계단거리, 2번 계단거리] 를 넣는다.
# 계단들의 큐에 [i, j, 계단의 길이]를 넣는다.
# 첫번째 계단으로 갈 사람과 두번째 계단으로 갈 사람들로 나눈다.
# 각 계단마다 사람들이 통과하는 시간을 계산한다.
# 두 계단 중 시간이 가장 많이 걸리는 값이 모두 통과한 시간이믈 max()를 이용한다.
# 두 계단을 모두 통과했으면 해당 시간을 res와 비교하여 작은 값을 저장한다. (최소가 되는 시간을 찾기위해)




from collections import deque


def chk_time(stair, t):
    if len(stair) == 0:
        return 0

    # 거리가 짧은 순으로 계단에 들어간다.
    stair = sorted(stair)

    # 첫번째 사람의 시간을 저장
    time = stair[0]

    # 현재 계단에 사람이 있는지 확인
    using = [0]*3

    while True:
        for i in range(len(stair)):
            if not stair[i]: # 해당 번호의 사람이 계단을 내려간 경우에는 제외
                continue

            if stair[i] <= time: # 각 도착 시간이 현재 시간보다 큰 경우가 있을 수 없음. 따라서 작거나, 같은 경우에만 진입 가능.
                for j in range(3):
                    if using[j] <= 0: # 내려가고 있는 사람이 없으면
                        using[j] = t # 해당 위치에 해당 사람의 시간을 넣어준다.
                        stair[i] = 0 # 들어가고자 하는 사람을 0으로 만들어 다음에 들어오지 못하게 한다.

                        if i == len(stair) - 1: # 모두 내려갔으면
                            return time + t # 현재 시간을 저장한다.

                        break

        for i in range(3):
            using[i] -= 1

        time += 1


def select_stair(peoples, stairs, chk):
    first = deque()
    second = deque()

    for i in range(len(peoples)):
        if chk & (1 << i):
            first.append(peoples[i][2])
        else:
            second.append(peoples[i][3])

    return max(chk_time(first, stairs[0][2]), chk_time(second, stairs[1][2]))


def main():
    for t in range(1, int(input())+1):
        n = int(input())
        map_ = [list(map(int, input().split())) for _ in range(n)]
        peoples = deque()
        stairs = deque()

        # 사람들과 계단을 각각의 큐에 넣어둔다.
        for i in range(n):
            for j in range(n):
                if map_[i][j] == 1:
                    peoples.append([i, j, 0, 0])
                elif map_[i][j] > 1:
                    stairs.append([i, j, map_[i][j]])

        # 사람들의 큐를 탐색하면서 1번, 2번 계단의 거리를 저장해둔다.
        for i in range(len(peoples)):
            peoples[i][2] = abs(peoples[i][0] - stairs[0][0]) + abs(peoples[i][1] - stairs[0][1])
            peoples[i][3] = abs(peoples[i][0] - stairs[1][0]) + abs(peoples[i][1] - stairs[1][1])

        res = 99999
        # 각 사람들이 1번, 2번을 선택해서 들어간다.
        for i in range(1 << len(peoples)):
            res = min(res, select_stair(peoples, stairs, i))

        print("#%d %d" %(t, res+1))


if __name__ == '__main__':
    main()
