a = int(input("숫자를 입력하세요: "))

for i in range(a):
    for j in range(i):
        print("*", end="")
    print()