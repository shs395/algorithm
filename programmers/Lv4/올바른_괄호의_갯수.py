def solution(n):
    answer = 0
    dp = [1, 1, 2]
    for i in range(n + 1):
        if i >= 3:
            dp.append(0)
            temp = 0
            for j in range(1, i + 1):
                temp += dp[j - 1] * dp[i - j]
            
            dp[-1] = temp
            
    return dp[n]
