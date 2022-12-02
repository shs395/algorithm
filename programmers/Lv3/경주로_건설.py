from collections import deque
def solution(board):
    INF = int(1e9)
    dp = [[[INF, INF] for _ in range(len(board))] for _ in range(len(board))]
    dp[0][0][0] = 0
    dp[0][0][1] = 0
    # 가로 인덱스 0, 2
    # 세로 인덱스 1, 3
    # 인덱스 % 2 == 0 -> 가로 / 인덱스 % 2 == 1 -> 세로
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque([])
    if board[0][1] == 0:
        queue.append((0, 1, 0))
        dp[0][1][0] = 100
    if board[1][0] == 0:
        queue.append((1, 0, 1))
        dp[1][0][1] = 100
    
    while queue:
        i, j, direction = queue.popleft()
        for idx in range(4):
            ni = i + dx[idx]
            nj = j + dy[idx]
            if 0 <= ni < len(board) and 0 <= nj < len(board) and board[ni][nj] == 0:
                if idx % 2 == direction and dp[i][j][direction] + 100 < dp[ni][nj][direction]:
                    dp[ni][nj][direction] = dp[i][j][direction] + 100
                    queue.append((ni, nj, idx % 2))
                elif idx % 2 != direction and dp[i][j][direction] + 600 < dp[ni][nj][idx % 2]:
                    dp[ni][nj][idx % 2] = dp[i][j][direction] + 600
                    queue.append((ni, nj, idx % 2))
    return min(dp[-1][-1])


# solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
# solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
# solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]])