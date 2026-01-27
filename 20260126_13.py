num = {}

date = input("날짜를 입력 하세요 : ")
todo = input("일정을 입력 하세요 : ")

num[date] = todo

print("----------------------------------")
print(f"{date}의 일정은 {num[date]}입니다.")
