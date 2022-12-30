# 1793 - 타일링
while True:
    try:
        n = int(input())
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 3
            else:
                dp[i] = dp[i - 2] * 2 + dp[i - 1]
        print(dp[n])
    except:
        break
    



