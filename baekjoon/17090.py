# 17090 - 미로 탈출하기
import sys
sys.setrecursionlimit(100000000)
def dfs(i, j, graph, move, data, visited, N, M):
    visited[i][j] = True
    x = move[graph[i][j]]
    ni = i + x[0]
    nj = j + x[1]
    if ni < 0 or ni >= N or nj < 0 or nj >= M:
        data[i][j] = True
        return True
    else:
        if visited[ni][nj] == False:
            data[i][j] = dfs(ni, nj, graph, move, data, visited, N, M)
            return data[i][j]
        else:
            if data[ni][nj] == 0:
                return False
            else:
                data[i][j] = data[ni][nj]
                return data[ni][nj]

N, M = map(int, input().split())
graph = []
data = [[0] * M for _ in range(N)] 
move = {'U':(-1, 0), 'R':(0, 1), 'D':(1, 0), 'L':(0, -1)}
visited = [[False] * M for _ in range(N)]

for _ in range(N):
    graph.append(list(input()))

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            dfs(i, j, graph, move, data, visited, N, M)

cnt = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == True:
            cnt += 1
print(cnt)


