# 12865 - 평범한 배낭
import sys
input = sys.stdin.readline
def a():
    N, K = map(int, input().rstrip().split())
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    stuff_list = []
    for _ in range(N):
        W, V = map(int, input().rstrip().split())
        stuff_list.append((W, V))

    for i in range(N + 1):
        for j in range(K + 1):
            w = stuff_list[i - 1][0]
            v = stuff_list[i - 1][1]
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif w <= j:
                dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[N][K])
a()

# 지역변수가 전역변수보다 빨라서 함수를 만들어서 제출하면 시간 초과 해결