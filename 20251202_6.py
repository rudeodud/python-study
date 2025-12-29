li = []
st = input("문저열을 입력하세요:").strip()
li.append(st)
li.append(input("문자열을 입력하세요:").strip())
st = input("문자열을 입력하세요:").strip()
li += [st]
print(li)