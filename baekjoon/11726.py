# 11726 - 2xn 타일링
n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
if n >= 2:
    dp[2] = 2

if n >= 3:
    for i in range(3, n + 1):
        x = dp[i - 2] + dp[i - 1]
        if x > 10007:
            x %= 10007
        dp[i] = x
print(dp[n])
