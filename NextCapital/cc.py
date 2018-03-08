import re
name  = 'Cxcv3456mmxZ'
s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

print(s1)
print(s2)




#name = 'CamelCaseTest123'
splitted = re.sub('(?!^)([A-Z][a-z]+)', r' \1', name).split()
print(splitted)


a = [1,2,3]

try:
    col_len = len(a[0])
except:
    print('caught')
