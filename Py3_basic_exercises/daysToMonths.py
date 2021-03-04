days = int(input("Enter days: "))

months = days // 30
Remain_days = days % 30

print("Months = {} Days = {}".format(months, Remain_days))
print("===下面的方法也可以===")

days = int(input("Enter days: "))
print("Months = {} Days = {}".format(*divmod(days, 30)))
