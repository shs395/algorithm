def solution(land):
    answer = 0
    dp = land[0]
    for i in range(1, len(land)):
        temp = [0] * 4
        
        for j in range(4):
            max_val = 0
            for k in range(4):
                if j == k:
                    continue
                if dp[k] > max_val:
                    max_val = dp[k]
                    
            temp[j] = land[i][j] + max_val

        dp = temp
            
    return max(dp)
