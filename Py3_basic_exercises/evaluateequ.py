sum = 0
x = 1
N = int(input("N is: "))
for i in range(x, N):
    sum += 1.0 / i
    print("{:2d} {:6.4f}".format(i, sum))
