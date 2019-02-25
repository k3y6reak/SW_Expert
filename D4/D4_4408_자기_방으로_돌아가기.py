def main():
    tc = int(input())
    for t in range(1, tc+1):
        cnt_map = [0]*201 # 복도 번호
        num = int(input())
        for n in range(num):
            line = list(map(int, input().split()))
            if line[0] > line[1]: # 400 200 이면 200 400으로 변경
                line[0], line[1] = line[1], line[0]

            start = line[0]
            end = line[1]

            # 복도 번호단위 이므로 1~2는 1번복도 3~4는 2번복도.
            if line[0] % 2 == 1: # 홀수이면
                start += 1 # 더해서 짝수로 만들고
            start //= 2 # 해당 복도 번호가 된다.

            if line[1] % 2 == 1:
                end += 1
            end //= 2

            for c in range(start, end+1): # 시작 지점부터 끝 지점까지 돌면서 증가시킨다.
                cnt_map[c] += 1

        print("#"+str(t), max(cnt_map)) # 그 중 가장 큰 값이 답.


if __name__ == '__main__':
    main()
