lst = list(map(int, input().split()))
min_ = 1000

for num in lst:
    if num < min_:
        min_ = num
        
print(min_)