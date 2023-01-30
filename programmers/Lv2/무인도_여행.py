import sys
sys.setrecursionlimit(50000)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, visited, arr):
    x = 0
    for idx in range(4):
        ni = i + dx[idx]
        nj = j + dy[idx]
        if 0 <= ni < len(arr) and 0 <= nj < len(arr[0]) and visited[ni][nj] == False and arr[ni][nj] != 'X':
            visited[ni][nj] = True
            x += dfs(ni, nj, visited, arr)
    
    return int(arr[i][j]) + x
    
def solution(maps):
    answer = []
    
    arr = []
    for x in maps:
        arr.append(list(x))
    
    visited = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if visited[i][j] == False and arr[i][j] != 'X':
                visited[i][j] = True
                answer.append(dfs(i, j, visited, arr))
    
    answer.sort()
    
    if len(answer) == 0:
        return [-1]
    return answer
