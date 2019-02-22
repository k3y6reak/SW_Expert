def main():
    test_case = int(input())
    for t in range(0, test_case):
        line = input().split()
        num = [int(n) for n in line[0]]
        cnt = int(line[1])

        chk_cnt = 0
        meme = 0
        flag = False
        while True:
            for j in range(0, len(num)):
                max_list = [i for i, val in enumerate(num) if val == max(num[j:])]
                if max_list[-1] == j:
                    meme += 1
                    continue
                else:
                    meme -= 1
                    low = 99999
                    low_idx = 0
                    if len(max_list) > 1:
                        for k in range(j, max_list[-1]):
                            if low > num[k]:
                                low = num[k]
                                low_idx = k
                        num[low_idx], num[max_list[-1]] = num[max_list[-1]], num[low_idx]
                        chk_cnt += 1
                        if chk_cnt == cnt:
                            flag = True
                            break
                    else:
                        num[j], num[max_list[-1]] = num[max_list[-1]], num[j]
                        chk_cnt += 1
                        if chk_cnt == cnt:
                            flag = True
                            break

            if meme > 2:
                    num[-1], num[-2] = num[-2], num[-1]
                    chk_cnt += 1
                    flag = True

            if flag:
                break

        tmp_max = [i for i, val in enumerate(num) if val == max(num)]
        if num[0] != num[tmp_max[-1]]:
            num[tmp_max[-1]], num[0] = num[0], num[tmp_max[-1]]

        num2 = ''.join(str(e) for e in num)
        print("#" + str(t+1) + " " + num2)


if __name__ == '__main__':
    main()
