# 1753 - 최단경로
import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
distance[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

heap = [(0, K)]

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue

    for x in graph[now]:
        cost = dist + x[1]
        if cost < distance[x[0]]:
            distance[x[0]] = cost
            heapq.heappush(heap, (cost, x[0]))

for x in distance[1:]:
    if x == INF:
        print('INF')
    else:
        print(x)