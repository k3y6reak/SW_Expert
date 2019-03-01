cnt = 0

def palindrome_chk(arr):
    global cnt

    if arr == arr[::-1]:
        cnt += 1

def main():
    global cnt

    for t in range(1, 11):
        p_len = int(input())
        m = [[0]*8 for _ in range(8)]

        for i in range(8):
            line = input()
            for j in range(8):
                m[i][j] = line[j]


        cnt = 0
        for i in range(8):
            for j in range(0, 8 - p_len + 1):
                arr = []
                arr2 = []
                for k in range(j, j + p_len):
                    arr.append(m[i][k])
                    arr2.append(m[k][i])
                palindrome_chk(arr)
                palindrome_chk(arr2)

        print("#"+str(t), cnt)

if __name__ == '__main__':
    main()
