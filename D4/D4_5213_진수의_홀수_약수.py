nums = [0]*1000001

def main():
    for i in range(1, 1000001, 2):
        j = i
        while j <= 1000000:
            nums[j] += i
            j += i

    for i in range(1, 1000000):
        nums[i + 1] += nums[i]

    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        L = line[0]
        R = line[1]

        result = nums[R] - nums[L-1]
        print("#"+str(t), result)


if __name__ == '__main__':
    main()
