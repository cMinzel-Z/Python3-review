def partition(data_set, left, right):
    tmp = data_set[left]
    while left < right:
        # 从右边找比P位小的数
        while left < right and data_set[right] >= tmp:
            # 往左走1
            right -= 1
        # 把右边的值写到左边空位上
        data_set[left] = data_set[right]

        while left < right and data_set[left] <= tmp:
            left += 1
        # 把左边的值写道右边空位上
        data_set[right] = data_set[left]
    # 把tmp归位
    data_set[left] = tmp
    return left


def quick_sort(data_set, left, right):
    # 至少两个元素才开始递归
    if left < right:
        mid = partition(data_set, left, right)
        quick_sort(data_set, left, mid - 1)
        quick_sort(data_set, mid + 1, right)


if __name__ == '__main__':
    li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    quick_sort(li, 0, len(li) - 1)
    print(li)
