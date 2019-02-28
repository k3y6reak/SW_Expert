lis = []


def main():
    global lis

    tc = int(input())
    for t in range(1, tc+1):
        num_len = int(input())
        nums = list(map(int, input().split()))
        lis = [0]*len(nums)

        for i in range(num_len):
            lis[i] = 1
            for j in range(i):
                if nums[j] < nums[i] and 1 + lis[j] > lis[i]:
                    lis[i] = 1 + lis[j]

        print("#" + str(t), max(lis))


if __name__ == '__main__':
    main()
