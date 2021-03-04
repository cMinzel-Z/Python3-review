d = {"Tom" : 500, "Stuart" : 1000, "Bob" : 55, "Dave" : 21274}
'''
We can also check if items are present in the dictionary. Enter the following code and check
if the results are what you expect:
"Dave" in d
"Peter" in d
500 in d
'''
print("Dave" in d)
print("Peter" in d)
print(500 in d)

print('-----Next one practice-----')

'''
What is the difference between the code:
'''
print('-----1st-----')
for key, value in d.items():
    print(key, value)
    
print('-----2nd-----')
for i in d:
    print(i)
