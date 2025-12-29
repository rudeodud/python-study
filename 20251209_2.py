a = input().strip()
b = input().strip()
c = input().strip()

# 숫자로 변환 (문자열 비교를 피하기 위해)
a, b, c = int(a), int(b), int(c)

if a >= b >= c:
    print(a, b, c)
elif a >= c >= b:
    print(a, c, b)
elif b >= a >= c:
    print(b, a, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
else:
    print(c, b, a)
