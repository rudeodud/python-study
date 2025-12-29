a = [0 for i in range(3)]
for i in range(3):
    msg = "첫번째 배열 %d행: " % (i+1)
    a[i] = list(map(int, input(msg).split()))

b = []
for i in range(3):
    msg = "두번째 배열 %d행: " % (i+1)
    tmp = input(msg).split()
    b.append(list(map(int, tmp)))

c = [[0 for i in range(3)] for j in range(3)]
for i in range(4):
    for j in range(4):
        c[i][j] = a[i][j] + b[i][j]

for i in range(3):
    for j in range(3):
        print(c[i][j], end=' ')
    print()
