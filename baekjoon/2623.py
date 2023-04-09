# 2623 - 음악프로그램
import sys
from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N + 1)
data = [[] for _ in range(N + 1)]
answer = []

for i in range(M):
    pd = list(map(int, input().split()))
    for j in range(1, len(pd) - 1):
        data[pd[j]].append(pd[j + 1])
        indegree[pd[j + 1]] += 1

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    answer.append(now)

    for x in data[now]:
        indegree[x] -= 1
        if indegree[x] == 0:
            queue.append(x)

if len(answer) == N:
    for x in answer:
        print(x)
else:
    print(0)