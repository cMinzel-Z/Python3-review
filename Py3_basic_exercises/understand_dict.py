'''
What is the output for each of the following sequence of statements executed in a Python shell?
Try to figure out by looking at the code, then run the code to verify whether the result is as you
expected.
'''
print('-----1st-----')
s = 'structure'
dic = {}
for i in range(len(s)):
    dic[s[i]] = i
print(dic)

print('-----2nd-----')
listA = list(range(11, 100, 11))
listB = list(range(1, 10))
listC = [(listA[i], listB[i]) for i in range(9)]
dicB = dict(listC)
print(dicB)

print('-----3rd-----')
for a, b in dicB.items():
    print(a, b, end=" # ")
print()
