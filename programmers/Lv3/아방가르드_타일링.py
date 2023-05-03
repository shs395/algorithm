def solution(n):
    answer = 0
    dp = [0] * (100001)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10
    if n >= 4:
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + 2 * dp[i - 2] + 6 * dp[i - 3] + dp[i - 4] - dp[i - 6]) % 1000000007
    return dp[n]
