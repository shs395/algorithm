# 11780 - 플로이드 2
import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
answer = [[[] for i in range(n)] for _ in range(n)]


for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c
        answer[a - 1][b - 1] = [a, b]

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                answer[a][b] = []
                answer[a][b].extend(answer[a][k])
                answer[a][b].extend(answer[k][b][1:])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()


for i in range(n):
    for j in range(n):
        print(len(answer[i][j]), *answer[i][j])