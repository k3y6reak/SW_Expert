def main():
    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        n = line[0]
        k = line[1]
        score = list(map(int, input().split()))

        ans = 0
        for i in range(k):
            tmp = max(score)
            ans += tmp
            score.remove(tmp)

        print("#%d %d"%(t, ans))


if __name__ == '__main__':
    main()
