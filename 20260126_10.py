months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

num = int(input("달의 번호를 입력하세요: "))

if num in months:
    print(months[num])
else:
    print("1부터 12 사이의 숫자만 입력하세요.")
