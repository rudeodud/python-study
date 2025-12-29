kg = int(input("복싱 챔피언의 몸무게를 입력하세요(kg):"))

if kg > 88.45:
    print("Heavyweight")
elif kg < 88.45:
    print("Cruiserweight")
elif kg < 79.38:
    print("Middleweight")
elif kg < 61.23:
    print("Lightweight")
elif kg < 50.80:
    print("Flyweight")
else:
    print("Minimumweight")
