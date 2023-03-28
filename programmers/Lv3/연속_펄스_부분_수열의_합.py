from collections import deque

dx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def move(board, i, j, x):
    while True:
        di = dx[x][0] + i
        dj = dx[x][1] + j
        if di < 0 or dj < 0 or di >= len(board) or dj >= len(board[0]) or board[di][dj] == 'D':
            return (i, j)
        i = di
        j = dj
        
def solution(board):
    answer = -1
    new_board = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]
    
    for x in board:
        new_board.append(list(x))
    
    queue = deque([])
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                visited[i][j] = True
                break
        if queue:
            break
            
    while queue:
        i, j, cnt = queue.popleft()
        if new_board[i][j] == 'G':
            if answer == -1:
                answer = cnt
            else:
                answer = min(answer, cnt)
        
        for x in range(4):
            ni, nj = move(new_board, i, j, x)
            if visited[ni][nj] == False:
                visited[ni][nj] = True
                queue.append((ni, nj, cnt + 1))

    return answer
