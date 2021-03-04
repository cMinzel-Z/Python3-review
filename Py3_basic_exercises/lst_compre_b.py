'''
List b: A list of tuples containing a number and its square for all numbers
between 0 and 9 (the result should be [(0, 0), (1, 1), (2, 4), (3, 9),
(4, 16), (5, 25), (6, 36), (7, 49), (8, 64)])
'''
b = [(x, x*x) for x in range(0, 9)]
print(b)
