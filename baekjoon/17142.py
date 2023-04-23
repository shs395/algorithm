# 17142 - 연구소 3
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
answer = int(1e9)

def bfs(case, virus):
    visited = [[-1] * N for _ in range(N)]
    max_cnt = 0
    global answer
    queue = deque()

    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                visited[i][j] = -2

    for i, j in case:
        visited[i][j] = 0
        queue.append((i, j, 0))

    for i, j in virus:
        if visited[i][j] == -1:
            visited[i][j] = '*'

    while queue:
        i, j, cnt = queue.popleft()

        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] != -2:
                if visited[ni][nj] == -1:
                    visited[ni][nj] = cnt + 1
                    queue.append((ni, nj, cnt + 1))
    
                elif visited[ni][nj] == '*':
                    visited[ni][nj] = -3
                    queue.append((ni, nj, cnt + 1))
            

    flag = True
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                flag = False
            if visited[i][j] != '*' and visited[i][j] > max_cnt:
                max_cnt = visited[i][j]

    if flag == True:
        if max_cnt < answer:
            answer = max_cnt




N, M = map(int, input().split())
data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

virus = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            virus.append((i, j))

for case in list(combinations(virus, M)):
    bfs(case, virus)

if answer == int(1e9):
    print(-1)
else:
    print(answer)