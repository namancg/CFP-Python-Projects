import re

pattern = '^by?.s$'
test_string = 'bvvs'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")
