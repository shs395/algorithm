# 11399 - ATM
N = int(input())
P = list(map(int, input().split()))
P.sort()
time = 0
ans = 0
for i in P:
    time = time + i
    ans += time
print(ans)