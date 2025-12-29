str = " abcdefgabc "
print("str :", str)

str = str.strip()
print("str.strip() :", str)
print("len(str) :", len(str))

print("str.count('b') :", str.count('b'))
print("str.find('b') :", str.find('b'))
print("str.index('b') :", str.index('b'))

print("str.isupper() :", str.isupper())
print("str.islower() :", str.islower())
print("str.isalpha() :", str.isalpha())
print("str.isdigit() :", str.isdigit())
print("str.isalnum() :", str.isalnum())

str = str.upper()
print("str.upper()", str)

str = str.lower()
print("str.lower() :", str)

str = str.replace('d', 'z')
print("str.replace('d', 'z') :", str)

str = ','.join(str)
print("','.join(str) :", str)

lst = str.split(',')
print("str.split(',') :", lst)