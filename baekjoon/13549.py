# 13549 - 숨바꼭질 3
from collections import deque
N, K = map(int, input().split())
# visited = dict()
visited = [False for _ in range(100001)]
visited[N] = True
count = 0
queue = deque([[N, 0]])
dx = [-1, 1]
while queue:
    position, temp_count = queue.popleft()
    if position == K:
        count = temp_count
        break
    # if 0 <= 2 * position <= 100000 and 2 * position not in visited:
    if 0 <= 2 * position <= 100000 and visited[2 * position] == False:

        visited[2*position] = True
        queue.append([2*position, temp_count])
    for i in dx:
        nx = position + i
        # if 0 <= nx <= 100000 and nx not in visited:
        if 0 <= nx <= 100000 and visited[nx] == False:
            visited[nx] = True
            queue.append([nx, temp_count + 1])
    
print(count)