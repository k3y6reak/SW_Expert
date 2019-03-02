def main():
    tc = int(input())
    for t in range(1, tc+1):
        d = {}
        line = list(map(int, input().split()))
        for i in line:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        print("#%d " %(t), end='')
        for i in d:
            if d[i] % 2 == 1:
                print(i, end='')
        print()

if __name__ == '__main__':
    main()
