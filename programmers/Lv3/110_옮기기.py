def solution(s):
    answer = []
    
    for string in s:
        stack = []
        cnt = 0
        for i in range(len(string)):
            stack.append(string[i])
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                cnt += 1
        
        
        k = -1
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '0':
                k = i
                break
        
        
        answer.append(''.join(stack[:k + 1]) + '110' * cnt + ''.join(stack[k + 1:]))
        
    return answer
