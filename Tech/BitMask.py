def main():
    items = ['Apple', 'Potato2', 'coffee', 'juice']

    for i in range(0, 1 << len(items)):
        for j in range(0, len(items)):
            if i & (1 << j):
                print(items[j] + " ", end='')
        print()

if __name__ == '__main__':
    main()
