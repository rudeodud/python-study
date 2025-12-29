ch = ord("A")
n = int(input("숫자 입력: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(ch), end='')
        ch -= 1 
    print()
