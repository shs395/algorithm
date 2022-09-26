def solution(s):
    answer = ''
    isblank = True
    for c in s:
        if isblank == True and c != ' ':
            answer += c.upper()
            isblank = False
        elif c == ' ':
            answer += c
            isblank = True
        else:
            answer += c.lower()
    return answer
            
