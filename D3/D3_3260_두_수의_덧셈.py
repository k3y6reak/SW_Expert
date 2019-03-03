def main():
    tc = int(input())
    for t in range(1, tc+1):
        nums = list(map(int, input().split()))
        print("#%d %d"%(t, nums[0]+nums[1]))

if __name__ == '__main__':
    main()
