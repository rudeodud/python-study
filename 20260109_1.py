def plus(num1, num2):
    print(f"({num1} + {num2}) = {num1 + num2}")

def minus(num1, num2):
    print(f"({num1} - {num2}) = {num1 - num2}")

def multi(num1, num2):
    print(f"({num1} * {num2}) = {num1 * num2}")

def div(num1, num2):
    if num2 != 0:
        print(f"({num1} / {num2}) = {num1 / num2}")
    else:
        print("0으로 나눌 수 없습니다.")

def main():
    num1 = int(input("첫번째 숫자를 입력: "))
    num2 = int(input("두번째 숫자를 입력: "))

    plus(num1, num2)
    minus(num1, num2)
    multi(num1, num2)
    div(num1, num2)

main()
