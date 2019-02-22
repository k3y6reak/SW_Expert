def main():
    tc = int(input())
    for t in range(tc):
        line = input()
        ans = 1
        for l in range(0, len(line)//2):
            if line[l] != line[-(l+1)]:
                ans = 0
                break

        print("#"+str(t+1), ans)



if __name__ == '__main__':
    main()
