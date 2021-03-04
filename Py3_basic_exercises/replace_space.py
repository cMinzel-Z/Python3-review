'''
The list [' alpha ','beta\n\n ', ' \n gamma \n'] contains words with a lot of
whitespace around. Remove the whitespace.
'''
lst = [' alpha ','beta\n\n ', ' \n gamma \n']
print('带空格：', lst)
# str.replace()是去字符串空格的方法
lst_r = [x.replace(' ', '') for x in lst]
print('去空格后：', lst_r)
