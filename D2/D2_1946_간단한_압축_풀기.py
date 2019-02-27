def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())

        ch_list = [0]
        for i in range(n):
            line = input().split()
            ch = line[0]
            cnt = int(line[1])
            ch_list += ch*cnt

        print("#"+str(t))
        for i in range(1, len(ch_list)):
            if i % 10 == 0:
                print(ch_list[i], end='')
                print()
            else:
                print(ch_list[i], end='')
        print()


if __name__ == '__main__':
    main()
