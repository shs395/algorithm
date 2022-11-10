# 2573 - 빙산
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().rstrip().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = 0
max_val = 0
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

for i in range(N):
    max_val = max(max_val, max(graph[i]))

def dfs(visited, n, m):
    visited[n][m] = True
    for i in range(4):
        nn = n + dx[i]
        nm = m + dy[i]
        if 0 <= nn < N and 0 <= nm < M and graph[nn][nm] != 0 and visited[nn][nm] == False:
            dfs(visited, nn, nm)

for i in range(1000):
    temp_graph = []
    visited = [[False for _ in range(M)]for _ in range(N)]
    for j in range(N):
        for k in range(M):
            if graph[j][k] == 0:
                visited[j][k] = True
    for j in range(N):
        for k in range(M):
            if graph[j][k] != 0 and visited[j][k] == False:
                dfs(visited, j, k)
                cnt += 1
    if cnt >= 2:
        ans = i
        break
    elif max_val == 0:
        break
    else:
        cnt = 0

    for j in range(N):
        temp = []
        for k in range(M):
            count = 0
            for l in range(4):
                nj = j + dx[l]
                nk = k + dy[l]
                if 0 <= nj < N and 0 <= nk < M and graph[nj][nk] == 0:
                    count += 1
            temp.append(max(graph[j][k] - count, 0))
        temp_graph.append(temp)
    graph = temp_graph


print(ans)