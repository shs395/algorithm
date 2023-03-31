# 1655 - 가운데를 말해요
import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
max_heap = []
min_heap = []
standard = 0
for i in range(N):
    x = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)
    
    if max_heap and min_heap:
        while True:
            if -max_heap[0] <= min_heap[0]:
                break
            a = heapq.heappop(min_heap)
            b = heapq.heappop(max_heap)
            heapq.heappush(max_heap, -a)
            heapq.heappush(min_heap, -b)
    
    print("%d\n" % -max_heap[0])