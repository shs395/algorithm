# 7576 - 토마토
from collections import deque

M, N = map(int, input().split())

box = []
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0

for _ in range(N):
    temp = list(map(int, input().split()))
    box.append(temp)

queue = deque([])


for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            visited[i][j] = True
            queue.append([i, j, 0])
            
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    temp_i, temp_j, day = queue.popleft()
    answer = max(day, answer)
    if box[temp_i][temp_j] == 1:
        for i in range(4):
            nx = temp_i + dx[i]
            ny = temp_j + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and box[nx][ny] != -1:
                visited[nx][ny] = True
                queue.append([nx, ny, day + 1])
                if box[nx][ny] != -1:
                    box[nx][ny] = 1


for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            answer = -1

print(answer)