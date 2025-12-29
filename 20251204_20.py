st = input("문자 입력:").strip()
len_ = len(st)

for i in range(len_ - 1, -1, -1):
    print(st[i], end=" ")
