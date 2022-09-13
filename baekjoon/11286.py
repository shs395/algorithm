# 11286 - 절댓값 힙
import heapq, sys
input = sys.stdin.readline
N = int(input())
minus_heap = []
plus_heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not minus_heap and not plus_heap:
            print(0)
        elif not minus_heap:
            print(heapq.heappop(plus_heap))
        elif not plus_heap:
            print(-heapq.heappop(minus_heap))
        else:
            if minus_heap[0] <= plus_heap[0]:
                print(-heapq.heappop(minus_heap))
            else:
                print(heapq.heappop(plus_heap))
    else:
        if x > 0:
            heapq.heappush(plus_heap, x)
        else:
            heapq.heappush(minus_heap, abs(x))


