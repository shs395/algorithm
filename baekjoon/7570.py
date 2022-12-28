# 7570 - 줄 세우기
# 그냥 data 배열 순서대로 점화식을 실행하면 자연스럽게 하나씩 증가하는 배열이 됨
N = int(input())
data = list(map(int, input().split()))
dp = [0] * (N + 1)

for x in data:
    dp[x] = dp[x - 1] + 1

print(N - max(dp))