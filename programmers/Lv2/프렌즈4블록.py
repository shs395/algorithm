import copy
def search(m, n, board):
    temp_board = copy.deepcopy(board)
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != '' and board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j + 1]:
                temp_board[i][j] = '1'
                temp_board[i + 1][j] = '1'
                temp_board[i][j + 1] = '1'
                temp_board[i + 1][j + 1] = '1'
    return temp_board

def count_block(m, n, board):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == '1':
                cnt += 1
    return cnt

def rearrange(m, n, board):
    new_board = [[''] * n for _ in range(m)]
    for j in range(n):
        cnt = 0
        temp = []
        for i in range(m):
            if board[i][j] == '' or board[i][j] == '1':
                cnt += 1
            else:
                temp.append(board[i][j])
        
        idx = 0
        for i in range(cnt, m):
            new_board[i][j] = temp[idx]
            idx += 1
    
    return new_board
        
    
    

def solution(m, n, board):
    answer = 0
    temp = []
    
    for x in board:
        temp.append(list(x))
    board = temp
    
    while True:
        board = search(m, n, board)
        result = count_block(m, n, board)
        if result == 0:
            break
        answer += result
        board = rearrange(m, n, board)
        
        
    return answer
