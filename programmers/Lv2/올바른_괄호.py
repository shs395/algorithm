def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        if i == ')' and len(stack) >= 2:
            if stack[-2] == '(':
                stack.pop()
                stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
            
