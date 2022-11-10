# 1520 - 내리막 길
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

M, N = map(int, input().rstrip().split())
graph = []
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(m, n):
    global cnt
    if m == M - 1 and n == N - 1:
        return 1

    if dp[m][n] != -1:
        return dp[m][n]
    
    cnt = 0
    for i in range(4):
        nm = m + dx[i]
        nn = n + dy[i]
        if 0 <= nm < M and 0 <= nn < N and graph[nm][nn] < graph[m][n]:
            cnt += dfs(nm, nn)
            dp[m][n] = cnt
            
    return cnt



for _ in range(M):
    graph.append(list(map(int, input().rstrip().split())))


print(dfs(0, 0))