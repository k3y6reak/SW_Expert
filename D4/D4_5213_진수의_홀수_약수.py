nums = [0]*1000001

def main():
    for i in range(1, 1000001, 2): # i는 홀수만 가져온다.
        j = i
        while j <= 1000000: # 해당 홀수부터~
            nums[j] += i # 1000000 까지 각 수들의 홀수 합을 저장.
            j += i

    for i in range(1, 1000000):
        nums[i + 1] += nums[i] # 이전까지의 합을 더해준다.

    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        L = line[0]
        R = line[1]

        result = nums[R] - nums[L-1]
        print("#"+str(t), result)


if __name__ == '__main__':
    main()
