# 2056 - 작업
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
data = [0] * (N + 1)
max_data = [0] * (N + 1) 
queue = deque()

for i in range(1, N + 1):
    x = list(map(int, input().split()))
    data[i] = x[0]
    indegree[i] = x[1]
    if indegree[i] == 0:
        queue.append(i)
    for y in x[2:]:
        graph[y].append(i)

while queue:
    now = queue.popleft()
    for x in graph[now]:
        indegree[x] -= 1
        max_data[x] = max(max_data[x], data[now])
        if indegree[x] == 0:
            queue.append(x)
            data[x] = data[x] + max_data[x]

print(max(data))