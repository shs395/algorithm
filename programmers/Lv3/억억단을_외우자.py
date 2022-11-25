def solution(e, starts):
    answer = []
    data = [1] * (e + 1)
    
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            data[j] += 1
        
    arr = [0 for _ in range(e + 1)]
    max_val = data[-1]
    idx = len(data) - 1
    
    for i in range(len(data) - 1, 0, -1):
        if data[i] >= max_val:
            idx = i
            max_val = data[i]
        arr[i] = idx
        
    for start in starts:
        answer.append(arr[start])
        
    return answer
