# 13904 - 과제
import heapq

N = int(input())
data = []
heap = []

for _ in range(N):
    d, w = map(int, input().split())
    data.append((d, w))

data.sort()

for x in data:
    heapq.heappush(heap, x[1])
    if len(heap) > x[0]:
        heapq.heappop(heap)

print(sum(heap))
