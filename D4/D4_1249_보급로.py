# [아이디어]
# [0, 0] 부터 [n-1, n-1]까지 이동하면서 가장 가중치가 작은것을 선택해야한다.
# BFS 방식을 선택한다.
# 미로찾기처럼 0과 1로만 이루어져 특정 값일때 큐에 넣고 이동하면 되는 방식과는 다르다.
# 각 위치마다 가중치가 있기 때문에 가중치를 위한 배열을 맵과 같은 크기로 만든다.
# 상, 하, 좌, 우 는 델타 배열을 이용한다.
# 먼저 큐에 [0, 0]을 넣고 해당 위치는 방문 표시한다.
# 큐가 비어있지 않는 동안 계속해서 루프를 돈다.
# 큐에서 하나꺼내고 델타배열을 이용해 상, 하, 좌, 우를 계산한다.
# 범위 외인 경우는 버리고 범위 내의 경우만 생각한다. 이를 nx, ny로 표시하자.
# **** [중요!] ****
# BFS를 이용해 탐색하면 이전 가중치들의 합이 저장된다.
# 다음 가중치의 값이 현재 가중치에 앞으로 갈 가중치를 더한 것보다 크면 더한 값을 넣어 작게 만들어준다. (코드 확인)
# 해당 좌표를 큐에 넣고 방문표시한다.
#
# 0100                      XX00                                    XXXX  
# 1110 과 같은 맵이 있다 하자.   1X10  X가 지나온 방향이라하고,                111X    
# 1011                      1XXX  방문표시가 되었다 하자. BFS 탐색에 의해    101X <- 해당 위치는 방문 했으나 가중치가 2이다. 작으면 변경이 필요하다.
# 1010                      101X  다음고 같이 탐색한다하자.                101X



import queue
q = queue.Queue()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(m, vi, ti):
    global q, dx, dy
    q = queue.Queue()
    q.put([0, 0])
    vi[0][0] = True

    while not q.empty():
        p = q.get()
        x = p[0]
        y = p[1]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(m) or ny >= len(m):
                continue

            # 방문을 했으나 가중치가 더 작은 경우가 생긴다면 넣어줘야 한다.
            if (not vi[nx][ny]) or ti[nx][ny] > ti[x][y] + m[nx][ny]: # 방문을 하지 않았거나 다음 가중치가 앞으로 가고자하는 가중치보다 크면
                ti[nx][ny] = ti[x][y] + m[nx][ny] # 다음 가중치를 앞으로 가고자하는 가중치로 변경한다.
                q.put([nx, ny])
                vi[nx][ny] = True


def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        m = [[0]*n for _ in range(n)]
        ti = [[0]*n for _ in range(n)]
        vi = [[False]*n for _ in range(n)]
        for i in range(n):
            line = input()
            for j in range(n):
                m[i][j] = int(line[j])

        bfs(m, vi, ti)
        print("#%d %d"%(t, ti[-1][-1]))



if __name__ == '__main__':
    main()
