def main():
    tc = int(input())
    for t in range(tc):
        num = int(input())
        cnt = [0]*12
        for i in range(2, num):
            while num % i == 0:
                num /= i
                cnt[i] += 1

        print("#"+str(t+1)+" ", end='')
        for i in range(0, len(cnt)):
            if i == 2 or i == 3 or i == 5 or i == 7 or i == 11:
                print(str(cnt[i])+" ", end='')
        print()


if __name__ == '__main__':
    main()
