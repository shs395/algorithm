# 3109 - 빵집
import sys
input = sys.stdin.readline

di = [-1, 0, 1]
dj = [1, 1, 1]
answer = 0

def dfs(i, j):
    global answer
    visited[i][j] = True

    if j == C - 1:
        answer += 1
        return True
    
    for idx in range(3):
        ni = di[idx] + i
        nj = dj[idx] + j

        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == False and arr[ni][nj] == '.':
            result = dfs(ni, nj)
            if result == True:
                return True

    return False



R, C = map(int, input().split())
arr = []
visited = [[False] * C for _ in range(R)]

for _ in range(R):
    arr.append(list(input().rstrip()))

for i in range(R):
    dfs(i, 0)

print(answer)