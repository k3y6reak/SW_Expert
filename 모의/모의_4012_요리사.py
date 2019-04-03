# [아이디어]
# 각 요리는 A, B로 두 분류로 나누게된다.
# 두 분류로 나누기 위해 조합을 이용해 절반만 가져온다. (나머지는 결국 똑같아지기 때문)
# 두 분류로 나누면 다시 하나의 분류에서 나올 수 있는 조합을 구하여 최소의 값을 구한다.

from itertools import combinations as comb

low = 99999


def find(map_, c, vi):
    global low

    d = []
    for i in range(len(vi)):
        if not vi[i]:
            d.append(i)

    if len(c) == 2:
        low = min(low, abs((map_[c[0]][c[1]] + map_[c[1]][c[0]]) - (map_[d[0]][d[1]] + map_[d[1]][d[0]])))
    else:
        left_sum = 0
        right_sum = 0

        for t in comb(c, 2):
            left_sum += (map_[t[0]][t[1]] + map_[t[1]][t[0]])

        for t in comb(d, 2):
            right_sum += (map_[t[0]][t[1]] + map_[t[1]][t[0]])

        low = min(low, abs(left_sum - right_sum))

def main():
    global low

    for t in range(1, int(input()) + 1):
        n = int(input())
        map_ = [list(map(int, input().split())) for _ in range(n)]

        C = list(comb(range(n), n//2))
        C = C[:len(C)//2]

        low = 99999
        for c in C:
            vi = [False]*n
            for c_ in c:
                vi[c_] = True
            find(map_, c, vi)

        print("#%d %d" %(t, low))


if __name__ == '__main__':
    main()
