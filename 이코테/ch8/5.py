# 5 - 효율적인 화폐 구성
N, M = map(int, input().split())
money = []
dp = [M + 1 for _ in range(M + 1)]
for _ in range(N):
    money.append(int(input()))

if max(money) > M:
    print(-1)
else:
    for m in money:
        dp[m] = 1

    for m in money:
        for i in range(m, M + 1):
            dp[i] = min(dp[i - m] + 1, dp[i])
    
    if dp[-1] == M + 1:
        print(dp)
        print(-1)
    else:
        print(dp)
        print(dp[-1])


