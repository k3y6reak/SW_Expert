def main():
    for t in range(1, 11):
        node_len = int(input())
        flag = False
        for i in range(0, node_len//2):
            line = input().split()
            node_operation = line[1]
            if(node_operation.isnumeric()):
                flag = True
            else:
                continue
        for i in range(node_len//2, node_len):
            line = input()
        if(flag):
            print("#" + str(t) + " 0")
        else:
            print("#" + str(t) + " 1")

if __name__ == '__main__':
    main()
