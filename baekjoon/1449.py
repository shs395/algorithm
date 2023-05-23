# 1449 - 수리공 항승
N, L = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
answer = 0
now = -10000

for x in data:
    if x >= now + L:
        now = x
        answer += 1

print(answer)