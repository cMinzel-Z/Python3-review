# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:57:21 2021

@author: Minzel
"""


def linear_search(data_set, value):
    for i in range(len(data_set)):
        if data_set[i] == value:
            return i
    return None


def binary_search(data_set, value):
    left = 0
    right = len(data_set) - 1

    # 候选区有值
    while left <= right:
        mid = (left + right) // 2
        if data_set[mid] == value:
            return mid

        # 待查找值在左侧
        elif data_set[mid] > value:
            right = mid - 1

        # 待查找值在右侧
        else:
            left = mid + 1
    else:
        return None


if __name__ == '__main__':
    #    # 顺序查找
    #    list_a = [2,5,7,9,1,2,4,5]
    #    a = linear_search(list_a, 9)
    #    print(a)

    # 二分查找
    list_b = [1, 2, 3, 5, 6, 7, 8, 9]
    print(binary_search(list_b, 8))
