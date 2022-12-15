# 7579 - 앱

# 배낭 문제는 보통 어떤 값을 전부 배열로 쓰면 된다.
# 여기서 M 은 천만이고 모든 N에 대해서 할 시 10억이 되므로 이것은 불가능
# cost 를 기준으로 한다면? 100 * 100이므로 최대 만개까지 밖에 배열이 안나오므로 가능하다
N, M = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(N + 1)]
# dp = [0] * (sum(cost) + 1)

for i in range(1, N + 1):
    temp_mem = mem[i - 1]
    temp_cost = cost[i - 1]
    for j in range(1, sum(cost) + 1):
        if j - temp_cost >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - temp_cost] + temp_mem)
        else:
            dp[i][j] = dp[i - 1][j]

for idx, x in enumerate(dp[-1]):
    if x >= M:
        print(idx)
        break


