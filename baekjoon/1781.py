# 1781 - 컵라면
import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []
data = []
answer = 0


for _ in range(N):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort()

for x in data:
    heapq.heappush(heap, x[1])
    if len(heap) > x[0]:
        heapq.heappop(heap)

print(sum(heap))