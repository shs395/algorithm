# 2178 - 미로 탐색
from collections import deque
N, M = map(int, input().split())
graph = []
visited = [[False for _ in range(M)] for _ in range(N)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    graph.append(list(map(int, list(input()))))

queue = deque([])
queue.append([0, 0, 1])
visited[0][0] = True
while queue:
    x, y, cnt = queue.popleft()
    if x == N - 1 and y == M - 1:
        ans = cnt
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and graph[nx][ny] == 1:
            visited[nx][ny] = True
            queue.append([nx, ny, cnt + 1])

print(ans)