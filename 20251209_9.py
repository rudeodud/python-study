classavg = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]

user1 = int(input("첫 번째 반 입력(1~6): "))
user2 = int(input("두 번째 반 입력(1~6): "))

num = classavg[user1 - 1] + classavg[user2 - 1]

print("{:.1f}".format(num))
