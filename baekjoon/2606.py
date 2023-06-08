# 2606 - 바이러스
from collections import deque
N = int(input())
C = int(input())
answer = 0
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(C):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
queue = deque()
queue.append(1)

while queue:
    now = queue.popleft()

    for x in graph[now]:
        if visited[x] == False:
            visited[x] = True
            queue.append(x)
            answer += 1

print(answer)
