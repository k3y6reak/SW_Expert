def main():
    for t in range(1, 11):
        n = input()
        s = set()
        m = [[0]*100 for _ in range(100)]
        for i in range(100):
            line = list(map(int, input().split()))
            for j in range(100):
                m[i][j] = line[j]

        for i in range(100):
            s.add(sum(m[i]))

        for i in range(100):
            tmp = 0
            for j in range(100):
                tmp += m[j][i]
            s.add(tmp)

        print("#%d %d" %(t, max(s)))



if __name__ == '__main__':
    main()
