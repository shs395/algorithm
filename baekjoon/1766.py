# 1766 - 문제집
import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())

data = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    data[A].append(B)
    indegree[B] += 1

heap = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    now = heapq.heappop(heap)
    result.append(now)

    for x in data[now]:
        indegree[x] -= 1
        if indegree[x] == 0:
            heapq.heappush(heap, x)

print(*result)


