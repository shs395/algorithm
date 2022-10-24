# 1541 - 잃어버린 괄호
data = input()
temp = ''
op = '+'
ans = 0
for c in data:
    if c == '+':
        if op == '+':
            ans += int(temp)
        else:
            ans -= int(temp)
        temp = ''
    elif c == '-':
        if op == '+':
            ans += int(temp)
            op = '-'
        else:
            ans -= int(temp)
        temp = ''
    else:
        temp += c

if op == '-':
    ans -= int(temp)
else:
    ans += int(temp)
print(ans)