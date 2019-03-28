# [아이디어]
# 입력받은 문자열을 하나씩 빼서 앞에 넣어준다.
# 입력받은 n을 4로 나눠 한 줄에 몇개씩 있을지 정하고, 처음 입력받은 문자열에서 한 줄에 있을 수 만큼 가져와 따로 저장한다.
# 하나씩 빼서 앞에 넣어주는 작업을 진행하면서 저장한 값이 변경된 값의 앞부분과 같으면 멈추고
# 변경하는 동안 한 줄에 있을 수 만큼 가져와 set에 저장한다
# 그 후 정렬하고 k-1의 값을 출력하면 된다.


num = set()


def chk(nums, p):
    global num

    for i in range(0, len(nums), p):
        num.add(''.join(nums[i:i+p]))


def main():
    global num

    for t in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        nums = list(input())
        p = n//4
        save = nums[-1:-p-1:-1][::-1]
        nums.insert(0, nums.pop())
        chk(nums, p)

        while nums[0:p] != save:
            nums.insert(0, nums.pop())
            chk(nums, p)

        num = list(num)
        num.sort(key=lambda x:-int("0x"+x, 16))
        print("#%d %d" %(t, int(num[k-1], 16)))
        num = set()


if __name__ == '__main__':
    main()
