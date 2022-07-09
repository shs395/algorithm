def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    for move in moves:
        for i in range(N):
            temp = board[i][move - 1]
            if temp == 0:
                continue
            else:
                stack.append(temp)
                board[i][move - 1] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer
