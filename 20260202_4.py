phrase = input("문자열을 입력 하세요:")

acronym = ''
for word in phrase.split():
    acronym += word[0]

print( acronym )