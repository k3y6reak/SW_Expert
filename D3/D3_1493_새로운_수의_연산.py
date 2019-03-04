m = [[0]*301 for _ in range(301)]
and_map = {}


def main():
    global m
    global and_map

    for i in range(1, 301):
        for j in range(1, 301):
            k = (i + j) * (i + j - 1) // 2 - (j - 1)
            m[i][j] = k
            and_map[k] = (i, j)

    tc = int(input())
    for t in range(1, tc+1):
        nums = list(map(int, input().split()))
        left = and_map[nums[0]]
        right = and_map[nums[1]]
        i = left[0] + right[0]
        j = left[1] + right[1]
        res = (i + j) * (i + j - 1) // 2 - (j - 1)
        print("#%d %d"%(t, res))


if __name__ == '__main__':
    main()
