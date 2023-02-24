# 4 - 커리큘럼
from collections import deque
N = int(input())

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
time_table = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    data = data[:-1]
    time = data[0]
    time_table[i] = time
    before = data[1:]
    indegree[i] = len(before)
    for x in before:
        graph[x].append(i)

print(graph, indegree)
queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            time_table[i] += time_table[now]
            queue.append(i)

print(time_table)



# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1 
# 3 3 -1