cnt = 0
num = list(map(int,input().split()))

for x in num:
    if x % 2 == 0:
        cnt += 1

print(cnt)