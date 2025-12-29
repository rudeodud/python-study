N = int(input("숫자를 입력하세요: "))
alpha = ord('A')
num = 0
for i in range(1, N + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    for j in range(N - i):
        print(chr(alpha), end=" ")
        alpha += 1
    print()