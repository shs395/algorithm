import heapq
def dij(start, n, graph):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] :
                heapq.heappush(heap, (cost, i[0]))
                distance[i[0]] = cost
    for i in range(1, len(distance)):
        if distance[i] == INF:
            distance[i] = -1
    return distance
 
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        graph[road[0]].append((road[1], 1))
        graph[road[1]].append((road[0], 1))
        
    temp = dij(destination, n, graph)
    for source in sources:
        answer.append(temp[source])
        
    return answer

# BFS
# from collections import deque
# def bfs(start, graph, n, dest):
#     if start == dest:
#         return 0
#     queue = deque([])
#     queue.append([start, 0])
#     visited = [False] * (n + 1)
#     visited[start] = True
#     while queue:
#         now, dist = queue.popleft()
#         for next_node in graph[now]:
#             if next_node == dest:
#                 return dist + 1
#             if visited[next_node] == False:
#                 visited[next_node] = True
#                 queue.append([next_node, dist + 1])
#     return -1
            
# def solution(n, roads, sources, destination):
#     answer = []
#     graph = [[] for _ in range(n + 1)]
#     for road in roads:
#         graph[road[0]].append(road[1])
#         graph[road[1]].append(road[0])
    
#     for source in sources:
#         answer.append(bfs(source, graph, n, destination))
#     return answer

# # 다익스트라
# import heapq
# def dij(start, n, dest, graph):
#     INF = int(1e9)
#     distance = [INF] * (n + 1)
#     distance[start] = 0
#     heap = []
#     heapq.heappush(heap, (0, start))
#     while heap:
#         dist, now = heapq.heappop(heap)
        
#         if distance[now] < dist:
#             continue
            
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]] :
#                 heapq.heappush(heap, (cost, i[0]))
#                 distance[i[0]] = cost
    
#     return distance[dest]
 
# def solution(n, roads, sources, destination):
#     answer = []
#     graph = [[] for _ in range(n + 1)]
#     for road in roads:
#         graph[road[0]].append((road[1], 1))
#         graph[road[1]].append((road[0], 1))
    
#     for source in sources:
#         temp = dij(source, n, destination, graph)
#         if temp == int(1e9):
#             answer.append(-1)
#         else:
#             answer.append(temp)
#     return answer
