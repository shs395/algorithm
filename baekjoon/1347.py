# 1347 - 미로 만들기
N = int(input())
data = list(input())
direction = {
    "E" : (0, 1, 'S', 'N'),
    "W" : (0, -1, 'N', 'S'),
    "S" : (1, 0, 'W', 'E'),
    "N" : (-1, 0, 'E', 'W')
}

now = (0, 0)
now_direction = 'S'
maze = [now]
for x in data:
    if x == 'R':
        now_direction = direction[now_direction][2]
    elif x == 'L':
        now_direction = direction[now_direction][3]
    else:
        now = (now[0] + direction[now_direction][0], now[1] + direction[now_direction][1])
        maze.append(now)

min_x = int(1e9)
min_y = int(1e9)
max_x = -1
max_y = -1

for x in maze:
    if x[0] < min_x:
        min_x = x[0]
    
    if x[1] < min_y:
        min_y = x[1]
    if x[0] > max_x:
        max_x = x[0]

new_maze = []

for x in maze:
    if x[0] - min_x > max_x:
        max_x = x[0] - min_x
    if x[1] - min_y > max_y:
        max_y = x[1] - min_y
    new_maze.append((x[0] - min_x, x[1] - min_y))

answer_maze = [['#' for _ in range(max_y + 1)] for _ in range(max_x + 1)]

for x in new_maze:
    answer_maze[x[0]][x[1]] = '.'

for x in answer_maze:
    print(''.join(x))