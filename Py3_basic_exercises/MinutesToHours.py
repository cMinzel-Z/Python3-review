import sys

def Hours(minute):
    if minute < 0:
        raise ValueError("Parameter cannot be negative")
    else:
        print("{} Hours, {} Minutes".format(minute // 60, minute % 60))

try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
