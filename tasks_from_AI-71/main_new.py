f = open('exl1')
s = f.read()
count = 1
for i in range(len(s)-1):
    r = s.find('x')
    if s[r+1] == 'y':
        if s[r+2] == 'z':
            count += 2
        else:
           count += 1
print(count)
