def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def perm(arr, idx):
    if idx == len(arr):
        print(arr)
        return

    for i in range(idx, len(arr)):
        swap(arr, idx, i)
        perm(arr, idx+1)
        swap(arr, idx, i)

def main():
    perm([1, 2, 3], 0)

if __name__ == '__main__':
    main()