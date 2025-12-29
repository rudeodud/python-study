name, IDNo, midterm = input("이름, 학번, 중간고사 점수를 차례로 입력하세요: ").split()
midterm = float(midterm)
IDNo = int(IDNo)

sentence1 = "I am %s(IDNo %d), I got %f in my midterm exam."
sentence1 %= (name, IDNo, midterm)
print(sentence1)