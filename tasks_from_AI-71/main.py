f = open('exl1')
countAB, countAC, s = 0, 0, f.read()
for i in range(len(s)-1):
    if s[i] == 'A':
        if s[i+1] == 'B': countAB += 1
        else: countAC += 1
print(f"количество AB: {countAB}, количество AC: {countAC}")
