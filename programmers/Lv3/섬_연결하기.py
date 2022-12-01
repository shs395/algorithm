import heapq
def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    heap = []
    for cost in costs:
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))
        
    heapq.heappush(heap, (0, 0))
    
    while heap:
        cost, now = heapq.heappop(heap)
        if visited[now] == False:
            visited[now] = True
            answer += cost
            for i in graph[now]:
                heapq.heappush(heap, (i[1], i[0]))
    

    return answer
