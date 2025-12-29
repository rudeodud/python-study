name, height, weight = input("이름, 키, 몸무게를 차례로 입력하세요: ").split()
height = float(height)
weight = float(weight)

sentence1 = "%s의 키는 %dcm이고, 몸무게는 %fkg입니다."
sentence1 %= (name, height, weight)
print(sentence1)