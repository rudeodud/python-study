score = list(map(int, input().split()))
sum_ = 0

for num in score:
    sum_ += num

avg = sum_ / 10
print("총점 = ", sum_)
print("평균 + ", round(avg, 1))