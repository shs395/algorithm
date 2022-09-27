def isRight(x):
    stack = []
    for i in range(len(x)):
        if len(stack) == 0:
            stack.append(x[i])
        elif x[i] == '[' or x[i] == '(' or x[i] == '{':
            stack.append(x[i])
        elif x[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 0
        elif x[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif x[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
    else: 
        return 0
    
    
def solution(s):
    answer = 0
    if len(s) % 2 != 0:
        return 0
    else:
        for i in range(1, len(s) + 1):
            temp = ''
            temp += s[i - 1:] + s[:i - 1]
            answer += isRight(temp)
            
    return answer
