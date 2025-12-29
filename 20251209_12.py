words = ["champion", "tel", "pencil", "jungol", "olympiad", "class", "ass", "information", "lesson", "book","lion"]
ch = input("문자를 입력 하세요:").strip()
flag = 0

for word in words:
    if word[0] == ch:
        print(word)
        flag = 1

if flag == 0:
    print("찾는 단어가 없습니다.")
