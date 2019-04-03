# [아이디어]
# DFS를 이용한다. depth는 행을 나타낸다.
# depth가 전체 행 d 보다 같거나 커지는 경우, 보호 필름을 검사한다.
# 보호필름을 검사하고, 통과되면 그 때의 cnt (약품 처리 횟수) 와 low를 비교하여 작은 값을 넣는다.
# 위의 과정까지 진행하면 Python기준 47개에서 시간초과가 발생한다.
# k가 1인 경우에는 검사할 필요가 없기 때문에 바로 0을 출력한다. 여기까지는 48개에서 시간초과가 발생한다.
# 보호필름을 검사할 때 해당 열이 통과되지 못하면 다음 열을 볼 필요가 없다. 이 조건을 추가하면 통과한다.

low = 99999

def check(map_, d, w, k, cnt):
    global low

    vi = [False]*w

    for j in range(w):
        for i in range(d-k+1): # k개 전까지만 보면 된다.
            t = map_[i][j] # 현재 위치의 값을 가져오고
            find_flag = True
            for l in range(i, i+k): # 현재 위치부터 k 만큼 확인한다.
                if t != map_[l][j]:
                    find_flag = False
                    break

            if find_flag:
                vi[j] = True
        if not vi[j]: # 해당 위치가 통과되지 못하면 더이상 볼 필요가 없음.
            return

    vi = set(vi)
    if len(vi) == 1 and list(vi)[0]:
        low = min(cnt, low)


def dfs(map_, d, w, k, depth, cnt):
    global low

    if cnt > low:
        return

    # 한 줄씩 뿌리면서 해당 필름이 통과되는지 확인.
    if d <= depth:
        check(map_, d, w, k, cnt)
        return

    # 안뿌림
    dfs(map_, d, w, k, depth+1, cnt)

    # A 뿌림
    save = map_[depth] # 해당 row를 저장하고
    # 해당 row를 A로 변경
    map_[depth] = [0]*w
    dfs(map_, d, w, k, depth+1, cnt+1)
    map_[depth] = save

    # B 뿌림
    save = map_[depth]
    map_[depth] = [1]*w
    dfs(map_, d, w, k, depth+1, cnt+1)
    map_[depth] = save


def main():
    global low

    for t in range(1, int(input()) + 1):
        d, w, k = map(int, input().split())
        map_ = [list(map(int, input().split())) for _ in range(d)]

        low = 99999
        if k == 1:
            print("#%d %d" % (t, 0))
        else:
            dfs(map_, d, w, k, 0, 0)
            print("#%d %d" % (t, low))


if __name__ == '__main__':
    main()
