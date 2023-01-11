def check(a, b):
    same = 0
    min_len = min(len(a), len(b))
    
    for i in range(min_len):
        if a[i] == b[i]:
            same += 1
        else:
            break
    
    if len(a) == same:
        return same
    else:
        return same + 1
    
def solution(words):
    answer = 0
    words.sort()
    for i in range(len(words)):
        if i == 0:
            answer += check(words[i], words[i + 1])
        elif i == len(words) - 1:
            answer += check(words[i], words[i - 1])
        else:
            answer += max(check(words[i], words[i - 1]), check(words[i], words[i + 1]))
            
        
    return answer
