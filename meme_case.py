import sys
s = list(' '.join(sys.argv[1:]).lower())
for i in range(1, len(s), 2):
    s[i] = s[i].upper()
print(''.join(s))
