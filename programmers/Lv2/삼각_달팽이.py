def solution(n):
    answer = []
    data = []
    now = 1
    x = 0
    y = -1
    for i in range(1, n + 1):
        data.append([0] * i)
    
    for i in range(n):
        for j in range(n - i):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            data[y][x] = now
            now += 1
            
    for i in data:
        for j in i:
            answer.append(j)
            
    return answer
