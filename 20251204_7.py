n = int(input("숫자 입력:"))

for i in range(1, n + 1):
    print((" " * (n - 1 )) + ("*" * i))