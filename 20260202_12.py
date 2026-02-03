import re

def check():
    while True:
        password = input("비밀번호를 입력 하세요:")
        if len(password) < 8:
            print("비밀번호는 8자 이상 입력 하세요.")
        elif re.search('[0-9]',password) is None:
            print("비밀번호는 숫자를 포함해야 합니다.")
        elif re.search('[A-Z]',password) is None:
            print("비밀번호는 대문자를 포함해야 합니다.")
        else:
            print("비밀번호가 올바르게 입력되었습니다.")
            break

check() 