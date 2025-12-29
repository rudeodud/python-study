a = list(map(int, input().split()))

for i in range(9):
    for j in range(i + 1, 10):
        if a[i] < a[j]:
            a[j], a[i] = a[i], a[j]

for i in range(10):
    print(a[i], end = ' ')