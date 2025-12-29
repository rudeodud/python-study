height = float(input("키를 입력하세요(m):"))
a = float(input("체중을 입력하세요(kg):"))
bmi = a + 100 - height
if bmi > 0:
    print(bmi)
    print("Obesity")
elif bmi == 0:
    print("표준체중입니다.")
else:
    print("저체중입니다.")