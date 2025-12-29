score = []
for i in range(3):
    tmp = input("%d번째 학생 점수: " % (i + 1)).split()
    score.append(list(map(int, tmp)))
    score[i] += [0]
score += [[0,0,0,0]]

for i in range(3):
    for j in range(3):
        score[i][3] += score[i][j]
        score[3][j] += score[i][j]
        score[3][3] += score[i][j] 

print("국어 영어 수학 총점")
for i in range(4):
    if i < 3: print("%d번" % (i + 1), end=' ')
    else : print("합계", end=' ')
    for j in range(4):
        print("%3d" % score[i][j], end=' ')
    print()