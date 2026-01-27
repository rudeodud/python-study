calender = {}

for i in range(0, 2, 1):
    date = input("날짜를 입력 하시오:")
    schedule = input("일정을 입력 하세요:")
    if date in calender:
        calender[date].append(schedule)
    else:
        calender[date]=[schedule]

print(calender)