def main():
    tc = int(input())
    for t in range(tc):
        line = list(map(int, input().split()))
        A_P = line[0]
        B_Q = line[1]
        B_R = line[2]
        B_S = line[3]
        W = line[4]
        A_total = A_P * W
        B_total = 0
        if W <= B_R:
            B_total = B_Q
        else:
            W_tmp = W - B_R
            B_total = W_tmp * B_S + B_Q

        ans = 0
        if A_total < B_total:
            ans = A_total
        else:
            ans = B_total

        print("#"+str(t+1), ans)

if __name__ == '__main__':
    main()
