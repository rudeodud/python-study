a = input("문자를 입력하세요: ").split()
for i in range(ord(a[0]), ord(a[1]) + 1):
    print(chr(i), end=" ")