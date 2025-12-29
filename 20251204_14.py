n = int(input("숫자 입력: "))
num = 1
ch = ord("a")

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1
    for j in range(n - i + 1):
        print(chr(ch), end=' ')
        ch += 1
    print()
