# 14938 - 서강그라운드
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
answer = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for x in range(1, n + 1):
    graph[x][x] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            cnt += items[j - 1]
    
    answer = max(cnt, answer)
    
print(answer)