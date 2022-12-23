# 3190 - 뱀
from collections import deque
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
rotate = deque()
for _ in range(K):
    c, r = map(int, input().split())
    board[c - 1][r - 1] = 1
L = int(input())
for _ in range(L):
    X, C = input().split()
    rotate.append((int(X), C))

board[0][0] = -1
direction = 'R'
snake = deque()
snake.append([0, 0])
move = {'R':[0, 1], 'L':[0, -1], 'U':[-1, 0], 'D': [1, 0]}
direction_dict = {
    'L':{
        'R':'U', 
        'U':'L', 
        'L':'D', 
        'D':'R'
    }, 
    'D':{
        'R':'D', 
        'D':'L',
        'L':'U',
        'U':'R'
    }
}
time = 0
while True:
    head_x, head_y = snake[-1]
    next_head_x = head_x + move[direction][0]
    next_head_y = head_y + move[direction][1]

    # print(head_x, head_y, next_head_x, next_head_y, direction)
    # for x in board:
    #     print(*x)
    # print('*****************')
    
    # 이동 가능한 경우
    if 0 <= next_head_x < N and 0 <= next_head_y < N and board[next_head_x][next_head_y] != -1:
        # 사과
        if board[next_head_x][next_head_y] == 1:
            snake.append([next_head_x, next_head_y])
            board[next_head_x][next_head_y] = -1
        # 사과 없는 경우
        else:
            snake.append([next_head_x, next_head_y])
            board[next_head_x][next_head_y] = -1
            tail = snake.popleft()
            board[tail[0]][tail[1]] = 0
    else:
        break   
    time += 1
    if rotate and rotate[0][0] == time:
        temp_time, temp_dir = rotate.popleft()
        direction = direction_dict[temp_dir][direction]
    
print(time + 1)