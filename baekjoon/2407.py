# 2407 - 조합
n, m = map(int, input().split())
answer = 1
for i in range(n, n - m, -1):
    answer *= i
for i in range(m):
    answer //= i + 1

print(answer)