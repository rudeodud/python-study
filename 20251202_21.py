a, b, c = input("세 수를 입력하세요:").split()
a, b, c = int(a), int(b), int(c)

if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c: max = b
    else: max = c

print("입력받은 가장 큰 함수는 %d 입니다." %max)