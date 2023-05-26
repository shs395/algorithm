# 11659 - 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(N):
    dp[i + 1] = data[i] + dp[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])

