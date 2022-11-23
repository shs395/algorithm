# 3 - 전보
import heapq
N, M, C = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    x, y, z = map(int, input().split()) 
    graph[x].append((y, z))

heap = []
distance[C] = 0
heapq.heappush(heap, (0, C))

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))

cnt = 0
ans = 0

for i in range(1, len(distance)):
    if distance[i] > 0:
        cnt +=1 
        ans = max(distance[i], ans)

print(cnt, ans)