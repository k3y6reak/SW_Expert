def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def card_shuffle(cards, cnt, n):
    if cnt == n:
        print(cards)
        return

    for i in range(0, len(cards)):
        for j in range(i+1, len(cards)):
            swap(cards, i, j)
            card_shuffle(cards, cnt+1, n)
            swap(cards, i, j)

def main():
    cards = [1, 2, 3, 4, 5]

    card_shuffle(cards, 0, 2)

if __name__ == '__main__':
    main()