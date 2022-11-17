# 4889 - 안정적인 문자열
import sys
input = sys.stdin.readline
idx = 1

while True:
    data = input().rstrip()
    if data.count('-') >= 1:
        break
    stack = []
    ans = 0
    for d in data:
        if len(stack) >= 1:
            if d =='}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(d)
        else:
            stack.append(d)
    
    second_stack = []
    for s in stack:
        if len(second_stack) >= 1:
            if s =='}' and second_stack[-1] == '{':
                second_stack.pop()
            elif s == '{' and second_stack[-1] == '{':
                second_stack.pop()
                ans += 1
            else:
                second_stack.append(s)
        else:
            if s == '}':
                second_stack.append('{')
                ans += 1
            else:
                second_stack.append(s)

    print(str(idx) + '. ' + str(ans))
    idx += 1