# 1516 - 게임 개발
from collections import deque

N = int(input())

data = [[] for _ in range(N + 1)]
time = [0] * (N + 1)
indegree = [0] * (N + 1)
answer = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    before = tmp[1:-1]
    time[i + 1] = tmp[0]
    for x in before:
        data[x].append(i + 1)
    indegree[i + 1] += len(before)

queue = deque()
dp = time[:]

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for x in data[now]:
        indegree[x] -= 1
        time[x] = max(time[x], time[now] + dp[x])
        if indegree[x] == 0:
            queue.append(x)

for x in time[1:]:
    print(x)


