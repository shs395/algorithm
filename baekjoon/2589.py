# 2589 - 보물섬
from collections import deque
import sys 
input = sys.stdin.readline
height, width = map(int, input().split())
map_arr = []
answer = 0

for i in range(height):
    map_arr.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(height):
    for j in range(width):
        if map_arr[i][j] == 'W':
            continue
        else:
            visited = [[False for _ in range(width)] for _ in range(height)]
            visited[i][j] = True
            distance = 0
            queue = deque([[i, j, distance]])
            while queue:
                ii, jj, distance = queue.popleft()
                answer = max(distance, answer)
                for idx in range(4):
                    ni = ii + dx[idx]
                    nj = jj + dy[idx]
                    if ni < 0 or ni >= height or nj < 0 or nj >= width or map_arr[ni][nj] == 'W' or visited[ni][nj] == True:
                        continue
                    
                    queue.append([ni, nj, distance + 1])
                    visited[ni][nj] = True
        
print(answer)


