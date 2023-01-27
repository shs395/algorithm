def solution(board):
    answer = 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            elif board[i][j - 1] > 0 and board[i - 1][j] > 0 and board[i - 1][j - 1] > 0:
                board[i][j] = board[i][j] + min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1])
                
    for x in board:
        answer = max(answer, max(x))
    return answer * answer
