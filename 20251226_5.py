for i in range(1, 4):
    for j in range(3 - i):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print("*", end="")
    print() 