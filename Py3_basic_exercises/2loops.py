'''
1.1 Warming up exercise: Nested lists
Define the nested list a = [[1,2,3,4], [5,6,7,8], ['a','b','c','d']].
The ’outer’ list consists of three lists; every ’inner’ list consists of 4 elements.
Write a program that prints every element.
(Hint: use two for loops. You only need 3 lines of code for the loops and the printing).
'''
# 设置列表a
a = [[1,2,3,4], [5,6,7,8], ['a','b','c','d']]

#两次for循环输出内层列表元素
def lst_a(a):
    for i in a:
        for x in i:
            print(x)
lst_a(a)
