# 11727 - 2xn 타일링 2
dp = [0] * 1000
n = int(input())

dp[0] = 1
dp[1] = 3

for i in range(2, n):
    dp[i] = (dp[i - 2] * 2 + dp[i - 1]) % 10007

print(dp[n - 1])