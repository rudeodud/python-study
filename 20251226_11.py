a = int(input("숫자를 입력하세요: "))
alpha = ord('A')

for i in range(a, 0, -1):
    for j in range(i):
        print(chr(alpha), end="")
        alpha += 1
    print()
