# 2458 - 키 순서
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
INF = int(1e9)
answer = 0
graph = [[[INF, INF] for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a][b][1] = 1
    graph[b][a][0] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b][1] = min(graph[a][b][1], graph[a][k][1] + graph[k][b][1])
            graph[a][b][0] = min(graph[a][b][0], graph[a][k][0] + graph[k][b][0])

for i in range(1, N + 1):
    temp = 0
    for j in range(1, N + 1):
        if graph[i][j][0] != INF or graph[i][j][1] != INF:
            temp += 1

    if temp == N - 1:
        answer += 1

print(answer)