'''
A list where each element is the sum of the elements of List a and the first element of each
tuple from List b. However, you choose only those elements for which List a yields an
uneven number.
'''
a = [-1, 0, 3, 8, 15, 24, 35, 48, 63]
b = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)]
print('列表a: ', a)
print('列表b: ', b)

# 返回多个元组的第一个元素
c = [x[0] for x in b]
print('列表c(由列表b的每个元组中第一个元素组成): ', c)

res = [(x + y) for x, y in zip(a, c)]
print('求和: ', res)
