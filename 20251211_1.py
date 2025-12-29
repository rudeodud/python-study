words = []  

for i in range(1, 11):
    word = input(str(i) + "번째 단어를 입력하세요: ")
    words.append(word)

lastch = input("찾을 마지막 글자를 입력하세요: ")

found = False
for word in words:
    if word[-1] == lastch:
        print(word)
        found = True

if not found:
    print("찾을 수 없음")

