# 10026 - 적록색약
from collections import deque
N = int(input())
grid = []
grid_yes = []
visited_no = [[False for _ in range(N)] for _ in range(N)]
visited_yes = [[False for _ in range(N)] for _ in range(N)]

for _ in range(N):
    temp = input()
    grid.append(list(map(str, temp)))
    grid_yes.append(list(map(str, temp.replace('R', 'G'))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue_no = deque([])
queue_yes = deque([])

no_counter = 0
yes_counter = 0

for i in range(N):
    for j in range(N):
        if visited_no[i][j] == False:
            queue_no.append([i, j, grid[i][j]])
            visited_no[i][j] = True
            while queue_no:
                temp_i, temp_j, temp_color = queue_no.popleft()
                for x in range(4):
                    nx = temp_i + dx[x]
                    ny = temp_j + dy[x]
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == temp_color and visited_no[nx][ny] == False:
                        visited_no[nx][ny] = True
                        queue_no.append([nx, ny, temp_color])
            no_counter += 1


        if visited_yes[i][j] == False:
            queue_yes.append([i, j, grid_yes[i][j]])
            visited_yes[i][j] = True
            while queue_yes:
                temp_i, temp_j, temp_color = queue_yes.popleft()
                for x in range(4):
                    nx = temp_i + dx[x]
                    ny = temp_j + dy[x]
                    if 0 <= nx < N and 0 <= ny < N and grid_yes[nx][ny] == temp_color and visited_yes[nx][ny] == False:
                        visited_yes[nx][ny] = True
                        queue_yes.append([nx, ny, temp_color])
            yes_counter += 1



print(no_counter, yes_counter)