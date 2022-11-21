# 4 - 바닥 공사
n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = 1
dp[0] = 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[n])