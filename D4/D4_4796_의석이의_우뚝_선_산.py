# 입출력 문제로 잠시 킵

def main():
    for t in range(1, int(input()) + 1):
        n = int(input())
        map_ = list(map(int, input().split()))

        high, low = 0, 0
        cnt = 0

        for i in range(1, n):

            if low > 0 and high == 0 and map_[i] > map_[i-1]:
                low = 0

            if high > 0 and low > 0 and map_[i] > map_[i-1]:
                cnt += (high * low)
                high, low = 0, 0

            if map_[i] > map_[i-1]:
                high += 1

            if map_[i] < map_[i-1]:
                low += 1

        if high > 0 and low > 0:
            cnt += (high * low)

        print("#%s %s" %(t, cnt))


if __name__ == '__main__':
    main()
