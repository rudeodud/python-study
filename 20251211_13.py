lst = input().split()

cnt = {}

for ch in lst:
    if ch in cnt:
        cnt[ch] += 1
    else:
        cnt[ch] = 1

for ch in cnt:
    print(ch, ":", cnt[ch], "개")
   