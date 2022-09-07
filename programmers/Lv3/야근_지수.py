import heapq
def solution(n, works):
    answer = 0 
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
        
    for i in range(n):
        work = heapq.heappop(heap) + 1
        if work >= 0:
            heapq.heappush(heap, 0)
        else:
            heapq.heappush(heap, work)
    
    for e in heap:
        answer += e ** 2
            
    return answer
