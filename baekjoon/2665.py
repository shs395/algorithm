# 2665 - 미로만들기
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
data = []
for _ in range(n):
    data.append(list(input().rstrip()))

queue = deque()
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

queue.append((0, 0, 0))
visited = [[False for _ in range(n)] for _ in range(n)]
answer = int(1e9)

while queue:
    i, j, cnt = queue.popleft()
    
    if i == n - 1 and j == n - 1:
        answer = cnt

    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == False:
            visited[ni][nj] = True
            if data[ni][nj] == '1':
                queue.appendleft((ni, nj, cnt))
            else:
                queue.append((ni, nj, cnt + 1))

print(answer)