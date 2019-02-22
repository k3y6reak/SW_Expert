ans = 0

def powerset(num, bool, idx, e_num):
    global ans
    chk = False
    for i in range(0, len(num)):
        for j in range(0, len(bool)):
            if bool[num[i][0]-1]:
                chk = True
            if chk and bool[num[i][1]-1]:
                return
            chk = False

    if idx == e_num:
        ans += 1
        return

    bool[idx] = True
    powerset(num, bool, idx + 1, e_num)
    bool[idx] = False
    powerset(num, bool, idx + 1, e_num)

def main():
    global ans
    test_case = int(input())
    for t in range(test_case):
        line1 = input().split()
        e_num = int(line1[0])
        c_num = int(line1[1])

        num = [[0]*2 for i in range(c_num)]
        for i in range(c_num):
            line2 = input().split()
            num[i][0] = int(line2[0])
            num[i][1] = int(line2[1])

        ans = 0
        powerset(num, [False]*e_num, 0, e_num)
        print('#'+str(t+1), str(ans))

if __name__ == '__main__':
    main()
