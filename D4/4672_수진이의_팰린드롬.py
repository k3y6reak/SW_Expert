# [아이디어]
# 부분 문자열의 정의가 문제에 제시가 되어있다. 문자열이 붙어있어야 한다는것.
# 처음 순열을 이용해서 모든 조합에 대해 팰린드롬을 계산했지만, 제한시간 초과가 발생한다.
# 1자리, 2자리, 3자리 ... 문자의 길이까지 해서 팰린드롬이 되는 경우를 생각해보자.
# abcabc의 경우 정렬하면 aabbcc 가 되며, 1자리: [a,a,b,b,c,c] 2자리:[aa,bb,cc] 가 만들어진다.
# 최대한 많은 자리가 팰린드롬이려면 정렬하는 것이 가장 클 것이다.

big = 0

def main():
    global big
    for t in range(1, int(input()) + 1):
        big = 0
        s = list(input())
        s.sort()
        part = []
        for i in range(1, len(s) + 1):
            for j in range(len(s)):
                tmp = s[j: j + i]
                if len(tmp) == i:
                    part.append(tmp)

        cnt = 0
        for p in part:
            if p == p[::-1]:
                cnt += 1

        big = max(cnt, big)

        print("#%d %d" % (t, big))


if __name__ == '__main__':
    main()
