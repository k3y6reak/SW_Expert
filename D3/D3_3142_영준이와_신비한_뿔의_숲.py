def main():
    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        h = line[0] - line[1]
        print("#%d %d %d" %(t, line[1]-h, h))

if __name__ == '__main__':
    main()
