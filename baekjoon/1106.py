# 1106 - 호텔
C, N = map(int, input().split())

# 비용을 기준으로 dp를 만들 경우 
# dp = [0] * (C * 100 + 1)
# cities = []
# answer = 0
# for _ in range(N):
#     cost, customer = map(int, input().split())
#     cities.append((cost, customer))

# for city in cities:
#     cost, customer = city
#     for i in range(cost, len(dp)):
#         dp[i] = max(dp[i - cost] + customer, dp[i])

# for cost, customer in enumerate(dp):
#     if customer >= C:
#         answer = cost
#         break
# print(answer) 

# 고객의 수를 기준으로 dp를 만들 경우
INF = int(1e9)
dp = [INF] * (C + 100)
dp[0] = 0
cities = []
answer = 0
for _ in range(N):
    cost, customer = map(int, input().split())
    cities.append((cost, customer))

for city in cities:
    cost, customer = city
    for i in range(customer, len(dp)):
        dp[i] = min(dp[i - customer] + cost, dp[i])

print(min(dp[C:]))