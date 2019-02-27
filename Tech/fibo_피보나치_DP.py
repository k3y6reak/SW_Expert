fibo_list = [0]*10000


def fibo(n):
    fibo_list[0] = 0
    fibo_list[1] = 1

    for i in range(2, n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

    return fibo_list[i]


def main():
    n = 1000
    print(fibo(n))


if __name__ == '__main__':
    main()
