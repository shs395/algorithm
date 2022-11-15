# 2468 - 안전 영역
from collections import deque
N = int(input())
graph = []
graph_max = 0
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j, visited):
    visited[i][j] = True
    queue = deque([[i, j]])
    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            ni = dx[idx] + i
            nj = dy[idx] + j
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and graph[ni][nj] > 0:
                visited[ni][nj] = True
                queue.append([ni, nj])

for _ in range(N):
    temp = list(map(int, input().split()))
    graph_max = max(max(temp), graph_max)
    graph.append(temp)

for _ in range(graph_max + 1):
    visited = [[False for _ in range(N)] for _ in range(N)]
    safearea = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0 and visited[i][j] == False:
                bfs(i, j, visited)
                safearea += 1
    ans = max(ans, safearea)

    for i in range(N):
        for j in range(N):
            graph[i][j] -= 1

print(ans)