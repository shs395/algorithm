# 13460 - 구슬 탈출 2
from collections import deque
import copy
# direction = ['left', 'right', 'up', 'down']
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def move_ball(board, dir, ball):
    while True:
        ni = ball[0] + dir[0]
        nj = ball[1] + dir[1]
        if board[ni][nj] == '#' or board[ni][nj] == 'R' or board[ni][nj] == 'B':
            return [ball, False]
        elif board[ni][nj] == 'O':
            board[ball[0]][ball[1]] = '.'
            return [ball, True]
        else:
            board[ni][nj] = board[ball[0]][ball[1]]
            board[ball[0]][ball[1]] = '.'
            ball[0] = ni
            ball[1] = nj
            

def move_board(board, dir, red, blue):
    red_flag = False
    blue_flag = False
    first = red
    second = blue
    
    if dir == (1, 0):
        if red[1] == blue[1] and red[0] < blue[0]:
            first = blue
            second = red

    elif dir == (-1, 0):
        if red[1] == blue[1] and red[0] > blue[0]:
            first = blue
            second = red

    elif dir == (0, 1):
        if red[0] == blue[0] and red[1] < blue[1]:
            first = blue
            second = red

    elif dir == (0, -1):
        if red[0] == blue[0] and red[1] > blue[1]:
            first = blue
            second = red
    
    if first == red:
        moved_red, red_flag = move_ball(board, dir, first)
        moved_blue, blue_flag = move_ball(board, dir, second)
    else:
        moved_blue, blue_flag = move_ball(board, dir, first)
        moved_red, red_flag = move_ball(board, dir, second)

    if red_flag == True and blue_flag == False:
        return [True, moved_red, moved_blue]
    elif red_flag == False and blue_flag == False:
        return [board, moved_red, moved_blue]
    else:
        return [False, moved_red, moved_blue]

n, m = map(int, input().split())
board = []
answer = -1
red = ''
blue = ''
visited = set()
for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = [i, j]
        elif board[i][j] == 'B':
            blue = [i, j]

queue = deque()
visited.add((red[0], red[1], blue[0], blue[1]))
queue.append((0, board, red, blue))

while queue:
    cnt, board, red, blue = queue.popleft()
    if cnt < 10:
        for i in range(4):
            moved_board, moved_red, moved_blue = move_board(copy.deepcopy(board), direction[i], red[:], blue[:])
            if moved_board == True:
                answer = cnt + 1
                print(answer)
                exit()
            elif moved_board == False:
                continue
            else:
                if (moved_red[0], moved_red[1], moved_blue[0], moved_blue[1]) not in visited:
                    visited.add((moved_red[0], moved_red[1], moved_blue[0], moved_blue[1]))
                    queue.append((cnt + 1, moved_board, moved_red[:], moved_blue[:]))
    else: 
        break

print(-1)