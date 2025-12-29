st = input("문자 입력:").strip()
len_ = len(st)

for i in range(0, len_, 2):
    print(st[i], end=" ")