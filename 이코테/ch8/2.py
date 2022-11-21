# 2 - 1로 만들기
x = int(input())

dp = [30001 for _ in range(x + 1)]
dp[x] = 0

for i in range(x, 1, -1):
    if i % 5 == 0:
        dp[i // 5] = min(dp[i] + 1, dp[i // 5])
    if i % 3 == 0:
        dp[i // 3] = min(dp[i] + 1, dp[i // 3])
    if i % 2 == 0:
        dp[i // 2] = min(dp[i] + 1, dp[i // 2])
    dp[i - 1] = min(dp[i] + 1, dp[i - 1])
print(dp[1])
