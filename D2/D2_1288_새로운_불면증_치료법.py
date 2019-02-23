def main():
    tc = int(input())
    for t in range(tc):
        num = set()
        N = input()
        j = 1
        num.update(list(N))
        while len(num) != 10:
            T = str(j*int(N))
            num.update(list(T))
            j += 1

        print("#"+str(t+1), T)


if __name__ == '__main__':
    main()
