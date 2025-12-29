lst = list(map(int, input().split()))
max_, min_ = -10000, 10000

for num in lst:
    if num % 2 == 0:
        if num > max_ : max_ = num
    else:
        if num < min_:min_ = num

print("%d %d" % (min_,max_))