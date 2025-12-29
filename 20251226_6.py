a = int(input("숫자를 입력하세요: "))

for i in range(a, 0, -1):
    for j in range(a - i):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print("*", end="")
    print()
