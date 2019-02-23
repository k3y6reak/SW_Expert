def main():
    tc = int(input())
    for t in range(tc):
        d = {}
        n = input()
        for num in list(map(int, input().split())):
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        print("#"+n+" " + str(max(d, key=lambda z:d[z])))

if __name__ == '__main__':
    main()
