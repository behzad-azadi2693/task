import re

r=r'^\\b([آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی])\\1\\1+\\b'
r = r'.*[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی\s]+[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی\s].*'
l = '۱ن۵م'

print(bool(re.search(r, l)))
print(bool(re.match(r, l)))
print(bool(re.findall(r, l)))
