# 3 - 개미 전사
n = int(input())
k = list(map(int, input().split()))
dp = [0 for _ in range(len(k))]
dp[0] = k[0]
dp[1] = max(k[0], k[1])
for i in range(2, len(k)):
    dp[i] = max(dp[i - 1], dp[i - 2] + k[i])

print(dp[-1])