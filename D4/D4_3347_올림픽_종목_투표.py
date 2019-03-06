# [아이디어]
# 종목 배열을 하나 만들고, 투표 수를 저장할 배열을 하나 더 만든다.
# 투표자 배열을 하나 만들고 각 투표자들을 하나씩 꺼내서 종목 배열을 확인한다.
# 종목 배열에서 하나씩 꺼내어 투표자의 값과 비교하여 이하인 경우 투표 수 배열에 값을 증가하고 해당 반복문은 탈출한다.
# 투표 수가 가장 많은 값을 찾고 해당 값의 인덱스를 찾아 출력하면 된다.


def main():
    tc = int(input())
    for t in range(1, tc+1):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        A_num = [0]*n
        B = list(map(int, input().split()))

        for b in B:
            for i in range(len(A)):
                if b >= A[i]:
                    A_num[i] += 1
                    break

        print("#%d %d" %(t, A_num.index(max(A_num))+1))


if __name__ == '__main__':
    main()
