days = [0, 31, 28, 31, 30, 31, 31, 31, 30, 31, 30, 31]

while True:
    year = int(input("year = "))
    month = int(input("month = "))
    if month == 0: break
    if month < 0 or month > 12:
        print("잘못 입력했습니다. \n")
    else:
        if year % 400 == 0:
            days[2] = 29
        elif year % 4 == 0 and year % 100 != 0:
            days[2] = 29
        else:
            days[2] = 28
        print("입력하신 달의 날 수는 %d일 입니다.\n" %days[month]) 