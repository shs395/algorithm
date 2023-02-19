from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(maps, start, end):
    w = len(maps[0])
    h = len(maps)
    start_i = 0
    start_j = 0
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == start:
                start_i = i
                start_j = j
                
    queue = deque()
    visited = [[False] * w for _ in range(h)]
    visited[start_i][start_j] = True
    queue.append((start_i, start_j, 0))
    
    while queue:
        i, j, cost = queue.popleft()
        
        if maps[i][j] == end:
            return cost
        
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == False and maps[ni][nj] != 'X':
                visited[ni][nj] = True
                queue.append((ni, nj, cost + 1))
    return 0
                
    
def solution(maps):
    maps = list(map(list, maps))
    
    sl = bfs(maps, 'S', 'L')
    if sl == 0:
        return -1
    
    le = bfs(maps, 'L', 'E')    
    if le == 0:
        return -1
    
    return sl + le
