import itertools

def main():
    test_case = int(input())

    for i in range(0, test_case):
        bracket = input()

        line = 0
        count = 0
        for j in range(0, len(bracket)):
            b = bracket[j]
            if b == ')': #오른쪽일때 
                left_bracket = bracket[j-1]
                if left_bracket == '(':# 전에 왼쪽이면 레이저
                    line -= 1 # 해당 괄호는 레이저 괄호 
                    count += line # 그 전까지 괄호는 막대기이므로 증가
                else:
                    line -= 1 # 막대기 왼쪽 괄호와 오른쪽 괄호가 끝남. 다음 막대를 위해서 
                    count += 1 # 잘린 후 나머지가 1개씩 있음.
            if b == '(': # 막대를 카운트
                line += 1
        print("#" + str(i+1) + " " + str(count))

if __name__ == '__main__':
    main()


