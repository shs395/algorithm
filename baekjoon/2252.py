# 2252 - 줄 세우기
import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
result = []

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        result.append(i)
        

while queue:
    now = queue.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
            result.append(i)

print(*result)