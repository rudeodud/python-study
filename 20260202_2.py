while True:
    password = input("비밀번호를 입력 하세요:")
    if password.isalnum():
        break
    print("비밀번호는 영문과 숫자로만 입력 하세요.")