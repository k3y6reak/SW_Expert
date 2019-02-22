import queue

def main():
    for i in range(0, 10):
        test_cae = int(input())
        num_list = [int(num) for num in input().split()]
        que = queue.Queue(9)

        for n in num_list:
            que.put(n)

        cnt = 1
        flag = False
        while True:
            # cnt가 1~5까지만 돈다.
            while cnt != 6:
                num = que.get() # 큐에서 값을 하나 가져온다.
                tmp = num - cnt # 해당 cnt와 값을 뺀다.
                if tmp <= 0: # 그때 0보다 작거나 같은 경우에
                    tmp = 0 # 0으로 만들고
                    flag = True # 0이라는 플래그를 true로 한다. 반복문 탈출.
                    que.put(tmp) # 그때 큐에 넣고 끝낸다.
                    break
                que.put(tmp) # 0보다 크면 뺀 값을 넣고
                cnt += 1 # cnt를 증가시킨다.
            cnt = 1 # 1 사이클은 1~5까지 이므로 다시 1로 초기화 한다.
            if flag: # 끝나는 플래그라면 반복문을 나간다.
                break

        print("#" + str(i+1) + " ", end='')
        for j in list(que.queue):
            print(str(j) + " ", end='')
        print()

if __name__ == '__main__':
    main()


