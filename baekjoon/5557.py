# 5557 - 1학년
# 처음에는 bfs 로 풀까 했는데 깊이가 깊어질 때마다 두 배씩 늘어나 말이 안되었다.
# dp 를 이용하면 역시 코드는 간단한데 생각하는 과정이 어렵다.
N = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(N - 1)]
dp[0][arr[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] != 0:
            if 0 <= j + arr[i] <= 20:
                dp[i][j + arr[i]] = dp[i][j + arr[i]] + dp[i - 1][j]
            if 0 <= j - arr[i] <= 20:
                dp[i][j - arr[i]] = dp[i][j - arr[i]] + dp[i - 1][j] 

print(dp[-1][arr[-1]])