for i in range(1, 101):
    if i % 7 == 0:
        print('')
    elif i % 10 == 7:
        print('')
    elif i // 10 == 7:
        print('')
    else:
        print(i)
    i += 1
