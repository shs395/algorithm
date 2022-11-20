# 3 - 음료수 얼려 먹기
from collections import deque
N, M = map(int, input().split())
graph = []
visited = [[False] * M for _ in range(N)]
for _ in range(N):
    # graph.append(list(map(int, input().split())))
    graph.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
# DFS 풀이
# def dfs(i, j):
#     visited[i][j] = True
#     for idx in range(4):
#         ni = dx[idx] + i
#         nj = dy[idx] + j
#         if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False and graph[ni][nj] == 0:
#             dfs(ni, nj)
#     return

# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 0 and visited[i][j] == False:
#             dfs(i, j)
#             ans += 1
#         elif graph[i][j] == 1:
#             visited[i][j] = True

# BFS 풀이
queue = deque([])
for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j] == 0:
            queue.append([i, j])
            visited[i][j] = True
            while queue:
                temp_i, temp_j = queue.popleft()
                for idx in range(4):
                    ni = dx[idx] + temp_i
                    nj = dy[idx] + temp_j
                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False and graph[ni][nj] == 0:
                        visited[ni][nj] = True
                        queue.append([ni, nj])
            ans += 1



print(ans)

# 입력
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111