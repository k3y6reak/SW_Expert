def main():
    tc = int(input())
    for t in range(tc):
        num = int(input())
        total = 0
        for n in range(1, num+1):
            if n % 2 == 0:
                total -= n
            else:
                total += n
        print("#"+str(t+1), total)


if __name__ == '__main__':
    main()
