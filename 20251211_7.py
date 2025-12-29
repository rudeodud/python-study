score = list(map(int, input().split()))

even_sum = 0
odd_sum = 0
odd_count = 0

for num in score:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
        odd_count += 1

print("sum :", even_sum)

if odd_count > 0:
    print("avg :", odd_sum / odd_count)
else:
    print("avg : 0 (홀수가 없음)")
