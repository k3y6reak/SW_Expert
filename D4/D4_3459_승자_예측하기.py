def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        start = 1

        turn = True
        while n > 0:
            n -= start
            if turn:
                start *= 4

            turn = not turn

        win = ""

        if turn:
            win = "Alice"
        else:
            win = "Bob"

        print("#%d %s" %(t, win))


if __name__ == '__main__':
    main()
