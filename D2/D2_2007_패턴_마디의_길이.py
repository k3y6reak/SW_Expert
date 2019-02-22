import re

def main():
    test_case = int(input())
    for k in range(test_case):
        line = input()
        find_flag = False
        i = 1
        p = line[0:1]
        while not find_flag:
            t = line[len(p):i+len(p)]
            if p != t:
                i += 1
                p = line[0:i]
            else:
                find_flag = True

        print("#" + str(k+1), len(p))


if __name__ == '__main__':
    main()


