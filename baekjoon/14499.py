# 14499 - 주사위 굴리기
import sys
input = sys.stdin.readline

def move_dice(direction):
    global dice
    temp_dice = dict()
    if direction == 1:
        temp_dice[1] = dice[5]
        temp_dice[2] = dice[2]
        temp_dice[3] = dice[1]
        temp_dice[4] = dice[4]
        temp_dice[5] = dice[6]
        temp_dice[6] = dice[3]
    elif direction == 2:
        temp_dice[1] = dice[3]
        temp_dice[2] = dice[2]
        temp_dice[3] = dice[6]
        temp_dice[4] = dice[4]
        temp_dice[5] = dice[1]
        temp_dice[6] = dice[5]
    elif direction == 3:
        temp_dice[1] = dice[4]
        temp_dice[2] = dice[1]
        temp_dice[3] = dice[3]
        temp_dice[4] = dice[6]
        temp_dice[5] = dice[5]
        temp_dice[6] = dice[2]
    elif direction == 4:
        temp_dice[1] = dice[2]
        temp_dice[2] = dice[6]
        temp_dice[3] = dice[3]
        temp_dice[4] = dice[1]
        temp_dice[5] = dice[5]
        temp_dice[6] = dice[4]

    dice = temp_dice


N, M, x, y, K = map(int, input().rstrip().split())
board = []
dice = {
    1 : 0,
    2 : 0, 
    3 : 0, 
    4 : 0, 
    5 : 0, 
    6 : 0
}
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

ops = list(map(int, input().rstrip().split()))

for op in ops:
    nx = x + dxy[op - 1][0]
    ny = y + dxy[op - 1][1]

    if 0 <= nx < N and 0 <= ny < M:
        x = nx
        y = ny
        move_dice(op)
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y] 
            board[x][y] = 0
        print(dice[1])
        