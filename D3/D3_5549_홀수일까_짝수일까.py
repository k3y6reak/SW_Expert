def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())

        if n & 1 == 1:
            print("#%d Odd"%(t))
        else:
            print("#%d Even"%(t))


if __name__ == '__main__':
    main()
