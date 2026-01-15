student = 5
lst = []
count = 0

for i in range(student):
    value = int(input())
    lst.append(value)

print(sum(lst) / len(lst))
print(max(lst))
print(min(lst))

for score in lst:
    if score >= 80:
        count += 1

print(count)