# 1082 - 방 번호
import bisect

N = int(input())
P = list(map(int, input().split()))
M = int(input())

dp = [[] for _ in range(M + 1)]
answer = 0

for idx, x in enumerate(P):
    if x <= M:
        if len(dp[x]) != 0:
            if idx > dp[x][0]:
                dp[x] = [idx]
        else:
            dp[x].append(idx)

for idx, x in enumerate(P):
    for tmp in range(M + 1 - x):
        if len(dp[tmp]) != 0:
            tmp_dp = dp[tmp][:]
            tmp_dp.insert(bisect.bisect_left(tmp_dp, idx), idx)
            if len(dp[tmp + x]) == 0:
                dp[tmp + x] = tmp_dp
            else:
                if int(''.join(reversed(list(map(str, tmp_dp))))) > int(''.join(reversed(list(map(str, dp[tmp + x]))))):
                    dp[tmp + x] = tmp_dp

for x in dp:
    if x:
        answer = max(answer, int(''.join(reversed(list(map(str, x))))))
        
print(answer)