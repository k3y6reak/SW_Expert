# [아이디어]
# 3개의 재료가 있을때 (1, 2)와 (2, 3) 재료가 함께 들어가면 안된다.
# 재료 수 만큼 방문 배열을 하나 만든다.
# (1, 2) 와 (2, 3)에 대한 부분 집합을 만든다.
# 재료는 (1, 2) / (2, 3) 2가지가 있고 방문 배열은 재료의 수인 3이 된다.
# 부분집합을 구하는 코드에서 선택하고, 선택하지 않은 경우를 구현하는데,
# 재료들을 하나씩 꺼내면서 방문배열의 재료의 첫번째와 두번째 재료 모두 방문한 것이면 return 한다.
# 두개가 모두 방문 했다는 것은 두 재료가 모두 들어갔다는 것이다.
# 둘 중 하나라도 방문하지 않은 것은 ans를 1증가 시켜주면 된다.


ans = 0


def power_set(el, vi, n, idx):
    global ans

    for i in range(0, len(el)):
        if vi[el[i][0]-1] and vi[el[i][1]-1]:
            return

    if idx == n:
        ans += 1
        return

    vi[idx] = True
    power_set(el, vi, n, idx + 1)
    vi[idx] = False
    power_set(el, vi, n, idx + 1)


def main():
    global ans

    tc = int(input())
    for t in range(1, tc+1):
        n, m = map(int, input().split())

        el = [[0]*2 for _ in range(m)]
        for i in range(m):
            el[i][0], el[i][1] = map(int, input().split())

        ans = 0
        power_set(el, [False]*n, n, 0)
        print("#%d %d" %(t, ans))


if __name__ == '__main__':
    main()


