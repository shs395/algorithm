import heapq
def solution(n, edge):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for e in edge:
        graph[e[0]].append((e[1], 1))
        graph[e[1]].append((e[0], 1))
        
    heap = []
    distance[1] = 0
    heapq.heappush(heap, (0, 1))
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    
    ans_num = 0
    answer = 0
    for i in range(1, len(distance)):
        if distance[i] == ans_num:
            answer += 1
        elif distance[i] > ans_num:
            answer = 1
            ans_num = distance[i]
    return answer
