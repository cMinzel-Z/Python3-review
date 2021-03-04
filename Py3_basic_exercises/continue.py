while True:
    n = int(input("Plz enter an Integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("Square is ", n ** 2)
print("Goodbye")
