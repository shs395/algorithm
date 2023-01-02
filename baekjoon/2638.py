# 2638 - 치즈
# N * M = 10000
# 4변 모두 확인 40000 vs 모든 칸마다 4개의 방향 확인 -> 40000보다는 적음 + 모든 칸 확인
# 치즈 있는 칸만 확인하기
import sys
input = sys.stdin.readline
import copy
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def check(i, j):
    cnt = 0
    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 2:
            cnt += 1
        if cnt >= 2:
            return True
    return False

def count_cheese():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
    return cnt

def initial_external_air():
    for i in range(N):
        if board[i][0] == 0:
            board[i][0] = 2
        if board[i][M - 1] == 0:
            board[i][M - 1] = 2
        
    for j in range(1, M - 1):
        if board[0][j] == 0:
            board[0][j] = 2
        if board[N - 1][j] == 0:
            board[N - 1][j] = 2 

def external_air():
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    for i in range(N):
        if board[i][0] == 2:
            queue.append((i, 0))
            visited[i][0] = True
        if board[i][M - 1] == 2:
            queue.append((i, M - 1))
            visited[i][M - 1] = True
        
    for j in range(1, M - 1):
        if board[0][j] == 2:
            queue.append((0, j))
            visited[0][j] = True
        if board[N - 1][j] == 2:
            queue.append((N - 1, j))
            visited[N - 1][j] = True    

    while queue:
        temp_i, temp_j = queue.popleft()

        for idx in range(4):
            ni = temp_i + di[idx]
            nj = temp_j + dj[idx]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False and (board[ni][nj] == 0 or board[ni][nj] == 2):
                visited[ni][nj] = True
                board[ni][nj] = 2
                queue.append((ni, nj))

board = []
answer = 0
N, M = map(int, input().rstrip().split())
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

if count_cheese() == 0:
    print(0)
else:
    initial_external_air()
    while True:
        external_air()
        temp_board = copy.deepcopy(board)
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    if check(i, j) == True:
                        temp_board[i][j] = 2

        board = temp_board
        answer += 1

        if count_cheese() == 0:
            break

print(answer)

