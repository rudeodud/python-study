numa1, numa2 = input().split()
numb1, numb2 = input().split()
numc1, numc2 = input().split()

st1 = numa1 + " sounds " + numa2
print(st1)

st1 = "%s sounds %s"  % (numb1, numb2)
print(st1)  

st3 = "{} sounds {}".format(numc1, numc2)
print(st3)