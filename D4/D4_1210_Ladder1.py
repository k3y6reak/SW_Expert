def left(x, y, size, arr, move):
    i = y - 1
    for j in range(i, -1, -1):
        if x + 1 < size:
            if arr[x+1][j] != 1:
                move[x][j] = 3
            else:
                move[x][j] = 3
                return x, j, "down"

def right(x, y, size, arr, move):
    i = y + 1
    for j in range(i, size):
        if x+1 < size:
            if arr[x+1][j] != 1:
                move[x][j] = 3
            else:
                move[x][j] = 3
                return x, j, "down"

def down(x, y, size, arr, move):
    left_flag = False
    right_flag = False
    i = y
    for j in range(x, size):
        if arr[j][i] == 1:
            move[j][i] = 3
            if i-1 > 0:
                if arr[j][i-1] == 1 and move[j][i-1] != 3:
                    return j, i, "left"
            if i+1 < size:
                if arr[j][i+1] == 1 and move[j][i+1] != 3:
                    return j, i, "right"
        elif arr[j][i] == 2:
            return j, i, "end"

    return j, i, "end_x"


def main():

    for t in range(0, 10):
        case_num = int(input())
        size = 100
        
        arr = [[0] * size for i in range(size)]
        move = [[0] * size for i in range(size)]
        tmp = []
        for i in range(0, size):
            tmp += input().split()
        t_num = 0
        for i in range(0, size):
            for j in range(0, size):
                arr[i][j]  = int(tmp[t_num])
                t_num += 1

        starts = [num for num in arr[0]]

        for i in range(0, size):
            x = 0
            y = i
            res_x = x
            res_y = y
            way = "down"
            while(True):
                if starts[i] == 1:
                    if way == "down":
                        x, y, way = down(x, y, size, arr, move)
                    elif way == "left":
                        x, y, way = left(x, y, size, arr, move)
                    elif way == "right":
                        x, y, way = right(x, y, size, arr, move)
                    elif way == "end":
                        print("#" + str(case_num) + " " + str(res_y))
                        break
                    elif way == "end_x":
                        break
                else:
                    break


            move = [[0] * size for i in range(size)]


if __name__ == '__main__':
    main()


