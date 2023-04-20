# 14002 - 가장 긴 증가하는 부분 수열 4
import bisect
N = int(input())
A = list(map(int, input().split()))
lis = []
dp = [-1] * N
answer = []

for i in range(len(A)):
    if len(lis) == 0:
        lis.append(A[i])
        dp[i] = 0
    else:
        if A[i] > lis[-1]:
            lis.append(A[i])
            dp[i] = len(lis) - 1
        elif A[i] <= lis[-1]:
            y = bisect.bisect_left(lis, A[i])
            lis[y] = A[i]
            dp[i] = y

x = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == x:
        answer.append(A[i])
        x -= 1

answer.reverse()
print(len(answer))
print(*answer)

