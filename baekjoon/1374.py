# 1374 - 강의실
import sys
import heapq

input = sys.stdin.readline
count = 0
data = []
start_heap = []
end_heap = []
N = int(input())
for i in range(N):
    num, start, end = map(int, input().split())
    data.append([num, start, end])

data.sort(key=lambda x:x[1])



for i in data:
    if end_heap:
        if i[1] < end_heap[0]:
            heapq.heappush(end_heap, i[2])
            count += 1
        else:
            heapq.heappop(end_heap)
            heapq.heappush(end_heap, i[2])
    else:
        heapq.heappush(end_heap, i[2])
        count += 1

print(count)

