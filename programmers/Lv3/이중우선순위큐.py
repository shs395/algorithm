import heapq
def solution(operations):
    answer = []
    maxheap = []
    minheap = []
    for operation in operations:
        o, num = operation.split()
        num = int(num)
        if o == 'I':
            heapq.heappush(maxheap, -num)
            heapq.heappush(minheap, num)
        elif o == 'D':
            if len(minheap) == 0:
                continue
            if num == 1:
                minheap.remove(-heapq.heappop(maxheap))
            elif num == -1:
                maxheap.remove(-heapq.heappop(minheap))
    if len(minheap) == 0:
        return [0, 0]
    else:
        return [-heapq.heappop(maxheap), heapq.heappop(minheap)]
