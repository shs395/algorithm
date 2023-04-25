# 1325 - 효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [[] for _ in range(N + 1)]
max_num = -1
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    data[b].append(a)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    queue = deque([i])
    visited[i] = True
    cnt = 1

    while queue:
        now = queue.popleft()
        
        for x in data[now]:
            if visited[x] == False:
                visited[x] = True
                cnt += 1
                queue.append(x)

    if cnt > max_num:
        max_num = cnt
        answer = []
        answer.append(i)
    elif cnt == max_num:
        answer.append(i)

answer.sort()
print(*answer)

