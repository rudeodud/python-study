n = int(input("숫자 입력:"))

for i in range(0, n+1, +1):
    print(' ' * (n + i) + "*" * (n - i))