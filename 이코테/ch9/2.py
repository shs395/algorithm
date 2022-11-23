# 2 - 미래 도시
N, M  = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0


for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

X, K = map(int, input().split())

ans = 0
if graph[1][K] == INF or graph[K][X] == INF:
    ans = -1
else:
    ans = graph[1][K] + graph[K][X]

print(ans)


# 입력
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 결과 3

# 4 2
# 1 3
# 2 4
# 3 4
# 결과 -1