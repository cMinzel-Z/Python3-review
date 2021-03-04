d = {"Tom" : 500, "Stuart" : 1000, "Bob" : 55, "Dave" : 21274}
'''
When using a dictionary it is possible to add and delete items from it.
Provide code to delete the entry for "Bob" and add an entry for "Phil".
'''
print('修改前: ', d)

# delete the entry for "Bob"
del d['Bob']
print('删除后: ', d)

# add an entry for "Phil"
d['Phil'] = 2222
print('添加后: ', d)
