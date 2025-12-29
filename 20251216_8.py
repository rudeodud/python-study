lst = [3,5,1,10]
print("lst :", lst)
print("lst(lst)", len(lst))

lst.append(10)
print("lst append(10):", lst)

lst.pop()
print("lst pop():", lst)

lst.reverse()
print("lst reverse():", lst)

lst.sort()
print("lst sort():", lst)

lst.sort(reverse=True)
print("lst sort(reverse=True):", lst)

lst.remove(1)
print("lst remove(1):", lst)

lst.insert(1,5)
print("lst insert(1,5):", lst)

tmp = [6,2,4]
print("tmp :", tmp)

lst.extend(tmp)
print("lst extend(tmp):", lst)
print("lst count(5):", lst.count(5))
print("lst index(10):", lst.index(10))

del(lst[1 : 3])
print("del(lst[1 : 3]):", lst)