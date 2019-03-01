def main():
    tc = int(input())
    for t in range(1, tc+1):
        chk = ['a', 'e', 'i', 'o', 'u']
        s = list(input())

        for c in chk:
            while c  in s:
                s.remove(c)

        print("#" + str(t), ''.join(s))

if __name__ == '__main__':
    main()
