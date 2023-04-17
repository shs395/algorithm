# 1719 - 택배
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
answer = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0
    answer[i][i] = '-'

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    answer[a][b] = b
    answer[b][a] = a

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                answer[a][b] = answer[a][k]
                answer[b][a] = answer[b][k]

for x in answer[1:]:
    print(*x[1:])


