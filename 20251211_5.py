lst = list(map(int, input().split()))
max_, min_ = -10000, 10000

for num in lst:
    if num < 100:
        if num > max_ : max_ = num
    elif num >= 100:
        if num < min_:min_ = num

print("%d %d" % (max_,min_))