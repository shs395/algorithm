# 11403 - 경로 찾기
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for g in graph:
    print(*g)