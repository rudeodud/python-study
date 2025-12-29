def menu():
    print("1- 잔액보기 2- 인출 3- 저금 4- 종료")
    return int(input("번호를 입력 하세요: "))


def pinnumber():
    return int(input("핀 번호를 입력 하세요: "))


def withdrawal(mony):
    withd = int(input("얼마를 인출하시겠습니까: "))
    if withd > mony:
        print("잔액이 부족합니다.")
    else:
        mony -= withd
        print(f"{withd}원이 인출되었습니다.")
    return mony


def deposit(mony):
    depo = int(input("금액을 입력하시오: "))
    mony += depo
    print(f"{depo}원이 저금되었습니다.")
    return mony


def total(mony):
    while True:
        index = menu()

        if index == 1:
            print(f"잔액은 {mony}원 입니다")

        elif index == 2:
            mony = withdrawal(mony)

        elif index == 3:
            mony = deposit(mony)

        elif index == 4:
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")

    return mony


def main():
    mony = 0
    pin2 = 0
    if pin2 != 1234:
        while True:
            pin2 = pinnumber()
            print("잘못된 핀 입니다.")
            if pin2 == 1234:
                break
        total(mony)
    else:
        total(mony)
main()
