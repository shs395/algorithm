# 16194 - 카드 구매하기 2
N = int(input())
P = list(map(int, input().split()))

INF = int(1e9)
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(len(P)):
    for j in range(i, N + 1):
        dp[j] = min(dp[j - (i + 1)] + P[i], dp[j])

print(dp[N])
