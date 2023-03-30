# 2206 - 벽 부수고 이동하기
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
distance = [[[0, 0] for _ in range(M)] for _ in range(N)]
distance[0][0][0] = 1

for i in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

queue = deque([(0, 0, 0)])

while queue:
    i, j, b = queue.popleft()

    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        
        if 0 <= ni < N and 0 <= nj < M:
            if graph[ni][nj] == 0 and distance[ni][nj][b] == 0:
                queue.append((ni, nj, b))
                distance[ni][nj][b] = distance[i][j][b] + 1
            
            if graph[ni][nj] == 1 and b == 0:
                queue.append((ni, nj, 1))
                distance[ni][nj][1] = distance[i][j][b] + 1

if distance[N - 1][M - 1][0] == 0 and distance[N - 1][M - 1][1] == 0:
    print(-1)
elif distance[N - 1][M - 1][1] == 0:
    print(distance[N - 1][M - 1][0])
elif distance[N - 1][M - 1][0] == 0:
    print(distance[N - 1][M - 1][1])
else:
    print(min(distance[N - 1][M - 1]))
