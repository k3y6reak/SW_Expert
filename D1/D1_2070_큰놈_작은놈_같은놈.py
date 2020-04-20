def cmp(num1, num2):
    result = (num1 > num2) - (num1 < num2)

    if result > 0:
        return ">"
    elif result < 0:
        return "<"

    return "="


def main():
    for t in range(1, int(input()) + 1):
        num1, num2 = map(int, input().split())

        print("#"+str(t) + " " + cmp(num1, num2))


if __name__ == '__main__':
    main()
