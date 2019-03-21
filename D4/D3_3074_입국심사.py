# [아이디어]
# 처음 각 심사원들의 배열을 만들어 해당 심사원에 사람이 없으면 사람을 넣고, 시간을 하나씩 줄여가며 체크를 했다.
# 위와 같은 경우 일부는 맞게된다. (최소의 시간을 체크하는 것이 어렵다.)
# 바이너리 서치(이진 탐색)을 이용한다.
# 가장 최악의 시간은 최대의 시간이 걸리는 심사원 * 사람 수가 된다.
# 그러면 0부터 최악의 시간까지 탐색을 하는데, (0 + 최악의 시간) / 2 = 중간 시간을 기준으로, 해당 시간 / 각 심사원 시간 = 진행된 사람 수 가 된다.
# 진행된 사람 수가 넘으면 최악의 시간을 중간값 - 1로 변경하고 진행된 사람의 수가 적다면 시작 시간을 중간값 + 1 로 변경한다.


def main():
    tc = int(input())
    for t in range(1, tc + 1):
        n, m = map(int, input().split())
        chk = [0] * n
        for i in range(n):
            chk[i] = int(input())

        end = max(chk)*m
        start = 0
        low = end

        while start <= end:
            mid = (start + end) // 2
            ans = 0

            for i in range(n):
                ans += (mid // chk[i])

            if ans < m:
                start = mid + 1
            else:
                if low > mid:
                    low = mid
                end = mid - 1

        print("#%d %d" %(t, low))


if __name__ == '__main__':
    main()
