def insert_sort(data_set):
    # i表示摸到的牌的下标
    for i in range(1, len(data_set)):
        tmp = data_set[i]
        # j指的是手里的牌
        j = i - 1
        while data_set[j] > tmp and j >= 0:
            data_set[j + 1] = data_set[j]
            j -= 1
        data_set[j + 1] = tmp
    return data_set


if __name__ == '__main__':
    li = [3, 2, 4, 1, 5, 7, 8, 4, 9]
    print(insert_sort(li))
