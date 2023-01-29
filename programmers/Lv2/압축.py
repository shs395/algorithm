def solution(msg):
    answer = []
    idx = 1
    data = dict()
    for i in range(65, 91):
        data[chr(i)] = idx
        idx += 1
    a = list(msg)[::-1]
    
    w = ''
    while True:
        if len(a) <= 0:
            answer.append(data[w])
            break
        c = a.pop() 
        if w + c not in data:
            answer.append(data[w])
            data[w + c] = idx
            idx += 1
            w = c
            continue
        w += c
        
    return answer
