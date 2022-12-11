# 1504 - 특정한 최단 경로
import sys
import heapq
input = sys.stdin.readline
N, E = map(int, input().rstrip().split())
INF = int(1e9)
graph = [[] for _ in range(N + 1)]

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    
    if distance[end] == INF:
        return -1
    else:
        return distance[end]


for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())

a = dijkstra(1, v1)
b = dijkstra(1, v2)
c = dijkstra(v1, v2)
d = dijkstra(v1, N)
e = dijkstra(v2, N)

if a != -1 and c != -1 and e != -1:
    answer = a + c + e
else:
    answer = -1

if answer != -1 and b != -1 and c != -1 and d != -1:
    answer = min(answer, b + c + d)
else:
    answer = -1

print(answer)