# 2156 - 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
data = []
dp = [[0, 0, 0] for _ in range(n)]

for _ in range(n):
    data.append(int(input()))

dp[0][0] = 0
dp[0][1] = data[0]
dp[0][2] = 0

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = dp[i - 1][0] + data[i]
    dp[i][2] = dp[i - 1][1] + data[i]

print(max(dp[-1]))



