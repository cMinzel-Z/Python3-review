ids = ('a', 'b', 'c', 'd', 'e', 'f')
mywords = ('Tim', 'Sara', 'flew', 'space', 'pair', 'slippers')
'''
Write a function that takes the ids and mywords as input,
creates and returns a dictionary that use items in ids as keys and items in mywords as values.
At the end of the program, print out the dictionary you have created.
It should look like this:
{'a': 'Tim', 'c': 'flew', 'b': 'Sara', 'e': 'pair', 'd':'space', 'f': 'slippers'}
'''
dic = dict(zip(ids, mywords))
print(dic)
print(dic.keys())
print(dic.values())
