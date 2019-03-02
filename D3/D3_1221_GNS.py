def main():
    d = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    tc = int(input())
    for t in range(1, tc+1):
        line = input().split()
        l = int(line[1])
        m = [0]*l
        line = input().split()
        for i in range(l):
            m[i] = line[i]

        m.sort(key=lambda x:d[x])

        print("#%d" %t)
        for i in m:
            print(i+" ", end='')
        print()


if __name__ == '__main__':
    main()
