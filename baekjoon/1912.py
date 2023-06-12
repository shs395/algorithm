# 1912 - 연속합
n = int(input())
data = list(map(int, input().split()))
dp = [data[0]]

for i in range(1, n):
    dp.append(max(dp[-1] + data[i], data[i]))

print(max(dp))