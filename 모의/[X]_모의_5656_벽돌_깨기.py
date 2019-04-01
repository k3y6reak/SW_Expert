

def clear_map(map_, h, w):
    for i in range(h-1, -1, -1):
        for j in range(w):
            if map_[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if map_[k][j] != 0:
                        map_[i][j] = map_[k][j]
                        map_[k][j] = 0
                        break


def del_map(map_, vi, h, w):
    for i in range(h):
        for j in range(w):
            if vi[i][j]:
                map_[i][j] = 0


def up_clear(map_, vi, x, y, h, w):
    if 0 <= x < h and 0 <= y < w:
        for i in range(x-1, x-map_[x][y], -1):
            if i >= 0:
                vi[i][y] = True
                left_clear(map_, vi, i, y, h, w)
                right_clear(map_, vi, i, y, h, w)


def left_clear(map_, vi, x, y, h, w):
    if 0 <= x < h and 0 <= y < w:
        for i in range(y-1, y-map_[x][y], -1):
            if i >= 0:
                vi[x][i] = True
                up_clear(map_, vi, x, i, h, w)
                down_clear(map_, vi, x, i, h, w)
                left_clear(map_, vi, x, i, h, w)


def right_clear(map_, vi, x, y, h, w):
    if 0 <= x < h and 0 <= y < w:
        for i in range(y+1, y+map_[x][y]):
            if i < w:
                vi[x][i] = True
                up_clear(map_, vi, x, i, h, w)
                down_clear(map_, vi, x, i, h, w)
                right_clear(map_, vi, x, i, h, w)


def down_clear(map_, vi, x, y, h, w):
    if 0 <= x < h and 0 <= y < w:
        for i in range(x+1, x+map_[x][y]):
            if i < h:
                vi[i][y] = True
                right_clear(map_, vi, i, y, h, w)
                left_clear(map_, vi, i, y, h, w)
                down_clear(map_, vi, i, y, h, w)


def clear(map_, vi, x, y, h, w):
    down_clear(map_, vi, x, y, h, w)
    left_clear(map_, vi, x, y, h, w)
    right_clear(map_, vi, x, y, h, w)
    up_clear(map_, vi, x, y, h, w)


def shot(map_, sel, h, w):
    for s in sel:
        vi = [[False]*w for _ in range(h)]
        for i in range(h):
            if map_[i][s] != 0:
                vi[i][s] = True
                clear(map_, vi, i, s, h, w)
                del_map(map_, vi, h, w)
                clear_map(map_, h, w)
                break

    return map_


low = 99999


def cnt_map(map_, h, w):
    global low
    cnt = 0
    for i in range(h):
        for j in range(w):
            if map_[i][j] != 0:
                cnt += 1

    if low > cnt:
        low = cnt


def set_map(map_, h, w):
    tmp_map = [[0]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            tmp_map[i][j] = map_[i][j]

    return tmp_map


def rd_comb(arr, sel, idx, cnt, map_, h, w):
    if cnt == len(sel):
        tmp_map = set_map(map_, h, w)
        tmp_map = shot(tmp_map, sel, h, w)
        cnt_map(tmp_map, h, w)
        return

    if idx == len(arr):
        return

    sel[cnt] = arr[idx]
    rd_comb(arr, sel, idx, cnt+1, map_, h, w)
    sel[cnt] = 0
    rd_comb(arr, sel, idx + 1, cnt, map_, h, w)


def main():
    global low

    for t in range(1, int(input()) + 1):
        n, w, h = map(int, input().split())
        map_ = [list(map(int, input().split())) for _ in range(h)]
        low = 99999
        rd_comb(range(w), [False]*n, 0, 0, map_, h, w)
        print("#%d %d" %(t, low))


if __name__ == '__main__':
    main()
