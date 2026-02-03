s1 = input("문자열을 입력 하세요:")
s2 = input("문자열을 입력 하세요:")

list1 = list(set(s1) & set(s2))
print('\n 공통적인 글:', end=' ')
for i in list1:
    print(i, end=' ')