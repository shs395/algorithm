def solution(strs, t):
    answer = 0
    dp = [100000] * (len(t) + 1)
    dp[0] = 0
    data = dict()
    for s in strs:
        data[s] = ''
    
    for i in range(1, len(t) + 1):
        for j in range(1, min(6, i + 1)):
            if t[:i][-1 * j:] in data:
                dp[i] = min(dp[i], dp[i - j] + 1)
                
    if dp[-1] == 100000:
        return -1
    return dp[-1]
