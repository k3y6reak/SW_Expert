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
    global parents
    global rank
    parents[x] = x
    rank[x] = 0


def main():
    global parents
    global rank
    test_case = int(input())
    for t in range(test_case):
        line = list(map(int, input().split()))
        V, E = line[0], line[1]
        # 출발, 도착, 비용
        edges = [[0] * 3 for _ in range(E)]

        for e in range(E):
            line = list(map(int, input().split()))
            edges[e][0] = line[0]
            edges[e][1] = line[1]
            edges[e][2] = line[2]

        edges.sort(key=lambda x:x[2])

        parents = [0]*(V+1)
        rank = [0] * (V+1)

        for i in range(V):
            make_set(i)

        w = 0
        j = 0
        for i in range(len(edges)):
            if j == V-1:
                break
            if find_set(edges[i][0]) != find_set(edges[i][1]):
                w += edges[i][2]
                union(edges[i][0], edges[i][1])
                j += 1

        print("#" + str(t+1), w)


if __name__ == '__main__':
    main()


