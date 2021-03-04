# 它将会从键盘读取一个数字并且检查这个数字是否小于100
number = int(input("Enter an integer: "))

if number < 100:
    print("Your number is less than 100.")
elif number == 100:
    print("Your number is equal to 100.")
else:
    print("Your number is bigger than 100.")
