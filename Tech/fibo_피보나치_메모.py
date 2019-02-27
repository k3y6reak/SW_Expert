fibo_list = [0]*10000


def fibo(n):
    if n >= 2 and fibo_list[n] == 0:
        fibo_list[n] = fibo(n-1) + fibo(n-2)

    return fibo_list[n]


def main():
    n = 3
    fibo_list[0] = 1
    fibo_list[1] = 1
    print(fibo(n))


if __name__ == '__main__':
    main()
