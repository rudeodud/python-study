data = list(map(int, input("숫자들을 입력하세요: ").split()))

unique_data = list(set(data))

print("주어진 리스트:", data)
print("정리된 리스트(중복제거):", unique_data)
