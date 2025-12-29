# 첫 번째 배열 입력
a = []
for i in range(4):
    while True:
        msg = "첫번째 배열 %d행 (숫자 4개): " % (i + 1)
        row = list(map(int, input(msg).split()))
        if len(row) == 4:
            a.append(row)
            break
        else:
            print("⚠ 숫자 4개를 정확히 입력하세요!")

# 두 번째 배열 입력
b = []
for i in range(4):
    while True:
        msg = "두번째 배열 %d행 (숫자 4개): " % (i + 1)
        row = list(map(int, input(msg).split()))
        if len(row) == 4:
            b.append(row)
            break
        else:
            print("⚠ 숫자 4개를 정확히 입력하세요!")

# 결과 배열 (4x4)
c = [[0 for _ in range(4)] for _ in range(4)]

# 같은 위치 원소끼리 곱하기
for i in range(4):
    for j in range(4):
        c[i][j] = a[i][j] * b[i][j]

# 결과 출력
print("\n결과 배열:")
for i in range(4):
    for j in range(4):
        print(c[i][j], end=' ')
    print()
