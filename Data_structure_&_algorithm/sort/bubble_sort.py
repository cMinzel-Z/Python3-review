import random


def bubble_sort(data_set):
    # 第i趟
    for i in range(len(data_set) - 1):
        exchange = False
        # 箭头位置
        for j in range(len(data_set) - i - 1):
            # 前面的数比后面大则交换
            if data_set[j] > data_set[j + 1]:
                data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]
                exchange = True
        # 没有位置交换则说明没有无序区
        if not exchange:
            return


if __name__ == '__main__':
    # li = [random.randint(0, 10000) for i in range(1000)]
    li = [1, 2, 3, 4, 5]
    print(li)
    print('-' * 20)
    bubble_sort(li)
    print(li)
