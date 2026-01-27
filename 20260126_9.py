text = input("문자열을 입력하세요: ")
word_count = {}

for char in text:
    word_count[char] = word_count.get(char, 0) + 1

print(word_count)
