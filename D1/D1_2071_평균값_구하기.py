def main():
    tc = int(input())
    for t in range(1, tc+1):
        print("#"+str(t),  format(sum([n for n in list(map(int, input().split()))])/10, ".0f"))

if __name__ == '__main__':
    main()
