name, heigt, weight = input("이름, 키, 몸무게를 차례로 입력하세요: ").split()
heigt = int(heigt)
weight = float(weight)

sentence1 = "%s의 키는 %dcm이고, 몸무게는 %.1fkg입니다."
print(sentence1 % (name, heigt, weight))