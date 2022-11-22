# 1389 - 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A][B] = 1
    graph[B][A] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans_idx = 0
ans_sum = INF
for i in range(1, N + 1):
    temp_sum = 0
    for j in range(1, N + 1):
        temp_sum += graph[i][j]
    if temp_sum < ans_sum:
        ans_idx = i
        ans_sum = temp_sum
print(ans_idx)
