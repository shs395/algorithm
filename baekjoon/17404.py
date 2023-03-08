# 17404 - RGB거리 2
import sys
input = sys.stdin.readline
N = int(input())

data = []
INF = int(1e9)

for _ in range(N):
    data.append(list(map(int, input().split())))

answer = INF

for i in range(3):
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = data[0][:]

    for j in range(3):
        if j != i:
            dp[0][j] = INF
    
    for k in range(1, N):
        r, g, b = data[k]
        if i != N - 1:
            dp[k][0] = data[k][0] + min(dp[k - 1][1], dp[k- 1][2])
            dp[k][1] = data[k][1] + min(dp[k - 1][0], dp[k - 1][2])
            dp[k][2] = data[k][2] + min(dp[k - 1][0], dp[k - 1][1])
        else:
            dp[k][0] = data[k][0] + min(dp[k - 1][1], dp[k - 1][2])
            dp[k][1] = data[k][1] + min(dp[k - 1][0], dp[k - 1][2])
            dp[k][2] = data[k][2] + min(dp[k - 1][0], dp[k - 1][1])
    
    for j in range(3):
        if j != i:
            answer = min(dp[-1][j], answer)
print(answer)