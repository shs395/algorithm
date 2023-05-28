# 1935 - 후위 표기식2
N = int(input())
data = input()
stack = []
num = dict()
for i in range(N):
    x = int(input())
    num[chr(i + 65)] = x

for x in data:
    if len(stack) == 0:
        stack.append(num[x])
    else:
        if 'A' <= x <= 'Z':
            stack.append(num[x])
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(eval(str(a) + x + str(b)))

print(f'{stack[0]:.2f}')