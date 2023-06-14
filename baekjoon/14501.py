# 14501 - 퇴사
N = int(input())
data = [0] * N
dp = [0] * (N + 1)
for i in range(N):
    T, P = map(int, input().split())
    data[i] = (T, P)

for i in range(N - 1, -1, -1):
    if i + data[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + data[i][0]] + data[i][1])

print(dp[0])

