'''
List a: The formula x
2 − 1 for x taking all numbers between 0 and 9 (the result should be
[-1, 0, 3, 8, 15, 24, 35, 48, 63])
'''
a = [(x * x - 1) for x in range(0, 9)]
print(a)
