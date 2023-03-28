# 7662 - 이중 우선순위 큐
import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    idx_list = [False] * k
    for i in range(k):
        c, n = input().split()
        n = int(n)
        
        if c == 'I':
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
        elif c == 'D':
            if n == -1:
                while min_heap:
                    if idx_list[min_heap[0][1]] == True:
                        heapq.heappop(min_heap)
                    else:
                        break
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    idx_list[idx] = True

            elif n == 1:
                while max_heap:
                    if idx_list[max_heap[0][1]] == True:
                        heapq.heappop(max_heap)
                    else:
                        break
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    idx_list[idx] = True

    while min_heap:
        if idx_list[min_heap[0][1]] == True:
            heapq.heappop(min_heap)
        else:
            break

    while max_heap:
        if idx_list[max_heap[0][1]] == True:
            heapq.heappop(max_heap)
        else:
            break

    if min_heap:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    else:
        print('EMPTY')
        