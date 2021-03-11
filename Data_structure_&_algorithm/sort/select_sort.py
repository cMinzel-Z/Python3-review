def select_sort_simple(data_set):
    new_data_set = []
    # 第一个O(n)
    for i in range(len(data_set)):
        # 第二个O(n)
        min_val = min(data_set)
        new_data_set.append(min_val)
        # 第三个O(n), 但和第二个视为同一个O(n)
        data_set.remove(min_val)
    return new_data_set


def select_sort(data_set):
    # i是第几趟
    for i in range(len(data_set) - 1):
        min_loc = i
        for j in range(i + 1, len(data_set)):
            if data_set[j] < data_set[min_loc]:
                min_loc = j
        if min_loc != i:
            data_set[i], data_set[min_loc] = data_set[min_loc], data_set[i]
    return data_set


if __name__ == '__main__':
    li = [3, 2, 1, 4, 5, 9, 2, 6, 5, 3]
    print(select_sort(li))
