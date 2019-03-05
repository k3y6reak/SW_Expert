def nine_to_ten(num):
    num_len = len(num)
    new_num = 0

    j = 0
    for i in range(num_len-1, -1, -1):
        new_num += (int(num[i]) * (9 ** j))
        j += 1

    return new_num


def ten_to_nine(num):
    new_num = ""
    for i in num:
        if int(i) >= 4:
            new_num += str(int(i) - 1)
        else:
            new_num += i

    return new_num


def main():
    tc = int(input())
    for t in range(1, tc+1):
        start, end = input().split()

        s_min = False
        e_min = False
        if start[:1] == '-':
            s_min = True
            start = start[1:]
        if end[:1] == '-':
            e_min = True
            end = end[1:]

        start = ten_to_nine(start)
        end = ten_to_nine(end)

        start = nine_to_ten(start)
        end = nine_to_ten(end)

        if s_min:
            start = (-1)*start
        if e_min:
            end = (-1)*end

        if s_min == e_min:
            print("#%d %d" % (t, (end - start)))
        else:
            print("#%d %d"%(t, (end-start)-1))


if __name__ == '__main__':
    main()
    exit(0)
