def main():
    for i in range(0, 10):
        bracket_len = int(input())
        bracket = input()

        isOk = False
        stack = []
        for j in range(0, bracket_len):
            b = bracket[j]
            if b == '{' or b == '[' or b == '<' or b == '(':
                stack.append(b)
            else:
                left = stack.pop()
                if b == '}':
                    if left == '{':
                        isOk = True
                    else:
                        isOk = False
                        break
                elif b == ']':
                    if left == '[':
                        isOk = True
                    else:
                        isOk = False
                        break
                elif b == '>':
                    if left == '<':
                        isOk = True
                    else:
                        isOk = False
                        break
                elif b == ')':
                    if left == '(':
                        isOk = True
                    else:
                        isOk = False
                        break

        if isOk == True:
            print ("#" + str(i+1) + " " + '1')
            isOk = False
        else:
            print ("#" + str(i+1) + " " + '0')
            isOk = False


if __name__ == '__main__':
    main()


