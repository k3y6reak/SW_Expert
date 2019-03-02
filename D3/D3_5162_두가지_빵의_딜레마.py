def main():
    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        low = 0
        if line[0] < line[1]:
            low = line[0]
        else:
            low = line[1]

        print("#%d %d" %(t, line[2]//low))

if __name__ == '__main__':
    main()
