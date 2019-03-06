def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        m = [[0]*n for _ in range(n)]

        rows = dict()
        for i in range(n):
            row = 0
            line = list(map(int, input().split()))
            for j in range(n):
                if line[j] == 0:
                    if row not in rows:
                        rows[row] = 1
                    else:
                        rows[row] += 1
                    row = 0
                else:
                    row += 1
                m[i][j] = line[j]
            if row not in rows:
                rows[row] = 1
            else:
                rows[row] += 1

        arr = []
        for key in rows:
            if key != 0:
                arr.append([rows[key], key, rows[key]*key])

        arr.sort(key=lambda x:(x[2], x[0]))

        print("#%d %d " %(t, len(arr)), end='')
        for i in arr:
            print(i[0], str(i[1]) + " ", end='')
        print()


if __name__ == '__main__':
    main()
