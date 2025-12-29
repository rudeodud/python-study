lst = list(map(int, input().split()))
max_ = 0

for num in lst:
    if num > max_:
        max_ = num
        
print(max_)