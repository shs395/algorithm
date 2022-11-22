# 18352 - 특정 거리의 도시 찾기
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N, M, K, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append((b, 1))

heap = []
heapq.heappush(heap, (0, X))
distance[X] = 0

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))

ans = []
for i in range(1, len(distance)):
    if distance[i] == K:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)