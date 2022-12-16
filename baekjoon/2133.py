# 2133 - 타일 채우기
N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 0

if N > 1:
    dp[2] = 3

    for i in range(3, N + 1):
        if i % 2 != 0:
            dp[i] = dp[i - 2]
        else:
            dp[i] = dp[i - 2] * 3 + 2
            for j in range(2, i - 2, 2):
                dp[i] += dp[j] * 2

print(dp[-1])


