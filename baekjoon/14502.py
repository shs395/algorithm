# 14502 - 연구소
# pypy3 에서만 통과한다..
# combinations 으르 하면 python3에서도 시간초과가 안날 듯 하다.
from collections import deque
N, M = map(int, input().split())
data = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for _ in range(N):
    data.append(list(map(int, input().split())))

def bfs():
    queue = deque([])
    visited = [[False for _ in range(M)] for _ in range(N)]
    temp_count = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                queue.append([i, j])
                visited[i][j] = True
                temp_count += 1
            elif data[i][j] == 1:
                visited[i][j] = True
                temp_count += 1
    while queue:
        temp_i, temp_j = queue.popleft()
        for i in range(4):
            nx = temp_i + dx[i]
            ny = temp_j + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx, ny])
                temp_count += 1
    temp_count = N * M - temp_count
    # for i in range(N):
    #     temp_count += visited[i].count(False)
        # for j in range(M):
        #     if visited[i][j] == False:
        #         temp_count += 1
    global ans 
    ans = max(ans, temp_count)


def wall(count):
    if count == 3:
        bfs()
        return 
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                wall(count + 1)
                data[i][j] = 0

wall(0)
print(ans)
