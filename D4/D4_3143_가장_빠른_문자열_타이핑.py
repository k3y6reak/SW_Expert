# [아이디어]
# 찾고자하는 패턴 b가 있는 개수를 정규표현식을 이용해 모두 구한다.
# 원래의 문자열 길이 - 찾은 패턴들의 길이 + 패턴개수 를 구하면 답이 된다.
# asakusa sa 라면
# sa, sa 두개의 패턴이 찾아진다.
# 원래의 문자열 길이 = 7
# 패턴들의 길이 sa 2개 = 4
# 패턴의 개수 = 2

import re


def main():
    tc = int(input())
    for t in range(1, tc+1):
        a, b = map(str, input().split())
        p = re.compile(b)
        a_l = len(a)

        result = p.findall(a)
        find_len = 0
        for r in result:
            find_len += len(r)

        print("#%d %d" %(t, a_l - find_len + len(result)))


if __name__ == '__main__':
    main()
