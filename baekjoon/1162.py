# 1162 - 도로포장
import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e40)
distance = [[INF] * (K + 1) for _ in range(N + 1)]
distance[1][0] = 0
heap = []
heapq.heappush(heap, (0, 1, 0))

while heap:
    dist, now, cnt = heapq.heappop(heap)

    if distance[now][cnt] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]

        if distance[i[0]][cnt] > cost:
            distance[i[0]][cnt] = cost
            heapq.heappush(heap, (cost, i[0], cnt))
        
        if cnt < K and distance[i[0]][cnt + 1] > dist:
            distance[i[0]][cnt + 1] = dist
            heapq.heappush(heap, (dist, i[0], cnt + 1))
    
print(min(distance[N]))