e_dict = {}


def main():
    global e_dict
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for idx, c in enumerate(char):
        e_dict[c] = idx

    tc = int(input())
    for t in range(tc):
        enc = input()
        bin_tmp = ""
        ans = ""
        for e in range(0, len(enc), 4):
            tmp = enc[e:e + 4]
            for tm in tmp:
                tt = bin(e_dict[tm])[2:]
                while len(tt) != 6:
                    tt = '0' + tt
                bin_tmp += tt

        for b in range(0, len(bin_tmp), 8):
            num = bin_tmp[b:b + 8]
            ans += chr(int(num, 2))

        print("#"+str(t+1), ans)


if __name__ == '__main__':
    main()
