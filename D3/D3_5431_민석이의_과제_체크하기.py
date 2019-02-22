def main():
    test_case = int(input())

    for i in range(0, test_case):
        tmp1 = input().split(" ")
        peoples = tmp1[0]
        peoples_list = [ num for num in  range(1, int(peoples)+1)]
        #check_num = tmp1[1]
        check_people = input().split(" ")

        uncheck_peoples = ""

        for num in peoples_list:
            if str(num) in check_people:
                pass
            else:
                uncheck_peoples += str(num) + " "

        print("#" + str(i+1) + " " + uncheck_peoples)

if __name__ == '__main__':
    main()
