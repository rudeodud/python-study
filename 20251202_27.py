sum_ = 0
scores = list(map(int,input().split()))
for score in scores:
    sum_ += score

avg = sum_ / len(scores)
print("총점:", sum_)
print("평균 : %.1f" % (avg))