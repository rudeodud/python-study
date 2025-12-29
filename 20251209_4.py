st1, st2, st3 = input().split()

if st1 < st2:
    min = st1
    if min > st3:
        min = st3
        print(min)
    else:
        print(min)
else:
    min = st2
    if min > st3:
        min = st3
        print(min)
    else :
        print(min)

