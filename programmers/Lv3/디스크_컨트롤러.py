# 현재 처리할 수 있는 작업 중 빨리 끝날 수 있는 작업부터 처리해야함
import heapq
def solution(jobs):
    answer = 0
    heap1 = []
    heap2 = []
    now = 0
    for job in jobs:
        heapq.heappush(heap1, (job[0], job[1]))
        
    while heap1 or heap2:
        while heap1 and heap1[0][0] <= now:
            a, b = heapq.heappop(heap1)
            heapq.heappush(heap2, (b, a))
        
        if heap2:
            time, start = heapq.heappop(heap2)
            answer += now - start + time
            now += time
        else:
            now += 1
            
    return answer // len(jobs)
