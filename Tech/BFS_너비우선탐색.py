import queue


def main():
    test_case = int(input())

    for t in range(test_case):
        line = input().split()
        dot = int(line[0])
        edge = int(line[1])
        m = [[0] * (dot + 1) for _ in range(dot + 1)]

        line2 = input().split()
        i = 0
        for e in range(edge):
            a = int(line2[i])
            b = int(line2[i + 1])
            m[a][b] = 1
            m[b][a] = 1
            i += 2

        vi = [False]*(dot+1)
        q = queue.Queue()
        q.put(1)
        vi[1] = True
        while not q.empty():
            v = q.get()
            print(v)
            for i in range(1, len(m)):
                if m[v][i] == 1 and (not vi[i]):
                    q.put(i)
                    vi[i] = True


if __name__ == '__main__':
    main()
