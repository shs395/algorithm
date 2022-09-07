def solution(m, n, puddles):
    data = [[-1 for _ in range(m)] for _ in range(n)]
    
    for i in puddles:
        data[i[1] - 1][i[0] - 1] = 0
    
    for i in range(n):
        if data[i][0] == 0:
            break
        data[i][0] = 1
        
    for i in range(m):
        if data[0][i] == 0:
            break
        data[0][i] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if data[i][j] == -1:
                data[i][j] = max(0, data[i - 1][j]) + max(0, data[i][j - 1])

    
    return data[n - 1][m - 1] % 1000000007
