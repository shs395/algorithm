from collections import deque

def solution(maps):
    answer = 0
    INF = 99
    queue = deque([[0, 0]])
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = [[INF for _ in range(m)] for _ in range(n)]
    count[0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n  or ny >= m:
                continue
            else:
                if visited[nx][ny] == False:
                    if maps[nx][ny] == 0:
                        visited[nx][ny] = True
                    else:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        count[nx][ny] = count[x][y] + 1
                else:
                    continue
    
    if visited[n - 1][m - 1] == False:
        return -1
    else:
        return count[n - 1][m - 1]

