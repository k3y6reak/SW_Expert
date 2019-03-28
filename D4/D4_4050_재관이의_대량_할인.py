# [아이디어]
# 입력받은 옷들의 가격을 내림차순으로 정렬한다.
# 3번째 옷들은 제외하고 나머지를 더한다.

def main():
    for t in range(1, int(input()) + 1):
        n = int(input())
        c = list(map(int, input().split()))
        c.sort(key=lambda x:-x)
        print("#%d %d" %(t, sum([c[i] for i in range(len(c)) if i % 3 != 2])))

if __name__ == '__main__':
    main()
