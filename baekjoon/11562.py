# 11562 - 백양로 브레이크
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 0:
        graph[u][v] = 0
        graph[v][u] = 1
    else:
        graph[u][v] = 0
        graph[v][u] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(graph[s][e])
