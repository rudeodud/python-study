tuple = ("Forest","Ocean","Mountain","plain")

n = int(input("1~4 사이의 정수 입력: "))
n -= 1
if n == 0:
    print(tuple[0])
elif n == 1:
    print(tuple[1])
elif n == 2:
    print(tuple[2])
elif n == 3:
    print(tuple[3])
else:
    print("input error")
