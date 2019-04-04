# [아이디어]
# 자석을 돌릴때 현재 자석을 기준으로 왼쪽, 오른쪽을 판단한다.
# 해당 자석을 돌릴 수 있으면 vi에 True로 변경한다.
# 자석을 돌릴 때 돌리는 자석이 짝수이면 짝수는 같은 방향 홀수는 반대방향으로 돈다.
# 홀수면 홀수는 같은 방향 짝수는 반대방향으로 돈다.
# 자석을 deque로 만들어서 빼고 넣기를 빠르게 한다.

from collections import deque


def turn(magnet, num, go):
    vi = [0] * 4

    # 짝수 인덱스, 홀수 인덱스 끼리
    vi[num] = True

    flag = True # 홀수면
    if num % 2 == 0:
        flag = False # 짝수면

    # 돌아가는 자석을 기준으로 왼쪽이 도는지
    for i in range(num, -1, -1):
        if magnet[i][6] != magnet[i-1][2]:
            if vi[i] != 0:
                if i - 1 >= 0:
                    vi[i-1] = True

    # 돌아가는 자석을 기준으로 오른쪽이 도는지
    for i in range(num, 3):
        if magnet[i][2] != magnet[i+1][6]:
            if vi[i] != 0:
                vi[i+1] = True


    if flag: # 홀수이면
        for i in range(4):
            if vi[i] != 0:
                if i % 2 == 1:
                    vi[i] = go
                else:
                    vi[i] = -go

    else:
        for i in range(4):
            if vi[i] != 0:
                if i % 2 == 1:
                    vi[i] = -go
                else:
                    vi[i] = go

    for i in range(4):
        if vi[i] == 1: # 오른쪽으로 돈다.
            magnet[i].appendleft(magnet[i].pop()) # 오른쪽것을 꺼내서 왼쪽에 붙인다.
        elif vi[i] == -1:
            magnet[i].append(magnet[i].popleft()) # 왼쪽것을 꺼내서 오른쪽에 붙인다.


def main():
    for t in range(1, int(input()) + 1):
        k = int(input())
        magnet = [deque(list(map(int, input().split()))) for _ in range(4)]
        cmd = [list(map(int, input().split())) for _ in range(k)]

        for c in cmd:
            num = c[0]
            go = c[1]
            turn(magnet, num-1, go)

        hap = 0
        s = 1
        for m in magnet:
            if m[0] == 0:
                hap += 0
            else:
                hap += s
            s *= 2

        print("#%d %d" %(t, hap))

if __name__ == '__main__':
    main()
