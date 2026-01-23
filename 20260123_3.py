def Addcontant():
    name = input("이름:")
    number = input("전화번호:")
    contant[name]=number

def Removecontant():
    remove = input("삭제 할 역락처 이름을 쓰시오:")
    contant.pop(remove)

def Searchcontant():
    search = input("연락처가 알고싶은 사람의 이름을 쓰시오:")
    print("-------------------------------")
    if search in contant:
        print(search,"의 연락처:", contant[search] )
    print("-------------------------------")

def AllSearch():
    print("---------------ALL-----------------")
    for x in contant:
        print(x,"의 연락처:", contant[x])
    print("-----------------------------------")

def main():
    print("1.연락처 추가")
    print("2.연락처 삭제")
    print("3.연락처 검색")
    print("4.연락처 출력")
    print("5.종료")

    choice = int(input("메뉴를 선택 하세요: "))

    if choice == 1:
        Addcontant()
    elif choice == 2:
        Removecontant()
    elif choice == 3:
        Searchcontant()
    elif choice == 4:
        AllSearch()
    elif choice == 5:
        print("종료")
        return False
    else:
        print("올바른숫자를 입력 하세요")
contant = {}

while True:
    situation = main()
    if situation == False:
        break