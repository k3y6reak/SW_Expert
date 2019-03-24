# [아이디어]
# 입력받은 카드의 정보 중에서 3개씩 받아와 해당 줄에 중복이 있는지 먼저 확인하여 있으면 바로 ERROR르 출력한다.
# 중복이 없는 경우에는 입력받은 카드들의 배열에 True로 설정한다.
# 입력받은 모든 카드들에 대해 설정이 완료된 후에, 나머지 카드(False)들을 카운팅한다.
# False의 개수가 필요한 카드의 개수가 된다.


S_cnt = 0
C_cnt = 0
H_cnt = 0
D_cnt = 0

S_cards = []
C_cards = []
H_cards = []
D_cards = []


def main():
    global S_cnt, C_cnt, H_cnt, D_cnt, S_cards, C_cards, H_cards, D_cards

    for t in range(1, int(input())+1):
        cards = input()
        S_cnt, C_cnt, H_cnt, D_cnt = 0, 0, 0, 0
        S_cards, C_cards, H_cards, D_cards = [False]*14, [False]*14, [False]*14, [False]*14
        S_cards[0], C_cards[0], H_cards[0], D_cards[0] = True, True, True, True
        b_flag = False
        for c in range(0, len(cards), 3):
            tmp = cards[c:c + 3]
            pattern = tmp[0]
            card_num = int(tmp[1:])
            if pattern == "S":
                S_cards[card_num] = True

            elif pattern == "C":
                C_cards[card_num] = True

            elif pattern == "H":
                H_cards[card_num] = True

            elif pattern == "D":
                D_cards[card_num] = True

            for i in range(c+3, len(cards), 3):
                if tmp == cards[i:i + 3]:
                    b_flag = True
                    break
        if b_flag:
            print("#%d ERROR" %(t))
        else:
            for i in S_cards:
                if not i:
                    S_cnt += 1
            for i in C_cards:
                if not i:
                    C_cnt += 1
            for i in H_cards:
                if not i:
                    H_cnt += 1
            for i in D_cards:
                if not i:
                    D_cnt += 1

            print("#%d %d %d %d %d" %(t, S_cnt, D_cnt, H_cnt, C_cnt))


if __name__ == '__main__':
    main()
