# 5719 - 거의 최단 경로
import sys, heapq
from collections import deque
input = sys.stdin.readline

while True:
    N, M = map(int, input().rstrip().split())
    if N == 0 and M == 0:
        break
    
    graph = [[] for _ in range(N)]
    reverse_graph = [[] for _ in range(N)]
    visited = [[False] * (N) for _ in range(N)]
    S, D = map(int, input().rstrip().split())
    for _ in range(M):
        U, V, P = map(int, input().rstrip().split())
        graph[U].append((V, P))
        reverse_graph[V].append((U, P))
    
    INF = int(1e20)
    distance = [INF] * (N)
    distance[S] = 0
    heap = []
    heapq.heappush(heap, (0, S))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist: 
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

    queue = deque()
    queue.append((D, 0))
    while queue:
        node, cnt = queue.popleft()
        
        for i in reverse_graph[node]:
            if visited[node][i[0]] == False and distance[i[0]] + cnt + i[1] == distance[D]:
                visited[node][i[0]] = True
                queue.append((i[0], cnt + i[1]))


    distance = [INF] * N
    distance[S] = 0
    heap = []
    heapq.heappush(heap, (0, S))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist: 
            continue

        for i in graph[now]:
            if visited[i[0]][now] == False:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(heap, (cost, i[0]))
    
    if distance[D] < INF:
        print(distance[D])
    else:
        print(-1)