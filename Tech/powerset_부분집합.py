def powerset(arr, bool, idx):

    if idx == len(arr):
        for i in range(0, len(arr)):
            if bool[i]:
                print(arr[i], end='')
        print()
        return

    bool[idx] = False
    powerset(arr, bool, idx + 1)
    bool[idx] = True
    powerset(arr, bool, idx + 1)

def main():
    arr = [1, 2, 3]
    powerset(arr, [False, False, False], 0)

if __name__ == '__main__':
    main()