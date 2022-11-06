# 12852 - 1로 만들기 2
N = int(input())
dp = [[0, N] for _ in range(N + 1)]

for i in range(N - 1, 0, -1):
    if i * 3 <= N:
        temp_min = min(dp[i*3][0] + 1, dp[i*2][0] + 1, dp[i + 1][0] + 1)
        if temp_min == dp[i * 3][0] + 1:
            dp[i][0] = temp_min
            dp[i][1] = i * 3
        elif temp_min == dp[i * 2][0] + 1:
            dp[i][0] = temp_min
            dp[i][1] = i * 2
        else:
            dp[i][0] = temp_min
            dp[i][1] = i + 1

    elif i * 2 <= N and i * 3 > N:
        temp_min = min(dp[i*2][0] + 1, dp[i + 1][0] + 1)
        if temp_min == dp[i * 2][0] + 1:
            dp[i][0] = temp_min
            dp[i][1] = i * 2
        else:
            dp[i][0] = temp_min
            dp[i][1] = i + 1
    else:
        dp[i][0] = dp[i + 1][0] + 1
        dp[i][1] = i + 1
        

ans = []
idx = 1
while True:
    ans.append(idx)
    if idx >= N:
        break
    idx = dp[idx][1]
    
ans.reverse()
print(dp[1][0])
print(*ans)