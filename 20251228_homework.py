reservation = input("항공편 예약을 하시겠습니까? (Y/N): ")

if reservation.upper() != 'Y':
    print("항공편 예약이 취소되었습니다.")
    exit()

print("----지금 운행중인 항공편은 다음과 같습니다.----")
print("1. 미국(어른: 500,000원 / 청소년: 400,000원 / 어린이: 300,000원)")
print("2. 중국(어른: 300,000원 / 청소년: 250,000원 / 어린이: 200,000원)")
print("3. 일본(어른: 400,000원 / 청소년: 350,000원 / 어린이: 300,000원)")


while True:
    country = input("어느 국가로 가시겠습니까?: ")

    if country not in ["미국", "중국", "일본"]:
        print("죄송합니다. 해당 국가로는 운행하지 않습니다.")
        continue

    age = int(input("나이를 입력하세요: "))
    if age < 0:
        print("잘못된 나이입니다. 다시 입력해주세요.")
        continue
    seat = int(input("좌석 1~10까지 번호를 입력하세요 (1~3 비지니스 / 4~5 퍼스트 / 6~10 이코노미): "))

    if seat < 1 or seat > 10:
        print("좌석 번호는 1부터 10까지입니다. 다시 입력해주세요.")
        continue
    
    if seat in [1,2,3]:
        seat_type = "비지니스"
        plusprice = 200000
    elif seat in [4,5]:
        seat_type = "퍼스트"
        plusprice = 100000
    else:
        seat_type = "이코노미"
        plusprice = 0

    if country == "미국":
        if age >= 19:
            price = 500000
        elif age >= 13:
            price = 400000
        else:
            price = 300000
    elif country == "중국":
        if age >= 19:
            price = 300000
        elif age >= 13:
            price = 250000
        else:
            price = 200000
    elif country == "일본":
        if age >= 19:
            price = 400000
        elif age >= 13:
            price = 350000
        else:
            price = 300000

    print("\n" + "=" * 40)
    print("       AIRLINE TICKET        ")
    print("=" * 40)
    print(f" 목적지   : {country}")
    print(f" 좌석등급 : {seat_type}")
    print(f" 좌석번호 : {seat}")
    print("-" * 40)
    print(f" 탑승객   : {'성인' if age >= 19 else '청소년' if age >= 13 else '어린이'}")
    print(f" 기본요금 : {price:,}원")
    print(f" 좌석등급별 요금추가({seat_type}):{plusprice:,}원")
    print("-" * 40)
    print(f"총 금액 : {price + plusprice:,}원")
    print("=" * 40)
    print("   즐거운 여행 되세요!")
    print("=" * 40)

    break
