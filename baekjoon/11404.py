# 11404 - 플로이드
import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)



for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0
        if graph[a][b] == INF:
            graph[a][b] = 0

for x in graph:
    print(*x)
