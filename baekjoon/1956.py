# 1956 - 운동
# 마을 - 노드 , 도로 - 간선, 일반 통행 - 단방향 그래프
INF = int(1e9)
V, E = map(int, input().split())
graph = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = INF
for i in range(1, V + 1):
    ans = min(ans, graph[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)