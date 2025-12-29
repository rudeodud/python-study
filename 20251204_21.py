st = input()
len_ = len(st)

for i in range(len_):
    st = st[-1] + st[:-1] 
    print(st)
