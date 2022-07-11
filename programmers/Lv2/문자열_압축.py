import math
def solution(s):
    answer = len(s)
    n = math.floor(len(s) / 2)
    cmp = ''
    for i in range(1, n + 1):
        j = i
        cmp = s[0:j]
        count = 1
        temp = ''
        while j <= len(s):
            if cmp == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    temp += cmp
                    cmp = s[j:j+i]
                else:
                    temp += str(count)
                    temp += cmp
                    count = 1
                    cmp = s[j:j+i]
            j += i
        if len(s) % i != 0:
            temp += s[-(len(s) % i):]
        answer = min(answer, len(temp))
    return answer
