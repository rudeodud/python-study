a = input("문자를 입력하세요: ")
b = input("문자를 입력하세요: ")

for i in range(ord(a), ord(b) + 1):
    print(chr(i), end=" ")