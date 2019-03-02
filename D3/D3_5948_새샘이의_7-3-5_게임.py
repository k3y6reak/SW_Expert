ans = set()

def comb(nums, select, idx, cnt):
    global ans

    if cnt == len(select):
        ans.add(sum(select))
        return

    if idx == len(nums):
        return

    select[cnt] = nums[idx]
    comb(nums, select, idx + 1, cnt + 1)
    select[cnt] = 0
    comb(nums, select, idx + 1, cnt)

def main():
    global ans

    tc = int(input())
    for t in range(1, tc+1):
        ans = set()
        nums = list(map(int, input().split()))
        select = [0]*3
        comb(nums, select, 0, 0)
        ans = list(ans)
        ans.sort()
        print("#%d %d"%(t, ans[-5]))

if __name__ == '__main__':
    main()
