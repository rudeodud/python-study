s = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15]]

rows = len(s)

for r in range(rows):
    for c in range(len(s[r])):
        print(s[r][c], end=" ")
    print()