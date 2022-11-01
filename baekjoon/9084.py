# 9084 - 동전
T = int(input())
for _ in range(T):
    N = int(input())
    coin_list = list(map(int, input().split()))
    M = int(input())
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j]
            if j - coin_list[i - 1] >= 0:
                dp[i][j] += dp[i][j - coin_list[i - 1]]

                
    print(dp[-1][-1])
