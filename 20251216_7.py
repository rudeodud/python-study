pas = [[0 for i in range(6)] for j in range(6)]
pas[1][1] = 1

for i in range(2, 6):
    for j in range(1, i + 1):
        pas[i][j] = pas[i - 1][j - 1] + pas[i - 1][j]

for i in range(1, 6):
    for j in range(1, i + 1):
        print(pas[i][j] , end=' ')
    print()