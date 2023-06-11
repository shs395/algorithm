# 4963 - 섬의 개수
from collections import deque
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    data = []
    visited = [[False for _ in range(w)] for _ in range(h)]
    answer = 0
    for _ in range(h):
        data.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False:
                visited[i][j] = True
                if data[i][j] == 1:
                    answer += 1
                    queue = deque()
                    queue.append((i, j))

                    while queue:
                        ii, jj = queue.popleft()

                        for idx in range(8):
                            ni = ii + di[idx]
                            nj = jj + dj[idx]
                            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == False and data[ni][nj] == 1:
                                visited[ni][nj] = True
                                queue.append((ni, nj))
    print(answer)
