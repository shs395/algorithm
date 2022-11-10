# 1937 - 욕심쟁이 판다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input().rstrip())
graph = []
dp = [[-1 for _ in range(n)] for _ in range(n)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    num = 1
    for idx in range(4):
        ni = dx[idx] + i
        nj = dy[idx] + j
        if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] > graph[i][j]:
            if dp[ni][nj] != -1:
                num = max(num, dp[ni][nj] + 1)
            else:
                num = max(num, dfs(ni, nj) + 1)
    dp[i][j] = num
    return num
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

for i in range(n):
    for j in range(n):
        dfs(i, j)

for d in dp:
    ans = max(max(d) ,ans)
print(ans)