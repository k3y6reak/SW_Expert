ans = 0


def backtrack(m, line, n):
    global ans
    if line == n: # 여기서 어떤 작업을 진행하면 된다.
        ans += 1
        for i in range(0, n):
            for j in range(0, n):
                print(m[i][j], end='')
            print()
        print()
        print(ans)
        return

    for i in range(0, n):
        possible = True

        left = i
        right = i
        for j in range(line-1, -1, -1):
            left -= 1
            right += 1
            if m[j][i] == 1:
                possible = False
                break
            if left >= 0 and m[j][left] == 1:
                possible = False
                break
            if right >= 0  and right < n and m[j][right] == 1:
                possible = False
                break

        if possible:
            m[line][i] = 1 # 1 is Q
            backtrack(m, line+1, n)
            m[line][i] = 0


def main():
    n = int(input())
    m = [[0]*n for i in range(n)]
    backtrack(m, 0, n)


if __name__ == '__main__':
    main()