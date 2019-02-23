def main():
    tc = int(input())
    for t in range(tc):
        num = list(map(int, input().split()))
        num.remove(min(num))
        num.remove(max(num))
        tmp = 0
        num_len = len(num)
        for n in num:
            tmp += n

        print("#"+str(t+1), format(tmp/num_len, '.0f'))

if __name__ == '__main__':
    main()
