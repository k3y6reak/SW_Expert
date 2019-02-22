
def main():
    test_case = int(input())

    for i in range(0, test_case):
        original = input()

        count = 0
        j = original.find('1')
        count += 1
        while j < len(original):
            if original[j] == '1':
                flag = '1'
                count += 1
                for k in range(j+1, len(original)):
                    if original[k] == flag:
                        j += 1
                        continue
                    else:
                        flag = '0'
                        count+=1
                        j = k
                        break
                if flag != '0':
                    j += 1
            else:
                j += 1

        print("#" + str(i + 1) + " " + str(count-1))

if __name__ == '__main__':
    main()
