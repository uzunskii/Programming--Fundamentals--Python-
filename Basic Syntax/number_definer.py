num = float(input())
if num == 0:
    print("zero")
elif num < 0:
    if abs(num) < 1 and abs(num) != 0:
        print("small", end=" ")
    elif num > 1000000:
        print("large", end=" ")
    print("negative")
elif num > 0:
    if abs(num) < 1 and abs(num) != 0:
        print("small", end=" ")
    elif num > 1000000:
        print("large", end=" ")
    print("positive")

