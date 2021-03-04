name = input("Enter the file name: ")
with open(name) as f:
    print(f.read())
