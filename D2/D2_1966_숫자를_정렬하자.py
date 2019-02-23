def main():
    tc = int(input())
    for t in range(tc):
        l = input()
        num = list(map(int, input().split()))
        num.sort()

        print("#"+str(t+1)+" ", end='')
        for n in num:
            print(str(n)+" ", end='')
        print()


if __name__ == '__main__':
    main()
