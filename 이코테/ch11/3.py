# 3 - 문자열 뒤집기
s = input()
start = s[0]
data = dict()
data['0'] = 0
data['1'] = 0
data[start] += 1

for c in s:
    if c != start:
        data[c] += 1
        start = c

print(min(data['0'], data['1']))