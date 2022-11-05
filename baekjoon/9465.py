# 9465 - 스티커
import sys
input = sys.stdin.readline
# 풀이 1 : 함수 사용 x / 시간 : 968ms

# T = int(input().rstrip())
# for _ in range(T):
#     n = int(input().rstrip())
#     arr = []
#     dp = [[0 for _ in range(n)] for _ in range(2)]
#     arr.append(list(map(int, input().rstrip().split())))
#     arr.append(list(map(int, input().rstrip().split())))
#     dp[0][0] = arr[0][0]
#     dp[1][0] = arr[1][0]
#     for i in range(1, n):
#         dp[0][i] = max(dp[1][i - 1] + arr[0][i], dp[0][i - 1])
#         dp[1][i] = max(dp[0][i - 1] + arr[1][i], dp[1][i - 1])
#     print(max(dp[0][-1], dp[1][-1]))

# 풀이 2 : 함수 사용 o / 시간 : 816ms
def a():

    T = int(input().rstrip())
    for _ in range(T):
        n = int(input().rstrip())
        arr = []
        dp = [[0 for _ in range(n)] for _ in range(2)]
        arr.append(list(map(int, input().rstrip().split())))
        arr.append(list(map(int, input().rstrip().split())))
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        for i in range(1, n):
            dp[0][i] = max(dp[1][i - 1] + arr[0][i], dp[0][i - 1])
            dp[1][i] = max(dp[0][i - 1] + arr[1][i], dp[1][i - 1])
        print(max(dp[0][-1], dp[1][-1]))
a()