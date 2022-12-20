# 13398 - 연속합 2
n = int(input())
data = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n)]

dp[0][0] = data[0]
dp[0][1] = 0

answer = data[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + data[i], data[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + data[i])
    answer = max(answer, dp[i][0])
    answer = max(answer, dp[i][1])

print(answer)