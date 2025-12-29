num = 1
ch = ord("a")
for i in range(1, 5):
    for j in range(i):
        print(chr(ch), end = ' ')
        ch += 1
    for j in range(5 - i):
        print(num, end=' ')
        num += 1
    print()