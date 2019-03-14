# [아이디어]
# 시작점부터 해당 시작점과 연결된 사람들을 큐에 넣어서 BFS로 탐색한다.
# 1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2 (시작 2)
# 위와 같은 경우 2와 연결된 모든 값을 큐에 넣어준다.
# 이때, 몇번을 이동했는지 확인하기 위해 시작의 depth를 0으로 주고
# 해당 시작점에서 추가된 사람들은 시작점의 depth + 1을 준다.
# 큐에 추가된 값을 따로 lasts 배열에 넣어주고 이 배열을 depth 와 사람번호를 기준으로 정렬한다.
# depth가 크면서 사람 번호가 큰 것이 제일 마지막에 나타나므로 마지막 사람 번호를 출력한다.


import queue

lasts = []


def bfs(start, vi, f_t):
    global lasts

    q = queue.Queue()
    q.put([start, 0])
    vi[start] = True

    while not q.empty():
        p = q.get()
        lasts.append(p)

        for i in range(len(f_t)):
            if f_t[i][0] == p[0] and (not vi[f_t[i][1]]):
                vi[f_t[i][1]] = True
                q.put([f_t[i][1], p[1] + 1])


def main():
    global lasts

    for t in range(1, 11):
        n, start = map(int, input().split())
        f_t = []

        line = list(map(int, input().split()))
        big = max(line)+1
        vi = [False]*big
        for i in range(0, n, 2):
            f_t.append([line[i], line[i+1]])

        lasts = []
        bfs(start, vi, f_t)
        lasts.sort(key=lambda x: (x[1], x[0]))

        print("#%d %d"%(t, lasts[-1][0]))


if __name__ == '__main__':
    main()
