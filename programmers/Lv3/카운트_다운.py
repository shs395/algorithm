def solution(target):
    answer = []
    single = [i for i in range(1, 21)]
    double = [i * 2 for i in range(1, 21)]
    triple = [i * 3 for i in range(1, 21)]
    single.append(50)
    dp = [(100001, 0) for _ in range(target + 1)]
    dp[0] = (0, 0)
    for i in single:
        for j in range(1, target + 1):
            if j - i >= 0:
                if dp[j - i][0] + 1 < dp[j][0]:
                    dp[j] = (dp[j - i][0] + 1, dp[j - i][1] + 1)
                elif dp[j - i][0] + 1 == dp[j][0]:
                    dp[j] = (dp[j][0], max(dp[j - i][1] + 1, dp[j][1]))
                
    for i in double:
        for j in range(1, target + 1):
            if j - i >= 0:
                if dp[j - i][0] + 1 < dp[j][0]:
                    dp[j] = (dp[j - i][0] + 1, dp[j - i][1])
                elif dp[j - i][0] + 1 == dp[j][0]:
                    dp[j] = (dp[j][0], max(dp[j - i][1], dp[j][1]))
    
    for i in triple:
        for j in range(1, target + 1):
            if j - i >= 0:
                if dp[j - i][0] + 1 < dp[j][0]:
                    dp[j] = (dp[j - i][0] + 1, dp[j - i][1])
                elif dp[j - i][0] + 1 == dp[j][0]:
                    dp[j] = (dp[j][0], max(dp[j - i][1], dp[j][1]))
                    
    return [dp[-1][0], dp[-1][1]]
