# 求 N 个数字的平均值
sum = 0
N = int(input("求N个数字的平均数, N是: "))

for i in range(N):
    number = float(input("Plz enter 10 numbers: "))
    sum += number

average = sum/N
print("Average is: " + str(average))
print("Average is: {:.2f}".format(average))
