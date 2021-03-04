basic_salary = 1500
bonus = 200
draw_rate = 0.02

num_camera = int(input("Enter the number of camera: "))
price = float(input("Enter the price of camera: "))

gross_salary = basic_salary + (bonus + draw_rate * price) * num_camera
print("{:6.2f}".format(gross_salary))
