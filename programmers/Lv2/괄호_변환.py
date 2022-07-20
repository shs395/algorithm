def recursion(p):
    if p == '':
        return ''
    stack = []
    for i in range(len(p)):
        if len(stack) == 0:
            stack.append(p[i])
        else:
            stack.append(p[i])
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
        if p[:i + 1].count(')') == p[:i + 1].count('('):
            if len(stack) == 0:
                return p[:i + 1] + recursion(p[i + 1:])
            else:
                temp = '('
                temp += recursion(p[i + 1:])
                temp += ')'
                for i in p[1:i]:
                    if i == '(':
                        temp += ')'
                    else: 
                        temp += '('
                return temp

def solution(p):
    stack = []
    for i in range(len(p)):
        if len(stack) == 0:
            stack.append(p[i])
        else:
            stack.append(p[i])
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        return p
    
    return recursion(p)
