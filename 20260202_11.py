import re

pattern = r'[\w]+@[\w]+\.[A-Za-z]{2,4}$'

def checkEmail(emailAddress):
    if(re.search(pattern, emailAddress)):
        print(f"{emailAddress}는 올바른 이메일 주소입니다.")
    else:
        print(f"{emailAddress}는 올바른 이메일 주소가 아닙니다.")

email = "abc123@gmail.com"
checkEmail(email)

email = "abc.cde@.com"
checkEmail(email)