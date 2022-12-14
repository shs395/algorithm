# 1800 - 인터넷 설치
import sys, heapq
input = sys.stdin.readline

N, P, K = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(P):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e30)
distance = [[INF] * (K + 1) for _ in range(N + 1)]
distance[1][0] = 0
heap = []
heapq.heappush(heap, (0, 1, 0))
while heap:
    dist, now, cnt = heapq.heappop(heap)

    if distance[now][cnt] < dist:
        continue

    for i in graph[now]:
        cost = max(dist, i[1])

        if distance[i[0]][cnt] > cost:
            distance[i[0]][cnt] = cost
            heapq.heappush(heap, (cost, i[0], cnt))
        
        if cnt < K and distance[i[0]][cnt + 1] > dist:
            distance[i[0]][cnt + 1] = dist
            heapq.heappush(heap, (dist, i[0], cnt + 1))

if distance[N][K] >= INF:
    print(-1)
else:
    print(distance[N][K])