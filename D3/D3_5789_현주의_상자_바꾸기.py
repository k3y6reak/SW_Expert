def main():
    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        n = line[0]
        q = line[1]

        m = [0]*n
        for i in range(1, q+1):
            line = list(map(int, input().split()))
            for j in range(line[0]-1, line[1]):
                m[j] = i

        print("#%d "%t, end='')
        for i in m:
            print(str(i)+" ", end='')
        print()


if __name__ == '__main__':
    main()
