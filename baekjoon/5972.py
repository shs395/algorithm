# 5972 - 택배 배송
import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

heap = []
heapq.heappush(heap, (0, 1))
distance[1] = 0


while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))

print(distance[N])

