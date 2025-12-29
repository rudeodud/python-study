gender = input("성별을 입력(F = 여성/M = 남성):")
age = int(input("나이를 입력하시오:"))

if gender == "M":
    if age >= 18:
        print("MAN")
    elif age < 18:
        print("boy")
    else:
        print("error")
elif gender == "F":
    if age >= 18:
        print("WOMAN")
    elif age < 18:
        print("GIRL")
    else:
        print("error")
else:
    print("errro")