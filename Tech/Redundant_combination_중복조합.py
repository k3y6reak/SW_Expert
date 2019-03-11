def combination(arr, sel, idx, cnt):
    if cnt == len(sel):
        print(sel)
        return

    if idx == len(arr):
        return

    sel[cnt] = arr[idx]
    combination(arr, sel, idx, cnt+1)
    sel[cnt] = 0
    combination(arr, sel, idx + 1, cnt)

def main():
    arr = [0, 1, 2, 3, 4]
    sel = [0]*2 # 두개선택
    combination(arr, sel, 0, 0)
if __name__ == '__main__':
    main()
