# 1238 - 파티
import sys, heapq
input = sys.stdin.readline

def dijkstra(graph, X, distance):
    heap = []
    heapq.heappush(heap, (0, X))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue
        
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(heap, (cost, x[0]))
            
N, M, X = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
graph_reverse = [[] for _ in range(N + 1)]
distance_reverse = [INF] * (N + 1)
answer = -1

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph_reverse[b].append((a, t))

dijkstra(graph, X, distance)
dijkstra(graph_reverse, X, distance_reverse)

for i in range(1, N + 1):
    if i != X:
        answer = max(answer, distance[i] + distance_reverse[i])

print(answer)