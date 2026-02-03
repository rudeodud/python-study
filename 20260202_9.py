import re

pattern = r'010-\d\d\d\d-\d\d\d\d'
found = re.search(pattern, '010-1234-5678')
print(found.group())
