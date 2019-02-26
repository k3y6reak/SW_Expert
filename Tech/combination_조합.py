def combination(arr, bool, idx, cnt):
    if cnt == len(bool):
        print(bool)
        return

    if idx == len(arr):
        return

    bool[cnt] = arr[idx]
    combination(arr, bool, idx + 1, cnt+1)
    bool[cnt] = 0
    combination(arr, bool, idx + 1, cnt)
    
def main():
    arr = [1, 2, 3]
    combination(arr, [False, False], 0, 0)
if __name__ == '__main__':
    main()