a, b = input("주사위를 던진 결과를 입력하세요:").split()
a, b = int(a), int(b)

if a >= 4 and b >= 4:
    print("승리")
elif a >= 4 or b > 4:
    print("무승부")
else:
    print("패배")