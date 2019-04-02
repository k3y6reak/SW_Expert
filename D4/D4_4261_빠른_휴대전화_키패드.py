# [아이디어]
# 각 키패드마다 입력할 수 있는 문자들의 딕셔너리를 구성한다.
# 입력받은 단어들을 하나씩 가져와 입력한 번호의 길이와 다르면 걸러낸다.
# 길이가 같은 경우, 해당 단어가 딕셔너리에 포함되는지 확인하고, 아니면 걸러낸다.

def main():
    d = {'1': (), '2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
         '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}

    for t in range(1, int(input()) + 1):
        s, n = map(int, input().split())
        words = input().split()
        s = list(str(s))
        cnt = 0

        for w in words:
            flag = True
            if len(w) != len(s):
                flag = False

            else:
                for i in range(len(w)):
                    if w[i] not in d[s[i]]:
                        flag = False
                        break
            if flag:
                cnt += 1

        print("#%d %d" %(t, cnt))


if __name__ == '__main__':
    main()
