# 11265 - 끝나지 않는 파티
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    x = list(map(int, input().split()))
    graph.append(x)

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

for _ in range(M):
    A, B, C = map(int, input().split())
    if graph[A - 1][B - 1] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')


