a, b = input().split()
a, b = int(a), int(b)
print(a, b)
if a > b:
    c = a
    a = b
    b = c
print(a, b)