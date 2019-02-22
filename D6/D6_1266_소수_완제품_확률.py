from itertools import combinations



def percent(master):
    prime_map = [2, 3, 5, 7, 11, 13, 17]

    if master == 0:
        return 0

    per = master/100

    Success = [0]*19
    Fail = [0]*19

    Success[1] = per
    Fail[1] = 1-per

    for i in range(2, 18):
        Success[i] = Success[i-1]*per
        Fail[i] = Fail[i-1]*(1-per)

    result = 0

    for i in range(0, len(prime_map)):
        c = [cc for cc in combinations(range(18), prime_map[i])]
        result += len(c) * Success[prime_map[i]] * Fail[18-prime_map[i]]

    return result

def main():
    test_case = int(input())
    for t in range(0, test_case):
        line = input().split()
        master_a = int(line[0])
        master_b = int(line[1])

        percent_a = percent(master_a)
        percent_b = percent(master_b)

        result = percent_a + percent_b - (percent_a*percent_b)
        print("#" + str(t+1) + " " + format(result, '.6f'))


if __name__ == '__main__':
    main()
