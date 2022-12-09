# 2278 - 그래프 복원
import copy
import sys
N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
answer = 0
cnt = 0

for i in range(1, N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        graph[i][i + j + 1] = temp[j]
        graph[i + j + 1][i] = temp[j]

for i in range(1, N + 1):
    graph[i][i] = 0

cp_graph = copy.deepcopy(graph)

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == k or b == k  or a == b:
                continue
            if graph[a][b] == graph[a][k] + graph[k][b]:
                cp_graph[a][b] = 0
            elif graph[a][b] < graph[a][k] + graph[k][b]:
                continue
            elif graph[a][b] > graph[a][k] + graph[k][b]:
                print(0)
                sys.exit()

for i in range(1, N + 1):
    for j in range(i, N + 1):
        if i == j:
            continue
        if cp_graph[i][j] > 0:
            cnt += 1

if M < cnt or M > (N * (N - 1)) // 2:
    print(0)
else:
    print(1)
    need = M - cnt
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if i == j:
                continue
            else:
                if cp_graph[i][j] > 0:
                    print(i, j, cp_graph[i][j])
                elif cp_graph[i][j] == 0 and need > 0:
                    print(i, j, 500)
                    need -= 1

# input
# 4 6 
# 1 1 2
# 2 1
# 1


# input
# 5 10
# 3 3 13 8
# 6 13 5
# 10 11
# 8

# input
# 5 6
# 500 3 500 500
# 500 500 500
# 500 500 
# 500