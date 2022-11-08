# 2583 - 영역 구하기
import sys
sys.setrecursionlimit(10000)
M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[i][j] = 1
            visited[i][j] = True

cnt = 0
ans = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    global cnt
    visited[y][x] = True
    cnt += 1
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= nx < N and 0 <= ny < M and visited[ny][nx] == False:
            dfs(ny, nx)

for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans))
print(*ans)


