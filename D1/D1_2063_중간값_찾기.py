def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


def main():
    cnt = int(input())
    num_list = [int(num) for num in input().split(" ")]
    sorted_data = bubble_sort(num_list)

    mid = int(len(num_list) / 2)
    print(sorted_data[mid])

if __name__ == '__main__':
    main()
