def main():
    tc = int(input())
    for t in range(1, tc+1):
        print("#"+str(t),  sum([n for n in list(map(int, input().split())) if n%2 == 1]))

if __name__ == '__main__':
    main()
