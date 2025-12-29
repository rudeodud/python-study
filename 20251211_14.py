cnt = [0 for i in range(10)]
lst = list(map(int, input().split()))

for num in lst:
    cnt[num % 10] += 1

for i in range(0, 10):
    if cnt[i] > 0:
        print("%d : %d개" % (i, cnt[i]))