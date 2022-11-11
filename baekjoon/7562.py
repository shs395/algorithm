# 7562 - 나이트의 이동
from collections import deque
T = int(input())
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(l, x, y, mx, my):
    queue = deque([])
    visited = [[False for _ in range(l)] for _ in range(l)]
    visited[x][y] = True
    count = 0
    if x == mx and y == my:
        print(count)
        return
    queue.append([x, y, 0])


    while queue:
        temp_x, temp_y, temp_count = queue.popleft()
        if temp_x == mx and temp_y == my:
            print(temp_count)
            return

        for idx in range(8):
            nx = dx[idx] + temp_x
            ny = dy[idx] + temp_y
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx, ny, temp_count + 1])


for _ in range(T):
    l = int(input())
    x, y = map(int, input().split())
    mx, my = map(int, input().split())
    bfs(l, x, y, mx, my)
    

