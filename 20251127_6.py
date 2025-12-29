a, b = input().split()
st1 = a + " like " + b
print(st1)

st2 = "%s like %s"  % (a, b)
print(st2)

st3 = "{} like {}".format(a, b)
print(st3)

st4 = f"{a} like {b}"
print(st4)