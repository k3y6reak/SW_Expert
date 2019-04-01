# [아이디어]
# 서로소 집합을 만들 수 있는 make_set, find, union을 이용한다.
# 0이 들어오면 a, b를 union하고, 1이 들어오면 find(a) == find(b) 이면 1을, 아니면 0을 출력한다.

parents = []
rank = []


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if rank[px] > rank[py]:
        parents[py] = px
    else:
        parents[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


def make_set(x):
    parents[x] = x
    rank[x] = 0


def main():
    global parents, rank
    for t in range(1, int(input()) + 1):
        n, m = map(int, input().split())

        parents = [0]*(n+1)
        rank = [0]*(n+1)

        for i in range(1, n+1):
            make_set(i)

        ans = []
        for j in range(m):
            c, a, b = map(int, input().split())
            if c == 0:
                union(a, b)
            elif c == 1:
                if find_set(a) == find_set(b):
                    ans.append('1')
                else:
                    ans.append('0')

        print("#%d %s" %(t, ''.join(ans)))


if __name__ == '__main__':
    main()
