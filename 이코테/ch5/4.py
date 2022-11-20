# 4 - 미로 탈출
from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

queue = deque([[0, 0]])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    temp_i, temp_j = queue.popleft()
    for i in range(4):
        ni = dx[i] + temp_i
        nj = dy[i] + temp_j
        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 1:
            graph[ni][nj] += graph[temp_i][temp_j]
            queue.append([ni, nj])

print(graph[N - 1][M - 1])
print(graph)
# 입력
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111