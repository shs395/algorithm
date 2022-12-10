# 13141 - Ignition
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

INF = int(1e9)
min_graph = [[INF] * (N + 1) for _ in range(N + 1)]
max_graph = [[0] * (N + 1) for _ in range(N + 1)]
answer = INF

for _ in range(M):
    S, E, L = map(int, input().rstrip().split())
    if min_graph[S][E] > L:
        min_graph[S][E] = L
        min_graph[E][S] = L
    
    if max_graph[S][E] < L:
        max_graph[S][E] = L
        max_graph[E][S] = L

for i in range(1, N + 1):
    if min_graph[i][i] == INF:
        min_graph[i][i] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if min_graph[a][b] > min_graph[a][k] + min_graph[k][b]:
                min_graph[a][b] = min_graph[a][k] + min_graph[k][b]

for i in range(1, N + 1):
    temp = 0
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if (min_graph[i][j] + min_graph[i][k] + max_graph[j][k]) / 2 > temp:
                temp = (min_graph[i][j] + min_graph[i][k] + max_graph[j][k]) / 2
    answer = min(answer, temp)

print(answer)