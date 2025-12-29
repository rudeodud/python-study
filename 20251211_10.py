print("단어 5개 입력하세요")
word = []

for i in range(5):
    word.append(input().strip())

for i in range(4):
    for j in range(i + 1, 5):
        if word[i] > word[j]:
            word[i], word[j] = word[j], word[i]
print("_____________________________")
for st in word:
    print(st)