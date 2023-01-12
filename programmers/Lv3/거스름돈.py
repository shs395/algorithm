def solution(n, money):
    answer = 0
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    
    for m in money:
        for i in range(m, n + 1):
            dp[i] = dp[i - m] + dp[i]
            
    return dp[-1]
