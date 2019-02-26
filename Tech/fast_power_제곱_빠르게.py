def power(a, n):
    # cnt = log2(n)
    # cnt+1 크기의 배열을 생성한다.
    # 0번 칸에는 밑인 a, 1번칸부터 앞에칸 수를 거듭제곱해 저장하여 1, 2, 4, 8, 16 승이 저장되게 배열을 채운다.
    # n을 비트마스킹하여 자릿수를 곱해간다.( 9승 = 8승*1승)

    k = n
    cnt = 0
    while k != 1:
        k //= 2
        cnt += 1

    powMap = [0]*(cnt+1)
    powMap[0] = a
    for i in range(1, len(powMap)):
        powMap[i] = powMap[i-1] * powMap[i-1]

    result = 1
    for i in range(0, cnt+1):
        if n & (1 << i) != 0:
            result *= powMap[i]
    print(result)


def main():
    power(2, 20)


if __name__ == '__main__':
    main()
