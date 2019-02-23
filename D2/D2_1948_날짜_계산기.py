m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def main():
    tc = int(input())
    for t in range(tc):
        line = list(map(int, input().split()))
        s_m = line[0]
        s_d = line[1]
        e_m = line[2]
        e_d = line[3]

        if s_m == e_m:
            a = 0
        else:
            a = m[s_m] - s_d + 1
        for e in range(s_m+1, e_m):
            a += m[e]
        a += e_d

        print("#"+str(t+1), a)

if __name__ == '__main__':
    main()
