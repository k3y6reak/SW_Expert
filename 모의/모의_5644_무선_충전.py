# [아이디어]
# A가 이동하는 방향, B가 이동하는 방향을 큐에 넣는다.
# 처음 시점부터 충전이 가능하므로 미리 충전량을 파악한 뒤에 이동한다.
# 충전을 할때 겹치는 경우, 같은 AP에 있는 경우를 확인해야 한다.
# AP 범위 내에 있는지 확인하고, 2중 for loop으로 AP의 개수 만큼 돌려 i == j인 경우 같은 AP이므로
# A가 충전할 수 있는 량, B가 충전할 수 있는 량 중 큰 것을 빼낸다. ( 나눠서 더해도 어짜피 하나의 양)


from collections import deque

    #X, 상, 우, 하, 좌
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

# AP_list = [x, y, 거리, 충전량]

def charge(A_x, A_y, B_x, B_y, AP_list, AP_num):
    # 해당 위치에서 충전을 할 수 있는지 확인.
    # AP_list들에서 A의 위치와 B의 위치가 되는지 확인.

    A_charge = [0]*AP_num
    B_charge = [0]*AP_num

    for i in range(AP_num):
        dist_A = abs(AP_list[i][1] - A_x) + abs(AP_list[i][0] - A_y) # AP의 x, y가 반대
        dist_B = abs(AP_list[i][1] - B_x) + abs(AP_list[i][0] - B_y)

        # 각 AP에서 A, B의 거리가 AP의 범위 내인지 확인.
        if dist_A <= AP_list[i][2]:
            A_charge[i] = AP_list[i][3] # 범위 내이면 최대 충전량을 가져간다.
        if dist_B <= AP_list[i][2]:
            B_charge[i] = AP_list[i][3]

    charge_sum = 0
    for i in range(AP_num):
        for j in range(AP_num):
            if i == j: # 같은 AP라면.
                # 어짜피 더하기때문에 하나의 값만 빼오면 됨.
                # 같은 AP면 나눠서 더해도 어짜피 하나임.
                charge_sum = max(charge_sum, A_charge[i], B_charge[j])
            else:
                charge_sum = max(charge_sum, A_charge[i] + B_charge[j])

    return charge_sum


def main():
    for t in range(1, int(input())  + 1):
        M, AP_num = map(int, input().split())
        A_q = deque(list(map(int, input().split())))
        B_q = deque(list(map(int, input().split())))

        AP_list = [list(map(int, input().split())) for _ in range(AP_num)]

        A_x, A_y = 1, 1
        B_x, B_y = 10, 10

        # 처음부터 충전가능.
        ans = charge(A_x, A_y, B_x, B_y, AP_list, AP_num)
        for i in range(M):
            A_x += dx[A_q[i]]
            A_y += dy[A_q[i]]

            B_x += dx[B_q[i]]
            B_y += dy[B_q[i]]

            ans += charge(A_x, A_y, B_x, B_y, AP_list, AP_num)

        print("#%d %d" %(t, ans))

if __name__ == '__main__':
    main()
