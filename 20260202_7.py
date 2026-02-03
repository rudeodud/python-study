import random
s = '01023456789'
passlen = 4

p = "".join(random.sample(s, passlen))
print(p)