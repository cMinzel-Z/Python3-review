# 自己做的
with open("String.txt") as f:
    s = f.read()

def findDigits(s):
    aStr = ""
    for x in s:
        if x.isdigit():
            aStr += x
    return aStr

a_Str = findDigits(s)
print(a_Str)

# 参考答案
# 打开并读取文件里的字符串
with open('String.txt') as f:
    s = f.read()
res = ""

# 循环字符串里的每个字符，判断是否为数字
for char in s:
    if char.isdigit():
        res += char
print(res)
        
