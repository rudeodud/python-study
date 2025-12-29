score = [[0 for _ in range(4)] for _ in range(5)]
for i in range(5):
    tmp = input("%d번째 학생 점수 4개 입력: " % (i + 1)).split()
    for j in range(4):
        score[i][j] = int(tmp[j])

avg = [0 for _ in range(5)]
for i in range(5):
    total = 0
    for j in range(4):
        total += score[i][j]
    avg[i] = total / 4

count = 0
for i in range(5):
    if avg[i] >= 80:
        print("pass")
        count += 1
    else:
        print("fail")

print("Successful %d" % count)
