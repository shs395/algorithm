from collections import deque

def check(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    
    if count == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    queue = deque([[begin, 0]])
    while queue:
        a, depth = queue.popleft()
        for b in words:
            if a != b:
                if check(a, b) == True:
                    if b == target:
                        return depth + 1
                    else:
                        queue.append([b, depth + 1])
    return 0
