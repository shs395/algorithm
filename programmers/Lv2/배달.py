# 다익스트라
import heapq
def solution(N, road, K):
    INF = int(1e9)
    answer = 0
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    heap = []
    distance[1] = 0
    heapq.heappush(heap, (0, 1))
    
    while heap:
        d, node = heapq.heappop(heap)
        
        # if distance[node] + d > distance[node]:
        #     continue
        if distance[node] < d:
            continue
            
        for x in graph[node]:
            if distance[node] + x[1] < distance[x[0]]:
                distance[x[0]] = distance[node] + x[1]
                heapq.heappush(heap, (distance[node] + x[1], x[0]))
                
    for x in distance[1:]:
        if x <= K:
            answer += 1
    return answer

# 플로이드 워셜
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    
    for x in range(1, N + 1):
        graph[x][x] = 0
        
    for x in road:
        if x[2] < graph[x[0]][x[1]]:
            graph[x[0]][x[1]] = x[2]
            graph[x[1]][x[0]] = x[2]
    
    for c in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                if graph[a][c] + graph[c][b] < graph[a][b]:
                    graph[a][b] = graph[a][c] + graph[c][b]  
    
    for x in graph[1][1:]:
        if x <= K:
            answer += 1
    return answer


