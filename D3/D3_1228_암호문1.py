import Tree

def main():
    for t in range(1, 11):
        str_len = int(input())
        original_enc = list(map(str, input().split()))
        cmd_len = int(input())
        tmp_cmd = [s for s in input().split("I")]

        for cmd in tmp_cmd:
            if cmd != '':
                cc = cmd.split(" ")
                idx = int(cc[1])
                insert_len = cc[2]
                original_enc[idx:idx] = cc[3:len(cc)-1]
        print("#"+str(t) + " ", end='')
        for i in range(0, 10):
            print(original_enc[i] + " ", end='')
        print()

if __name__ == '__main__':
    main()
