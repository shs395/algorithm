# 1417 - 국회의원 선거
import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
count = 0
dasom = int(input())
for _ in range(N - 1):
    heapq.heappush(heap, -int(input()))
    
if heap:
    while dasom <= -heap[0]:
        temp = heapq.heappop(heap)
        if temp < 0:
            dasom += 1
            temp += 1
            count += 1
            if temp < 0:
                heapq.heappush(heap, temp)


print(count)

