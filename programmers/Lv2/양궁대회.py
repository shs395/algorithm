from collections import deque

def compare(a, b):
    for i in range(10, -1, -1):
        if a[i] > b[i]:
            return a
        elif a[i] < b[i]:
            return b
    return a

def solution(n, info):
    answer = [0] * 11
    answer[-1] = -1
    diff = 0
    queue = deque()
    
    queue.append((0, [0] * 11, n, 0, 0))
    
    while queue:
        idx, arr, left_arrow, a_score, l_score = queue.popleft()
        if idx < 10:
            # 라이언이 안쏘기
            if info[idx] > 0:
                queue.append((idx + 1, arr[:], left_arrow, a_score + 10 - idx, l_score))
            else:
                queue.append((idx + 1, arr[:], left_arrow, a_score, l_score))
                
            # 라이언이 한 발 더 많이
            if info[idx] + 1 <= left_arrow:
                arr[idx] = info[idx] + 1
                left_arrow -= info[idx] + 1
                queue.append((idx + 1, arr[:], left_arrow, a_score, l_score + 10 - idx))
            # 라이언이 못 쏨
            else:
                if info[idx] > 0:
                    queue.append((idx + 1, arr[:], left_arrow, a_score + 10 - idx, l_score))
                else:
                    queue.append((idx + 1, arr[:], left_arrow, a_score, l_score))
                    
        elif idx == 10:
            arr[idx] += left_arrow
            temp_diff = l_score - a_score
            if temp_diff > diff:
                diff = temp_diff
                answer = arr
            elif temp_diff > 0 and temp_diff == diff:
                answer = compare(answer, arr)
                
    if diff == 0:
        answer = [-1]
    return answer


