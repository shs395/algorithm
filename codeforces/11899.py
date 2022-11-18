# 11899 - 괄호 끼워넣기
data = input()
stack = []
for d in data:
    if len(stack) == 0:
        stack.append(d)
    else:
        if d == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(d)
        else:
            stack.append(d)

print(len(stack))