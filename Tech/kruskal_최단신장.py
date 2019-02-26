# 최소비용 간선 

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

    line = list(map(int, input().split()))
    V, E = line[0], line[1]
    # 출발, 도착, 비용
    edges = [[0] * 3 for _ in range(E)]

    for e in range(E):
        line = list(map(int, input().split()))
        edges[e][0] = line[0]
        edges[e][1] = line[1]
        edges[e][2] = line[2]

    # edges를 2번칸의 크기순으로 오름차순 정렬
    edges.sort(key=lambda x:x[2])
    print(edges)
    # V개의 정점만큼 상호배타집합을 위한 parents 배열 생성
    parents = [0]*V
    rank = [0] * V

    # V개 정점들을 모두 make_set 해서 각자 독립된 집합으로 만든다.
    for i in range(V):
        make_set(i)

    # edges 배열을 탐색하면서 가장 짧은 간선의 출발-도착 정점이 서로 다른 집합이라면 간선을 선택하고 두 집합을 합친다.
    w = 0
    j = 0
    for i in range(len(edges)):
        if j == V-1:
            break
        if find_set(edges[i][0]) != find_set(edges[i][1]):
            w += edges[i][2]
            print(edges[i][2])
            union(edges[i][0], edges[i][1])
            j += 1

    # v-1개의 간선이 선택되면 종료.
    print(w)


if __name__ == '__main__':
    main()
