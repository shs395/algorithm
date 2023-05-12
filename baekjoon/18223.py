# 18223 - 민준이와 마산 그리고 건우
import sys, heapq
input = sys.stdin.readline

V, E, P = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
distance_p = [INF] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance[1] = 0
distance_p[P] = 0

heap = []
heapq.heappush(heap, (0, 1))

while heap:
    dist, now = heapq.heappop(heap)
    for x in graph[now]:
        if dist > distance[x[0]]:
            continue
        
        cost = dist + x[1]
        if cost < distance[x[0]]:
            distance[x[0]] = cost
            heapq.heappush(heap, (cost, x[0]))

heap = []
heapq.heappush(heap, (0, P))

while heap:
    dist, now = heapq.heappop(heap)
    for x in graph[now]:
        if dist > distance_p[x[0]]:
            continue
        
        cost = dist + x[1]
        if cost < distance_p[x[0]]:
            distance_p[x[0]] = cost
            heapq.heappush(heap, (cost, x[0]))

if distance[V] == distance[P] + distance_p[V]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
