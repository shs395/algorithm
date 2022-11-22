# 1916 - 최소비용 구하기
import sys
input = sys.stdin.readline
import heapq
N = int(input().rstrip())
M = int(input().rstrip())
INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

start, end = map(int, input().rstrip().split())
heap = []
distance[start] = 0
heapq.heappush(heap, (0, start))
while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]

        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))
    
print(distance[end])


